#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

# Изолированная реплика шага "Build C++ Extension" для tt-metal/ttnn
# Без git sync/submodule операций. Запускайте из любого места.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

export TT_METAL_HOME="${TT_METAL_HOME:-$(realpath ./torch_ttnn/cpp_extension/third-party/tt-metal)}"

# Determine tt-metal version for CMake
# Try to get version from git tag, fallback to TT_METAL_REF env var, or default
TT_METAL_VERSION=""
if [ -d "$TT_METAL_HOME/.git" ]; then
    # Try to get version from git describe
    TT_METAL_VERSION=$(cd "$TT_METAL_HOME" && git describe --abbrev=0 --tags 2>/dev/null | sed 's/^v//' || echo "")
fi
if [ -z "$TT_METAL_VERSION" ] && [ -n "${TT_METAL_REF:-}" ]; then
    # Use TT_METAL_REF if provided (e.g., v0.60.1 -> 0.60.1)
    TT_METAL_VERSION="${TT_METAL_REF#v}"
fi
if [ -z "$TT_METAL_VERSION" ]; then
    # Fallback to default version
    TT_METAL_VERSION="0.60.1"
    echo "> Warning: Could not determine tt-metal version, using fallback: $TT_METAL_VERSION"
else
    echo "> Detected tt-metal version: $TT_METAL_VERSION"
fi

# Activate tt-metal venv if it exists
TT_METAL_VENV="${TT_METAL_HOME}/python_env"
if [ -f "${TT_METAL_VENV}/bin/activate" ]; then
    echo "> Activating tt-metal venv: ${TT_METAL_VENV}"
    source "${TT_METAL_VENV}/bin/activate"
    echo "> Python: $(which python3)"
else
    echo "> Warning: tt-metal venv not found at ${TT_METAL_VENV}"
    echo "> Continuing with system Python: $(which python3)"
fi
TOOLCHAIN_PATH="cmake/x86_64-linux-clang-17-libstdcpp-toolchain.cmake"

# Проверки окружения
echo "Python: $(python3 -V)"
echo "Pip: $(python3 -m pip -V)"
command -v clang-17 >/dev/null 2>&1 && clang-17 --version || echo "clang-17 НЕ найден (это может привести к провалу сборки)"
command -v cmake >/dev/null 2>&1 && cmake --version || true
command -v ninja >/dev/null 2>&1 && ninja --version || true

# 1) Подтянуть инструменты для сборки колёс
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade scikit-build-core cmake ninja pybind11

# 2) Настройка окружения как в CI
export CC=clang-17
export CXX=clang++-17

# CMAKE_PREFIX_PATH из текущего Python (если torch установлен)
set +e
CMAKE_PREFIX_PATH_VAL=$(python3 - <<'PY'
try:
    import torch
    print(torch.utils.cmake_prefix_path)
except Exception:
    print("")
PY
)
set -e
export CMAKE_PREFIX_PATH="${CMAKE_PREFIX_PATH_VAL}"

# Pass VERSION_NUMERIC to tt-metal CMake to avoid fallback warnings
export CMAKE_ARGS="-DCMAKE_TOOLCHAIN_FILE=${TT_METAL_HOME}/${TOOLCHAIN_PATH} -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER_LAUNCHER=ccache -DCMAKE_CXX_COMPILER_LAUNCHER=ccache -DWITH_PYTHON_BINDINGS=ON -DVERSION_NUMERIC=${TT_METAL_VERSION}"
export LD_LIBRARY_PATH="${TT_METAL_HOME}/build/lib:${LD_LIBRARY_PATH:-}"

# 3) Чистая установка ttnn из исходников сабмодуля
python3 -m pip uninstall -y ttnn || true
unset VIRTUAL_ENV || true
USER_SCRIPTS_DIR=$(python3 -c 'import sysconfig; print(sysconfig.get_path("scripts"))')
export PATH="${USER_SCRIPTS_DIR}:${PATH}"

echo "Начинаю сборку ttnn из ${TT_METAL_HOME}"
# Note: CMAKE_ARGS with VERSION_NUMERIC is already set above, scikit-build-core will pass it to tt-metal's CMake
python3 -m pip install -v --no-build-isolation "${TT_METAL_HOME}" 2>&1 | tee run-build.err

# 4) Ранняя проверка наличия модуля
set +e
python3 - <<'PY'
import os, importlib, pathlib, sys
print('TT_METAL_HOME=', os.environ.get('TT_METAL_HOME'))
try:
    import ttnn
    importlib.import_module('ttnn._ttnn')
    lib_dir = pathlib.Path(ttnn.__file__).parent.joinpath('build','lib')
    print('ttnn импортирован OK, build lib dir =', lib_dir)
except Exception as e:
    print('ОШИБКА импорта ttnn/_ttnn:', e)
    sys.exit(1)
PY
rc=$?
set -e

if [[ $rc -ne 0 ]]; then
  echo "Сборка неуспешна. Ключевые подсказки по диагностике:"
  echo "- Установлен ли clang-17? (см. вывод выше)"
  echo "- Заполнён ли CMAKE_PREFIX_PATH (особенно если нужен torch)? Текущее: '${CMAKE_PREFIX_PATH}'"
  echo "- Просмотрите первые реальные ошибки компиляции в run-build.err:"
  echo "    grep -nE '\\b(error:|fatal error:|No such file or directory)\\b' run-build.err | head -n 50"
  exit 1
fi

echo "Сборка и импорт ttnn успешны"


