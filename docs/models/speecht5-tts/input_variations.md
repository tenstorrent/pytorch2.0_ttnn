# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |
|  1 | aten._softmax.default                             |                  1 |
|  2 | aten._to_copy.default                             |                  2 |
|  3 | aten._unsafe_view.default                         |                  1 |
|  4 | aten.add.Tensor                                   |                  2 |
|  5 | aten.addmm.default                                |                  1 |
|  6 | aten.arange.start                                 |                  1 |
|  7 | aten.bernoulli.p                                  |                  1 |
|  8 | aten.bmm.default                                  |                  1 |
|  9 | aten.cat.default                                  |                  1 |
| 10 | aten.clamp_min.default                            |                  1 |
| 11 | aten.clone.default                                |                  2 |
| 12 | aten.convolution.default                          |                 11 |
| 13 | aten.div.Tensor                                   |                  3 |
| 14 | aten.embedding.default                            |                  2 |
| 15 | aten.eq.Scalar                                    |                  1 |
| 16 | aten.expand.default                               |                  5 |
| 17 | aten.gelu.default                                 |                  1 |
| 18 | aten.leaky_relu.default                           |                  2 |
| 19 | aten.linalg_vector_norm.default                   |                  1 |
| 20 | aten.masked_fill.Scalar                           |                  1 |
| 21 | aten.mul.Tensor                                   |                  3 |
| 22 | aten.native_layer_norm.default                    |                  1 |
| 23 | aten.relu.default                                 |                  1 |
| 24 | aten.repeat.default                               |                  1 |
| 25 | aten.rsub.Scalar                                  |                  1 |
| 26 | aten.scalar_tensor.default                        |                  1 |
| 27 | aten.select.int                                   |                  1 |
| 28 | aten.slice.Tensor                                 |                  5 |
| 29 | aten.squeeze.dim                                  |                  1 |
| 30 | aten.sub.Tensor                                   |                  1 |
| 31 | aten.sym_size.int                                 |                  1 |
| 32 | aten.t.default                                    |                  1 |
| 33 | aten.tanh.default                                 |                  1 |
| 34 | aten.transpose.int                                |                  5 |
| 35 | aten.unsqueeze.default                            |                  3 |
| 36 | aten.view.default                                 |                 27 |
| 37 | aten.where.self                                   |                  1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 100]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bool     | Unknown  |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int] size = [1, 24, 768] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ? | Unknown  |
|  1 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                 | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 24,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bernoulli.p
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 256]> self = ?,<br>float p = 0.5 | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [clone_2, expand_1],<br>int dim = -1 | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 24, 768]> self = ?                                                              | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  |
|  1 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  |
|  2 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  |
|  3 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  |
|  4 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  |
|  5 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  |
|  6 | Tensor<[1, 512, 100]> input = ?,<br>Tensor<[512, 256, 8]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  |
|  7 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  |
|  8 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  |
|  9 | Tensor<[1, 80, 100]> input = ?,<br>Tensor<[256, 80, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1          | Unknown  |
| 10 | Tensor<[1, 80, 100]> input = ?,<br>Tensor<[512, 80, 7]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 0.5      | Unknown  |
|  1 | Tensor<[1, 256, 400]> self = ?,<br>Tensor other = 3      | Unknown  |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ? | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                        | Unknown  |
|  1 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1 | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>number other = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24] | Unknown  |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [-1, 1, -1]      | Unknown  |
|  2 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 512]              | Unknown  |
|  3 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]    | Unknown  |
|  4 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]    | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 24, 3072]> self = ? | Unknown  |
### aten.leaky_relu.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 25600]> self = ?                                | Unknown  |
|  1 | Tensor<[1, 512, 100]> self = ?,<br>number negative_slope = 0.1 | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1      | Unknown  |
|  1 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125 | Unknown  |
|  2 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.relu.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ? | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number s = 0,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
### aten.select.int
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
|  1 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1     | Unknown  |
|  2 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int]<s0> end = ? | Unknown  |
|  3 | Tensor<[1, 24]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1           | Unknown  |
|  4 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 25600]> self = ?,<br>int dim = 0 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ? | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 1 | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 256, 100]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 80]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1    | Unknown  |
|  1 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
|  2 | Tensor<[1, 25600]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0      | Unknown  |
|  3 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1    | Unknown  |
|  4 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1  | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2 | Unknown  |
|  1 | Tensor<[1, 24]> self = ?,<br>int dim = 1    | Unknown  |
|  2 | Tensor<[24]> self = ?,<br>int dim = 0       | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, 1280]               | Unknown  |
|  1 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [1, 256]                 | Unknown  |
|  2 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]               | Unknown  |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                 | Unknown  |
|  4 | Tensor<[1, 1, 80]> self = ?,<br>List[int] size = [1, 80]                   | Unknown  |
|  5 | Tensor<[1, 12, 1, 24]> self = ?,<br>List[int] size = [12, 1, 24]           | Unknown  |
|  6 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  |
|  7 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]             | Unknown  |
|  8 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]               | Unknown  |
|  9 | Tensor<[1, 256]> self = ?,<br>List[int] size = [1, 1, 256]                 | Unknown  |
| 10 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]               | Unknown  |
| 11 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                 | Unknown  |
| 12 | Tensor<[1, s0, 1280]> self = ?,<br>List[int] size = [sym_size_int_2, 1280] | Unknown  |
| 13 | Tensor<[1, s0, 256]> self = ?,<br>List[int] size = [sym_size_int, 256]     | Unknown  |
| 14 | Tensor<[1, s0, 80]> self = ?,<br>List[int] size = [arg10_1, 80]            | Unknown  |
| 15 | Tensor<[12, 1, 24]> self = ?,<br>List[int] size = [1, 12, 1, 24]           | Unknown  |
| 16 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]           | Unknown  |
| 17 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]            | Unknown  |
| 18 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]         | Unknown  |
| 19 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]            | Unknown  |
| 20 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]            | Unknown  |
| 21 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]             | Unknown  |
| 22 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]            | Unknown  |
| 23 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]               | Unknown  |
| 24 | Tensor<[25600, 1]> self = ?,<br>List[int] size = [-1]                      | Unknown  |
| 25 | Tensor<[s0, 256]> self = ?,<br>List[int] size = [1, arg10_1, 256]          | Unknown  |
| 26 | Tensor<[s0, 768]> self = ?,<br>List[int] size = [1, sym_size_int_1, 768]   | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> condition = ?,<br>Tensor<[1, 1, 256]> self = ?,<br>Tensor<[]> other = ? | Unknown  |

