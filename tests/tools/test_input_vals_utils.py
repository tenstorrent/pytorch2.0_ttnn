# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pytest
import torch
from tests.utils import render_metric_string_list_to_input_args_kwargs as render


def check_self():
    input_args, input_kwargs, status = render(None, ["Tensor<[1, 2, 3]> self = ?", "Tensor<[4, 5, 6]> tensor = ?"])
    assert len(input_args) == 1
    assert input_args[0].shape == torch.Size([1, 2, 3])
    assert input_kwargs["tensor"].shape == torch.Size([4, 5, 6])

    input_args, input_kwargs, status = render(
        None, ["Tensor<[1, 2, 3]> tensor1 = ?", "Tensor<[4, 5, 6]> self = ?", "Tensor<[7, 8, 9]> tensor2 = ?"]
    )
    assert len(input_args) == 2
    assert input_args[0].shape == torch.Size([1, 2, 3])
    assert input_args[1].shape == torch.Size([4, 5, 6])
    assert input_kwargs["tensor2"].shape == torch.Size([7, 8, 9])


def check_tensor():
    input_args, input_kwargs, status = render(None, ["Tensor<[1, 2, 3]> tensor = ?"])
    assert input_kwargs["tensor"].shape == torch.Size([1, 2, 3])

    input_args, input_kwargs, status = render(None, ["Tensor<[]> empty_tensor = ?"])
    assert input_kwargs["empty_tensor"].shape == torch.Size([])

    # aten.mul.Tensor
    input_args, input_kwargs, status = render(None, ["Tensor<[0]> zero_tensor = ?"])
    assert input_kwargs["zero_tensor"].shape == torch.Size([0])

    input_args, input_kwargs, status = render(None, ["Tensor scale_tensor = -6.0"])
    assert input_kwargs["scale_tensor"] == -6.0

    # aten.lift_fresh_copy.default
    input_args, input_kwargs, status = render(None, ["Tensor scale_tensor2 = ?"])
    assert input_kwargs["scale_tensor2"] == None

    input_args, input_kwargs, status = render(None, ["Optional[Tensor]<[4, 5, 6]> optional_tensor = ?"])
    assert input_kwargs["optional_tensor"].shape == torch.Size([4, 5, 6])

    # aten.cat.default
    input_args, input_kwargs, status = render(None, ["List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 196, 1024]>]"])
    assert input_kwargs["tensors"][0].shape == torch.Size([1, 1, 1024])
    assert input_kwargs["tensors"][1].shape == torch.Size([1, 196, 1024])

    # aten._unsafe_index.Tensor
    input_args, input_kwargs, status = render(
        None, ["List[Optional[Tensor]] list_optional_tensor = [None, None, <[12, 1]>, <[16]>]"]
    )
    assert input_kwargs["list_optional_tensor"][0] == None
    assert input_kwargs["list_optional_tensor"][1] == None
    assert input_kwargs["list_optional_tensor"][2].shape == torch.Size([12, 1])
    assert input_kwargs["list_optional_tensor"][3].shape == torch.Size([16])

    # aten.index.Tensor
    input_args, input_kwargs, status = render(None, ["List[Optional[Tensor]] indices = [<[1]>, <[1]>]"])
    assert input_kwargs["indices"][0].shape == torch.Size([1])
    assert input_kwargs["indices"][1].shape == torch.Size([1])

    input_args, input_kwargs, status = render(
        None, ["Optional[List[Tensor]] optional_list_tensor = [<[1, 1, 1024]>, <[1, 196, 1024]>]"]
    )
    assert input_kwargs["optional_list_tensor"][0].shape == torch.Size([1, 1, 1024])
    assert input_kwargs["optional_list_tensor"][1].shape == torch.Size([1, 196, 1024])

    input_args, input_kwargs, status = render(None, ["Tensor<[1, 1, 1, s10 + 1]> condition = ?"])
    assert status == False


def check_scalar():
    input_args, input_kwargs, status = render(None, ["bool the_bool = False"])
    assert input_kwargs["the_bool"] == False

    input_args, input_kwargs, status = render(None, ["int the_int = -1"])
    assert input_kwargs["the_int"] == -1

    input_args, input_kwargs, status = render(None, ["float the_float = 0.0"])
    assert input_kwargs["the_float"] == 0.0

    # aten.arange.start
    input_args, input_kwargs, status = render(None, ["number the_number = 1"])
    assert input_kwargs["the_number"] == 1

    # aten.baddbmm.default
    input_args, input_kwargs, status = render(None, ["number the_number2 = 0.10206207261596577"])
    assert input_kwargs["the_number2"] == 0.10206207261596577

    # aten.full.default
    input_args, input_kwargs, status = render(None, ["number the_number3 = -3.4028234663852886e+38"])
    assert input_kwargs["the_number3"] == -3.4028234663852886e38

    # aten.masked_fill.Scalar
    input_args, input_kwargs, status = render(None, ["number the_number4 = -inf"])
    assert input_kwargs["the_number4"] == float("-inf")

    input_args, input_kwargs, status = render(None, ["Optional[bool] optional_bool = False"])
    assert input_kwargs["optional_bool"] == False

    input_args, input_kwargs, status = render(None, ["Optional[int] optional_int = torch.bfloat16"])
    assert input_kwargs["optional_int"] == torch.bfloat16

    # aten.clone.default
    input_args, input_kwargs, status = render(None, ["Optional[int] optional_int2 = torch.contiguous_format"])
    assert input_kwargs["optional_int2"] == torch.contiguous_format

    input_args, input_kwargs, status = render(None, ["Optional[float] optional_float = 1.0"])
    assert input_kwargs["optional_float"] == 1.0

    # aten.clamp.default
    input_args, input_kwargs, status = render(None, ["Optional[number] optional_number = 4.135166556742356"])
    assert input_kwargs["optional_number"] == 4.135166556742356

    input_args, input_kwargs, status = render(None, ["Optional[number] optional_number2 = ?"])
    assert input_kwargs["optional_number2"] == None

    input_args, input_kwargs, status = render(None, ["List[bool] list_bool = [True, False, True]"])
    assert input_kwargs["list_bool"] == [True, False, True]

    input_args, input_kwargs, status = render(None, ["List[int] list_int = [1, 2, 3]"])
    assert input_kwargs["list_int"] == [1, 2, 3]

    input_args, input_kwargs, status = render(None, ["List[float] list_float = [1.0, 2.0, 3.0]"])
    assert input_kwargs["list_float"] == [1.0, 2.0, 3.0]

    input_args, input_kwargs, status = render(None, ["List[number] list_number = [1.0, 2, None]"])
    assert input_kwargs["list_number"] == [1.0, 2, None]

    input_args, input_kwargs, status = render(None, ["List[Optional[bool]] list_optional_bool = [True, False, None]"])
    assert input_kwargs["list_optional_bool"] == [True, False, None]

    input_args, input_kwargs, status = render(None, ["List[Optional[int]] list_optional_int = [None, 2, 3]"])
    assert input_kwargs["list_optional_int"] == [None, 2, 3]

    input_args, input_kwargs, status = render(None, ["List[Optional[float]] list_optional_float = [1.0, 2.0, None]"])
    assert input_kwargs["list_optional_float"] == [1.0, 2.0, None]

    input_args, input_kwargs, status = render(None, ["List[Optional[number]] list_optional_number = [1.0, 2, None]"])
    assert input_kwargs["list_optional_number"] == [1.0, 2, None]

    input_args, input_kwargs, status = render(None, ["Optional[List[bool]] optional_list_bool = [True, False, True]"])
    assert input_kwargs["optional_list_bool"] == [True, False, True]

    input_args, input_kwargs, status = render(None, ["Optional[List[int]] optional_list_int = [1, 2, 3]"])
    assert input_kwargs["optional_list_int"] == [1, 2, 3]

    input_args, input_kwargs, status = render(None, ["Optional[List[float]] optional_list_float = [1.0, 2.0, 3.0]"])
    assert input_kwargs["optional_list_float"] == [1.0, 2.0, 3.0]

    input_args, input_kwargs, status = render(None, ["Optional[List[number]] optional_list_number = [1.0, 2, None]"])
    assert input_kwargs["optional_list_number"] == [1.0, 2, None]

    # aten.mean.dim
    input_args, input_kwargs, status = render(None, ["Optional[List[int]] dim = [-1]"])
    assert input_kwargs["dim"] == [-1]


def check_device():
    input_args, input_kwargs, status = render(None, ["Device device = cpu"])
    assert input_kwargs["device"] == "cpu"

    input_args, input_kwargs, status = render(None, ["Optional[Device] optional_device = cpu"])
    assert input_kwargs["optional_device"] == "cpu"


def check_specific_op():
    input_args, input_kwargs, status = render("aten.bitwise_not.default", ["Tensor<[1, 23, 40]> self = ?"])
    assert input_args[0].dtype == torch.int

    input_args, input_kwargs, status = render(
        "aten.masked_fill.Scalar",
        [
            "Tensor<[1, 1, 19, 19]> self = ?",
            "Tensor<[1, 1, 19, 19]> mask = ?",
            "number value = -3.4028234663852886e+38",
        ],
    )
    assert input_kwargs["mask"].dtype == torch.bool

    input_args, input_kwargs, status = render(
        "aten.where.self",
        ["Tensor<[1, 1, 1, 46]> condition = ?", "Tensor<[1, 12, 1, 46]> self = ?", "Tensor<[]> other = ?"],
    )
    assert input_args[0].dtype == torch.bool

    input_args, input_kwargs, status = render(
        "aten.embedding.default", ["Tensor<[1, 768]> weight = ?", "Tensor<[1, 10]> indices = ?"]
    )
    weight_shape0 = input_kwargs["weight"].shape[0]
    assert input_kwargs["indices"].min() >= 0 and input_kwargs["indices"].max() < weight_shape0

    input_args, input_kwargs, status = render(
        "aten.embedding.default",
        ["Tensor<[514, 768]> weight = ?", "Tensor<[1, 10]> indices = ?", "int padding_idx = 1"],
    )
    weight_shape0 = input_kwargs["weight"].shape[0]
    assert input_kwargs["indices"].min() >= 0 and input_kwargs["indices"].max() < weight_shape0

    input_args, input_kwargs, status = render(
        "aten.index_select.default", ["Tensor<[2050, 1024]> self = ?", "int dim = 0", "Tensor<[19]> index = ?"]
    )
    self_shape = input_args[0].shape
    dim = input_kwargs["dim"]
    assert input_kwargs["index"].min() >= 0 and input_kwargs["index"].max() < self_shape[dim]


@pytest.mark.parametrize(
    "test_func",
    (
        check_self,
        check_tensor,
        check_scalar,
        check_device,
        check_specific_op,
    ),
)
def test_render_vals_from_metric_str(test_func):
    test_func()
