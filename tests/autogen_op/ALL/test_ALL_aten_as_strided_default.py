import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, render_metric_string_list_to_input_args_kwargs


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten.as_strided.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.as_strided.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[7840]> self = ?",
            "List[int] size = [160, 7, 7]",
            "List[int] stride = [49, 7, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[7840]> self = ?",
            "List[int] size = [1, 160, 7, 7]",
            "List[int] stride = [7840, 49, 7, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 160, 7, 7]> self = ?",
            "List[int] size = [1, 160, 7, 7]",
            "List[int] stride = [7840, 49, 7, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[21952]> self = ?",
            "List[int] size = [112, 14, 14]",
            "List[int] stride = [196, 14, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[21952]> self = ?",
            "List[int] size = [1, 112, 14, 14]",
            "List[int] stride = [21952, 196, 14, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 112, 14, 14]> self = ?",
            "List[int] size = [1, 112, 14, 14]",
            "List[int] stride = [21952, 196, 14, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[15680]> self = ?",
            "List[int] size = [80, 14, 14]",
            "List[int] stride = [196, 14, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[15680]> self = ?",
            "List[int] size = [1, 80, 14, 14]",
            "List[int] stride = [15680, 196, 14, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 80, 14, 14]> self = ?",
            "List[int] size = [1, 80, 14, 14]",
            "List[int] stride = [15680, 196, 14, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[31360]> self = ?",
            "List[int] size = [40, 28, 28]",
            "List[int] stride = [784, 28, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[31360]> self = ?",
            "List[int] size = [1, 40, 28, 28]",
            "List[int] stride = [31360, 784, 28, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 40, 28, 28]> self = ?",
            "List[int] size = [1, 40, 28, 28]",
            "List[int] stride = [31360, 784, 28, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[75264]> self = ?",
            "List[int] size = [24, 56, 56]",
            "List[int] stride = [3136, 56, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[75264]> self = ?",
            "List[int] size = [1, 24, 56, 56]",
            "List[int] stride = [75264, 3136, 56, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 24, 56, 56]> self = ?",
            "List[int] size = [1, 24, 56, 56]",
            "List[int] stride = [75264, 3136, 56, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[200704]> self = ?",
            "List[int] size = [16, 112, 112]",
            "List[int] stride = [12544, 112, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[200704]> self = ?",
            "List[int] size = [1, 16, 112, 112]",
            "List[int] stride = [200704, 12544, 112, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 16, 112, 112]> self = ?",
            "List[int] size = [1, 16, 112, 112]",
            "List[int] stride = [200704, 12544, 112, 1]",
            "Optional[int] storage_offset = 0",
        ],
        [
            "Tensor<[1, 1024, 1, 1]> self = ?",
            "List[int] size = [1, 1024, 1, 1]",
            "List[int] stride = [1024, 1, 1024, 1024]",
        ],
        ["Tensor<[1, 768, 1, 1]> self = ?", "List[int] size = [1, 768, 1, 1]", "List[int] stride = [768, 1, 768, 768]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.as_strided.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.as_strided.default", input_strings
    )
    if status == False:
        pytest.skip("Invalid input strings")
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
        metric["native_run"] = False
    if metric["native_run"] == True:
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False

    if metric["run"] == True:
        try:
            # Check inference result
            metric["accuracy"] = calculate_accuracy(result_before, result_after)
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if not any(["aten." in str(node.target) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] >= 0.99
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
