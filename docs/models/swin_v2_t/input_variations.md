# High Level Operations Status
|    | Operations                      |   Input Variations |
|---:|:--------------------------------|-------------------:|
|  0 | aten._softmax.default           |                  1 |
|  1 | aten._unsafe_view.default       |                 15 |
|  2 | aten.add.Tensor                 |                  1 |
|  3 | aten.addmm.default              |                  1 |
|  4 | aten.as_strided.default         |                  1 |
|  5 | aten.bmm.default                |                  1 |
|  6 | aten.cat.default                |                  1 |
|  7 | aten.clamp.default              |                  1 |
|  8 | aten.clamp_min.default          |                  1 |
|  9 | aten.clone.default              |                  2 |
| 10 | aten.constant_pad_nd.default    |                  1 |
| 11 | aten.convolution.default        |                  1 |
| 12 | aten.div.Tensor                 |                  1 |
| 13 | aten.eq.Scalar                  |                  1 |
| 14 | aten.exp.default                |                  1 |
| 15 | aten.expand.default             |                 12 |
| 16 | aten.gelu.default               |                  1 |
| 17 | aten.index.Tensor               |                  4 |
| 18 | aten.linalg_vector_norm.default |                  1 |
| 19 | aten.masked_fill.Scalar         |                  2 |
| 20 | aten.mean.dim                   |                  1 |
| 21 | aten.mm.default                 |                  1 |
| 22 | aten.mul.Tensor                 |                  2 |
| 23 | aten.native_layer_norm.default  |                  4 |
| 24 | aten.ne.Scalar                  |                  1 |
| 25 | aten.new_zeros.default          |                  3 |
| 26 | aten.permute.default            |                  6 |
| 27 | aten.relu.default               |                  1 |
| 28 | aten.roll.default               |                  2 |
| 29 | aten.select.int                 |                  3 |
| 30 | aten.sigmoid.default            |                  1 |
| 31 | aten.slice.Tensor               |                  6 |
| 32 | aten.sub.Tensor                 |                  1 |
| 33 | aten.t.default                  |                  1 |
| 34 | aten.transpose.int              |                  2 |
| 35 | aten.unsqueeze.default          |                  3 |
| 36 | aten.view.default               |                 65 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] size = [4, 64, 384]     | Unknown  |
|  1 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384] | Unknown  |
|  2 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] size = [16, 64, 192]    | Unknown  |
|  3 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192] | Unknown  |
|  4 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int] size = [1, 64, 768]          | Unknown  |
|  5 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [64, 64, 96]      | Unknown  |
|  6 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [96, 32, 64]          | Unknown  |
|  7 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [96, 64, 32]          | Unknown  |
|  8 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                  | Unknown  |
|  9 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [48, 32, 64]          | Unknown  |
| 10 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [48, 64, 32]          | Unknown  |
| 11 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                 | Unknown  |
| 12 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [192, 32, 64]         | Unknown  |
| 13 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [192, 64, 32]         | Unknown  |
| 14 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ? | Unknown  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768] | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [slice_7, slice_10, slice_13, slice_16],<br>int dim = -1 | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.605170185988092 | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[64, 3, 64, 64]> self = ?                                                       | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Unknown  |
### aten.exp.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[3, 1, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64] | Unknown  |
|  1 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]  | Unknown  |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64] | Unknown  |
|  3 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64] | Unknown  |
|  4 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]  | Unknown  |
|  5 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64] | Unknown  |
|  6 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64] | Unknown  |
|  7 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]  | Unknown  |
|  8 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64] | Unknown  |
|  9 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64] | Unknown  |
| 10 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]  | Unknown  |
| 11 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 64, 64, 384]> self = ? | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]] indices = [primals_219] | Unknown  |
|  1 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]] indices = [primals_231] | Unknown  |
|  2 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]] indices = [primals_211]  | Unknown  |
|  3 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]] indices = [primals_215]  | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 3, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0    | Unknown  |
|  1 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0 | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16            | Unknown  |
|  1 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 32, 32, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  2 | Tensor<[1, 64, 64, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05     | Unknown  |
|  3 | Tensor<[1, 8, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05   | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | Unknown  |
|  2 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  1 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Unknown  |
|  2 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]           | Unknown  |
|  3 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]     | Unknown  |
|  4 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Unknown  |
|  5 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
### aten.relu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Unknown  |
### aten.roll.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]  | Unknown  |
|  1 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  |
|  1 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  |
|  2 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 3, 64, 64]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  1 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  2 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  3 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
|  4 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  5 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2  | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[512, 2]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  |
|  1 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[16, 64]> self = ?,<br>int dim = 2    | Unknown  |
|  1 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[64, 64]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]     | Unknown  |
|  1 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]              | Unknown  |
|  2 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]              | Unknown  |
|  3 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]               | Unknown  |
|  4 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                | Unknown  |
|  5 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]           | Unknown  |
|  6 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                | Unknown  |
|  7 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]         | Unknown  |
|  8 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384] | Unknown  |
|  9 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]           | Unknown  |
| 10 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]    | Unknown  |
| 11 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]          | Unknown  |
| 12 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]          | Unknown  |
| 13 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]          | Unknown  |
| 14 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192] | Unknown  |
| 15 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]          | Unknown  |
| 16 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]          | Unknown  |
| 17 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]   | Unknown  |
| 18 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]      | Unknown  |
| 19 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]    | Unknown  |
| 20 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]          | Unknown  |
| 21 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]   | Unknown  |
| 22 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                | Unknown  |
| 23 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]               | Unknown  |
| 24 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]            | Unknown  |
| 25 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]            | Unknown  |
| 26 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]   | Unknown  |
| 27 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]          | Unknown  |
| 28 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]             | Unknown  |
| 29 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]          | Unknown  |
| 30 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                 | Unknown  |
| 31 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]          | Unknown  |
| 32 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]             | Unknown  |
| 33 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]      | Unknown  |
| 34 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]         | Unknown  |
| 35 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]         | Unknown  |
| 36 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]             | Unknown  |
| 37 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]             | Unknown  |
| 38 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]               | Unknown  |
| 39 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]           | Unknown  |
| 40 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]               | Unknown  |
| 41 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]          | Unknown  |
| 42 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]          | Unknown  |
| 43 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]             | Unknown  |
| 44 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]         | Unknown  |
| 45 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]           | Unknown  |
| 46 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                 | Unknown  |
| 47 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]          | Unknown  |
| 48 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]      | Unknown  |
| 49 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]               | Unknown  |
| 50 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]             | Unknown  |
| 51 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]          | Unknown  |
| 52 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                | Unknown  |
| 53 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]               | Unknown  |
| 54 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]          | Unknown  |
| 55 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]          | Unknown  |
| 56 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]              | Unknown  |
| 57 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]         | Unknown  |
| 58 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]            | Unknown  |
| 59 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]      | Unknown  |
| 60 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Unknown  |
| 61 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                 | Unknown  |
| 62 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]              | Unknown  |
| 63 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]          | Unknown  |
| 64 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]          | Unknown  |

