# THIS FILE IS AUTOGENERATED BY tools/generate_guard_function_from_input_var_metric.py
# DO NOT EDIT THIS FILE MANUALLY
# YOU CAN DEBUG THESE INPUT VAR VIA tests/autogen-op/ALL
import torch
import torch_ttnn.metrics as metrics
from functools import partial


aten_clamp_default_blocklist = [
    ["Tensor<[128]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 127"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 63"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 31"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 15"],
    ["Tensor<[320]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
    ["Tensor<[3234, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
    ["Tensor<[30]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[40]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[30]> self = ?", "Optional[number] min = ?", "Optional[number] max = 14"],
    ["Tensor<[40]> self = ?", "Optional[number] min = ?", "Optional[number] max = 19"],
    ["Tensor<[60]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[80]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[60]> self = ?", "Optional[number] min = ?", "Optional[number] max = 29"],
    ["Tensor<[80]> self = ?", "Optional[number] min = ?", "Optional[number] max = 39"],
    ["Tensor<[120]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[160]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[120]> self = ?", "Optional[number] min = ?", "Optional[number] max = 59"],
    ["Tensor<[160]> self = ?", "Optional[number] min = ?", "Optional[number] max = 79"],
    ["Tensor<[240]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[240]> self = ?", "Optional[number] min = ?", "Optional[number] max = 119"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 159"],
    ["Tensor<[480]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[640]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[480]> self = ?", "Optional[number] min = ?", "Optional[number] max = 239"],
    ["Tensor<[640]> self = ?", "Optional[number] min = ?", "Optional[number] max = 319"],
    ["Tensor<[3, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[6, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[12, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[24, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[800]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[1066]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[800]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
    ["Tensor<[1066]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
    ["Tensor<[0, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
    ["Tensor<[0, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 1066"],
    ["Tensor<[0, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 800"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 319"],
    ["Tensor<[300]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[300]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
    ["Tensor<[300]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
    ["Tensor<[8732, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
    ["Tensor<[4, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[8, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[16, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[32, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
]
aten_maximum_default_blocklist = [
    ["Tensor<[1, 16, 19, 19]> self = ?", "Tensor other = ?"],
    ["Tensor<[1, 16, 59, 59]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 16, 1, 60]> self = ?", "Tensor<[]> other = ?"],
]
aten__log_softmax_default_blocklist = [["Tensor<[19, 256008]> self = ?", "int dim = 1", "bool half_to_float = False"]]
aten_full_default_blocklist = [
    [
        "List[int] size = [19, 19]",
        "number fill_value = -3.4028234663852886e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
    [
        "List[int] size = [7, 7]",
        "number fill_value = -3.3895313892515355e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
    [
        "List[int] size = [45, 45]",
        "number fill_value = -3.3895313892515355e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
    [
        "List[int] size = [59, 59]",
        "number fill_value = -3.3895313892515355e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
    [
        "List[int] size = [19, 19]",
        "number fill_value = -3.3895313892515355e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
]
aten_rsub_Scalar_blocklist = [
    ["Tensor<[1, 1, 19, 19]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 9]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 25]> self = ?", "number other = 1.0"],
    ["Tensor<[2, 1, 7, 7]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 7]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 5]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 15]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 17]> self = ?", "number other = 1.0"],
]
aten__scaled_dot_product_flash_attention_default_blocklist = [
    ["Tensor<[1, 16, 197, 64]> query = ?", "Tensor<[1, 16, 197, 64]> key = ?", "Tensor<[1, 16, 197, 64]> value = ?"],
    ["Tensor<[1, 12, 197, 64]> query = ?", "Tensor<[1, 12, 197, 64]> key = ?", "Tensor<[1, 12, 197, 64]> value = ?"],
    ["Tensor<[1, 16, 50, 64]> query = ?", "Tensor<[1, 16, 50, 64]> key = ?", "Tensor<[1, 16, 50, 64]> value = ?"],
    ["Tensor<[1, 8, 4096, 40]> query = ?", "Tensor<[1, 8, 4096, 40]> key = ?", "Tensor<[1, 8, 4096, 40]> value = ?"],
    ["Tensor<[1, 8, 1024, 80]> query = ?", "Tensor<[1, 8, 9, 80]> key = ?", "Tensor<[1, 8, 9, 80]> value = ?"],
    ["Tensor<[1, 8, 256, 160]> query = ?", "Tensor<[1, 8, 256, 160]> key = ?", "Tensor<[1, 8, 256, 160]> value = ?"],
    ["Tensor<[1, 8, 64, 160]> query = ?", "Tensor<[1, 8, 64, 160]> key = ?", "Tensor<[1, 8, 64, 160]> value = ?"],
    ["Tensor<[1, 12, 50, 64]> query = ?", "Tensor<[1, 12, 50, 64]> key = ?", "Tensor<[1, 12, 50, 64]> value = ?"],
    ["Tensor<[1, 16, 1370, 80]> query = ?", "Tensor<[1, 16, 1370, 80]> key = ?", "Tensor<[1, 16, 1370, 80]> value = ?"],
    ["Tensor<[1, 12, 1, 64]> query = ?", "Tensor<[1, 12, 1, 64]> key = ?", "Tensor<[1, 12, 1, 64]> value = ?"],
    [
        "Tensor<[1, 12, 4, 64]> query = ?",
        "Tensor<[1, 12, 4, 64]> key = ?",
        "Tensor<[1, 12, 4, 64]> value = ?",
        "float dropout_p = 0.0",
        "bool is_causal = True",
    ],
]
aten_transpose_int_blocklist = [
    ["Tensor<[1, 197, 1, 3, 1024]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[12, 197, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[12, 64, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[1, 12, 64, 197]> self = ?", "int dim0 = -1", "int dim1 = -2"],
    ["Tensor<[1, 197, 1, 3, 768]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[1, 768, 49]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[16, 7, 7]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[16, 64, 7]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[1, 50, 1, 3, 1024]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[1, 50, 1, 3, 768]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[1, 1370, 1, 3, 1280]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[16, 197, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[16, 64, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[1, 16, 64, 197]> self = ?", "int dim0 = -1", "int dim1 = -2"],
]
aten_zeros_like_default_blocklist = [
    ["Tensor<[13685]> self = ?", "Optional[int] dtype = torch.bool", "Optional[bool] pin_memory = False"],
    ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[1, 1]> self = ?", "Optional[bool] pin_memory = False"],
    ["Tensor<[17, 17]> self = ?", "Optional[bool] pin_memory = False"],
]
aten_div_Tensor_blocklist = [
    ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 12, 9, 9]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 64, 9, 9]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 23, 40, 1]> self = ?", "Tensor<[128]> other = ?"],
    ["Tensor<[1, 12, 25, 25]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 16, 9, 9]> self = ?", "Tensor other = 11.313708498984761"],
    ["Tensor<[1, 16, 9, 9]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1280, 8, 8]> self = ?", "Tensor other = 1"],
    ["Tensor<[10, 10]> self = ?", "Tensor other = 8"],
    ["Tensor<[2, 2]> self = ?", "Tensor other = 16"],
    ["Tensor<[1, 16, 5, 5]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 16, 1, 6]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 128, 1568]> self = ?", "Tensor other = 3"],
    ["Tensor<[1, 64, 6272]> self = ?", "Tensor other = 3"],
    ["Tensor<[1, 32, 25088]> self = ?", "Tensor other = 3"],
    ["Tensor<[15, 15]> self = ?", "Tensor other = 8"],
    ["Tensor<[15, 15]> self = ?", "Tensor other = 2.772588722239781"],
    ["Tensor<[17, 17]> self = ?", "Tensor other = 16"],
    ["Tensor<[17, 17]> self = ?", "Tensor other = 2.0794415416798357"],
]
aten_mul_Tensor_blocklist = [
    ["Tensor<[]> self = ?", "Tensor<[3234, 1]> other = ?"],
    ["Tensor<[300]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 64, 30, 40]> self = ?", "Tensor<[1, 1, 30, 40]> other = ?"],
    ["Tensor<[1, 64, 60, 80]> self = ?", "Tensor<[1, 1, 60, 80]> other = ?"],
    ["Tensor<[1, 64, 120, 160]> self = ?", "Tensor<[1, 1, 120, 160]> other = ?"],
    ["Tensor<[64, 3, 64, 64]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
    ["Tensor<[16, 6, 64, 64]> self = ?", "Tensor<[6, 1, 1]> other = ?"],
    ["Tensor<[4, 12, 64, 64]> self = ?", "Tensor<[12, 1, 1]> other = ?"],
    ["Tensor<[136]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[100]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[68]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[50]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[34]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[25]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[17]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[13]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[9]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[7]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[0]> self = ?", "Tensor other = 0.5"],
    ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[0, 1]> other = ?"],
    ["Tensor<[0]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[16, 1]> self = ?", "Tensor<[1, 1, 32]> other = ?"],
    ["Tensor<[2, 1]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 71, 7, 64]> self = ?", "Tensor<[1, 1, 7, 64]> other = ?"],
    ["Tensor<[1, 3, 64, 64, 2]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 3, 32, 32, 2]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 3, 16, 16, 2]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[8732, 1]> other = ?"],
    ["Tensor<[12]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[64, 4, 64, 64]> self = ?", "Tensor<[4, 1, 1]> other = ?"],
    ["Tensor<[16, 8, 64, 64]> self = ?", "Tensor<[8, 1, 1]> other = ?"],
    ["Tensor<[4, 16, 64, 64]> self = ?", "Tensor<[16, 1, 1]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[1, 24, 768]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[1, 1, 768]> other = ?"],
]
aten_slice_Tensor_blocklist = [
    ["Tensor<[1, 512]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 9"],
    ["Tensor<[1, 512]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 25"],
    ["Tensor<[1, 1, 7, 1024]> self = ?", "int dim = 3", "Optional[int] start = 0", "Optional[int] end = 7"],
    ["Tensor<[1, 1, 45, 2048]> self = ?", "int dim = 3", "Optional[int] start = 0", "Optional[int] end = 45"],
    [
        "Tensor<[1, 1, 2048, 2048]> self = ?",
        "int dim = 2",
        "Optional[int]<s10> start = ?",
        "Optional[int]<s10 + 1> end = ?",
    ],
    ["Tensor<[1, 1, 1, 2048]> self = ?", "int dim = 3", "Optional[int] start = 0", "Optional[int]<s10 + 1> end = ?"],
    ["Tensor<[1, 1, 5, 2048]> self = ?", "int dim = 3", "Optional[int] start = 0", "Optional[int] end = 5"],
    ["Tensor<[1, 1876, 768]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int]<s0> end = ?"],
    ["Tensor<[448, 768]> self = ?", "int dim = 0", "Optional[int]<s2> start = ?", "Optional[int]<s2 + 1> end = ?"],
]
aten_native_layer_norm_default_blocklist = [
    [
        "Tensor<[1, 9, 4096]> input = ?",
        "List[int] normalized_shape = [4096]",
        "Optional[Tensor]<[4096]> weight = ?",
        "Optional[Tensor]<[4096]> bias = ?",
        "float eps = 1e-12",
    ],
    [
        "Tensor<[1, 7, 4544]> input = ?",
        "List[int] normalized_shape = [4544]",
        "Optional[Tensor]<[4544]> weight = ?",
        "Optional[Tensor]<[4544]> bias = ?",
        "float eps = 1e-05",
    ],
]
aten_sub_Tensor_blocklist = [
    ["Tensor<[64, 1, 64]> self = ?", "Tensor<[64, 64, 1]> other = ?"],
    ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 1]> other = ?"],
    ["Tensor<[4, 1, 64]> self = ?", "Tensor<[4, 64, 1]> other = ?"],
    ["Tensor<[0]> self = ?", "Tensor<[0]> other = ?"],
    ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
    ["Tensor<[64, 1, 49]> self = ?", "Tensor<[64, 49, 1]> other = ?"],
    ["Tensor<[16, 1, 49]> self = ?", "Tensor<[16, 49, 1]> other = ?"],
    ["Tensor<[4, 1, 49]> self = ?", "Tensor<[4, 49, 1]> other = ?"],
    ["Tensor<[1, 10]> self = ?", "Tensor<[10, 1]> other = ?"],
    ["Tensor<[1, 2]> self = ?", "Tensor<[2, 1]> other = ?"],
    ["Tensor<[24, 1]> self = ?", "Tensor<[1, 24]> other = ?"],
    ["Tensor<[1, 15]> self = ?", "Tensor<[15, 1]> other = ?"],
    ["Tensor<[1, 17]> self = ?", "Tensor<[17, 1]> other = ?"],
]
aten_exp_default_blocklist = [["Tensor<[0, 1]> self = ?"], ["Tensor<[]> self = ?"]]
aten_split_Tensor_blocklist = [
    ["Tensor<[768, 256]> self = ?", "int split_size = 256"],
    ["Tensor<[768]> self = ?", "int split_size = 256"],
    ["Tensor<[1, 7, 2304]> self = ?", "int split_size = 768", "int dim = 2"],
]
aten_ones_default_blocklist = [
    [
        "List[int] size = [7, 7]",
        "Optional[int] dtype = torch.bool",
        "Optional[int] layout = torch.strided",
        "Optional[Device] device = cpu",
    ],
    [
        "List[int] size = [1, 1]",
        "Optional[int] dtype = torch.int64",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
    ["List[int] size = [1, 1]", "Optional[Device] device = cpu", "Optional[bool] pin_memory = False"],
    [
        "List[int] size = [1, 1, 1]",
        "Optional[int] dtype = torch.float32",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
]
aten_where_self_blocklist = [
    ["Tensor<[1, 1, 7, 7]> condition = ?", "Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1, 45, 45]> condition = ?", "Tensor<[1, 12, 45, 45]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1, 1, 46]> condition = ?", "Tensor<[1, 12, 1, 46]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1, 5, 5]> condition = ?", "Tensor<[1, 16, 5, 5]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1, 1, 6]> condition = ?", "Tensor<[1, 16, 1, 6]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1, 256]> condition = ?", "Tensor<[1, 1, 256]> self = ?", "Tensor<[]> other = ?"],
]
aten_empty_memory_format_blocklist = [
    [
        "List[int] size = []",
        "Optional[int] dtype = torch.int64",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ]
]
aten_constant_pad_nd_default_blocklist = [
    ["Tensor<[1, 3, 224, 224]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 96, 112, 112]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 240, 28, 28]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 672, 17, 17]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
    ["Tensor<[1, 240, 29, 29]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 144, 59, 59]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
    ["Tensor<[1, 96, 113, 113]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 225, 225]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 380, 380]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 144, 190, 190]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 336, 48, 48]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 960, 27, 27]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
    ["Tensor<[1, 336, 49, 49]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 192, 99, 99]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
    ["Tensor<[1, 144, 191, 191]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 381, 381]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 300, 300]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 144, 150, 150]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 288, 38, 38]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 816, 23, 23]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
    ["Tensor<[1, 288, 39, 39]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 192, 79, 79]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
    ["Tensor<[1, 144, 151, 151]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 301, 301]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 240, 240]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 96, 120, 120]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 240, 30, 30]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 672, 19, 19]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
    ["Tensor<[1, 240, 31, 31]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 144, 63, 63]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
    ["Tensor<[1, 96, 121, 121]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 241, 241]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 260, 260]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 96, 130, 130]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
    ["Tensor<[1, 720, 21, 21]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
    ["Tensor<[1, 288, 35, 35]> self = ?", "List[int] pad = [-1, -1, -1, -1]"],
    ["Tensor<[1, 144, 69, 69]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
    ["Tensor<[1, 96, 131, 131]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ["Tensor<[1, 3, 261, 261]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
]
aten_log_default_blocklist = [
    ["Tensor<[10, 10]> self = ?"],
    ["Tensor<[1, 1]> self = ?"],
    ["Tensor<[2, 2]> self = ?"],
    ["Tensor<[15, 15]> self = ?"],
    ["Tensor<[17, 17]> self = ?"],
]
aten_rsqrt_default_blocklist = [["Tensor<[1, 1, 1]> self = ?"]]
aten_bernoulli_p_blocklist = [["Tensor<[1, 256]> self = ?", "float p = 0.5"]]
aten_eq_Scalar_blocklist = [["Tensor<[1, 1, 256]> self = ?", "number other = 1"]]
aten_native_dropout_default_blocklist = [
    ["Tensor<[1, 1280]> input = ?", "float p = 0.2", "Optional[bool] train = True"]
]
aten_new_empty_strided_default_blocklist = [
    ["Tensor<[1, 160, 7, 7]> self = ?", "List[int] size = [1, 160, 7, 7]", "List[int] stride = [7840, 49, 7, 1]"],
    [
        "Tensor<[1, 112, 14, 14]> self = ?",
        "List[int] size = [1, 112, 14, 14]",
        "List[int] stride = [21952, 196, 14, 1]",
    ],
    ["Tensor<[1, 80, 14, 14]> self = ?", "List[int] size = [1, 80, 14, 14]", "List[int] stride = [15680, 196, 14, 1]"],
    ["Tensor<[1, 40, 28, 28]> self = ?", "List[int] size = [1, 40, 28, 28]", "List[int] stride = [31360, 784, 28, 1]"],
]
aten_mm_default_blocklist = [["Tensor<[1, 21843]> self = ?", "Tensor<[21843, 768]> mat2 = ?"]]
aten_masked_fill_scalar_blocklist = [
    ["Tensor<[2, 1, 7, 7]> self = ?", "Tensor<[2, 1, 7, 7]> mask = ?", "number value = -3.3895313892515355e+38"],
]


def get_inputs(node):
    node_inputs = metrics.collect_input_variation_from_node(node)
    if type(node_inputs) == metrics.InputVariation:
        return node_inputs.inputs
    elif type(node_inputs) == metrics.ConvertedInput:
        return node_inputs.original_input_variation.inputs
    else:
        return None


def guard_aten(blocklist, node):
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blocklist:
        return False
    return True


GUARD = {
    torch.ops.aten.clamp.default: partial(guard_aten, aten_clamp_default_blocklist),
    torch.ops.aten.maximum.default: partial(guard_aten, aten_maximum_default_blocklist),
    torch.ops.aten._log_softmax.default: partial(guard_aten, aten__log_softmax_default_blocklist),
    torch.ops.aten.full.default: partial(guard_aten, aten_full_default_blocklist),
    torch.ops.aten.rsub.Scalar: partial(guard_aten, aten_rsub_Scalar_blocklist),
    torch.ops.aten._scaled_dot_product_flash_attention.default: partial(
        guard_aten, aten__scaled_dot_product_flash_attention_default_blocklist
    ),
    torch.ops.aten.transpose.int: partial(guard_aten, aten_transpose_int_blocklist),
    torch.ops.aten.zeros_like.default: partial(guard_aten, aten_zeros_like_default_blocklist),
    torch.ops.aten.div.Tensor: partial(guard_aten, aten_div_Tensor_blocklist),
    torch.ops.aten.mul.Tensor: partial(guard_aten, aten_mul_Tensor_blocklist),
    torch.ops.aten.slice.Tensor: partial(guard_aten, aten_slice_Tensor_blocklist),
    torch.ops.aten.native_layer_norm.default: partial(guard_aten, aten_native_layer_norm_default_blocklist),
    torch.ops.aten.sub.Tensor: partial(guard_aten, aten_sub_Tensor_blocklist),
    torch.ops.aten.exp.default: partial(guard_aten, aten_exp_default_blocklist),
    torch.ops.aten.split.Tensor: partial(guard_aten, aten_split_Tensor_blocklist),
    torch.ops.aten.ones.default: partial(guard_aten, aten_ones_default_blocklist),
    torch.ops.aten.where.self: partial(guard_aten, aten_where_self_blocklist),
    torch.ops.aten.empty.memory_format: partial(guard_aten, aten_empty_memory_format_blocklist),
    torch.ops.aten.constant_pad_nd.default: partial(guard_aten, aten_constant_pad_nd_default_blocklist),
    torch.ops.aten.log.default: partial(guard_aten, aten_log_default_blocklist),
    torch.ops.aten.rsqrt.default: partial(guard_aten, aten_rsqrt_default_blocklist),
    torch.ops.aten.bernoulli.p: partial(guard_aten, aten_bernoulli_p_blocklist),
    torch.ops.aten.eq.Scalar: partial(guard_aten, aten_eq_Scalar_blocklist),
    torch.ops.aten.native_dropout.default: partial(guard_aten, aten_native_dropout_default_blocklist),
    torch.ops.aten.new_empty_strided.default: partial(guard_aten, aten_new_empty_strided_default_blocklist),
    torch.ops.aten.mm.default: partial(guard_aten, aten_mm_default_blocklist),
    torch.ops.aten.masked_fill.Scalar: partial(guard_aten, aten_masked_fill_scalar_blocklist),
}

guard_ops = [
    "torch.ops.aten.view.default",
    "torch.ops.aten._unsafe_view.default",
    "torch.ops.aten.add.Tensor",
    "torch.ops.aten.clamp.default",
    "torch.ops.aten.maximum.default",
    "torch.ops.aten._log_softmax.default",
    "torch.ops.aten.full.default",
    "torch.ops.aten.rsub.Scalar",
    "torch.ops.aten._scaled_dot_product_flash_attention.default",
    "torch.ops.aten.transpose.int",
    "torch.ops.aten.embedding.default",
    "torch.ops.aten.zeros_like.default",
    "torch.ops.aten.div.Tensor",
    "torch.ops.aten.mul.Tensor",
    "torch.ops.aten.slice.Tensor",
    "torch.ops.aten.native_layer_norm.default",
    "torch.ops.aten.sub.Tensor",
    "torch.ops.aten.exp.default",
    "torch.ops.aten.split.Tensor",
    "torch.ops.aten.t.default",
    "torch.ops.aten.ones.default",
    "torch.ops.aten.where.self",
    "torch.ops.aten.empty.memory_format",
    "torch.ops.aten.constant_pad_nd.default",
    "torch.ops.aten.log.default",
    "torch.ops.aten.rsqrt.default",
    "torch.ops.aten.bernoulli.p",
    "torch.ops.aten.eq.Scalar",
    "torch.ops.aten.native_dropout.default",
    "torch.ops.aten.new_empty_strided.default",
    "torch.ops.aten.mm.default",
    "torch.ops.aten.masked_fill.Scalar",
]
