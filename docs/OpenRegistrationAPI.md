# Integrating TTNN with Pytorch Open Registration API

Pytorch Open Registration API allows integrating TTNN implementation into Torch. We can access TTNN ops from higher-level Torch calls.

# Build Notes
There are currently two verified paths to build extra dependencies. Choose one:

* [Submodule build](#submodule-build) (Most simple)
* [External tt-metal and Pytorch build](#external-tt-metal-and-pytorch-build)

## Submodule build

1. Change to your preferred starting directory.
1. Clone pytorch2.0_ttnn
    ```
    git clone https://github.com/tenstorrent/pytorch2.0_ttnn.git
    ```
1. Create a new venv and install requirements
    ```
    pushd pytorch2.0_ttnn
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements-dev.txt
    ```
1. Fetch submodules, build tt-metal, and build cpp_extension.  
    Note: The ttnn python package from tt-metal will not be installed.
    ```
    pushd torch_ttnn/cpp_extension
    git submodule sync
    git submodule update --init --recursive
    CMAKE_FLAGS="-DENABLE_SUBMODULE_TT_METAL_BUILD=ON" python3 setup.py develop

    popd
    popd
    ```

    Note: you can pass multiple cmake flags with ';' separator:
    ```bash
    CMAKE_FLAGS="-DENABLE_SUBMODULE_TT_METAL_BUILD=ON;-DCMAKE_BUILD_TYPE=Debug" python3 setup.py develop
    ```

## External tt-metal and Pytorch build
###  Build tt-metal and set up venv
1. Change to your preferred starting directory.
1. Clone tt-metal
    ```
    git clone --recursive https://github.com/tenstorrent/tt-metal.git
    pushd tt-metal
    ```
1. Set `TT_METAL_HOME`
    ```
    export TT_METAL_HOME="$(PWD)"
    ```
1. Build tt-metal

    ```
    ./build_metal.sh --enable-ccache
    ```
1. Create new virtual environment
    ```
    ./create_venv.sh
    source ./python_env/bin/activate

    popd
    ```

### Install pytorch2.0_ttnn dependencies

1. Clone pytorch2.0_ttnn
    ```
    git clone https://github.com/tenstorrent/pytorch2.0_ttnn.git
    pushd
    ```
1. Edit `requirements.txt` and remove the line starting with `ttnn`. This part is important.
1. Install requirements
    ```
    pip install -r requirements-dev.txt

    popd
    ```

    You can ignore the following message for now:
    ```
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    tt-smi 3.0.12 requires pre-commit==3.5.0, but you have pre-commit 3.0.4 which is incompatible.
    ```

### Build pytorch
Wheel torch doesn't work with cmake cpp extension, probably due to different ABI used for pybind in ttnn and pytorch. One solution is to rebuild torch with clang-17
1. Remove existing torch
    ```
    pip uninstall -y torch torchvision torchmetrics torch-fidelity
    ```
1. Other dependencies
    ```
    sudo apt install libomp-17-dev
    ```
1. Clone torch and checkout compatible version with tt-metal
    ```
    git clone https://github.com/pytorch/pytorch.git
    pushd pytorch
    git checkout tags/v2.2.1
    git submodule sync
    git submodule update --init --recursive
    ```
1. Install dependencies and requirements for torch
    ```
    pip install mkl-static mkl-include
    pip install -U numpy==1.26.4
    pip install -r requirements.txt
    ```
1. Build torch
    ```
    CC=clang-17 CXX=clang++-17 CMAKE_POLICY_VERSION_MINIMUM=3.5 python setup.py develop

    popd
    ```

### Build torchvision
Optionally, you can build torchvision, which might be requires for some computer-vision models:
```bash
git clone https://github.com/pytorch/vision
pushd vision
git checkout v0.17.1
CC=clang-17 CXX=clang++-17 CMAKE_POLICY_VERSION_MINIMUM=3.5 python setup.py develop
popd
```


### Building cpp extension
Please make sure that extension is built while being in venv that was prepared before

1. Build with local tt-metal build. Assume `TT_METAL_HOME` is set
    ```bash
    pushd pytorch2.0_ttnn
    pushd torch_ttnn/cpp_extension
    python3 setup.py develop
    ```


## Running tests
Check to make sure `PYTHONPATH` is unset.

* If [Submodule build](#submodule-build) path was followed, make sure `TT_METAL_HOME` is still unset.
* If [External tt-metal and Pytorch build](#external-tt-metal-and-pytorch-build) path was followed, make sure `TT_METAL_HOME` is still set.

Run in the root of `pytorch2.0_ttnn` repo:
```
python -m pytest tests/cpp_extension/test_cpp_extension_functionality.py -s
```

You can also run with `DEBUG_CPP_EXT=1` ENV to enable logging messages.

## Troubleshooting
* Ensure `numpy < 2.0`

## Development
When developing cpp extension, it might be convenient to have `compile_commands.json` to enable syntax highlighting and indexing of code. bear utility can help generate them:
```bash
sudo apt install bear
rm -rf ${HOME}/.cache/torch_extensions
bear -- pytest tests/cpp_extension/test_cpp_extension_functionality.py -s
```

# References
https://github.com/bdhirsh/pytorch_open_registration_example