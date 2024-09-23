# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten.add.Tensor                |                  2 |           2 |
|  2 | aten.addmm.default             |                  4 |           4 |
|  3 | aten.bmm.default               |                  2 |           2 |
|  4 | aten.cat.default               |                  2 |           1 |
|  5 | aten.clone.default             |                  4 |           4 |
|  6 | aten.convolution.default       |                  1 |           1 |
|  7 | aten.div.Tensor                |                  1 |           1 |
|  8 | aten.expand.default            |                  4 |           0 |
|  9 | aten.gelu.default              |                  1 |           1 |
| 10 | aten.index.Tensor              |                 25 |          24 |
| 11 | aten.mean.dim                  |                  1 |           1 |
| 12 | aten.mm.default                |                  1 |           1 |
| 13 | aten.mul.Tensor                |                  1 |           1 |
| 14 | aten.native_layer_norm.default |                  2 |           2 |
| 15 | aten.permute.default           |                  3 |           3 |
| 16 | aten.slice.Tensor              |                  3 |           3 |
| 17 | aten.t.default                 |                  4 |           4 |
| 18 | aten.transpose.int             |                  2 |           2 |
| 19 | aten.unsqueeze.default         |                  1 |           1 |
| 20 | aten.view.default              |                 14 |          14 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Done     |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?       | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?   | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[197, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ? | Done     |
|  1 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?  | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 1, 1024])', 'torch.Size([1, 196, 1024])'],<br>int<> dim = 1 | Unknown  |
|  1 | List[Tensor]<> tensors = [Proxy(expand_default), Proxy(transpose_int)],<br>int<> dim = 1              | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?                                                            | Done     |
|  1 | Tensor<[1, 197, 1024]> self = ?                                                               | Done     |
|  2 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [16, 16],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<> other = 8.0 | Done     |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int]<> size = [1, -1, -1]            | Unknown  |
|  1 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int]<> size = [1, 16, 197, 197] | Unknown  |
|  2 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int]<> size = [1, 16, 197, 64]   | Unknown  |
|  3 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int]<> size = [1, 16, 64, 197]   | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 197, 4096]> self = ? | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([38809])']   | Unknown  |
|  1 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_109)] | Done     |
|  2 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_13)]  | Done     |
|  3 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_133)] | Done     |
|  4 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_157)] | Done     |
|  5 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_181)] | Done     |
|  6 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_205)] | Done     |
|  7 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_229)] | Done     |
|  8 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_253)] | Done     |
|  9 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_277)] | Done     |
| 10 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_301)] | Done     |
| 11 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_325)] | Done     |
| 12 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_349)] | Done     |
| 13 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_37)]  | Done     |
| 14 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_373)] | Done     |
| 15 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_397)] | Done     |
| 16 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_421)] | Done     |
| 17 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_445)] | Done     |
| 18 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_469)] | Done     |
| 19 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_493)] | Done     |
| 20 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_517)] | Done     |
| 21 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_541)] | Done     |
| 22 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_565)] | Done     |
| 23 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_61)]  | Done     |
| 24 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [Proxy(view_default_85)]  | Done     |
### aten.mean.dim
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]]<> dim = [1] | Done     |
### aten.mm.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ? | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-12      | Done     |
|  1 | Tensor<[1, 197, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  2 | Tensor<[197, 197, 16]> self = ?,<br>List[int]<> dims = [2, 0, 1]      | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Done     |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Done     |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1 | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     |
|  1 | Tensor<[1024, 1024]> self = ? | Done     |
|  2 | Tensor<[1024, 4096]> self = ? | Done     |
|  3 | Tensor<[4096, 1024]> self = ? | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 196]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
|  1 | Tensor<[1, 16, 197, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>int<> dim = 0 | Done     |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int]<> size = [1, 1024, 196] | Done     |
|  1 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int]<> size = [16, 197, 197] | Done     |
|  2 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int]<> size = [16, 197, 64]   | Done     |
|  3 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int]<> size = [16, 64, 197]   | Done     |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>List[int]<> size = [1, 197, 16, 64]  | Done     |
|  5 | Tensor<[1, 197, 1024]> self = ?,<br>List[int]<> size = [197, 1024]       | Done     |
|  6 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int]<> size = [1, 197, 1024]  | Done     |
|  7 | Tensor<[1, 197, 4096]> self = ?,<br>List[int]<> size = [197, 4096]       | Done     |
|  8 | Tensor<[16, 197, 197]> self = ?,<br>List[int]<> size = [1, 16, 197, 197] | Done     |
|  9 | Tensor<[16, 197, 64]> self = ?,<br>List[int]<> size = [1, 16, 197, 64]   | Done     |
| 10 | Tensor<[197, 1024]> self = ?,<br>List[int]<> size = [1, 197, 1024]       | Done     |
| 11 | Tensor<[197, 197]> self = ?,<br>List[int]<> size = [-1]                  | Done     |
| 12 | Tensor<[197, 4096]> self = ?,<br>List[int]<> size = [1, 197, 4096]       | Done     |
| 13 | Tensor<[38809, 16]> self = ?,<br>List[int]<> size = [197, 197, -1]       | Done     |

