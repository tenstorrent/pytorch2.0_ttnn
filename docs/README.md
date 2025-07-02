[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/tenstorrent/pytorch2.0_ttnn)

# PyTorch 2.0 TTNN Compiler
The PyTorch 2.0 TT-NN Compiler enables seamless execution of PyTorch models on [Tenstorrent](https://tenstorrent.com/) AI accelerators. 
By leveraging the TT-NN backend, you can achieve significant performance improvements while maintaining PyTorch's familiar API.

## 🚀 Quick Start

### Installation

Install from repo:
```bash
pip install git+https://bitbucket.org/tenstorrent/pytorch2.0_ttnn
```
or as editable package from source:
```bash
git clone https://github.com/tenstorrent/pytorch2.0_ttnn.git
cd pytorch2.0_ttnn
pip install -e .
```

### ✨ Basic Usage

**Option 1: Eager Mode:** get your model running by switching to TT device
```python
import torch
import torch_ttnn

model = YourModel()

device = ttnn.open_device(device_id=0)
model.to(torch_ttnn.ttnn_device_as_torch_device(device))

output = model(input_data)
```

**Option 2: Compilation Mode (Recommended):** get more perf with JIT compiler
```python
import torch
import torch_ttnn

model = YourModel()

device = ttnn.open_mesh_device(ttnn.MeshShape(1, 2))  # 1x2 device grid
option = torch_ttnn.TorchTtnnOption(device=device, data_parallel=2)

model = torch.compile(model, backend=torch_ttnn.backend, options=option)
output = model(input_data)
```

## 📊 Model Support

We've extensively tested the compiler across a diverse range of model architectures. Here's a summary of our validation results:

{metrics_md}

### Explanation of Metrics

{explanations_md}

***

# Contributing

Whether you are new to Tenstorrent hardware or an experienced developer, there are many ways to contribute.

## Getting Started

Start with our high level [Contribution guide](docs/Contributing.md).
You can find more information here:
* [Discussions](https://github.com/tenstorrent/pytorch2.0_ttnn/discussions)
* [Operations Report](docs/OperationsReport.md)
* [Lowering TT-NN Operation to PyTorch](docs/AddNewOperationLowering.md)
* [Native Device Integration Extesion](docs/OpenRegistrationAPI.md)
* [Build with Metal from Sources](docs/DevelopWithMetalFromSources.md)
* [Known Issues](docs/KnownIssues.md)
* [Problem Solving](docs/ProblemSolving.md)

We encourage contributions and offer [🤑 Bounties](https://github.com/tenstorrent/pytorch2.0_ttnn/issues?q=is%3Aissue%20state%3Aopen%20label%3Abounty) for some issues.

## Development Environment

To get started with development, you'll need Wormhole or Blackhole Tenstorrent accelerator card
* can be ordered on [Tenstorrent website](https://tenstorrent.com/) 
* can be requested on [Koyeb](https://www.koyeb.com/blog/tenstorrent-cloud-instances-unveiling-next-gen-ai-accelerators)

Install the development dependencies:
```shell
pip install -r requirements-dev.txt
pip install -e .
```

You can build the wheel file with
```shell
python -m build
```

## Project Structure

- `torch_ttnn/`: Main package directory containing the core implementation
- `tests/`: Test files for the project including models suits. We use `pytest` as our testing framework.
- `tools/`: Development and utility scripts
- `docs/`: Project documentation and reports
- `demo/`: Example code and usage demonstrations

## Questions and Support

If you have questions or need help getting started, please:
1. Review the existing documentation
2. Ask [PyTorch TT-NN DeepWiki](https://deepwiki.com/tenstorrent/pytorch2.0_ttnn) or [TT-Metal DeepWiki](https://deepwiki.com/tenstorrent/tt_metal)
3. Ask on [Discord](https://discord.gg/tenstorrent)
4. Open an issue on GitHub