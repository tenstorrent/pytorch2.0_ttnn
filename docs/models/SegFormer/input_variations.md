# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |
|  1 | aten._softmax.default                             |                  1 |
|  2 | aten._to_copy.default                             |                  1 |
|  3 | aten._unsafe_index.Tensor                         |                  4 |
|  4 | aten.add.Tensor                                   |                  2 |
|  5 | aten.addmm.default                                |                  1 |
|  6 | aten.arange.default                               |                  1 |
|  7 | aten.bmm.default                                  |                  1 |
|  8 | aten.cat.default                                  |                  1 |
|  9 | aten.ceil.default                                 |                  1 |
| 10 | aten.clamp.default                                |                  2 |
| 11 | aten.clone.default                                |                  3 |
| 12 | aten.convolution.default                          |                 11 |
| 13 | aten.div.Tensor                                   |                  1 |
| 14 | aten.expand.default                               |                 15 |
| 15 | aten.gelu.default                                 |                  1 |
| 16 | aten.mm.default                                   |                  1 |
| 17 | aten.mul.Tensor                                   |                  2 |
| 18 | aten.native_layer_norm.default                    |                  4 |
| 19 | aten.permute.default                              |                  3 |
| 20 | aten.relu.default                                 |                  1 |
| 21 | aten.rsub.Scalar                                  |                  1 |
| 22 | aten.sub.Tensor                                   |                  2 |
| 23 | aten.t.default                                    |                  1 |
| 24 | aten.transpose.int                                |                  2 |
| 25 | aten.unsqueeze.default                            |                  1 |
| 26 | aten.view.default                                 |                 59 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2] | Unknown  |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_10, _to_copy_14] | Unknown  |
|  2 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_7, _to_copy_10]  | Unknown  |
|  3 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_4, _to_copy_6]   | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ? | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                        | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 128,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [clone_46, clone_45, clone_44, clone_43],<br>int dim = 1 | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[128]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Optional[number] min = 0.0                                 | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 127 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                          | Unknown  |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last    | Unknown  |
|  2 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Unknown  |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Unknown  |
|  3 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  4 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  5 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | Unknown  |
|  6 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  7 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  8 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  9 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 10 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Unknown  |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Unknown  |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]       | Unknown  |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]       | Unknown  |
|  4 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]       | Unknown  |
|  5 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]       | Unknown  |
|  6 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Unknown  |
|  7 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Unknown  |
|  8 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Unknown  |
|  9 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Unknown  |
| 10 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]       | Unknown  |
| 11 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]       | Unknown  |
| 12 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Unknown  |
| 13 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Unknown  |
| 14 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]       | Unknown  |
### aten.gelu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 16384, 128]> self = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ? | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05    | Unknown  |
|  2 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05  | Unknown  |
|  3 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05     | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  |
|  1 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
|  2 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[128, 1]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ? | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>Tensor other = 0.5            | Unknown  |
### aten.t.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[32, 32]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
|  1 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   |
|---:|:---------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>int dim = 1 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256] | Unknown  |
|  1 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]   | Unknown  |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]         | Unknown  |
|  3 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]   | Unknown  |
|  4 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]         | Unknown  |
|  5 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384] | Unknown  |
|  6 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128] | Unknown  |
|  7 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]    | Unknown  |
|  8 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]     | Unknown  |
|  9 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]    | Unknown  |
| 10 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]       | Unknown  |
| 11 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Unknown  |
| 12 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]         | Unknown  |
| 13 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]       | Unknown  |
| 14 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]       | Unknown  |
| 15 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]   | Unknown  |
| 16 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]     | Unknown  |
| 17 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]         | Unknown  |
| 18 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]     | Unknown  |
| 19 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]           | Unknown  |
| 20 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128] | Unknown  |
| 21 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]           | Unknown  |
| 22 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]             | Unknown  |
| 23 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]    | Unknown  |
| 24 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]    | Unknown  |
| 25 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]             | Unknown  |
| 26 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]   | Unknown  |
| 27 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]       | Unknown  |
| 28 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]   | Unknown  |
| 29 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]         | Unknown  |
| 30 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]           | Unknown  |
| 31 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]   | Unknown  |
| 32 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]     | Unknown  |
| 33 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]       | Unknown  |
| 34 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]       | Unknown  |
| 35 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]       | Unknown  |
| 36 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]      | Unknown  |
| 37 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]      | Unknown  |
| 38 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]    | Unknown  |
| 39 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]    | Unknown  |
| 40 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]     | Unknown  |
| 41 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]       | Unknown  |
| 42 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]       | Unknown  |
| 43 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]         | Unknown  |
| 44 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]         | Unknown  |
| 45 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]       | Unknown  |
| 46 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Unknown  |
| 47 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Unknown  |
| 48 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Unknown  |
| 49 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]         | Unknown  |
| 50 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]           | Unknown  |
| 51 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Unknown  |
| 52 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]             | Unknown  |
| 53 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]         | Unknown  |
| 54 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]           | Unknown  |
| 55 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Unknown  |
| 56 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Unknown  |
| 57 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Unknown  |
| 58 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Unknown  |

