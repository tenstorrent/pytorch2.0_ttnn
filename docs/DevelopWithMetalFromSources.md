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

### 2. Build tt-metal from the submodule
```console
cd torch_ttnn/cpp_extension/third-party/tt-metal
git submodule update --init --recursive
sudo ./install_dependencies.sh
export ARCH_NAME=wormhole_b0  # Optional, for development
./build_metal.sh --debug --build-tests
./create_venv.sh
source python_env/bin/activate
```

**✅ No TT_METAL_HOME needed!** 
- tt-metal scripts work fine without it (they operate within their directory)
- pytorch2.0_ttnn CMake auto-detects the submodule
- If you set TT_METAL_HOME anyway, pytorch2.0_ttnn will ignore it

Things are going well if you can now call `ipython` and see something like this
```console
(python_env) ubuntu@dev-machine:~/tt-metal/$ ipython
Python 3.8.10 (default, Nov  7 2024, 13:10:47) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.3 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import ttnn
2024-12-13 00:02:45.792 | DEBUG    | ttnn:<module>:82 - Initial ttnn.CONFIG:
...
In [2]: print(ttnn.__file__)
/home/ubuntu/tt-metal/ttnn/ttnn/__init__.py
```

### 3. Install pytorch2.0_ttnn
Return to pytorch2.0_ttnn root and install:
```console
cd ../../../../  # Return to pytorch2.0_ttnn root
python -m pip install -e .[dev]
```

CMake will automatically detect tt-metal from the submodule. No `TT_METAL_HOME` needed.

---

## Run tests
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

Now you are ready to run tests / tools
```console
pytest tests/lowering/conv/test_conv2d.py -s
```

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
                "source python_env/bin/activate && PYTHONPATH=/home/ubuntu/tt-metal/:/home/ubuntu/pytorch2.0_ttnn pytest tests/lowering/conv/test_conv2d.py -s"

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

### TT_METAL_HOME Environment Variable

**Short answer: Never set it. It's not needed.**

**Details:**
- ✅ **tt-metal scripts** (`build_metal.sh`, `create_venv.sh`, `install_dependencies.sh`) - **DO NOT need** `TT_METAL_HOME`
- ✅ **pytorch2.0_ttnn build** (`pip install -e .`) - **DO NOT need** `TT_METAL_HOME` (CMake auto-detects from submodule)
- ⚠️ **Some tt-metal test scripts** MAY reference it - but they're not used in normal pytorch2.0_ttnn development

**If you set it anyway:**
- pytorch2.0_ttnn build will **detect, warn, and unset** it to prevent conflicts between TT projects

**Recommendation:**
```console
# Just don't set it - everything works without it!
cd torch_ttnn/cpp_extension/third-party/tt-metal
./build_metal.sh  # ✓ Works
./create_venv.sh  # ✓ Works
cd ../../../../
pip install -e .[dev]  # ✓ Works (CMake auto-detects submodule)
```