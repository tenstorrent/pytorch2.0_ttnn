# Integrating TTNN with Pytorch Open Registration API

Pytorch Open Registration API allows integrating TTNN implementation into Torch. We can access TTNN ops from higher-level Torch calls.

# Build Notes

## Build tt-metal and set up venv
tt-metal has its own script to create a Python venv with all the dependencies. Set this up first:

## Build tt-metal
1. Clone Build tt-metal using the `./build_metal.sh` script.

```
git clone --recursive https://github.com/tenstorrent/tt-metal.git
pushd tt-metal
./build_metal.sh --enable-ccache
```

2. Create a new venv and install tt-metal onto it. By default this will create a directory called `python_env` inside the `tt-metal` repo. You can set the environment variable `PYTHON_ENV_DIR` to a different location if desired.
```
./create_venv.sh
source ./python_env/bin/activate
popd
```

## Build pytorch
Wheel torch doesn't work with cmake cpp extension, probably due to different ABI used for pybind in ttnn and pytorch. One solution is to rebuild torch with clang-17
```bash
# Remove torch
pip uninstall torch torchvision torchmetrics torch-fidelity

# Other dependencies
sudo apt install libomp-17-dev

# Clone and build torch
git clone https://github.com/pytorch/pytorch.git
cd pytorch
git checkout tags/v2.2.1
git submodule sync
git submodule update --init --recursive

pip install mkl-static mkl-include
pip install -U numpy==1.26.4
pip install -r requirements.txt

CC=clang-17 CXX=clang++-17  CMAKE_POLICY_VERSION_MINIMUM=3.5 python setup.py develop
```

## Install pytorch2.0_ttnn dependencies
NOTE: The ttnn packages are intentionally removed for this branch. They will be restored once a ttnn dev package containing all the dependencies is available.

0. If you built torch from source, remove `torch` and `torchvision` from `requirements.txt`

1. Install requirements
    ```
    pip install -r requirements-dev.txt
    ```

    You can ignore the following message for now:
    ```
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    tt-smi 3.0.12 requires pre-commit==3.5.0, but you have pre-commit 3.0.4 which is incompatible.
    ```

## Building cpp extension
Please make sure that extension is built while being in venv that was prepared before

1. Build with local tt-metal build
```bash
export TT_METAL_HOME=/path/to/tt-metal
cd torch_ttnn/cpp_extension
python3 setup.py develop
```

2. Build fetch tt-metal from git submodule and build directly
```bash
git submodule sync
git submodule update --init --recursive
CMAKE_FLAGS="-DENABLE_SUBMODULE_TT_METAL_BUILD=ON" python3 setup.py develop
```

Note: you can pass multiple cmake flags with ';' separator:
```bash
CMAKE_FLAGS="-DENABLE_SUBMODULE_TT_METAL_BUILD=ON;-DCMAKE_BUILD_TYPE=Debug" python3 setup.py develop
```

## Running tests
Check to make sure `PYTHONPATH` is unset. Currently, this extension checks for `TT_METAL_HOME`. Have that set to the root of the `tt-metal` repo that you used to build tt-metal in the prior step.

Run in the root of `pytorch2.0_ttnn` repo:
```
python -m pytest tests/cpp_extension/test_cpp_extension_functionality.py -s
```

You can also run with `DEBUG_CPP_EXT=1` ENV to enable logging messages.

## Troubleshooting
* You may have to set `PYTHONPATH=$TT_METAL_HOME:<location-of-pytorch2.0_ttnn-repo>` after all
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