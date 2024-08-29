# High Level Operations Status
|    | Operations                           |   Input Variations |
|---:|:-------------------------------------|-------------------:|
|  0 | aten._softmax.default                |                  1 |
|  1 | aten._to_copy.default                |                  3 |
|  2 | aten._unsafe_index.Tensor            |                  1 |
|  3 | aten.add.Tensor                      |                  4 |
|  4 | aten.addmm.default                   |                  1 |
|  5 | aten.arange.default                  |                  1 |
|  6 | aten.baddbmm.default                 |                  1 |
|  7 | aten.bitwise_not.default             |                  1 |
|  8 | aten.bmm.default                     |                  1 |
|  9 | aten.cat.default                     |                  1 |
| 10 | aten.clone.default                   |                  1 |
| 11 | aten.convolution.default             |                  6 |
| 12 | aten.cos.default                     |                  1 |
| 13 | aten.cumsum.default                  |                  1 |
| 14 | aten.div.Tensor                      |                  3 |
| 15 | aten.expand.default                  |                  1 |
| 16 | aten.floor_divide.default            |                  1 |
| 17 | aten.masked_fill.Scalar              |                  1 |
| 18 | aten.max_pool2d_with_indices.default |                  1 |
| 19 | aten.mm.default                      |                  1 |
| 20 | aten.mul.Tensor                      |                  5 |
| 21 | aten.native_dropout.default          |                  1 |
| 22 | aten.native_layer_norm.default       |                  1 |
| 23 | aten.ones.default                    |                  1 |
| 24 | aten.permute.default                 |                  2 |
| 25 | aten.pow.Scalar                      |                  1 |
| 26 | aten.relu.default                    |                  1 |
| 27 | aten.repeat.default                  |                  1 |
| 28 | aten.rsqrt.default                   |                  1 |
| 29 | aten.select.int                      |                  2 |
| 30 | aten.sigmoid.default                 |                  1 |
| 31 | aten.sin.default                     |                  1 |
| 32 | aten.slice.Tensor                    |                  4 |
| 33 | aten.split.Tensor                    |                  1 |
| 34 | aten.stack.default                   |                  2 |
| 35 | aten.sub.Tensor                      |                  1 |
| 36 | aten.t.default                       |                  1 |
| 37 | aten.transpose.int                   |                  3 |
| 38 | aten.unsqueeze.default               |                  4 |
| 39 | aten.view.default                    |                 18 |
| 40 | aten.zeros.default                   |                  1 |
| 41 | aten.zeros_like.default              |                  2 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 23, 40]> self = ?,<br>Optional[int] dtype = torch.bool       | Unknown  |
|  1 | Tensor<[1, 1, 720, 1280]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
|  2 | Tensor<[23]> self = ?,<br>Optional[int] dtype = torch.int64                | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 720, 1280]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                   | Unknown  |
|  1 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                | Unknown  |
|  2 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ? | Unknown  |
|  3 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                           | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[256]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 23,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 920, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ? | Unknown  |
### aten.bitwise_not.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 23, 40]> self = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [view_213, view_212],<br>int dim = 3 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 180, 320]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  1 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  2 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  3 | Tensor<[1, 3, 720, 1280]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  4 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
|  5 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
### aten.cos.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?      | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>Tensor other = 128                      | Unknown  |
|  2 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1] | Unknown  |
### aten.floor_divide.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Tensor other = 2 | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 920]> self = ?,<br>Tensor<[1, 920]> mask = ?,<br>number value = -inf | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 360, 640]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586  | Unknown  |
|  1 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ? | Unknown  |
|  2 | Tensor<[128]> self = ?,<br>Tensor other = 2                        | Unknown  |
|  3 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957        | Unknown  |
|  4 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                      | Unknown  |
### aten.native_dropout.default
|    | ATen Input Variations                                                             | Status   |
|---:|:----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[8, 920, 920]> input = ?,<br>float p = 0.1,<br>Optional[bool] train = True | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[920, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 720, 1280],<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  |
|  1 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]       | Unknown  |
### aten.pow.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | number self = 10000,<br>Tensor<[128]> exponent = ? | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 64, 360, 640]> self = ? | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 64, 1, 1]> self = ? | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0   | Unknown  |
|  1 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[6, 1, 100, 4]> self = ? | Unknown  |
### aten.sin.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
|  1 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  2 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  3 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[768, 256]> self = ?,<br>int split_size = 256 | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [getitem_155, getitem_191, getitem_227, getitem_263, getitem_299, getitem_335] | Unknown  |
|  1 | List[Tensor] tensors = [sin, cos],<br>int dim = 4                                                     | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[256, 256]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
|  1 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1   | Unknown  |
|  2 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3    | Unknown  |
|  1 | Tensor<[1, 720, 1280]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[100, 256]> self = ?,<br>int dim = 1     | Unknown  |
|  3 | Tensor<[23]> self = ?,<br>int dim = -1          | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128] | Unknown  |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                | Unknown  |
|  2 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]      | Unknown  |
|  3 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]          | Unknown  |
|  4 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]             | Unknown  |
|  5 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]          | Unknown  |
|  6 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]            | Unknown  |
|  7 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]          | Unknown  |
|  8 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]            | Unknown  |
|  9 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]         | Unknown  |
| 10 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]         | Unknown  |
| 11 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]             | Unknown  |
| 12 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]           | Unknown  |
| 13 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                  | Unknown  |
| 14 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]          | Unknown  |
| 15 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]            | Unknown  |
| 16 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]          | Unknown  |
| 17 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]            | Unknown  |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 920]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                                    | Unknown  |

