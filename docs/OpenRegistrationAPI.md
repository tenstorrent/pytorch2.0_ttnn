# Integrating TTNN with Pytorch Open Registration API

> **⚠️ UPDATE:**  
> TT-Metal is now **ONLY** supported as a git submodule.  
> **TT_METAL_HOME is IGNORED during build** (auto-detects from submodule), but **REQUIRED for running tests**.  
> See [docs/BuildFlow.md](BuildFlow.md) for the current workflow.

Pytorch Open Registration API allows integrating TTNN implementation into Torch. We can access TTNN ops from higher-level Torch calls.

# Build Instructions

The only supported build path uses tt-metal as a git submodule.

## Build Steps

1. Clone pytorch2.0_ttnn
    ```bash
    git clone https://github.com/tenstorrent/pytorch2.0_ttnn.git
    cd pytorch2.0_ttnn
    ```

2. Install dependencies
    ```bash
    apt update && apt install -y git-lfs cmake ninja-build python3 python3-venv python3-pip \
        build-essential clang-17 llvm-17-dev ccache
    ```

3. Build tt-metal and create the Python environment that ships with it
    ```bash
    cd torch_ttnn/cpp_extension/third-party/tt-metal
    git submodule update --init --recursive
    ./install_dependencies.sh
    ./build_metal.sh --release --enable-ccache
    ./create_venv.sh
    source ./python_env/bin/activate
    cd ../../../..  # Return to pytorch2.0_ttnn root
    ```
    
    **Note:** No environment variables needed! tt-metal scripts work within their directory, and pytorch2.0_ttnn CMake auto-detects the submodule.

4. Install pytorch2.0_ttnn inside the freshly created virtual environment
    ```bash
    python -m pip config set global.extra-index-url https://download.pytorch.org/whl/cpu
    python -m pip install --upgrade pip
    python -m pip install -e .[dev]
    ```

## Advanced: Custom PyTorch Build (Optional)

> **Note:** This section is optional and rarely needed. The standard workflow uses PyTorch from pip.

**When you might need this:**
- Debugging PyTorch C++ internals with gdb
- ABI compatibility issues (rare - usually auto-detected correctly)
- Testing unreleased PyTorch features

**Build PyTorch from source with clang-17 (for ABI compatibility with tt-metal):**

1. Remove existing torch
    ```bash
    pip uninstall -y torch torchvision
    ```

2. Install dependencies
    ```bash
    apt install libomp-17-dev
    pip install mkl-static mkl-include numpy==1.26.4
    ```

3. Clone and build PyTorch
    ```bash
    git clone https://github.com/pytorch/pytorch.git
    cd pytorch
    git checkout tags/v2.7.1
    git submodule sync && git submodule update --init --recursive
    pip install -r requirements.txt
    CC=clang-17 CXX=clang++-17 python setup.py develop
    cd ..
    ```

4. (Optional) Build torchvision
    ```bash
    git clone https://github.com/pytorch/vision
    cd vision
    git checkout v0.22.1
    CC=clang-17 CXX=clang++-17 python setup.py develop
    cd ..
    ```


## Running tests

Use the test runner script which handles all environment setup automatically:

```bash
cd torch_ttnn/cpp_extension
./run_cpp_extension_tests.sh ../tests/cpp_extension/test_cpp_extension_functionality.py -s
```

The script automatically:
- Activates the virtual environment
- Sets TT_METAL_HOME (required for tt-metal runtime to locate firmware/kernels)
- Ensures proper environment configuration

**Note:** `TT_METAL_HOME` is **not required for building** but **is required for running tests**.

Check to make sure `PYTHONPATH` is unset if you encounter import issues.

You can also run with `DEBUG_CPP_EXT=1` ENV to enable logging messages:
```bash
DEBUG_CPP_EXT=1 python -m pytest tests/cpp_extension/test_cpp_extension_functionality.py -s
```

## Troubleshooting
* Ensure `numpy < 2.0`

# References
https://github.com/bdhirsh/pytorch_open_registration_example