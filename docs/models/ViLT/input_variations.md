# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  1 | aten._to_copy.default          |                  5 |           0 |         0 |          0 | ✘           |               0    |
|  2 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  3 | aten.add.Tensor                |                  6 |           1 |         0 |          0 | 🚧          |               0.17 |
|  4 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |               0    |
|  5 | aten.arange.default            |                  4 |           0 |         0 |          0 | ✘           |               0    |
|  6 | aten.bmm.default               |                  2 |           0 |         0 |          0 | ✘           |               0    |
|  7 | aten.cat.default               |                  3 |           0 |         0 |          0 | ✘           |               0    |
|  8 | aten.clone.default             |                  4 |           1 |         0 |          0 | 🚧          |               0.25 |
|  9 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 10 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 11 | aten.embedding.default         |                  4 |           3 |         0 |          0 | 🚧          |               0.75 |
| 12 | aten.expand.default            |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 13 | aten.full_like.default         |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 14 | aten.gelu.default              |                  2 |           0 |         0 |          0 | ✘           |               0    |
| 15 | aten.max.default               |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 16 | aten.mul.Tensor                |                  4 |           0 |         0 |          0 | ✘           |               0    |
| 17 | aten.native_layer_norm.default |                  3 |           1 |         0 |          0 | 🚧          |               0.33 |
| 18 | aten.permute.default           |                  2 |           0 |         0 |          0 | ✘           |               0    |
| 19 | aten.rsub.Scalar               |                  2 |           0 |         0 |          0 | ✘           |               0    |
| 20 | aten.select.int                |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 21 | aten.slice.Tensor              |                 18 |           1 |         0 |          0 | 🚧          |               0.06 |
| 22 | aten.stack.default             |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 23 | aten.sum.dim_IntList           |                  2 |           0 |         0 |          0 | ✘           |               0    |
| 24 | aten.t.default                 |                  5 |           0 |         0 |          0 | ✘           |               0    |
| 25 | aten.tanh.default              |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 26 | aten.transpose.int             |                  3 |           0 |         0 |          0 | ✘           |               0    |
| 27 | aten.unsqueeze.default         |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 28 | aten.view.default              |                 17 |           0 |         0 |          0 | ✘           |               0    |
| 29 | aten.zeros_like.default        |                  1 |           0 |         0 |          0 | ✘           |               0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>Optional[int]<> dtype = torch.float32   | Unknown  |
|  1 | Tensor<[1, 1, 12, 16]> self = ?,<br>Optional[int]<> dtype = torch.int64     | Unknown  |
|  2 | Tensor<[1, 1, 384, 512]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
|  3 | Tensor<[12]> self = ?,<br>Optional[int]<> dtype = torch.int64               | Unknown  |
|  4 | Tensor<[16]> self = ?,<br>Optional[int]<> dtype = torch.int64               | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 384, 512]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([12, 1])', 'torch.Size([16])'] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor<[1, 1, 1, 201]> other = ? | Unknown  |
|  1 | Tensor<[1, 193, 768]> self = ?,<br>Tensor<[1, 193, 768]> other = ?      | Unknown  |
|  2 | Tensor<[1, 201, 768]> self = ?,<br>Tensor<[1, 201, 768]> other = ?      | Unknown  |
|  3 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?          | Done     |
|  4 | Tensor<[12]> self = ?,<br>Tensor<> other = 0.0                          | Unknown  |
|  5 | Tensor<[16]> self = ?,<br>Tensor<> other = 0.0                          | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1536]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1536]> mat2 = ?   | Unknown  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[201, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  |
|  2 | Tensor<[3129]> self = ?,<br>Tensor<[1, 1536]> mat1 = ?,<br>Tensor<[1536, 3129]> mat2 = ? | Unknown  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[201, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[201, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 12,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False                                           | Unknown  |
|  1 | number<> end = 12,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  2 | number<> end = 16,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False                                           | Unknown  |
|  3 | number<> end = 16,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 201, 201]> self = ?,<br>Tensor<[12, 201, 64]> mat2 = ? | Unknown  |
|  1 | Tensor<[12, 201, 64]> self = ?,<br>Tensor<[12, 64, 201]> mat2 = ?  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 768, 12, 16])']                                           | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 8, 768])', 'torch.Size([1, 193, 768])'],<br>int<> dim = 1 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 8])', 'torch.Size([1, 193])'],<br>int<> dim = 1           | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?                                                            | Unknown  |
|  1 | Tensor<[1, 201, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  2 | Tensor<[1, 201, 768]> self = ?                                                                | Unknown  |
|  3 | Tensor<[1, 8, 768]> self = ?                                                                  | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 384, 512]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int]<> stride = [32, 32],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor<> other = 8.0 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 193]> indices = ?   | Unknown  |
|  1 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?     | Done     |
|  2 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ? | Done     |
|  3 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?    | Done     |
### aten.expand.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int]<> size = [1, 1, -1, -1, -1] | Unknown  |
|  1 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int]<> size = [1, 12, 201, 201]  | Unknown  |
|  2 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int]<> size = [1, 12, 201, 64]    | Unknown  |
|  3 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int]<> size = [1, 12, 64, 201]    | Unknown  |
|  4 | Tensor<[1, 16]> self = ?,<br>List[int]<> size = [12, 16]                     | Unknown  |
|  5 | Tensor<[12, 1]> self = ?,<br>List[int]<> size = [12, 16]                     | Unknown  |
### aten.full_like.default
|    | ATen Input Variations                                                                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 193]> self = ?,<br>number<> fill_value = 1,<br>Optional[int]<> dtype = torch.int64,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 1536]> self = ?      | Unknown  |
|  1 | Tensor<[1, 201, 3072]> self = ? | Unknown  |
### aten.max.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1]> self = ?    | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[12]> self = ?,<br>Tensor<> other = 32.0                              | Unknown  |
|  2 | Tensor<[16]> self = ?,<br>Tensor<> other = 32.0                              | Unknown  |
|  3 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                               | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1536]> input = ?,<br>List[int]<> normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float<> eps = 1e-05  | Unknown  |
|  1 | Tensor<[1, 201, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12 | Unknown  |
|  2 | Tensor<[1, 8, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12   | Done     |
### aten.permute.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Unknown  |
|  1 | Tensor<[1, 201, 12, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  1 | Tensor<[1, 192]> self = ?,<br>number<> other = 1         | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
|  1 | Tensor<[1, 12]> self = ?,<br>int<> dim = 1,<br>int<> index = 0        | Unknown  |
|  2 | Tensor<[1, 16]> self = ?,<br>int<> dim = 1,<br>int<> index = 0        | Unknown  |
|  3 | Tensor<[1, 201, 768]> self = ?,<br>int<> dim = 1,<br>int<> index = 0  | Unknown  |
|  4 | Tensor<[192, 2]> self = ?,<br>int<> dim = 1,<br>int<> index = 0       | Unknown  |
|  5 | Tensor<[1]> self = ?,<br>int<> dim = 0,<br>int<> index = 0            | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807    | Unknown  |
|  1 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807 | Unknown  |
|  2 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807 | Unknown  |
|  3 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int<> dim = 4,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807 | Unknown  |
|  4 | Tensor<[1, 1, 12, 16]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807    | Unknown  |
|  5 | Tensor<[1, 1, 384, 512]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807  | Unknown  |
|  6 | Tensor<[1, 1, 384, 512]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807  | Unknown  |
|  7 | Tensor<[1, 12]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807           | Unknown  |
|  8 | Tensor<[1, 144, 768]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807     | Unknown  |
|  9 | Tensor<[1, 145, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807     | Unknown  |
| 10 | Tensor<[1, 145, 768]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807     | Unknown  |
| 11 | Tensor<[1, 16]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807           | Unknown  |
| 12 | Tensor<[1, 201, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807     | Unknown  |
| 13 | Tensor<[1, 201]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807          | Unknown  |
| 14 | Tensor<[1, 384, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807     | Unknown  |
| 15 | Tensor<[1, 40]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807           | Unknown  |
| 16 | Tensor<[1, 40]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 8                             | Done     |
| 17 | Tensor<[192, 2]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807          | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([12, 16])', 'torch.Size([12, 16])'],<br>int<> dim = -1 | Unknown  |
### aten.sum.dim_IntList
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]]<> dim = [1] | Unknown  |
|  1 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]]<> dim = [2] | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1536, 768]> self = ?  | Unknown  |
|  1 | Tensor<[3072, 768]> self = ?  | Unknown  |
|  2 | Tensor<[3129, 1536]> self = ? | Unknown  |
|  3 | Tensor<[768, 3072]> self = ?  | Unknown  |
|  4 | Tensor<[768, 768]> self = ?   | Unknown  |
### aten.tanh.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 201, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Unknown  |
|  1 | Tensor<[1, 144, 768]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2      | Unknown  |
|  2 | Tensor<[1, 768, 192]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2      | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 201]> self = ?,<br>int<> dim = 2    | Unknown  |
|  1 | Tensor<[1, 12, 16, 2]> self = ?,<br>int<> dim = 1 | Unknown  |
|  2 | Tensor<[1, 201]> self = ?,<br>int<> dim = 1       | Unknown  |
|  3 | Tensor<[1, 384, 512]> self = ?,<br>int<> dim = 1  | Unknown  |
|  4 | Tensor<[12, 16, 2]> self = ?,<br>int<> dim = 0    | Unknown  |
|  5 | Tensor<[12]> self = ?,<br>int<> dim = -1          | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int]<> size = [1, 192, 2]    | Unknown  |
|  1 | Tensor<[1, 1, 12, 16]> self = ?,<br>List[int]<> size = [1, 192]          | Unknown  |
|  2 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int]<> size = [12, 201, 201] | Unknown  |
|  3 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int]<> size = [12, 201, 64]   | Unknown  |
|  4 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int]<> size = [12, 64, 201]   | Unknown  |
|  5 | Tensor<[1, 201, 12, 64]> self = ?,<br>List[int]<> size = [1, 201, 768]   | Unknown  |
|  6 | Tensor<[1, 201, 3072]> self = ?,<br>List[int]<> size = [201, 3072]       | Unknown  |
|  7 | Tensor<[1, 201, 768]> self = ?,<br>List[int]<> size = [1, 201, 12, 64]   | Unknown  |
|  8 | Tensor<[1, 201, 768]> self = ?,<br>List[int]<> size = [201, 768]         | Unknown  |
|  9 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int]<> size = [1, 768, 192]   | Unknown  |
| 10 | Tensor<[1, 768, 144]> self = ?,<br>List[int]<> size = [1, 768, 12, 12]   | Unknown  |
| 11 | Tensor<[12, 201, 201]> self = ?,<br>List[int]<> size = [1, 12, 201, 201] | Unknown  |
| 12 | Tensor<[12, 201, 64]> self = ?,<br>List[int]<> size = [1, 12, 201, 64]   | Unknown  |
| 13 | Tensor<[12]> self = ?,<br>List[int]<> size = [-1, 1]                     | Unknown  |
| 14 | Tensor<[16]> self = ?,<br>List[int]<> size = [1, -1]                     | Unknown  |
| 15 | Tensor<[201, 3072]> self = ?,<br>List[int]<> size = [1, 201, 3072]       | Unknown  |
| 16 | Tensor<[201, 768]> self = ?,<br>List[int]<> size = [1, 201, 768]         | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8]> self = ?,<br>Optional[int]<> dtype = torch.int64,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |

