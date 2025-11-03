#!/usr/bin/env bash

set -euo pipefail
trap 'echo "ERROR: команда завершилась с ошибкой: $BASH_COMMAND"; exit 1' ERR

# Полная локальная репликация job `cpp-extension-tests` из
# .github/workflows/run-cpp-native-tests.yaml (1-в-1 команды).
# Запускать из любого места — скрипт сам перейдет в корень репозитория.

# Определяем корень репозитория
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

# Эмуляция переменных окружения GitHub Actions
export GITHUB_WORKSPACE="${REPO_ROOT}"

###############################################################################
# Step: Checkout (LFS + full history + submodules)
###############################################################################
if command -v git-lfs >/dev/null 2>&1; then
  git lfs fetch --all || true
  git lfs pull || true
else
  echo "Warning: git-lfs not installed, skipping LFS operations"
fi

SHALLOW_REPO=$(git rev-parse --is-shallow-repository 2>/dev/null || echo "false")
if [ "$SHALLOW_REPO" = "true" ]; then
  git fetch --unshallow || true
fi

###############################################################################
# Step: Setup submodules
###############################################################################
# Allow git operations in runner workspace paths
git config --global --add safe.directory "${GITHUB_WORKSPACE}" || true
git config --global --add safe.directory "${GITHUB_WORKSPACE}/torch_ttnn/cpp_extension/third-party/tt-metal" || true

# Add all nested submodules to safe.directory to avoid "dubious ownership" errors
# This is needed when running in containers or with different file ownership
find "${GITHUB_WORKSPACE}/torch_ttnn/cpp_extension/third-party/tt-metal" -name ".git" -type d 2>/dev/null | while read -r gitdir; do
  submodule_path=$(dirname "$gitdir")
  git config --global --add safe.directory "$submodule_path" 2>/dev/null || true
done
# Also handle .git files (submodule pointers)
find "${GITHUB_WORKSPACE}/torch_ttnn/cpp_extension/third-party/tt-metal" -name ".git" -type f 2>/dev/null | while read -r gitfile; do
  submodule_path=$(dirname "$gitfile")
  git config --global --add safe.directory "$submodule_path" 2>/dev/null || true
done

# Retry helper with exponential backoff
retry() {
  local max_attempts=${1:-5}; shift
  local attempt=1
  until "$@"; do
    if (( attempt >= max_attempts )); then
      echo "Command failed after ${attempt} attempts: $*"
      return 1
    fi
    echo "Command failed (attempt ${attempt}/${max_attempts}): $*"
    sleep $(( 2 ** attempt ))
    ((attempt++))
  done
}

# Be tolerant to network hiccups for submodule operations
retry 5 git submodule sync --recursive
retry 5 git submodule update --init --recursive

# Fetch all branches and tags to ensure we have the version specified in .gitmodules
pushd torch_ttnn/cpp_extension/third-party/tt-metal >/dev/null
retry 5 git fetch --all --tags --force --prune
# Update to the branch specified in .gitmodules (no override)
retry 5 git submodule update --init --recursive --force
if command -v git-lfs >/dev/null 2>&1; then
  git lfs fetch --all || true
  git lfs pull || true
fi
echo "Current tt-metal version:"
git log --oneline -1
git describe --tags || git rev-parse HEAD
popd >/dev/null

###############################################################################
# Step: Install and configure ccache
###############################################################################
# ccache is required for efficient builds
if ! command -v ccache >/dev/null 2>&1; then
  echo "ccache not found, installing..."
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq && apt-get install -y ccache
  elif command -v yum >/dev/null 2>&1; then
    yum install -y ccache
  else
    echo "ERROR: Cannot install ccache automatically. Please install it manually." >&2
    exit 1
  fi
fi

CCACHE_DIR="${CCACHE_DIR:-.cache/ccache}"
mkdir -p "${CCACHE_DIR}"
ccache --set-config=cache_dir="${CCACHE_DIR}"
ccache --set-config=max_size="30G"
ccache --set-config=base_dir="${GITHUB_WORKSPACE}"
ccache --set-config=compression=true
ccache --zero-stats

###############################################################################
# Step: Build tt-metal native libs (matches CI workflow)
###############################################################################
# NOTE: TT_METAL_HOME is deprecated in latest tt-metal versions.
# CMake uses automatic discovery via find_package(tt-metal) to locate headers and libraries.
# We set it here only for legacy build script support, but it's not required for CMake builds.
export TT_METAL_HOME="${GITHUB_WORKSPACE}/torch_ttnn/cpp_extension/third-party/tt-metal"
export PYTHON_ENV_DIR="${GITHUB_WORKSPACE}/torch_ttnn/cpp_extension/third-party/tt-metal/python_env"
export CPM_SOURCE_CACHE="${GITHUB_WORKSPACE}/.cache/cpm"
export TT_METAL_TOOLS_DIR="${TT_METAL_HOME}/.local/bin"
mkdir -p "${CPM_SOURCE_CACHE}" "${TT_METAL_TOOLS_DIR}"

if ! command -v clang-17 >/dev/null 2>&1 || ! command -v clang++-17 >/dev/null 2>&1; then
  echo "Warning: clang-17/clang++-17 not found in PATH, using default compiler"
else
  export CC="${CC:-$(command -v clang-17)}"
  export CXX="${CXX:-$(command -v clang++-17)}"
  export CMAKE_C_COMPILER="${CMAKE_C_COMPILER:-${CC}}"
  export CMAKE_CXX_COMPILER="${CMAKE_CXX_COMPILER:-${CXX}}"
fi

export PATH="${TT_METAL_TOOLS_DIR}:${PATH}"

if [ -d "${TT_METAL_HOME}" ]; then
  echo "Building tt-metal native libraries at ${TT_METAL_HOME}"
  cd "${TT_METAL_HOME}"
  
  # Run install dependencies
  if [ -f "./install_dependencies.sh" ]; then
    ./install_dependencies.sh || true
  fi
  
  # Clean previous builds
  rm -rf build build_Release "${PYTHON_ENV_DIR}" 2>/dev/null || true
  
  # Find ninja
  NINJA_BIN="$(command -v ninja || true)"
  if [[ -z "${NINJA_BIN}" ]]; then
    echo "ninja not found in PATH" >&2
    exit 1
  fi
  export CMAKE_MAKE_PROGRAM="${NINJA_BIN}"
  
  # Build TT-Metal - generates build_Release/ with libraries and CMake configs
  ./build_metal.sh --release --enable-ccache
  
  # Create Python venv for tt-metal
  ./create_venv.sh
  if [[ ! -f "${PYTHON_ENV_DIR}/bin/activate" ]]; then
    echo "ERROR: Expected virtual environment not found at ${PYTHON_ENV_DIR}" >&2
    find "${TT_METAL_HOME}" -maxdepth 2 -type d -print >&2 || true
    exit 1
  fi
  
  # Activate venv
  source "${PYTHON_ENV_DIR}/bin/activate"
  export PATH="${TT_METAL_TOOLS_DIR}:${PATH}"
  
  cd "${GITHUB_WORKSPACE}"
else
  echo "ERROR: TT_METAL_HOME not found at ${TT_METAL_HOME}"
  exit 1
fi

###############################################################################
# Step: Install root package and dependencies
###############################################################################
# Set Python to use venv
PYTHON="python"
echo "Using Python: $(which ${PYTHON})"

# Configure PyPI extras
${PYTHON} -m pip config set global.extra-index-url https://download.pytorch.org/whl/cpu
${PYTHON} -m pip install --upgrade pip
${PYTHON} -m pip install --upgrade "scikit-build-core<0.11" cmake ninja

# Check if this is a ttnn-wheel-update PR (triggered by automated dependency update)
# If so, use [pypi,dev] to test the new ttnn version
# Otherwise use [dev] only (preserves locally built ttnn)
if git log --oneline -1 | grep -q "Update dependencies to"; then
  echo "Detected ttnn wheel update PR - installing with [pypi,dev] to test new ttnn"
  ${PYTHON} -m pip install -e "${GITHUB_WORKSPACE}"[pypi,dev]
else
  echo "Regular build - installing with [dev] only (uses local ttnn)"
  ${PYTHON} -m pip install -e "${GITHUB_WORKSPACE}"[dev]
fi

# Show ccache stats after build
ccache --show-stats

###############################################################################
# Step: Run C++ Extension Tests
###############################################################################
# NOTE: LD_LIBRARY_PATH is no longer required!
# The extension's RPATH is configured to include PyTorch's library directory automatically.
# CMake sets BUILD_RPATH="$ORIGIN:${PYTORCH_LIB_DIR}" during the build process.
echo "Running C++ extension functionality tests"
${PYTHON} -m pytest "${GITHUB_WORKSPACE}/tests/cpp_extension/test_cpp_extension_functionality.py" -v

echo "Running BERT C++ extension tests"
${PYTHON} -m pytest "${GITHUB_WORKSPACE}/tests/cpp_extension/test_bert_cpp_extension.py" -v

echo "Running models C++ extension tests"
${PYTHON} -m pytest "${GITHUB_WORKSPACE}/tests/models" --native_integration -v

echo "All tests passed!"


