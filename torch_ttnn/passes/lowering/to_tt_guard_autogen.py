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
aten_zeros_like_default_blocklist = [
    ["Tensor<[13685]> self = ?", "Optional[int] dtype = torch.bool", "Optional[bool] pin_memory = False"],
    ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[1, 1]> self = ?", "Optional[bool] pin_memory = False"],
    ["Tensor<[17, 17]> self = ?", "Optional[bool] pin_memory = False"],
]
aten_div_Tensor_blocklist = [
    ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 23, 40, 1]> self = ?", "Tensor<[128]> other = ?"],
    ["Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 16, 5, 5]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 16, 1, 6]> self = ?", "Tensor<[]> other = ?"],
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
aten_exp_default_blocklist = [["Tensor<[0, 1]> self = ?"], ["Tensor<[]> self = ?"]]
aten_split_Tensor_blocklist = [
    ["Tensor<[768, 256]> self = ?", "int split_size = 256"],
    ["Tensor<[768]> self = ?", "int split_size = 256"],
    ["Tensor<[1, 7, 2304]> self = ?", "int split_size = 768", "int dim = 2"],
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
aten_rsqrt_default_blocklist = [["Tensor<[1, 1, 1]> self = ?"]]
aten_bernoulli_p_blocklist = [["Tensor<[1, 256]> self = ?", "float p = 0.5"]]
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
aten_convolution_default_blocklist = [
    # TODO(#385): Guard and fallback (likely) OOM cases
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[768, 3, 32, 32]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[1024, 3, 32, 32]> weight = ?",
        "Optional[Tensor]<[1024]> bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 64, 480, 640]> input = ?",
        "Tensor<[64, 64, 3, 3]> weight = ?",
        "Optional[Tensor]<[64]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 64, 480, 640]> input = ?",
        "Tensor<[1, 64, 3, 3]> weight = ?",
        "Optional[Tensor]<[1]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 56, 56]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[256]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 384, 512]> input = ?",
        "Tensor<[768, 3, 32, 32]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 800, 1088]> input = ?",
        "Tensor<[64, 3, 7, 7]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [3, 3]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 200, 272]> input = ?",
        "Tensor<[512, 256, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 100, 136]> input = ?",
        "Tensor<[819, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[819]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 50, 68]> input = ?",
        "Tensor<[819, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[819]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 232, 112, 112]> input = ?",
        "Tensor<[232, 232, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 232, 56, 56]> input = ?",
        "Tensor<[232, 232, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 720, 1280]> input = ?",
        "Tensor<[64, 3, 7, 7]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [3, 3]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 180, 320]> input = ?",
        "Tensor<[512, 256, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 56, 56]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 1024, 14, 14]> input = ?",
        "Tensor<[1024, 512, 2, 2]> weight = ?",
        "Optional[Tensor]<[512]> bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = True",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 512, 56, 56]> input = ?",
        "Tensor<[256, 512, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 128, 112, 112]> input = ?",
        "Tensor<[128, 64, 2, 2]> weight = ?",
        "Optional[Tensor]<[64]> bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = True",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[768, 3, 32, 32]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 75, 75]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[256]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[768, 3, 16, 16]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [16, 16]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 512, 672]> input = ?",
        "Tensor<[192, 3, 16, 16]> weight = ?",
        "Optional[Tensor]<[192]> bias = ?",
        "List[int] stride = [16, 16]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 518, 518]> input = ?",
        "Tensor<[1280, 3, 14, 14]> weight = ?",
        "Optional[Tensor]<[1280]> bias = ?",
        "List[int] stride = [14, 14]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 720, 14, 14]> input = ?",
        "Tensor<[1920, 720, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[1024, 3, 16, 16]> weight = ?",
        "Optional[Tensor]<[1024]> bias = ?",
        "List[int] stride = [16, 16]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 528, 192, 192]> input = ?",
        "Tensor<[528, 264, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 2",
    ],
    [
        "Tensor<[1, 1056, 96, 96]> input = ?",
        "Tensor<[1056, 264, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 4",
    ],
    [
        "Tensor<[1, 2904, 48, 48]> input = ?",
        "Tensor<[2904, 264, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 11",
    ],
    [
        "Tensor<[1, 256, 112, 112]> input = ?",
        "Tensor<[256, 128, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 2",
    ],
    [
        "Tensor<[1, 256, 56, 56]> input = ?",
        "Tensor<[256, 128, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 2",
    ],
    [
        "Tensor<[1, 256, 56, 56]> input = ?",
        "Tensor<[256, 8, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 32",
    ],
    [
        "Tensor<[1, 720, 17, 17]> input = ?",
        "Tensor<[720, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [2, 2]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 720",
    ],
    [
        "Tensor<[1, 256, 75, 75]> input = ?",
        "Tensor<[256, 1, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 256",
    ],
    [
        "Tensor<[1, 256, 120, 160]> input = ?",
        "Tensor<[256, 1, 3, 3]> weight = ?",
        "Optional[Tensor]<[256]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 256",
    ],
    [
        "Tensor<[1, 2048, 15, 20]> input = ?",
        "Tensor<[2048, 1, 3, 3]> weight = ?",
        "Optional[Tensor]<[2048]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 2048",
    ],
    [
        "Tensor<[1, 816, 19, 19]> input = ?",
        "Tensor<[816, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [2, 2]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 816",
    ],
    [
        "Tensor<[1, 816, 23, 23]> input = ?",
        "Tensor<[816, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 816",
    ],
    [
        "Tensor<[1, 960, 24, 24]> input = ?",
        "Tensor<[960, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [2, 2]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 960",
    ],
    [
        "Tensor<[1, 256, 56, 56]> input = ?",
        "Tensor<[256, 4, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 64",
    ],
    [
        "Tensor<[1, 256, 64, 64]> input = ?",
        "Tensor<[256, 1, 3, 3]> weight = ?",
        "Optional[Tensor]<[256]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 256",
    ],
    [
        "Tensor<[1, 256, 100, 136]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 50, 68]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 50, 68]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[256]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 100, 136]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[256]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 100, 136]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 90, 160]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 45, 80]> input = ?",
        "Tensor<[256, 256, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    # TODO(tt-metal#16172): bias_ntiles == weight_matrix_width_ntiles
    [
        "Tensor<[1, 1024, 45, 80]> input = ?",
        "Tensor<[2048, 1024, 1, 1]> weight = ?",
        "Optional[Tensor]<[2048]> bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    # TODO(tt-metal#16172): weight_matrix_width_ntiles % weight_block_w_ntiles == 0
    [
        "Tensor<[1, 2904, 24, 24]> input = ?",
        "Tensor<[7392, 2904, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 1232, 14, 14]> input = ?",
        "Tensor<[3024, 1232, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
]

aten_argmax_default_blocklist = [
    ["Tensor<[2, 7]> self = ?", "Optional[int] dim = -1"],
    ["Tensor<[1, 7]> self = ?", "Optional[int] dim = -1"],
    ["Tensor<[1, 51865]> self = ?", "Optional[int] dim = -1"],
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
    torch.ops.aten._scaled_dot_product_flash_attention.default: partial(
        guard_aten, aten__scaled_dot_product_flash_attention_default_blocklist
    ),
    torch.ops.aten.zeros_like.default: partial(guard_aten, aten_zeros_like_default_blocklist),
    torch.ops.aten.div.Tensor: partial(guard_aten, aten_div_Tensor_blocklist),
    torch.ops.aten.native_layer_norm.default: partial(guard_aten, aten_native_layer_norm_default_blocklist),
    torch.ops.aten.exp.default: partial(guard_aten, aten_exp_default_blocklist),
    torch.ops.aten.split.Tensor: partial(guard_aten, aten_split_Tensor_blocklist),
    torch.ops.aten.where.self: partial(guard_aten, aten_where_self_blocklist),
    torch.ops.aten.empty.memory_format: partial(guard_aten, aten_empty_memory_format_blocklist),
    torch.ops.aten.rsqrt.default: partial(guard_aten, aten_rsqrt_default_blocklist),
    torch.ops.aten.bernoulli.p: partial(guard_aten, aten_bernoulli_p_blocklist),
    torch.ops.aten.native_dropout.default: partial(guard_aten, aten_native_dropout_default_blocklist),
    torch.ops.aten.new_empty_strided.default: partial(guard_aten, aten_new_empty_strided_default_blocklist),
    torch.ops.aten.mm.default: partial(guard_aten, aten_mm_default_blocklist),
    torch.ops.aten.convolution.default: partial(guard_aten, aten_convolution_default_blocklist),
    torch.ops.aten.argmax.default: partial(guard_aten, aten_argmax_default_blocklist),
}

guard_ops = [
    "torch.ops.aten.view.default",
    "torch.ops.aten._unsafe_view.default",
    "torch.ops.aten.add.Tensor",
    "torch.ops.aten.clamp.default",
    "torch.ops.aten.maximum.default",
    "torch.ops.aten._log_softmax.default",
    "torch.ops.aten.rsub.Scalar",
    "torch.ops.aten._scaled_dot_product_flash_attention.default",
    "torch.ops.aten.transpose.int",
    "torch.ops.aten.embedding.default",
    "torch.ops.aten.zeros_like.default",
    "torch.ops.aten.div.Tensor",
    "torch.ops.aten.mul.Tensor",
    "torch.ops.aten.native_layer_norm.default",
    "torch.ops.aten.sub.Tensor",
    "torch.ops.aten.exp.default",
    "torch.ops.aten.split.Tensor",
    "torch.ops.aten.t.default",
    "torch.ops.aten.where.self",
    "torch.ops.aten.empty.memory_format",
    "torch.ops.aten.log.default",
    "torch.ops.aten.rsqrt.default",
    "torch.ops.aten.bernoulli.p",
    "torch.ops.aten.eq.Scalar",
    "torch.ops.aten.native_dropout.default",
    "torch.ops.aten.new_empty_strided.default",
    "torch.ops.aten.mm.default",
    "torch.ops.aten.convolution.default",
]
