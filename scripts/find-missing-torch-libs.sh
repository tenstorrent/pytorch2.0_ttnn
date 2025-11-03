#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

# Находит отсутствующие .so из ttnn_device_extension и явно показывает, где их искать

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

log() { echo -e "$*"; }

# 1) Определим .so расширения
EXT_SO_PATH="$(python3 - <<'PY'
import sys, pathlib, importlib.util
names = ['ttnn_device_extension']
for name in names:
    spec = importlib.util.find_spec(name)
    if spec and spec.origin and spec.origin.endswith('.so'):
        print(spec.origin)
        break
else:
    # запасной путь — искать в дереве репо
    for p in pathlib.Path('torch_ttnn/cpp_extension').glob('ttnn_device_extension*.so'):
        print(str(p))
        break
PY
)"

if [ -z "${EXT_SO_PATH}" ] || [ ! -f "${EXT_SO_PATH}" ]; then
  log "[err] Не найден ttnn_device_extension*.so для анализа (попробуйте собрать расширение)"
  exit 2
fi

log "[info] Расширение: ${EXT_SO_PATH}"

# 2) ldd и сбор имён отсутствующих .so
MISSING_SOS=()
while IFS= read -r line; do
  name="$(awk '{print $1}' <<<"${line}")"
  MISSING_SOS+=("${name}")
done < <(ldd "${EXT_SO_PATH}" | grep '=> not found' || true)

if [ ${#MISSING_SOS[@]} -eq 0 ]; then
  log "[ok] Отсутствующих зависимостей не обнаружено"
  exit 0
fi

log "[miss] Отсутствуют: ${MISSING_SOS[*]}"

# 3) Сформируем корни поиска
SEARCH_ROOTS=()

# PyTorch: корень пакета и поддиректории
TORCH_ROOT="$(python3 - <<'PY'
import pathlib
try:
    import torch
    print(pathlib.Path(torch.__file__).parent)
except Exception: print("")
PY
)"
if [ -n "${TORCH_ROOT}" ]; then
  SEARCH_ROOTS+=("${TORCH_ROOT}")
  [ -d "${TORCH_ROOT}/lib" ] && SEARCH_ROOTS+=("${TORCH_ROOT}/lib")
fi

# site-packages
SITE_PKGS=( $(python3 - <<'PY'
import site
for d in set(site.getsitepackages() + [site.getusersitepackages()]):
    print(d)
PY
) )
for d in "${SITE_PKGS[@]:-}"; do
  [ -n "${d}" ] && SEARCH_ROOTS+=("${d}")
done

# venv/conda
[ -n "${VIRTUAL_ENV:-}" ] && SEARCH_ROOTS+=("${VIRTUAL_ENV}/lib" "${VIRTUAL_ENV}")
[ -n "${CONDA_PREFIX:-}" ] && SEARCH_ROOTS+=("${CONDA_PREFIX}/lib" "${CONDA_PREFIX}")

# TT_METAL
TT_METAL_HOME="${TT_METAL_HOME:-${REPO_ROOT}/torch_ttnn/cpp_extension/third-party/tt-metal}"
SEARCH_ROOTS+=("${TT_METAL_HOME}/build_Release/lib" "${TT_METAL_HOME}/build_Release/tt_metal" "${TT_METAL_HOME}/build/lib")

# TTNN
TTNN_ROOT="$(python3 - <<'PY'
import pathlib
try:
    import ttnn
    p = pathlib.Path(ttnn.__file__).parent
    print(p)
except Exception: print("")
PY
)"
if [ -n "${TTNN_ROOT}" ]; then
  SEARCH_ROOTS+=("${TTNN_ROOT}" "${TTNN_ROOT}/build/lib" "${TTNN_ROOT}/.libs")
fi

# Системные
SEARCH_ROOTS+=("/usr/local/lib" "/usr/local/lib64" "/usr/lib" "/usr/lib64" "/lib" "/lib64")

# Уникализируем
uniq_lines() {
  awk '!x[$0]++'
}
mapfile -t SEARCH_ROOTS < <(printf '%s\n' "${SEARCH_ROOTS[@]}" | uniq_lines)

log "[info] Корни поиска (${#SEARCH_ROOTS[@]}):"
for r in "${SEARCH_ROOTS[@]}"; do
  [ -d "${r}" ] && echo "  - ${r}"
done

# 4) Поиск каждого отсутствующего .so
FOUND_DIRS=()
for so in "${MISSING_SOS[@]}"; do
  echo "[find] ${so}"
  found_any=0
  for root in "${SEARCH_ROOTS[@]}"; do
    [ -d "${root}" ] || continue
    while IFS= read -r p; do
      [ -n "${p}" ] || continue
      echo "  -> ${p}"
      FOUND_DIRS+=("$(dirname "${p}")")
      found_any=1
    done < <(find "${root}" -type f -name "${so}" 2>/dev/null || true)
  done
  if [ ${found_any} -eq 0 ]; then
    echo "  !! НЕ НАЙДЕНО в рассмотренных директориях"
  fi
done

# 5) Рекомендованный LD_LIBRARY_PATH
if [ ${#FOUND_DIRS[@]} -gt 0 ]; then
  mapfile -t FOUND_DIRS < <(printf '%s\n' "${FOUND_DIRS[@]}" | uniq_lines)
  REC_LD="$(IFS=":"; echo "${FOUND_DIRS[*]}")"
  echo
  echo "[hint] Добавьте в LD_LIBRARY_PATH (перед существующим):"
  echo "export LD_LIBRARY_PATH=\"${REC_LD}:\${LD_LIBRARY_PATH:-}\""
fi

exit 0
