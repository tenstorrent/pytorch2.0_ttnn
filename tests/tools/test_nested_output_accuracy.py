from tests.utils import calculate_accuracy, comp_pcc
import torch
import numpy as np


def test_nested_output_accuracy():
    # Some models like CLIP have nested Dict outputs. The old implementation skips these nested items. These example outputs have intentionally mismatching values for the nested items in order to illustrate the inconsistent accuracy calculations.
    expected_outputs = {
        "key0": torch.tensor([0.12345]),
        "key1": {"subkey0": torch.tensor([0.12345])},
        "key2": [torch.tensor([0.12345])],
    }
    actual_outputs = {
        "key0": torch.tensor([0.12345]),
        "key1": {"subkey0": torch.tensor([0.0])},
        "key2": [torch.tensor([0.0])],
    }

    # Manually calculate pcc for every item.
    _, pcc_key0 = comp_pcc(expected_outputs["key0"], actual_outputs["key0"])
    _, pcc_key1_subkey0 = comp_pcc(expected_outputs["key1"]["subkey0"], actual_outputs["key1"]["subkey0"])
    _, pcc_key2_sublist0 = comp_pcc(expected_outputs["key2"][0], actual_outputs["key2"][0])

    # The mean result should be around 0.333333
    manual_accuracy = np.mean([pcc_key0, pcc_key1_subkey0, pcc_key2_sublist0])
    print(f"Manually calculated accuracy: {manual_accuracy}")

    # Using calculate_accuracy. If the nested inputs are skipped, only "key0" will be factored into the final pcc calculation. The resulting pcc would be 1.0 which is incorrect.
    utils_accuracy = calculate_accuracy(expected_outputs, actual_outputs)
    print(f"Calculated accuracy through utils: {utils_accuracy}")

    assert torch.allclose(torch.tensor(manual_accuracy), torch.tensor(utils_accuracy))
