#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

# Подготовка LD_LIBRARY_PATH для корректного импорта ttnn_device_extension

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

# Activate tt-metal venv if it exists
TT_METAL_VENV="${REPO_ROOT}/torch_ttnn/cpp_extension/third-party/tt-metal/python_env"
if [ -f "${TT_METAL_VENV}/bin/activate" ]; then
    echo "> Activating tt-metal venv: ${TT_METAL_VENV}"
    source "${TT_METAL_VENV}/bin/activate"
    echo "> Python: $(which python3)"
else
    echo "> Warning: tt-metal venv not found at ${TT_METAL_VENV}"
    echo "> Continuing with system Python: $(which python3)"
fi

# Диагностика Python окружения
echo "[python] which python3: $(command -v python3)"
python3 - <<'PY'
import sys, site, platform
print('[python] sys.executable =', sys.executable)
print('[python] sys.version    =', sys.version.split('\n')[0])
print('[python] site-packages  =', site.getsitepackages())
print('[python] user-site      =', site.getusersitepackages())
print('[python] platform       =', platform.platform())
PY

# TT_METAL_HOME по сабмодулю
export TT_METAL_HOME="${TT_METAL_HOME:-${REPO_ROOT}/torch_ttnn/cpp_extension/third-party/tt-metal}"

# Убедимся, что директория расширения доступна Python
export PYTHONPATH="${REPO_ROOT}/torch_ttnn/cpp_extension:${PYTHONPATH:-}"
echo "[paths] PYTHONPATH prefix added: ${REPO_ROOT}/torch_ttnn/cpp_extension"

# Соберём кандидаты путей к .so из установленного ttnn и всех site-packages
export TTNN_LIB_PATHS=$(python3 - <<'PY'
import pathlib, sys
lib_dirs = []
def add(p):
    if p.exists():
        s = str(p)
        if s not in lib_dirs:
            lib_dirs.append(s)
try:
    import ttnn, site
    ttnn_root = pathlib.Path(ttnn.__file__).parent
    # Типовые поддиректории
    for d in [ttnn_root/'build'/'lib', ttnn_root/'.libs', ttnn_root]:
        add(d)
    # Все site-packages (системные и пользовательские)
    site_dirs = set(site.getsitepackages() + [site.getusersitepackages()])
    for sd in site_dirs:
        base = pathlib.Path(sd)/'ttnn'
        for d in [base/'build'/'lib', base/'.libs', base]:
            add(d)
    # Явный поиск реальных местоположений libtt_*.so и добавление их директорий
    for root in [ttnn_root] + [pathlib.Path(s)/'ttnn' for s in site_dirs]:
        if root.exists():
            for so in root.rglob('libtt_*.so'):
                add(so.parent)
except Exception:
    pass
print(':'.join(lib_dirs))
PY
)

# Пути к библиотекам PyTorch (libtorch, libc10, libtorch_python и др.) из текущего Python
export TORCH_LIB_DIRS=$(python3 - <<'PY'
import pathlib, site, sys
dirs = []
try:
    import torch
    root = pathlib.Path(torch.__file__).parent
    libdir = root / 'lib'
    if libdir.exists():
        dirs.append(str(libdir))
    names = {'libc10.so','libtorch.so','libtorch_cpu.so','libtorch_python.so'}
    for so in root.rglob('*.so'):
        if so.name in names:
            pd = str(so.parent)
            if pd not in dirs:
                dirs.append(pd)
except Exception:
    pass
# Дополнительно: просканировать все site-packages на предмет torch/lib
try:
    for sp in set(site.getsitepackages() + [site.getusersitepackages()]):
        td = pathlib.Path(sp) / 'torch' / 'lib'
        if td.exists():
            sd = str(td)
            if sd not in dirs:
                dirs.append(sd)
except Exception:
    pass
# Глобальные стандартные пути для системного python (dist-packages/site-packages)
maj, mn = sys.version_info[:2]
for base in ('/usr/local/lib', '/usr/lib'):
    for kind in ('dist-packages', 'site-packages'):
        td = pathlib.Path(base) / f'python{maj}.{mn}' / kind / 'torch' / 'lib'
        if td.exists():
            sd = str(td)
            if sd not in dirs:
                dirs.append(sd)
print(':'.join(dirs))
PY
)
echo "[paths] TORCH_LIB_DIRS:"
IFS=':' read -r -a _torch_dirs <<<"${TORCH_LIB_DIRS}"
for d in "${_torch_dirs[@]:-}"; do
  [ -n "${d}" ] && echo "  - ${d} $( [ -d \"${d}\" ] && echo '[ok]' || echo '[miss]' )"
done

# Каталоги сборки проекта, которые могут содержать зависимости
EXT_BUILD_DIR="${REPO_ROOT}/torch_ttnn/cpp_extension/build/lib.linux-x86_64-3.10"
[ -d "${EXT_BUILD_DIR}" ] || EXT_BUILD_DIR=""
echo "[paths] EXT_BUILD_DIR=${EXT_BUILD_DIR:-<empty>} $( [ -n "${EXT_BUILD_DIR}" ] && echo '[ok]' || echo '' )"

# Кандидаты tt-metal (на случай, если нужны libdevice.so и пр.)
TT_METAL_LIBS="${TT_METAL_HOME}/build_Release/lib:${TT_METAL_HOME}/build_Release/tt_metal:${TT_METAL_HOME}/build/lib"
echo "[paths] TT_METAL_HOME=${TT_METAL_HOME}"
IFS=':' read -r -a _ttm_dirs <<<"${TT_METAL_LIBS}"
for d in "${_ttm_dirs[@]}"; do
  echo "  - ${d} $( [ -d "${d}" ] && echo '[ok]' || echo '[miss]' )"
done

echo "[paths] TTNN_LIB_PATHS candidates:"
IFS=':' read -r -a _ttnn_dirs <<<"${TTNN_LIB_PATHS}"
for d in "${_ttnn_dirs[@]}"; do
  echo "  - ${d} $( [ -d "${d}" ] && echo '[ok]' || echo '[miss]' )"
done

# Явно найдём фактические libtt_*.so и покажем их расположение
python3 - <<'PY'
import pathlib, site, json
found = {
  'libtt_stl': [],
  'libtt_metal': []
}
dirs = set(site.getsitepackages() + [site.getusersitepackages()])
for sd in dirs:
    base = pathlib.Path(sd)
    for so in base.rglob('libtt_*.so'):
        name = so.name
        if name == 'libtt_stl.so':
            found['libtt_stl'].append(str(so))
        if name == 'libtt_metal.so':
            found['libtt_metal'].append(str(so))
print('[libs] found:', json.dumps(found, indent=2))
PY

# Итоговый LD_LIBRARY_PATH
export LD_LIBRARY_PATH="${TT_METAL_LIBS}:${TTNN_LIB_PATHS}:${TORCH_LIB_DIRS:+${TORCH_LIB_DIRS}:}${EXT_BUILD_DIR:+${EXT_BUILD_DIR}:}${LD_LIBRARY_PATH:-}"
echo "LD_LIBRARY_PATH=${LD_LIBRARY_PATH}"

# Покажем где лежит ttnn и расширение
python3 - <<'PY'
import pathlib, importlib, json
info = {}
try:
    import ttnn
    p = pathlib.Path(ttnn.__file__).parent
    info['ttnn_root'] = str(p)
    info['ttnn_build_lib'] = str(p/'build'/'lib')
    info['ttnn_dotlibs'] = str(p/'.libs')
except Exception as e:
    info['ttnn_error'] = repr(e)

try:
    m = importlib.import_module('ttnn_device_extension')
    info['ttnn_device_extension'] = str(pathlib.Path(m.__file__))
except Exception as e:
    info['ttnn_device_extension_error'] = repr(e)

print(json.dumps(info, indent=2))
PY

# Попробуем найти .so расширения и показать его зависимости
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
if [ -n "${EXT_SO_PATH}" ] && [ -f "${EXT_SO_PATH}" ]; then
  echo "[ldd] ${EXT_SO_PATH}"
  ldd "${EXT_SO_PATH}" || true
else
  echo "[ldd] ttnn_device_extension .so не найден"
fi

# Проверка импорта с трассировкой загрузчика
set +e
LD_DEBUG=libs python3 -c "import ttnn_device_extension as m; print(m.__file__)" 1>"${REPO_ROOT}/debug-ttnn-loader.out" 2>&1
RC=$?
set -e
echo "LD_DEBUG rc=${RC} (первые 120 строк):"
head -n 120 "${REPO_ROOT}/debug-ttnn-loader.out" || true

exit ${RC}


