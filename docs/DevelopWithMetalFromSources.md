# Develop with TT-Metal build from source

This document shows how to develop pytorch2.0_ttnn with tt-metal built from source (using the git submodule).

> **📖 For complete build instructions:** See [docs/BuildFlow.md](BuildFlow.md)

---

## Quick Start

TT-Metal lives as a **git submodule** at `torch_ttnn/cpp_extension/third-party/tt-metal`. The build system automatically detects it.

### 1. Clone and initialize submodule
```console
git clone --recursive https://github.com/tenstorrent/pytorch2.0_ttnn.git
cd pytorch2.0_ttnn
```

### 2. One-time setup: Install system dependencies
```console
cd torch_ttnn/cpp_extension/third-party/tt-metal
sudo ./install_dependencies.sh
cd -
```

### 3. Build everything using the build script
```console
cd torch_ttnn/cpp_extension
./build_cpp_extension.sh              # Release build (default)
# ./build_cpp_extension.sh Debug      # Or Debug build
# ./build_cpp_extension.sh RelWithDebInfo  # Or with debug info
```

The build script handles:
- Building TT-Metal from the submodule
- Creating Python virtual environment  
- Installing torch-ttnn with C++ extension

**✅ No TT_METAL_HOME needed for building!** 
- The build script handles everything automatically
- pytorch2.0_ttnn CMake auto-detects the submodule
- If you have TT_METAL_HOME set, the build system will ignore it

After the build completes, activate the virtual environment:
```console
source third-party/tt-metal/python_env/bin/activate
```

Things are going well if you can now call `ipython` and see:
```console
(python_env) $ ipython
Python 3.10.12 (default, Nov  7 2024, 13:10:47) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.3 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import ttnn
2024-12-13 00:02:45.792 | DEBUG    | ttnn:<module>:82 - Initial ttnn.CONFIG:
...
In [2]: import torch_ttnn
In [3]: print('✓ Both packages available')
```

**Manual build (alternative):** See [BuildFlow.md](BuildFlow.md) for step-by-step manual build instructions.

---

## Run tests

**⚠️ Important: TT_METAL_HOME is REQUIRED for running tests** (but NOT for building)

The `TT_METAL_HOME` environment variable must be set before running tests. This is required because the tt-metal runtime needs to locate firmware binaries and kernel artifacts. The build process does not require this variable - it automatically detects tt-metal from the submodule.

Use the test runner script which handles all environment setup automatically:

```console
cd torch_ttnn/cpp_extension
./run_cpp_extension_tests.sh              # Run all tests
./run_cpp_extension_tests.sh -v           # Verbose output  
./run_cpp_extension_tests.sh -k test_name # Run specific test
```

The test runner automatically:
- Activates the virtual environment
- Sets TT_METAL_HOME to the tt-metal submodule path (required for runtime)
- Runs all C++ extension and model tests

**Manual testing (alternative):**

If you need to run pytest directly with custom arguments, you must set TT_METAL_HOME first:

```console
cd torch_ttnn/cpp_extension
export TT_METAL_HOME="$(pwd)/third-party/tt-metal"
./run_cpp_extension_tests.sh tests/cpp_extension/ -v -k specific_test
```

Or use the test runner script which handles TT_METAL_HOME automatically:

```console
cd torch_ttnn/cpp_extension
./run_cpp_extension_tests.sh tests/cpp_extension/ -v -k specific_test
```

### Verify Setup

At this stage Python can see both `ttnn` and `torch_ttnn` packages. You can verify:
```console
python -c "import ttnn; import torch_ttnn; print('✓ Both packages available')"
```

For PYTHONPATH-based development (without installing torch_ttnn), add both paths:
```console
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo $PYTHONPATH
```
You will see something like `/home/ubuntu/pytorch2.0_ttnn/torch_ttnn/cpp_extension/third-party/tt-metal:/home/ubuntu/pytorch2.0_ttnn`

You can check if python sees `torch_ttnn` package by importing it in `ipython`
```console
(python_env) ubuntu@dev-machine:~/tt-metal/$ ipython
Python 3.8.10 (default, Nov  7 2024, 13:10:47) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.3 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import torch_ttnn
2024-12-13 00:07:58.368 | DEBUG    | ttnn:<module>:82 - Initial ttnn.CONFIG:
...
In [2]: print(torch_ttnn.__file__)
/home/ubuntu/pytorch2.0_ttnn/torch_ttnn/__init__.py
```

### Run Tests

Now you are ready to run tests / tools:
```console
cd torch_ttnn/cpp_extension
./run_cpp_extension_tests.sh ../tests/lowering/conv/test_conv2d.py -s
```

**⚠️ Remember:** If running pytest manually, you must set `TT_METAL_HOME` first. The test runner script handles this automatically.

## Debug
To debug mixed C++/Python I recommend to install `gdb 15.1` built from sources with python modules enabled.
```console
sudo apt install libmpfr-dev -y
wget https://ftp.gnu.org/gnu/gdb/gdb-15.1.tar.gz
tar -xvf gdb-15.1.tar.gz
cd gdb-15.1
./configure --with-python
make -j$(nproc)
make install # might want sudo
```

If you use VSCode, setup `launch.json` in a similar manner
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python + C++ Debug",
            "type": "cppdbg",
            "request": "launch",
            "program": "/bin/bash",
            "args": [
                "-c",
                "source python_env/bin/activate && export TT_METAL_HOME=/home/ubuntu/pytorch2.0_ttnn/torch_ttnn/cpp_extension/third-party/tt-metal && PYTHONPATH=/home/ubuntu/tt-metal/:/home/ubuntu/pytorch2.0_ttnn pytest tests/lowering/conv/test_conv2d.py -s"

            ],                   
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}/pytorch2.0_ttnn",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "miDebuggerPath": "gdb",
            "preLaunchTask": "",
            "postDebugTask": ""
        }
    ]
}
```

Now you can set a breakpoint in c++ file and it will be hit when you run a python script.
You can also use bt to see more information from python execution.

---

## Notes

### Always Use the Test Runner Script

**For running tests, always use** `./run_cpp_extension_tests.sh` - it handles all environment setup:

```console
cd torch_ttnn/cpp_extension
./run_cpp_extension_tests.sh       # Run all tests
./run_cpp_extension_tests.sh -v    # Verbose
./run_cpp_extension_tests.sh -k specific_test  # Specific test
```

The script automatically sets `TT_METAL_HOME` (required for tt-metal runtime to locate firmware/kernels) and all other environment configuration.

> **Important:** 
> - **Building:** `TT_METAL_HOME` is **NOT required** - the build scripts automatically detect tt-metal from the submodule
> - **Running tests:** `TT_METAL_HOME` **IS REQUIRED** - the tt-metal runtime needs it to locate firmware binaries and kernel artifacts