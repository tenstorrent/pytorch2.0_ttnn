#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

# Изолированная диагностика рантайма: где лежат libtt_*.so и что подгружается

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

LOG_DIR="${REPO_ROOT}"
LOG_FILE="${LOG_DIR}/debug-ttnn-runtime.log"
: > "${LOG_FILE}"

echo "[env] LD_LIBRARY_PATH=${LD_LIBRARY_PATH:-}" | tee -a "${LOG_FILE}"
echo "[env] PYTHONPATH=${PYTHONPATH:-}" | tee -a "${LOG_FILE}"

# Определяем TT_METAL_HOME и пути пакета ttnn/расширения
export TT_METAL_HOME="${TT_METAL_HOME:-$(realpath ./torch_ttnn/cpp_extension/third-party/tt-metal)}"

python3 - <<'PY' 2>&1 | tee -a "debug-ttnn-runtime.log"
import sys, pathlib, json
info = {}
info['sys_path'] = sys.path
try:
    import ttnn
    ttnn_root = pathlib.Path(ttnn.__file__).parent
    info['ttnn_root'] = str(ttnn_root)
    info['ttnn_build_lib'] = str(ttnn_root / 'build' / 'lib')
    info['ttnn_dotlibs'] = str(ttnn_root / '.libs')
except Exception as e:
    info['ttnn_import_error'] = repr(e)

try:
    import importlib
    m = importlib.import_module('ttnn_device_extension')
    info['ttnn_device_extension'] = str(pathlib.Path(m.__file__))
except Exception as e:
    info['ttnn_device_extension_error'] = repr(e)

print(json.dumps(info, indent=2))
PY

echo "[find] Поиск libtt_*.so" | tee -a "${LOG_FILE}"
{
  echo "-- TT_METAL_HOME=${TT_METAL_HOME}"
  find "${TT_METAL_HOME}" -maxdepth 4 -type f -name 'libtt_*.so' 2>/dev/null || true
  echo "-- ttnn site-package"
  python3 - <<'PY'
import pathlib, sys
try:
    import ttnn
    p = pathlib.Path(ttnn.__file__).parent
    for d in [p, p/'.libs', p/'build'/'lib']:
        if d.exists():
            for so in d.rglob('libtt_*.so'):
                print(so)
except Exception:
    pass
PY
  echo "-- project build outputs"
  find ./torch_ttnn/cpp_extension -type f \( -name 'libtt_*.so' -o -name '*ttnn_device_extension*.so' \) 2>/dev/null || true
} | tee -a "${LOG_FILE}"

# Определяем путь к расширению для ldd
EXT_SO_PATH="$(python3 - <<'PY'
try:
    import importlib, pathlib
    m = importlib.import_module('ttnn_device_extension')
    print(pathlib.Path(m.__file__))
except Exception:
    print("")
PY
)"

if [ -n "${EXT_SO_PATH}" ] && [ -f "${EXT_SO_PATH}" ]; then
  echo "[ldd] ttnn_device_extension => ${EXT_SO_PATH}" | tee -a "${LOG_FILE}"
  ldd "${EXT_SO_PATH}" | tee -a "${LOG_FILE}"
else
  echo "[ldd] ttnn_device_extension не импортируется (см. ошибки выше)" | tee -a "${LOG_FILE}"
fi

# ldd для найденных libtt_*.so
echo "[ldd] libtt_*.so" | tee -a "${LOG_FILE}"
{
  for so in $(find "${TT_METAL_HOME}" -maxdepth 4 -type f -name 'libtt_*.so' 2>/dev/null); do
    echo "-- ${so}"; ldd "${so}" || true; echo
  done
} | tee -a "${LOG_FILE}"

# Трассировка загрузчика (libs) при импорте расширения
echo "[loader] LD_DEBUG=libs импорт ttnn_device_extension" | tee -a "${LOG_FILE}"
set +e
LD_DEBUG=libs python3 -c "import ttnn_device_extension as m; print(m.__file__)" 1>debug-ttnn-loader.out 2>&1
RC=$?
set -e
echo "[loader] rc=${RC}" | tee -a "${LOG_FILE}"

if [ -f debug-ttnn-loader.out ]; then
  echo "[loader] первые 120 строк:" | tee -a "${LOG_FILE}"
  head -n 120 debug-ttnn-loader.out | tee -a "${LOG_FILE}"
fi

# Предложение по LD_LIBRARY_PATH
echo "[hint] Предлагаемый LD_LIBRARY_PATH:" | tee -a "${LOG_FILE}"
PY_HINT="$(python3 - <<'PY'
import pathlib
paths=[]
try:
    import ttnn
    p = pathlib.Path(ttnn.__file__).parent
    for d in [p/'build'/'lib', p/'.libs', p]:
        if d.exists():
            paths.append(str(d))
except Exception:
    pass
print(':'.join(paths))
PY
)"
echo "export LD_LIBRARY_PATH=\"${TT_METAL_HOME}/build/lib:${PY_HINT}:","\${LD_LIBRARY_PATH:-}\"" | tee -a "${LOG_FILE}"

echo "Готово. Подробный лог: ${LOG_FILE}" | tee -a "${LOG_FILE}"


