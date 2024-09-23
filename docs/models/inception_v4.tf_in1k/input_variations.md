# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |          22 |
|  1 | aten.addmm.default                                |                  1 |           1 |
|  2 | aten.avg_pool2d.default                           |                  3 |           3 |
|  3 | aten.cat.default                                  |                 34 |          25 |
|  4 | aten.clone.default                                |                  1 |           1 |
|  5 | aten.convolution.default                          |                 38 |          38 |
|  6 | aten.max_pool2d_with_indices.default              |                  4 |           4 |
|  7 | aten.mean.dim                                     |                  1 |           1 |
|  8 | aten.relu.default                                 |                 22 |          22 |
|  9 | aten.t.default                                    |                  1 |           1 |
| 10 | aten.view.default                                 |                  1 |           1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 17, 17]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
|  1 | Tensor<[1, 192, 17, 17]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
|  2 | Tensor<[1, 192, 35, 35]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
|  3 | Tensor<[1, 192, 8, 8]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001   | Done     |
|  4 | Tensor<[1, 224, 17, 17]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
|  5 | Tensor<[1, 224, 35, 35]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
|  6 | Tensor<[1, 256, 17, 17]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
|  7 | Tensor<[1, 256, 8, 8]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001   | Done     |
|  8 | Tensor<[1, 32, 147, 147]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001    | Done     |
|  9 | Tensor<[1, 32, 149, 149]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001    | Done     |
| 10 | Tensor<[1, 320, 17, 17]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
| 11 | Tensor<[1, 320, 8, 8]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001   | Done     |
| 12 | Tensor<[1, 384, 17, 17]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001 | Done     |
| 13 | Tensor<[1, 384, 8, 8]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001   | Done     |
| 14 | Tensor<[1, 448, 8, 8]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001   | Done     |
| 15 | Tensor<[1, 512, 8, 8]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001   | Done     |
| 16 | Tensor<[1, 64, 147, 147]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001    | Done     |
| 17 | Tensor<[1, 64, 35, 35]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001      | Done     |
| 18 | Tensor<[1, 64, 73, 73]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001      | Done     |
| 19 | Tensor<[1, 96, 35, 35]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001      | Done     |
| 20 | Tensor<[1, 96, 71, 71]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001      | Done     |
| 21 | Tensor<[1, 96, 73, 73]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 0.001      | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1536]> mat1 = ?,<br>Tensor<[1536, 1000]> mat2 = ? | Done     |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                                                                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 17, 17]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>bool<> ceil_mode = False,<br>bool<> count_include_pad = False | Done     |
|  1 | Tensor<[1, 1536, 8, 8]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>bool<> ceil_mode = False,<br>bool<> count_include_pad = False   | Done     |
|  2 | Tensor<[1, 384, 35, 35]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>bool<> ceil_mode = False,<br>bool<> count_include_pad = False  | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 192, 35, 35])', 'torch.Size([1, 192, 35, 35])'],<br>int<> dim = 1                                                                 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 192, 8, 8])', 'torch.Size([1, 320, 8, 8])', 'torch.Size([1, 1024, 8, 8])'],<br>int<> dim = 1                                      | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 256, 8, 8])', 'torch.Size([1, 256, 8, 8])'],<br>int<> dim = 1                                                                     | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, 256, 8, 8])', 'torch.Size([1, 512, 8, 8])', 'torch.Size([1, 512, 8, 8])', 'torch.Size([1, 256, 8, 8])'],<br>int<> dim = 1         | Unknown  |
|  4 | List[Tensor]<> tensors = ['torch.Size([1, 384, 17, 17])', 'torch.Size([1, 256, 17, 17])', 'torch.Size([1, 256, 17, 17])', 'torch.Size([1, 128, 17, 17])'],<br>int<> dim = 1 | Unknown  |
|  5 | List[Tensor]<> tensors = ['torch.Size([1, 384, 17, 17])', 'torch.Size([1, 256, 17, 17])', 'torch.Size([1, 384, 17, 17])'],<br>int<> dim = 1                                 | Unknown  |
|  6 | List[Tensor]<> tensors = ['torch.Size([1, 64, 73, 73])', 'torch.Size([1, 96, 73, 73])'],<br>int<> dim = 1                                                                   | Unknown  |
|  7 | List[Tensor]<> tensors = ['torch.Size([1, 96, 35, 35])', 'torch.Size([1, 96, 35, 35])', 'torch.Size([1, 96, 35, 35])', 'torch.Size([1, 96, 35, 35])'],<br>int<> dim = 1     | Unknown  |
|  8 | List[Tensor]<> tensors = ['torch.Size([1, 96, 71, 71])', 'torch.Size([1, 96, 71, 71])'],<br>int<> dim = 1                                                                   | Unknown  |
|  9 | List[Tensor]<> tensors = [Proxy(getitem_9), Proxy(ttnn_relu_3)],<br>int<> dim = 1                                                                                           | Done     |
| 10 | List[Tensor]<> tensors = [Proxy(ttnn_relu_10), Proxy(getitem_35)],<br>int<> dim = 1                                                                                         | Done     |
| 11 | List[Tensor]<> tensors = [Proxy(ttnn_relu_103), Proxy(ttnn_relu_106), Proxy(ttnn_relu_111), Proxy(ttnn_relu_112)],<br>int<> dim = 1                                         | Done     |
| 12 | List[Tensor]<> tensors = [Proxy(ttnn_relu_11), Proxy(ttnn_relu_13), Proxy(ttnn_relu_16), Proxy(ttnn_relu_17)],<br>int<> dim = 1                                             | Done     |
| 13 | List[Tensor]<> tensors = [Proxy(ttnn_relu_114), Proxy(ttnn_relu_118), Proxy(getitem_363)],<br>int<> dim = 1                                                                 | Done     |
| 14 | List[Tensor]<> tensors = [Proxy(ttnn_relu_119), Proxy(cat_default_16), Proxy(cat_default_17), Proxy(ttnn_relu_128)],<br>int<> dim = 1                                       | Done     |
| 15 | List[Tensor]<> tensors = [Proxy(ttnn_relu_121), Proxy(ttnn_relu_122)],<br>int<> dim = 1                                                                                     | Done     |
| 16 | List[Tensor]<> tensors = [Proxy(ttnn_relu_126), Proxy(ttnn_relu_127)],<br>int<> dim = 1                                                                                     | Done     |
| 17 | List[Tensor]<> tensors = [Proxy(ttnn_relu_129), Proxy(cat_default_19), Proxy(cat_default_20), Proxy(ttnn_relu_138)],<br>int<> dim = 1                                       | Done     |
| 18 | List[Tensor]<> tensors = [Proxy(ttnn_relu_131), Proxy(ttnn_relu_132)],<br>int<> dim = 1                                                                                     | Done     |
| 19 | List[Tensor]<> tensors = [Proxy(ttnn_relu_136), Proxy(ttnn_relu_137)],<br>int<> dim = 1                                                                                     | Done     |
| 20 | List[Tensor]<> tensors = [Proxy(ttnn_relu_139), Proxy(cat_default_22), Proxy(cat_default_23), Proxy(ttnn_relu_148)],<br>int<> dim = 1                                       | Done     |
| 21 | List[Tensor]<> tensors = [Proxy(ttnn_relu_141), Proxy(ttnn_relu_142)],<br>int<> dim = 1                                                                                     | Done     |
| 22 | List[Tensor]<> tensors = [Proxy(ttnn_relu_146), Proxy(ttnn_relu_147)],<br>int<> dim = 1                                                                                     | Done     |
| 23 | List[Tensor]<> tensors = [Proxy(ttnn_relu_18), Proxy(ttnn_relu_20), Proxy(ttnn_relu_23), Proxy(ttnn_relu_24)],<br>int<> dim = 1                                             | Done     |
| 24 | List[Tensor]<> tensors = [Proxy(ttnn_relu_25), Proxy(ttnn_relu_27), Proxy(ttnn_relu_30), Proxy(ttnn_relu_31)],<br>int<> dim = 1                                             | Done     |
| 25 | List[Tensor]<> tensors = [Proxy(ttnn_relu_32), Proxy(ttnn_relu_34), Proxy(ttnn_relu_37), Proxy(ttnn_relu_38)],<br>int<> dim = 1                                             | Done     |
| 26 | List[Tensor]<> tensors = [Proxy(ttnn_relu_39), Proxy(ttnn_relu_42), Proxy(getitem_133)],<br>int<> dim = 1                                                                   | Done     |
| 27 | List[Tensor]<> tensors = [Proxy(ttnn_relu_43), Proxy(ttnn_relu_46), Proxy(ttnn_relu_51), Proxy(ttnn_relu_52)],<br>int<> dim = 1                                             | Done     |
| 28 | List[Tensor]<> tensors = [Proxy(ttnn_relu_5), Proxy(ttnn_relu_9)],<br>int<> dim = 1                                                                                         | Done     |
| 29 | List[Tensor]<> tensors = [Proxy(ttnn_relu_53), Proxy(ttnn_relu_56), Proxy(ttnn_relu_61), Proxy(ttnn_relu_62)],<br>int<> dim = 1                                             | Done     |
| 30 | List[Tensor]<> tensors = [Proxy(ttnn_relu_63), Proxy(ttnn_relu_66), Proxy(ttnn_relu_71), Proxy(ttnn_relu_72)],<br>int<> dim = 1                                             | Done     |
| 31 | List[Tensor]<> tensors = [Proxy(ttnn_relu_73), Proxy(ttnn_relu_76), Proxy(ttnn_relu_81), Proxy(ttnn_relu_82)],<br>int<> dim = 1                                             | Done     |
| 32 | List[Tensor]<> tensors = [Proxy(ttnn_relu_83), Proxy(ttnn_relu_86), Proxy(ttnn_relu_91), Proxy(ttnn_relu_92)],<br>int<> dim = 1                                             | Done     |
| 33 | List[Tensor]<> tensors = [Proxy(ttnn_relu_93), Proxy(ttnn_relu_96), Proxy(ttnn_relu_101), Proxy(ttnn_relu_102)],<br>int<> dim = 1                                           | Done     |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 1536]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[128, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  1 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[192, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  2 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  3 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[384, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  4 | Tensor<[1, 1536, 8, 8]> input = ?,<br>Tensor<[256, 1536, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  5 | Tensor<[1, 1536, 8, 8]> input = ?,<br>Tensor<[384, 1536, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  6 | Tensor<[1, 160, 73, 73]> input = ?,<br>Tensor<[64, 160, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Done     |
|  7 | Tensor<[1, 192, 17, 17]> input = ?,<br>Tensor<[192, 192, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  8 | Tensor<[1, 192, 17, 17]> input = ?,<br>Tensor<[192, 192, 7, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [3, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  9 | Tensor<[1, 192, 17, 17]> input = ?,<br>Tensor<[224, 192, 1, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 10 | Tensor<[1, 192, 35, 35]> input = ?,<br>Tensor<[224, 192, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 11 | Tensor<[1, 192, 71, 71]> input = ?,<br>Tensor<[192, 192, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 12 | Tensor<[1, 224, 17, 17]> input = ?,<br>Tensor<[224, 224, 7, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [3, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 13 | Tensor<[1, 224, 17, 17]> input = ?,<br>Tensor<[256, 224, 1, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 14 | Tensor<[1, 224, 17, 17]> input = ?,<br>Tensor<[256, 224, 7, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [3, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 15 | Tensor<[1, 224, 35, 35]> input = ?,<br>Tensor<[256, 224, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 16 | Tensor<[1, 256, 17, 17]> input = ?,<br>Tensor<[256, 256, 1, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 17 | Tensor<[1, 256, 17, 17]> input = ?,<br>Tensor<[320, 256, 7, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [3, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 18 | Tensor<[1, 3, 299, 299]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 19 | Tensor<[1, 32, 147, 147]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Done     |
| 20 | Tensor<[1, 32, 149, 149]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Done     |
| 21 | Tensor<[1, 320, 17, 17]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 22 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[192, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 23 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[384, 384, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 24 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[64, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Done     |
| 25 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[96, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Done     |
| 26 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[256, 384, 1, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 27 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[256, 384, 3, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 28 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[448, 384, 3, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 29 | Tensor<[1, 448, 8, 8]> input = ?,<br>Tensor<[512, 448, 1, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 30 | Tensor<[1, 512, 8, 8]> input = ?,<br>Tensor<[256, 512, 1, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 31 | Tensor<[1, 512, 8, 8]> input = ?,<br>Tensor<[256, 512, 3, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 32 | Tensor<[1, 64, 147, 147]> input = ?,<br>Tensor<[96, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Done     |
| 33 | Tensor<[1, 64, 35, 35]> input = ?,<br>Tensor<[96, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 34 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[64, 64, 1, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 35 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[64, 64, 7, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [3, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 36 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[96, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 37 | Tensor<[1, 96, 35, 35]> input = ?,<br>Tensor<[96, 96, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 17, 17]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2] | Done     |
|  1 | Tensor<[1, 192, 71, 71]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2]  | Done     |
|  2 | Tensor<[1, 384, 35, 35]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2]  | Done     |
|  3 | Tensor<[1, 64, 147, 147]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2] | Done     |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 128, 17, 17]> self = ?  | Done     |
|  1 | Tensor<[1, 192, 17, 17]> self = ?  | Done     |
|  2 | Tensor<[1, 192, 35, 35]> self = ?  | Done     |
|  3 | Tensor<[1, 192, 8, 8]> self = ?    | Done     |
|  4 | Tensor<[1, 224, 17, 17]> self = ?  | Done     |
|  5 | Tensor<[1, 224, 35, 35]> self = ?  | Done     |
|  6 | Tensor<[1, 256, 17, 17]> self = ?  | Done     |
|  7 | Tensor<[1, 256, 8, 8]> self = ?    | Done     |
|  8 | Tensor<[1, 32, 147, 147]> self = ? | Done     |
|  9 | Tensor<[1, 32, 149, 149]> self = ? | Done     |
| 10 | Tensor<[1, 320, 17, 17]> self = ?  | Done     |
| 11 | Tensor<[1, 320, 8, 8]> self = ?    | Done     |
| 12 | Tensor<[1, 384, 17, 17]> self = ?  | Done     |
| 13 | Tensor<[1, 384, 8, 8]> self = ?    | Done     |
| 14 | Tensor<[1, 448, 8, 8]> self = ?    | Done     |
| 15 | Tensor<[1, 512, 8, 8]> self = ?    | Done     |
| 16 | Tensor<[1, 64, 147, 147]> self = ? | Done     |
| 17 | Tensor<[1, 64, 35, 35]> self = ?   | Done     |
| 18 | Tensor<[1, 64, 73, 73]> self = ?   | Done     |
| 19 | Tensor<[1, 96, 35, 35]> self = ?   | Done     |
| 20 | Tensor<[1, 96, 71, 71]> self = ?   | Done     |
| 21 | Tensor<[1, 96, 73, 73]> self = ?   | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1536]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int]<> size = [1, 1536] | Done     |

