# Integrating TTNN with Pytorch Open Registration API

Pytorch Open Registration API allows integrating TTNN implementation into Torch. We can access TTNN ops from higher-level Torch calls.

# Build Nodes
There are currently two verified paths to build extra dependencies. Choose one:

* [Submodule build](#submodule-build) (Most simple)
* [External tt-metal and Pytorch build](#external-tt-metal-and-pytorch-build)

## Submodule build

## Prepare environment
1. Clone pytorch2.0_ttnn
    ```bash
    git clone https://github.com/tenstorrent/pytorch2.0_ttnn.git
    cd pytorch2.0_ttnn
    ```

2. Install dependencies
    ```bash
    apt upgrade -y && apt update -y
    apt install -y cmake python3 python3-venv python3-pip git-lfs ccache
    ```

3. Create a new venv and install python requirements
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip config set global.extra-index-url https://download.pytorch.org/whl/cpu
    pip install -r requirements-dev.txt
    pip install --force-reinstall pip==21.2.4
    python3 -m pip install numpy setuptools wheel
    python3 -m pip install -e .
    ```
4. Fetch submodules, build tt-metal, and build cpp_extension.  
    Note: The ttnn python package from tt-metal will not be installed.
    ```bash
    pushd torch_ttnn/cpp_extension
    git submodule sync
    git submodule update --init --recursive
    git submodule foreach 'git lfs fetch --all && git lfs pull'
    ./third-party/tt-metal/install_dependencies.sh
    ./build_cpp_extension.sh
    export TT_METAL_HOME="$(pwd)/third-party/tt-metal"
    popd
    ```

## External tt-metal and Pytorch build
Please note that ttnn c++ interface is constantly changing, so cpp extension might not work for newer ttnn versions "out-of-the-box"

###  Build tt-metal and set up venv
1. Change to your preferred starting directory.
1. Clone tt-metal
    ```
    git clone --recursive https://github.com/tenstorrent/tt-metal.git
    pushd tt-metal
    ```
1. Set `TT_METAL_HOME`
    ```
    export TT_METAL_HOME="$(pwd)"
    ```
1. Build tt-metal

    ```
    ./install_dependencies.sh
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
    pushd pytorch2.0_ttnn
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
Wheel torch might not work with cmake cpp extension, due to different ABI used for pybind in ttnn and pytorch. One solution is to rebuild torch with clang-17
1. Remove existing torch
    ```
    pip uninstall -y torch torchvision torchmetrics torch-fidelity
    ```
2. Other dependencies
    ```
    apt install libomp-17-dev
    ```
3. Clone torch and checkout compatible version with tt-metal
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
2. Build torch
    ```
    CC=clang-17 CXX=clang++-17 CMAKE_POLICY_VERSION_MINIMUM=3.5 python setup.py develop

    popd
    ```

### Build torchvision (Optional)
Optionally, you can build torchvision, which might be required for some computer-vision models:
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
    CMAKE_FLAGS="-DCMAKE_CXX_COMPILER=clang++-17;-DCMAKE_C_COMPILER=clang-17" python3 setup.py develop # Make sure TT_METAL_HOME is pointing to cloned tt-metal repo
    ```


## Running tests
Check to make sure `PYTHONPATH` is unset.

* If [Submodule build](#submodule-build) path was followed, make sure `TT_METAL_HOME` is set to tt-metal submodule
* If [External tt-metal and Pytorch build](#external-tt-metal-and-pytorch-build) path was followed, make sure `TT_METAL_HOME` is set to your local tt-metal clone

Run in the root of `pytorch2.0_ttnn` repo:
```
python -m pytest tests/cpp_extension/test_cpp_extension_functionality.py -s
```

You can also run with `DEBUG_CPP_EXT=1` ENV to enable logging messages.

## Troubleshooting
* Ensure `numpy < 2.0`

# References
https://github.com/bdhirsh/pytorch_open_registration_example