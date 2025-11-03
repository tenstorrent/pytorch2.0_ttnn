#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

REPO_ROOT="/workspace/pytorch2.0_ttnn"
cd "${REPO_ROOT}"

# 1) Базовые переменные
export TT_METAL_HOME="${TT_METAL_HOME:-${REPO_ROOT}/torch_ttnn/cpp_extension/third-party/tt-metal}"

# 2) Посмотрим, чего именно не хватает у расширения
EXT_SO="$(python3 - <<'PY'
try:
    import importlib, pathlib
    m = importlib.import_module('ttnn_device_extension')
    print(pathlib.Path(m.__file__))
except Exception:
    # запасной вариант: ищем в билде проекта
    import pathlib
    cands = list(pathlib.Path('torch_ttnn/cpp_extension').glob('ttnn_device_extension*.so'))
    print(cands[0] if cands else "")
PY
)"
if [ -n "${EXT_SO}" ] && [ -f "${EXT_SO}" ]; then
  echo "[ldd] ${EXT_SO}"
  ldd "${EXT_SO}"
else
  echo "[warn] ttnn_device_extension .so не найден/не импортируется"
fi

# 3) Найдём все libtt_*.so (убедимся, есть ли libtt_stl.so вообще)
echo "[find] libtt_*.so в TT_METAL_HOME=${TT_METAL_HOME}"
find "${TT_METAL_HOME}" -maxdepth 5 -type f -name 'libtt_*.so' -print || true

echo "[find] libtt_*.so в site-packages ttnn"
python3 - <<'PY'
import pathlib
try:
    import ttnn
    p = pathlib.Path(ttnn.__file__).parent
    for d in [p, p/'.libs', p/'build'/'lib']:
        if d.exists():
            for so in d.rglob('libtt_*.so'):
                print(so)
except Exception as e:
    print("ttnn import error:", e)
PY

# 4) Если libtt_stl.so НЕ найден, попробуем дособрать его в tt-metal
if ! find "${TT_METAL_HOME}" -maxdepth 6 -type f -name 'libtt_stl.so' | grep -q . ; then
  echo "[build] Пытаюсь дособрать tt-metal (ищу libtt_stl.so)"
  # предпочитаем build_Release если есть
  if [ -d "${TT_METAL_HOME}/build_Release" ]; then
    pushd "${TT_METAL_HOME}/build_Release" >/dev/null
    cmake --build . --config Release -j"$(nproc)" || true
    cmake --build . --target tt_stl --config Release -j"$(nproc)" || true
    cmake --build . --target libtt_stl --config Release -j"$(nproc)" || true
    popd >/dev/null
  elif [ -d "${TT_METAL_HOME}/build" ]; then
    pushd "${TT_METAL_HOME}/build" >/dev/null
    cmake --build . --config Release -j"$(nproc)" || true
    cmake --build . --target tt_stl --config Release -j"$(nproc)" || true
    cmake --build . --target libtt_stl --config Release -j"$(nproc)" || true
    popd >/dev/null
  else
    echo "[warn] build каталоги не найдены. Пропускаю точечную сборку."
  fi
fi

# 5) Ещё раз соберём корректный LD_LIBRARY_PATH
TTNN_ROOT="$(python3 - <<'PY'
import pathlib
try:
    import ttnn
    print(pathlib.Path(ttnn.__file__).parent)
except Exception:
    print("")
PY
)"

TTNN_PATHS=""
[ -n "${TTNN_ROOT}" ] && [ -d "${TTNN_ROOT}/build/lib" ] && TTNN_PATHS="${TTNN_ROOT}/build/lib"
[ -n "${TTNN_ROOT}" ] && [ -d "${TTNN_ROOT}/.libs" ] && TTNN_PATHS="${TTNN_PATHS:+${TTNN_PATHS}:}${TTNN_ROOT}/.libs"
[ -n "${TTNN_ROOT}" ] && TTNN_PATHS="${TTNN_PATHS:+${TTNN_PATHS}:}${TTNN_ROOT}"

CANDIDATES="${TT_METAL_HOME}/build_Release/lib:${TT_METAL_HOME}/build_Release/tt_metal:${TT_METAL_HOME}/build/lib"
export LD_LIBRARY_PATH="${CANDIDATES}:${TTNN_PATHS}:${LD_LIBRARY_PATH:-}"
echo "[env] LD_LIBRARY_PATH=${LD_LIBRARY_PATH}"

# 6) Короткая проверка импорта с трассировкой загрузчика
set +e
LD_DEBUG=libs python3 -c "import ttnn_device_extension as m; print(m.__file__)" 1>"${REPO_ROOT}/debug-ttnn-loader.out" 2>&1
RC=$?
set -e
echo "[loader] rc=${RC}"
head -n 120 "${REPO_ROOT}/debug-ttnn-loader.out" || true

exit ${RC}


