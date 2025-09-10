# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pytest

from huggingface_hub import auth_check


# Test access to gated models
@pytest.mark.parametrize(
    "model",
    [
        "meta-llama/Llama-3.1-8B",
        "meta-llama/Llama-3.2-1B",
        "meta-llama/Llama-3.2-3B",
    ],
)
def test_gated_models(model):
    auth_check(model)
    print(f"Successful auth for repository ({model}).")
