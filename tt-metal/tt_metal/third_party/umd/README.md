# Tenstorrent AI User-Mode Driver
## Official Repository
https://github.com/tenstorrent/tt-umd

## Software Dependencies
UMD requires Tenstorrent's [kernel-mode driver](https://github.com/tenstorrent/tt-kmd)

Required Ubuntu dependencies:
```
sudo apt install -y libhwloc-dev cmake ninja-build
```

Suggested third-party dependency is Clang 17:
```
wget https://apt.llvm.org/llvm.sh
chmod u+x llvm.sh
sudo ./llvm.sh 17
```


## IOMMU and Hugepage requirements
To determine whether your system requires hugepage configuration, run the provided script:

```bash
./scripts/iommu_detect.sh
```

#### Grayskull and Wormhole
[1G hugepages](https://www.kernel.org/doc/Documentation/admin-guide/mm/hugetlbpage.rst) are required for shared device/host memory.  Techniques for setup:
  * Recommended: the [tt-system-tools](https://github.com/tenstorrent/tt-system-tools) repository contains a .deb package which will configure your system
      * `sudo dpkg -i tenstorrent-tools_1.1-5_all.deb`
  * Alternative: Metal project provides instructions and a [script](https://github.com/tenstorrent/tt-metal/blob/main/INSTALLING.md#step-3-hugepages).
  * For experts:
    * Put system IOMMU in passthrough mode or disable it
    * Allocate 1 or more 1G hugepages
    * Mount the hugetlbfs at /dev/hugepages-1G (e.g. `mount -t hugetlbfs hugetlbfs /dev/hugepages-1G -o mode=777,pagesize=1024M`)
#### Blackhole
If your system IOMMU is enabled, no hugepage setup is required.

## Build flow

To build `libdevice.so`:
```
cmake -B build -G Ninja
cmake --build build
```

You also need to configure cmake to enable tests, hence the need to run cmake configuration step again.
To build tests:
```
cmake -B build -G Ninja -DTT_UMD_BUILD_TESTS=ON
cmake --build build
```

To build with GCC, set these environment variables before invoking `cmake`:
```
export CMAKE_C_COMPILER=/usr/bin/gcc
export CMAKE_CXX_COMPILER=/usr/bin/g++
```

## Build debian dev package
```
cmake --build build --target package

# Generates umd-dev-x.y.z-Linux.deb
```

# Integration
UMD can be consumed by downstream projects in multiple ways.

## From Source (CMake)
You can link `libdevice.so` by linking against the `umd::device` target.

### Using CPM Package Manager
```
CPMAddPackage(
  NAME umd
  GITHUB_REPOSITORY tenstorrent/tt-umd
  GIT_TAG v0.1.0
  VERSION 0.1.0
)
```

### As a submodule/external project
```
add_subdirectory(<path to umd>)
```

## From Prebuilt Binaries

### Ubuntu
```
apt install ./umd-dev-x.y.z-Linux.deb
```

## Simulator Integration
You can run UMD tests without silicon by following setup instructions [here](https://yyz-gitlab.local.tenstorrent.com/tenstorrent/tt-metal).

For UMD, sample tests can be found in `tests/simulation/test_simulation_device.cpp`

# Pre-commit Hook Integration for Formatting and Linting

As part of maintaining consistent code formatting across the project, we have integrated the [pre-commit](https://pre-commit.com/) framework into our workflow. The pre-commit hooks will help automatically check and format code before commits are made, ensuring that we adhere to the project's coding standards.

## What is Pre-commit?

Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. It helps catch common issues early by running a set of hooks before code is committed, automating tasks like:

- Formatting code (e.g., fixing trailing whitespace, enforcing end-of-file newlines)
- Running linters (e.g., `clang-format`, `black`, `flake8`)
- Checking for merge conflicts or other common issues.

For more details on pre-commit, you can visit the [official documentation](https://pre-commit.com/).

## How to Set Up Pre-commit Locally

To set up pre-commit on your local machine, follow these steps:

1. **Install Pre-commit**:
   Ensure you have Python installed, then run:
   ```bash
   pip install pre-commit
   ```
2. **Install the Git Hook Scripts**:
   In your local repository, run the following command to install the pre-commit hooks:
   ```bash
   pre-commit install
   ```
   This command will configure your local Git to run the defined hooks automatically before each commit.
3. **Run Pre-commit Hooks Manually**:
   You can also run the hooks manually against all files at any time with:
   ```bash
   pre-commit run --all-files
   ```
## Why You Should Use Pre-commit
By setting up pre-commit locally, you can help maintain the quality of the codebase and ensure that commits consistently meet the project's formatting standards. This saves time during code reviews and reduces the likelihood of code formatting issues slipping into the repository.

Since the hooks run automatically before each commit, you don't need to remember to manually format or check your code, making it easier to maintain consistency.

We strongly encourage all developers to integrate pre-commit into their workflow.

# Formatting C++ code

## Installing clang-format

If you're using an IRD docker, clang-format should be already available.
If you don't have clang-format in your working environment, follow the instructions
on [llvm website](https://apt.llvm.org/) for installing it.

## Formatting files

If working with VSCode, you can copy the provided default settings:
```bash
cp .vscode/default.settings.json .vscode/settings.json
```

From now on, c++ files will be formatted on save (given that clang-format is available).

Note that if you setup pre-commit hook, the files will be automatically formatted when you commit changes.
You can also manually auto format the whole repo using mentioned pre-commit:
```bash
   pre-commit run --all-files
```

# Grayskull End of Life

Grayskull is no longer actively supported by Tenstorrent. [Last UMD commit](https://github.com/tenstorrent/tt-umd/commit/a5b4719b7d44f0c7c953542803faf6851574329a) supporting Grayskull.