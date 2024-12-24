# Develop with TT-Metal build from source
It is often best to develop the compiler with metal build from sources instead of relying on a pre-built ttnn wheel.
This document provides hints on how to do that.

## Set up TT-Metal
Fetch repo and install dependencies
```console
git clone https://github.com/tenstorrent/tt-metal.git
cd tt-metal
sudo ./install_dependencies.sh
git submodule foreach 'git lfs fetch --all && git lfs pull'
```
setup env
```console
export ARCH_NAME=wormhole_b0
export TT_METAL_HOME=$(pwd) 
export PYTHONPATH=$(pwd) 
```
build the repo
```console
./build_metal.sh --debug --build-tests
```
setup and activate the env
```console
./create_venv.sh
source python_env/bin/activate
```

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

## Run tests
At this stage Python can see `ttnn` package, but not `torch_ttnn`. So we need to update `PYTHONPATH` to include both tt-metal and pytorch2.0_ttnn folders.
```consle
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo $PYTHONPATH
```
You will see something like `/home/ubuntu/tt-metal/:/home/ubuntu/pytorch2.0_ttnn`

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
