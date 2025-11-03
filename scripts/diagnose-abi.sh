#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

# Диагностика причины undefined symbol и ABI

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

echo "[python] $(command -v python3)"
python3 - <<'PY'
import torch, sys
print('[torch] version   =', getattr(torch, '__version__', 'unknown'))
print('[torch] cuda?     =', torch.cuda.is_available())
print('[torch] path      =', torch.__file__)
PY

# Найти расширение и его зависимости
EXT_SO="$(python3 - <<'PY'
import importlib.util, pathlib
spec = importlib.util.find_spec('ttnn_device_extension')
if spec and spec.origin and spec.origin.endswith('.so'):
    print(spec.origin)
else:
    for p in pathlib.Path('torch_ttnn/cpp_extension').glob('ttnn_device_extension*.so'):
        print(str(p))
        break
PY
)"

if [ -z "${EXT_SO}" ] || [ ! -f "${EXT_SO}" ]; then
  echo "[err] ttnn_device_extension .so не найден"
  exit 2
fi

echo "[ext] ${EXT_SO}"
ldd "${EXT_SO}" | sed 's/^/[ldd] /'

# Определить libc10.so, libtorch*.so, libtt_* из ldd
LIBC10_PATH="$(ldd "${EXT_SO}" | awk '/libc10\.so/ {print $3; exit}')"
LIBTORCH_CPU_PATH="$(ldd "${EXT_SO}" | awk '/libtorch_cpu\.so/ {print $3; exit}')"
LIBTORCH_SO_PATH="$(ldd "${EXT_SO}" | awk '/libtorch\.so/ {print $3; exit}')"
LIBTT_METAL_PATH="$(ldd "${EXT_SO}" | awk '/libtt_metal\.so/ {print $3; exit}')"
LIBTT_STL_PATH="$(ldd "${EXT_SO}" | awk '/libtt_stl\.so/ {print $3; exit}')"

echo "[paths] libc10        = ${LIBC10_PATH:-<missing>}"
echo "[paths] libtorch_cpu  = ${LIBTORCH_CPU_PATH:-<missing>}"
echo "[paths] libtorch      = ${LIBTORCH_SO_PATH:-<missing>}"
echo "[paths] libtt_metal   = ${LIBTT_METAL_PATH:-<missing>}"
echo "[paths] libtt_stl     = ${LIBTT_STL_PATH:-<missing>}"

# Проверить наличие символа в libc10
if [ -n "${LIBC10_PATH:-}" ] && [ -f "${LIBC10_PATH}" ]; then
  echo "[check] поиск символа в libc10.so"
  if nm -D --defined-only "${LIBC10_PATH}" | c++filt | grep -q "c10::Allocator::is_simple_data_ptr"; then
    echo "[ok] символ присутствует в libc10.so"
  else
    echo "[fail] символ ОТСУТСТВУЕТ в libc10.so (вероятно старая версия libtorch/c10)"
  fi
else
  echo "[warn] libc10.so не найден"
fi

# Диагностика libstdc++ ABI (_GLIBCXX_USE_CXX11_ABI) по образцам символов std::string
STDCPP_PATH="$(ldd "${EXT_SO}" | awk '/libstdc\+\+\.so/ {print $3; exit}')"
if [ -n "${STDCPP_PATH:-}" ] && [ -f "${STDCPP_PATH}" ]; then
  echo "[stdc++] $(strings -a "${STDCPP_PATH}" | grep -Eo 'GLIBCXX_[0-9\.]+(\.\d+)?' | sort -u | tail -n 1)"
fi

# Показать откуда _ttnncpp.so берётся
TTNNCPP_PATHS=( $(ldd "${EXT_SO}" | awk '/_ttnncpp\.so/ {print $3}') )
echo "[paths] _ttnncpp.so = ${TTNNCPP_PATHS[*]:-<missing>}"

echo "[hint] Если символа нет в libc10.so — установите совместимую версию torch в текущее окружение и пересоберите расширение."
echo "       Пример: python3 -m pip install --upgrade --extra-index-url https://download.pytorch.org/whl/cpu torch"

exit 0


