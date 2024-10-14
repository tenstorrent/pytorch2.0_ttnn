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
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-6/GLPN-KITTI eval", "aten.view.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 64, 120, 160]> self = ?', 'List[int] size = [1, 64, 19200]'], ['Tensor<[1, 19200, 64]> self = ?', 'List[int] size = [19200, 64]'], ['Tensor<[19200, 64]> self = ?', 'List[int] size = [1, 19200, 64]'], ['Tensor<[1, 19200, 64]> self = ?', 'List[int] size = [1, 19200, 1, 64]'], ['Tensor<[1, 64, 19200]> self = ?', 'List[int] size = [1, 64, 120, 160]'], ['Tensor<[1, 64, 15, 20]> self = ?', 'List[int] size = [1, 64, 300]'], ['Tensor<[1, 300, 64]> self = ?', 'List[int] size = [300, 64]'], ['Tensor<[300, 64]> self = ?', 'List[int] size = [1, 300, 64]'], ['Tensor<[1, 300, 64]> self = ?', 'List[int] size = [1, 300, 1, 64]'], ['Tensor<[1, 1, 19200, 64]> self = ?', 'List[int] size = [1, 19200, 64]'], ['Tensor<[1, 1, 64, 300]> self = ?', 'List[int] size = [1, 64, 300]'], ['Tensor<[1, 19200, 300]> self = ?', 'List[int] size = [1, 1, 19200, 300]'], ['Tensor<[1, 1, 19200, 300]> self = ?', 'List[int] size = [1, 19200, 300]'], ['Tensor<[1, 1, 300, 64]> self = ?', 'List[int] size = [1, 300, 64]'], ['Tensor<[1, 19200, 64]> self = ?', 'List[int] size = [1, 1, 19200, 64]'], ['Tensor<[1, 19200, 1, 64]> self = ?', 'List[int] size = [1, 19200, 64]'], ['Tensor<[19200, 256]> self = ?', 'List[int] size = [1, 19200, 256]'], ['Tensor<[1, 256, 19200]> self = ?', 'List[int] size = [1, 256, 120, 160]'], ['Tensor<[1, 256, 120, 160]> self = ?', 'List[int] size = [1, 256, 19200]'], ['Tensor<[1, 19200, 256]> self = ?', 'List[int] size = [19200, 256]'], ['Tensor<[1, 19200, 64]> self = ?', 'List[int] size = [1, 120, 160, -1]'], ['Tensor<[1, 128, 60, 80]> self = ?', 'List[int] size = [1, 128, 4800]'], ['Tensor<[1, 4800, 128]> self = ?', 'List[int] size = [4800, 128]'], ['Tensor<[4800, 128]> self = ?', 'List[int] size = [1, 4800, 128]'], ['Tensor<[1, 4800, 128]> self = ?', 'List[int] size = [1, 4800, 2, 64]'], ['Tensor<[1, 128, 4800]> self = ?', 'List[int] size = [1, 128, 60, 80]'], ['Tensor<[1, 128, 15, 20]> self = ?', 'List[int] size = [1, 128, 300]'], ['Tensor<[1, 300, 128]> self = ?', 'List[int] size = [300, 128]'], ['Tensor<[300, 128]> self = ?', 'List[int] size = [1, 300, 128]'], ['Tensor<[1, 300, 128]> self = ?', 'List[int] size = [1, 300, 2, 64]'], ['Tensor<[1, 2, 4800, 64]> self = ?', 'List[int] size = [2, 4800, 64]'], ['Tensor<[1, 2, 64, 300]> self = ?', 'List[int] size = [2, 64, 300]'], ['Tensor<[2, 4800, 300]> self = ?', 'List[int] size = [1, 2, 4800, 300]'], ['Tensor<[1, 2, 4800, 300]> self = ?', 'List[int] size = [2, 4800, 300]'], ['Tensor<[1, 2, 300, 64]> self = ?', 'List[int] size = [2, 300, 64]'], ['Tensor<[2, 4800, 64]> self = ?', 'List[int] size = [1, 2, 4800, 64]'], ['Tensor<[1, 4800, 2, 64]> self = ?', 'List[int] size = [1, 4800, 128]'], ['Tensor<[4800, 512]> self = ?', 'List[int] size = [1, 4800, 512]'], ['Tensor<[1, 512, 4800]> self = ?', 'List[int] size = [1, 512, 60, 80]'], ['Tensor<[1, 512, 60, 80]> self = ?', 'List[int] size = [1, 512, 4800]'], ['Tensor<[1, 4800, 512]> self = ?', 'List[int] size = [4800, 512]'], ['Tensor<[1, 4800, 128]> self = ?', 'List[int] size = [1, 60, 80, -1]'], ['Tensor<[1, 320, 30, 40]> self = ?', 'List[int] size = [1, 320, 1200]'], ['Tensor<[1, 1200, 320]> self = ?', 'List[int] size = [1200, 320]'], ['Tensor<[1200, 320]> self = ?', 'List[int] size = [1, 1200, 320]'], ['Tensor<[1, 1200, 320]> self = ?', 'List[int] size = [1, 1200, 5, 64]'], ['Tensor<[1, 320, 1200]> self = ?', 'List[int] size = [1, 320, 30, 40]'], ['Tensor<[1, 320, 15, 20]> self = ?', 'List[int] size = [1, 320, 300]'], ['Tensor<[1, 300, 320]> self = ?', 'List[int] size = [300, 320]'], ['Tensor<[300, 320]> self = ?', 'List[int] size = [1, 300, 320]'], ['Tensor<[1, 300, 320]> self = ?', 'List[int] size = [1, 300, 5, 64]'], ['Tensor<[1, 5, 1200, 64]> self = ?', 'List[int] size = [5, 1200, 64]'], ['Tensor<[1, 5, 64, 300]> self = ?', 'List[int] size = [5, 64, 300]'], ['Tensor<[5, 1200, 300]> self = ?', 'List[int] size = [1, 5, 1200, 300]'], ['Tensor<[1, 5, 1200, 300]> self = ?', 'List[int] size = [5, 1200, 300]'], ['Tensor<[1, 5, 300, 64]> self = ?', 'List[int] size = [5, 300, 64]'], ['Tensor<[5, 1200, 64]> self = ?', 'List[int] size = [1, 5, 1200, 64]'], ['Tensor<[1, 1200, 5, 64]> self = ?', 'List[int] size = [1, 1200, 320]'], ['Tensor<[1200, 1280]> self = ?', 'List[int] size = [1, 1200, 1280]'], ['Tensor<[1, 1280, 1200]> self = ?', 'List[int] size = [1, 1280, 30, 40]'], ['Tensor<[1, 1280, 30, 40]> self = ?', 'List[int] size = [1, 1280, 1200]'], ['Tensor<[1, 1200, 1280]> self = ?', 'List[int] size = [1200, 1280]'], ['Tensor<[1, 1200, 320]> self = ?', 'List[int] size = [1, 30, 40, -1]'], ['Tensor<[1, 512, 15, 20]> self = ?', 'List[int] size = [1, 512, 300]'], ['Tensor<[1, 300, 512]> self = ?', 'List[int] size = [300, 512]'], ['Tensor<[300, 512]> self = ?', 'List[int] size = [1, 300, 512]'], ['Tensor<[1, 300, 512]> self = ?', 'List[int] size = [1, 300, 8, 64]'], ['Tensor<[1, 8, 300, 64]> self = ?', 'List[int] size = [8, 300, 64]'], ['Tensor<[1, 8, 64, 300]> self = ?', 'List[int] size = [8, 64, 300]'], ['Tensor<[8, 300, 300]> self = ?', 'List[int] size = [1, 8, 300, 300]'], ['Tensor<[1, 8, 300, 300]> self = ?', 'List[int] size = [8, 300, 300]'], ['Tensor<[8, 300, 64]> self = ?', 'List[int] size = [1, 8, 300, 64]'], ['Tensor<[1, 300, 8, 64]> self = ?', 'List[int] size = [1, 300, 512]'], ['Tensor<[300, 2048]> self = ?', 'List[int] size = [1, 300, 2048]'], ['Tensor<[1, 2048, 300]> self = ?', 'List[int] size = [1, 2048, 15, 20]'], ['Tensor<[1, 2048, 15, 20]> self = ?', 'List[int] size = [1, 2048, 300]'], ['Tensor<[1, 300, 2048]> self = ?', 'List[int] size = [300, 2048]'], ['Tensor<[1, 300, 512]> self = ?', 'List[int] size = [1, 15, 20, -1]']])
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