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
|  0 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] size = [4, 49, 384]     | Unknown  |
|  1 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384] | Unknown  |
|  2 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] size = [16, 49, 192]    | Unknown  |
|  3 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192] | Unknown  |
|  4 | Tensor<[1, 49, 24, 32]> self = ?,<br>List[int] size = [1, 49, 768]          | Unknown  |
|  5 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]   | Unknown  |
|  6 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] size = [64, 49, 96]      | Unknown  |
|  7 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [96, 32, 49]          | Unknown  |
|  8 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [96, 49, 32]          | Unknown  |
|  9 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int] size = [4, 49]                  | Unknown  |
| 10 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [48, 32, 49]          | Unknown  |
| 11 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [48, 49, 32]          | Unknown  |
| 12 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int] size = [16, 49]                 | Unknown  |
| 13 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [192, 32, 49]         | Unknown  |
| 14 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [192, 49, 32]         | Unknown  |
| 15 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int] size = [64, 49]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[288]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ? | Unknown  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [slice_7, slice_10, slice_13, slice_16],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[64, 3, 49, 49]> self = ?                                                       | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [1, 24, 32, 49] | Unknown  |
|  1 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32] | Unknown  |
|  2 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49] | Unknown  |
|  3 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [16, 6, 32, 49] | Unknown  |
|  4 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32] | Unknown  |
|  5 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49] | Unknown  |
|  6 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [4, 12, 32, 49] | Unknown  |
|  7 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32] | Unknown  |
|  8 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49] | Unknown  |
|  9 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [64, 3, 32, 49] | Unknown  |
| 10 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32] | Unknown  |
| 11 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 56, 56, 384]> self = ? | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[169, 12]> self = ?,<br>List[Optional[Tensor]] indices = [primals_334] | Unknown  |
|  1 | Tensor<[169, 24]> self = ?,<br>List[Optional[Tensor]] indices = [primals_352] | Unknown  |
|  2 | Tensor<[169, 3]> self = ?,<br>List[Optional[Tensor]] indices = [primals_330]  | Unknown  |
|  3 | Tensor<[169, 6]> self = ?,<br>List[Optional[Tensor]] indices = [primals_332]  | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0    | Unknown  |
|  1 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0 | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 14, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05   | Unknown  |
|  1 | Tensor<[1, 28, 28, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05   | Unknown  |
|  2 | Tensor<[1, 28, 28, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05   | Unknown  |
|  3 | Tensor<[1, 56, 56, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05       | Unknown  |
|  4 | Tensor<[1, 7, 7, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [28, 28],<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [14, 14],<br>Optional[bool] pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [56, 56],<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  1 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  2 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]           | Unknown  |
|  3 | Tensor<[49, 49, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Unknown  |
|  4 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]     | Unknown  |
|  5 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
### aten.roll.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]  | Unknown  |
|  1 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
|  1 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
|  2 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  1 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  2 | Tensor<[1, 28, 28, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  3 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
|  4 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  5 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[288, 96]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  |
|  1 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[16, 49]> self = ?,<br>int dim = 2    | Unknown  |
|  1 | Tensor<[3, 49, 49]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[64, 49]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 49, 768]     | Unknown  |
|  1 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int] size = [196, 1536]         | Unknown  |
|  2 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 384] | Unknown  |
|  3 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int] size = [196, 768]           | Unknown  |
|  4 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int] size = [-1, 6, 49, 49]    | Unknown  |
|  5 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [24, 32, 49]          | Unknown  |
|  6 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [24, 49, 32]          | Unknown  |
|  7 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [24, 49, 49]          | Unknown  |
|  8 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 192] | Unknown  |
|  9 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int] size = [784, 384]           | Unknown  |
| 10 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int] size = [784, 768]           | Unknown  |
| 11 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int] size = [-1, 12, 49, 49]   | Unknown  |
| 12 | Tensor<[1, 49, 2304]> self = ?,<br>List[int] size = [1, 49, 3, 24, 32]      | Unknown  |
| 13 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [49, 768]                | Unknown  |
| 14 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int] size = [3136, 384]          | Unknown  |
| 15 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 96]   | Unknown  |
| 16 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int] size = [-1, 3, 49, 49]    | Unknown  |
| 17 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int] size = [49, 1536]            | Unknown  |
| 18 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int] size = [49, 3072]            | Unknown  |
| 19 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 768]   | Unknown  |
| 20 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]               | Unknown  |
| 21 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                 | Unknown  |
| 22 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [784, 192]              | Unknown  |
| 23 | Tensor<[16, 49, 576]> self = ?,<br>List[int] size = [16, 49, 3, 6, 32]      | Unknown  |
| 24 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [96, 49, 49]          | Unknown  |
| 25 | Tensor<[192, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]         | Unknown  |
| 26 | Tensor<[192, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]         | Unknown  |
| 27 | Tensor<[196, 1152]> self = ?,<br>List[int] size = [4, 49, 1152]             | Unknown  |
| 28 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [1, 14, 14, 1536]         | Unknown  |
| 29 | Tensor<[196, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]           | Unknown  |
| 30 | Tensor<[24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]          | Unknown  |
| 31 | Tensor<[24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]          | Unknown  |
| 32 | Tensor<[2401, 3]> self = ?,<br>List[int] size = [49, 49, -1]                | Unknown  |
| 33 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                 | Unknown  |
| 34 | Tensor<[3136, 288]> self = ?,<br>List[int] size = [64, 49, 288]             | Unknown  |
| 35 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [1, 56, 56, 384]          | Unknown  |
| 36 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [64, 49, 96]               | Unknown  |
| 37 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [48, 49, 49]          | Unknown  |
| 38 | Tensor<[4, 49, 1152]> self = ?,<br>List[int] size = [4, 49, 3, 12, 32]      | Unknown  |
| 39 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [196, 384]               | Unknown  |
| 40 | Tensor<[48, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]          | Unknown  |
| 41 | Tensor<[48, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]          | Unknown  |
| 42 | Tensor<[49, 2304]> self = ?,<br>List[int] size = [1, 49, 2304]              | Unknown  |
| 43 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 7, 7, 3072]            | Unknown  |
| 44 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]              | Unknown  |
| 45 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                 | Unknown  |
| 46 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [192, 49, 49]         | Unknown  |
| 47 | Tensor<[64, 49, 288]> self = ?,<br>List[int] size = [64, 49, 3, 3, 32]      | Unknown  |
| 48 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [3136, 96]               | Unknown  |
| 49 | Tensor<[784, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]           | Unknown  |
| 50 | Tensor<[784, 576]> self = ?,<br>List[int] size = [16, 49, 576]              | Unknown  |
| 51 | Tensor<[784, 768]> self = ?,<br>List[int] size = [1, 28, 28, 768]           | Unknown  |
| 52 | Tensor<[96, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]          | Unknown  |
| 53 | Tensor<[96, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]          | Unknown  |

