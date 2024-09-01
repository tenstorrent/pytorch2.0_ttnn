# Reference: https://github.com/arief25ramadhan/carvana-unet-segmentation

import os
import subprocess
import sys
from pathlib import Path
import tempfile
import torch
import pytest


def github_download(repo_name):
    repo_url = "https://github.com/" + repo_name + ".git"

    cache_dir = Path(tempfile.gettempdir()) / "github_repos"
    repo_dir = cache_dir / repo_name

    # Create the cache directory if it doesn't exist
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Check if the repository has already been cloned
    if not repo_dir.exists():
        subprocess.run(["git", "clone", repo_url, str(repo_dir)], check=True)
    else:
        print(f"Repository {repo_name} already exists. Skipping clone.")

    return repo_dir


@pytest.mark.compilation_xfail
def test_unet_carvana(record_property):
    record_property("model_name", "Unet-carvana")

    repo_dir = github_download("arief25ramadhan/carvana-unet-segmentation")

    # Import the module from the cloned repo
    sys.path.insert(0, str(repo_dir))
    from model import UNET

    model = UNET(in_channels=3, out_channels=1)

    input_batch = torch.rand((1, 3, 224, 224))
    output = model(input_batch)

    record_property("torch_ttnn", (model, input_batch, output))
