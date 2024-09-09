# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._unsafe_view.default      |                 16 |
|  2 | aten.add.Tensor                |                  1 |
|  3 | aten.addmm.default             |                  1 |
|  4 | aten.as_strided.default        |                  1 |
|  5 | aten.bmm.default               |                  1 |
|  6 | aten.cat.default               |                  1 |
|  7 | aten.clone.default             |                  2 |
|  8 | aten.constant_pad_nd.default   |                  1 |
|  9 | aten.convolution.default       |                  1 |
| 10 | aten.eq.Scalar                 |                  1 |
| 11 | aten.expand.default            |                 12 |
| 12 | aten.gelu.default              |                  1 |
| 13 | aten.index.Tensor              |                  4 |
| 14 | aten.masked_fill.Scalar        |                  2 |
| 15 | aten.mean.dim                  |                  1 |
| 16 | aten.mm.default                |                  1 |
| 17 | aten.mul.Tensor                |                  1 |
| 18 | aten.native_layer_norm.default |                  5 |
| 19 | aten.ne.Scalar                 |                  1 |
| 20 | aten.new_zeros.default         |                  3 |
| 21 | aten.permute.default           |                  6 |
| 22 | aten.roll.default              |                  2 |
| 23 | aten.select.int                |                  3 |
| 24 | aten.slice.Tensor              |                  6 |
| 25 | aten.sub.Tensor                |                  1 |
| 26 | aten.t.default                 |                  1 |
| 27 | aten.transpose.int             |                  2 |
| 28 | aten.unsqueeze.default         |                  3 |
| 29 | aten.view.default              |                 54 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] size = [4, 49, 512]     | Unknown  |
|  1 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512] | Unknown  |
|  2 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] size = [16, 49, 256]    | Unknown  |
|  3 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256] | Unknown  |
|  4 | Tensor<[1, 49, 32, 32]> self = ?,<br>List[int] size = [1, 49, 1024]         | Unknown  |
|  5 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128] | Unknown  |
|  6 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] size = [64, 49, 128]    | Unknown  |
|  7 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [128, 32, 49]         | Unknown  |
|  8 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [128, 49, 32]         | Unknown  |
|  9 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int] size = [4, 49]                  | Unknown  |
| 10 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [64, 32, 49]          | Unknown  |
| 11 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [64, 49, 32]          | Unknown  |
| 12 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int] size = [16, 49]                 | Unknown  |
| 13 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [256, 32, 49]         | Unknown  |
| 14 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [256, 49, 32]         | Unknown  |
| 15 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int] size = [64, 49]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[384]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ? | Unknown  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 1, 1],<br>List[int] stride = [1024, 1, 1024, 1024] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [slice_7, slice_10, slice_13, slice_16],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[64, 4, 49, 49]> self = ?                                                       | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [1, 32, 32, 49] | Unknown  |
|  1 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32] | Unknown  |
|  2 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49] | Unknown  |
|  3 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [16, 8, 32, 49] | Unknown  |
|  4 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32] | Unknown  |
|  5 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49] | Unknown  |
|  6 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [4, 16, 32, 49] | Unknown  |
|  7 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32] | Unknown  |
|  8 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49] | Unknown  |
|  9 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [64, 4, 32, 49] | Unknown  |
| 10 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32] | Unknown  |
| 11 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 56, 56, 512]> self = ? | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[169, 16]> self = ?,<br>List[Optional[Tensor]] indices = [primals_334] | Unknown  |
|  1 | Tensor<[169, 32]> self = ?,<br>List[Optional[Tensor]] indices = [primals_352] | Unknown  |
|  2 | Tensor<[169, 4]> self = ?,<br>List[Optional[Tensor]] indices = [primals_330]  | Unknown  |
|  3 | Tensor<[169, 8]> self = ?,<br>List[Optional[Tensor]] indices = [primals_332]  | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0    | Unknown  |
|  1 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0 | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 28, 28, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05     | Unknown  |
|  2 | Tensor<[1, 28, 28, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Unknown  |
|  3 | Tensor<[1, 56, 56, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05     | Unknown  |
|  4 | Tensor<[1, 7, 7, 2048]> input = ?,<br>List[int] normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float eps = 1e-05   | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [28, 28],<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [14, 14],<br>Optional[bool] pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [56, 56],<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]           | Unknown  |
|  1 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  2 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  3 | Tensor<[49, 49, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Unknown  |
|  4 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Unknown  |
|  5 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | Unknown  |
|  1 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
|  1 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
|  2 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  1 | Tensor<[1, 28, 28, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  2 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  3 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  4 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  5 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[384, 128]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  |
|  1 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[16, 49]> self = ?,<br>int dim = 2    | Unknown  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[64, 49]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]   | Unknown  |
|  1 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]             | Unknown  |
|  2 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int] size = [196, 1024]         | Unknown  |
|  3 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int] size = [196, 2048]         | Unknown  |
|  4 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 512] | Unknown  |
|  5 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int] size = [-1, 8, 49, 49]    | Unknown  |
|  6 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int] size = [784, 1024]         | Unknown  |
|  7 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 256] | Unknown  |
|  8 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int] size = [784, 512]           | Unknown  |
|  9 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [32, 32, 49]          | Unknown  |
| 10 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [32, 49, 32]          | Unknown  |
| 11 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [32, 49, 49]          | Unknown  |
| 12 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int] size = [-1, 16, 49, 49]   | Unknown  |
| 13 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [49, 1024]              | Unknown  |
| 14 | Tensor<[1, 49, 3072]> self = ?,<br>List[int] size = [1, 49, 3, 32, 32]      | Unknown  |
| 15 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 128] | Unknown  |
| 16 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int] size = [3136, 512]          | Unknown  |
| 17 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int] size = [-1, 4, 49, 49]    | Unknown  |
| 18 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 1024] | Unknown  |
| 19 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int] size = [49, 2048]            | Unknown  |
| 20 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int] size = [49, 4096]            | Unknown  |
| 21 | Tensor<[128, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]         | Unknown  |
| 22 | Tensor<[128, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]         | Unknown  |
| 23 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                 | Unknown  |
| 24 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [784, 256]              | Unknown  |
| 25 | Tensor<[16, 49, 768]> self = ?,<br>List[int] size = [16, 49, 3, 8, 32]      | Unknown  |
| 26 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [128, 49, 49]         | Unknown  |
| 27 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [4, 49, 1536]             | Unknown  |
| 28 | Tensor<[196, 2048]> self = ?,<br>List[int] size = [1, 14, 14, 2048]         | Unknown  |
| 29 | Tensor<[196, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]           | Unknown  |
| 30 | Tensor<[2401, 4]> self = ?,<br>List[int] size = [49, 49, -1]                | Unknown  |
| 31 | Tensor<[256, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]         | Unknown  |
| 32 | Tensor<[256, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]         | Unknown  |
| 33 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                 | Unknown  |
| 34 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [64, 49, 128]             | Unknown  |
| 35 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [64, 49, 384]             | Unknown  |
| 36 | Tensor<[3136, 512]> self = ?,<br>List[int] size = [1, 56, 56, 512]          | Unknown  |
| 37 | Tensor<[32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]          | Unknown  |
| 38 | Tensor<[32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]          | Unknown  |
| 39 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [64, 49, 49]          | Unknown  |
| 40 | Tensor<[4, 49, 1536]> self = ?,<br>List[int] size = [4, 49, 3, 16, 32]      | Unknown  |
| 41 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [196, 512]               | Unknown  |
| 42 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]            | Unknown  |
| 43 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 49, 3072]              | Unknown  |
| 44 | Tensor<[49, 4096]> self = ?,<br>List[int] size = [1, 7, 7, 4096]            | Unknown  |
| 45 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                 | Unknown  |
| 46 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [256, 49, 49]         | Unknown  |
| 47 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [3136, 128]             | Unknown  |
| 48 | Tensor<[64, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]          | Unknown  |
| 49 | Tensor<[64, 49, 384]> self = ?,<br>List[int] size = [64, 49, 3, 4, 32]      | Unknown  |
| 50 | Tensor<[64, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]          | Unknown  |
| 51 | Tensor<[784, 1024]> self = ?,<br>List[int] size = [1, 28, 28, 1024]         | Unknown  |
| 52 | Tensor<[784, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]           | Unknown  |
| 53 | Tensor<[784, 768]> self = ?,<br>List[int] size = [16, 49, 768]              | Unknown  |

