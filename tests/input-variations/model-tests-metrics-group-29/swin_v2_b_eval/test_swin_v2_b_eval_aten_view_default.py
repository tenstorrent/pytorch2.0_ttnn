import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, get_input_vals_from_metric_str


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten.view.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-29/swin_v2_b eval", "aten.view.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 15, 15, 2]> self = ?', 'List[int] size = [225, 2]'], ['Tensor<[225, 512]> self = ?', 'List[int] size = [1, 15, 15, 512]'], ['Tensor<[1, 15, 15, 512]> self = ?', 'List[int] size = [225, 512]'], ['Tensor<[225, 4]> self = ?', 'List[int] size = [1, 15, 15, 4]'], ['Tensor<[1, 15, 15, 4]> self = ?', 'List[int] size = [-1, 4]'], ['Tensor<[4096, 4]> self = ?', 'List[int] size = [64, 64, -1]'], ['Tensor<[1, 64, 64, 128]> self = ?', 'List[int] size = [1, 8, 8, 8, 8, 128]'], ['Tensor<[64, 64, 128]> self = ?', 'List[int] size = [4096, 128]'], ['Tensor<[4096, 384]> self = ?', 'List[int] size = [64, 64, 384]'], ['Tensor<[64, 64, 384]> self = ?', 'List[int] size = [64, 64, 3, 4, 32]'], ['Tensor<[256, 64, 64]> self = ?', 'List[int] size = [64, 4, 64, 64]'], ['Tensor<[64, 4, 64, 64]> self = ?', 'List[int] size = [256, 64, 64]'], ['Tensor<[256, 64, 32]> self = ?', 'List[int] size = [64, 4, 64, 32]'], ['Tensor<[4096, 128]> self = ?', 'List[int] size = [64, 64, 128]'], ['Tensor<[64, 64, 128]> self = ?', 'List[int] size = [1, 8, 8, 8, 8, 128]'], ['Tensor<[1, 64, 64, 128]> self = ?', 'List[int] size = [4096, 128]'], ['Tensor<[4096, 512]> self = ?', 'List[int] size = [1, 64, 64, 512]'], ['Tensor<[1, 64, 64, 512]> self = ?', 'List[int] size = [4096, 512]'], ['Tensor<[4096, 128]> self = ?', 'List[int] size = [1, 64, 64, 128]'], ['Tensor<[64, 64]> self = ?', 'List[int] size = [8, 8, 8, 8]'], ['Tensor<[64, 4, 64, 64]> self = ?', 'List[int] size = [1, 64, 4, 64, 64]'], ['Tensor<[1, 64, 4, 64, 64]> self = ?', 'List[int] size = [-1, 4, 64, 64]'], ['Tensor<[1, 32, 32, 512]> self = ?', 'List[int] size = [1024, 512]'], ['Tensor<[1024, 256]> self = ?', 'List[int] size = [1, 32, 32, 256]'], ['Tensor<[225, 8]> self = ?', 'List[int] size = [1, 15, 15, 8]'], ['Tensor<[1, 15, 15, 8]> self = ?', 'List[int] size = [-1, 8]'], ['Tensor<[4096, 8]> self = ?', 'List[int] size = [64, 64, -1]'], ['Tensor<[1, 32, 32, 256]> self = ?', 'List[int] size = [1, 4, 8, 4, 8, 256]'], ['Tensor<[16, 64, 256]> self = ?', 'List[int] size = [1024, 256]'], ['Tensor<[1024, 768]> self = ?', 'List[int] size = [16, 64, 768]'], ['Tensor<[16, 64, 768]> self = ?', 'List[int] size = [16, 64, 3, 8, 32]'], ['Tensor<[128, 64, 64]> self = ?', 'List[int] size = [16, 8, 64, 64]'], ['Tensor<[16, 8, 64, 64]> self = ?', 'List[int] size = [128, 64, 64]'], ['Tensor<[128, 64, 32]> self = ?', 'List[int] size = [16, 8, 64, 32]'], ['Tensor<[1024, 256]> self = ?', 'List[int] size = [16, 64, 256]'], ['Tensor<[16, 64, 256]> self = ?', 'List[int] size = [1, 4, 4, 8, 8, 256]'], ['Tensor<[1, 32, 32, 256]> self = ?', 'List[int] size = [1024, 256]'], ['Tensor<[1024, 1024]> self = ?', 'List[int] size = [1, 32, 32, 1024]'], ['Tensor<[1, 32, 32, 1024]> self = ?', 'List[int] size = [1024, 1024]'], ['Tensor<[32, 32]> self = ?', 'List[int] size = [4, 8, 4, 8]'], ['Tensor<[16, 8, 64, 64]> self = ?', 'List[int] size = [1, 16, 8, 64, 64]'], ['Tensor<[1, 16, 8, 64, 64]> self = ?', 'List[int] size = [-1, 8, 64, 64]'], ['Tensor<[1, 16, 16, 1024]> self = ?', 'List[int] size = [256, 1024]'], ['Tensor<[256, 512]> self = ?', 'List[int] size = [1, 16, 16, 512]'], ['Tensor<[225, 16]> self = ?', 'List[int] size = [1, 15, 15, 16]'], ['Tensor<[1, 15, 15, 16]> self = ?', 'List[int] size = [-1, 16]'], ['Tensor<[4096, 16]> self = ?', 'List[int] size = [64, 64, -1]'], ['Tensor<[1, 16, 16, 512]> self = ?', 'List[int] size = [1, 2, 8, 2, 8, 512]'], ['Tensor<[4, 64, 512]> self = ?', 'List[int] size = [256, 512]'], ['Tensor<[256, 1536]> self = ?', 'List[int] size = [4, 64, 1536]'], ['Tensor<[4, 64, 1536]> self = ?', 'List[int] size = [4, 64, 3, 16, 32]'], ['Tensor<[64, 64, 64]> self = ?', 'List[int] size = [4, 16, 64, 64]'], ['Tensor<[4, 16, 64, 64]> self = ?', 'List[int] size = [64, 64, 64]'], ['Tensor<[64, 64, 32]> self = ?', 'List[int] size = [4, 16, 64, 32]'], ['Tensor<[256, 512]> self = ?', 'List[int] size = [4, 64, 512]'], ['Tensor<[4, 64, 512]> self = ?', 'List[int] size = [1, 2, 2, 8, 8, 512]'], ['Tensor<[1, 16, 16, 512]> self = ?', 'List[int] size = [256, 512]'], ['Tensor<[256, 2048]> self = ?', 'List[int] size = [1, 16, 16, 2048]'], ['Tensor<[1, 16, 16, 2048]> self = ?', 'List[int] size = [256, 2048]'], ['Tensor<[16, 16]> self = ?', 'List[int] size = [2, 8, 2, 8]'], ['Tensor<[4, 16, 64, 64]> self = ?', 'List[int] size = [1, 4, 16, 64, 64]'], ['Tensor<[1, 4, 16, 64, 64]> self = ?', 'List[int] size = [-1, 16, 64, 64]'], ['Tensor<[1, 8, 8, 2048]> self = ?', 'List[int] size = [64, 2048]'], ['Tensor<[64, 1024]> self = ?', 'List[int] size = [1, 8, 8, 1024]'], ['Tensor<[225, 32]> self = ?', 'List[int] size = [1, 15, 15, 32]'], ['Tensor<[1, 15, 15, 32]> self = ?', 'List[int] size = [-1, 32]'], ['Tensor<[4096, 32]> self = ?', 'List[int] size = [64, 64, -1]'], ['Tensor<[1, 8, 8, 1024]> self = ?', 'List[int] size = [1, 1, 8, 1, 8, 1024]'], ['Tensor<[1, 1, 1, 8, 8, 1024]> self = ?', 'List[int] size = [1, 64, 1024]'], ['Tensor<[1, 64, 1024]> self = ?', 'List[int] size = [64, 1024]'], ['Tensor<[64, 3072]> self = ?', 'List[int] size = [1, 64, 3072]'], ['Tensor<[1, 64, 3072]> self = ?', 'List[int] size = [1, 64, 3, 32, 32]'], ['Tensor<[1, 32, 64, 32]> self = ?', 'List[int] size = [32, 64, 32]'], ['Tensor<[1, 32, 32, 64]> self = ?', 'List[int] size = [32, 32, 64]'], ['Tensor<[32, 64, 64]> self = ?', 'List[int] size = [1, 32, 64, 64]'], ['Tensor<[1, 32, 64, 64]> self = ?', 'List[int] size = [32, 64, 64]'], ['Tensor<[32, 64, 32]> self = ?', 'List[int] size = [1, 32, 64, 32]'], ['Tensor<[64, 1024]> self = ?', 'List[int] size = [1, 64, 1024]'], ['Tensor<[1, 64, 1024]> self = ?', 'List[int] size = [1, 1, 1, 8, 8, 1024]'], ['Tensor<[1, 1, 8, 1, 8, 1024]> self = ?', 'List[int] size = [1, 8, 8, 1024]'], ['Tensor<[1, 8, 8, 1024]> self = ?', 'List[int] size = [64, 1024]'], ['Tensor<[64, 4096]> self = ?', 'List[int] size = [1, 8, 8, 4096]'], ['Tensor<[1, 8, 8, 4096]> self = ?', 'List[int] size = [64, 4096]'], ['Tensor<[1, 1024, 1, 1]> self = ?', 'List[int] size = [1, 1024]']])
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
            "opname": "aten.view.default",
            "input_strings": input_strings,
            "native_run": False,
            "run": False,
            "accuracy": False,
            "convert_to_ttnn": False,
        }
    m = AtenModule()
    input_args, input_kwargs = get_input_vals_from_metric_str("aten.view.default", input_strings)
    if input_args is None and input_kwargs is None:
        pytest.skip("Invalid input strings:" + str(input_strings))
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
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

    if metric["run"] == True:
        # Check inference result
        accuracy = calculate_accuracy(result_before, result_after)
        if accuracy >= 0.99:
            metric["accuracy"] = True

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        if any(["ttnn" in str(node) for node in nodes]):
            metric["convert_to_ttnn"] = True

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True