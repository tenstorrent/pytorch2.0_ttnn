# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._to_copy.default          |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten.add.Tensor                |                  6 |           3 |         0 |          0 | 🚧          |    0.5  |
|  4 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.arange.default            |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.bmm.default               |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.cat.default               |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.clone.default             |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
|  9 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.embedding.default         |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.expand.default            |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.full_like.default         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.gelu.default              |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.max.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.mul.Tensor                |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 17 | aten.native_layer_norm.default |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 18 | aten.permute.default           |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.rsub.Scalar               |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.select.int                |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.slice.Tensor              |                 18 |           2 |         0 |          0 | 🚧          |    0.11 |
| 22 | aten.stack.default             |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.sum.dim_IntList           |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.t.default                 |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.tanh.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.transpose.int             |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 27 | aten.unsqueeze.default         |                  6 |           1 |         0 |          0 | 🚧          |    0.17 |
| 28 | aten.view.default              |                 17 |           1 |         0 |          0 | 🚧          |    0.06 |
| 29 | aten.zeros_like.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 12, 16]> self = ?,<br>Optional[int] dtype = torch.int64     | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 384, 512]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[12]> self = ?,<br>Optional[int] dtype = torch.int64               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[16]> self = ?,<br>Optional[int] dtype = torch.int64               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 384, 512]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[12, 1]>, <[16]>] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor<[1, 1, 1, 201]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 193, 768]> self = ?,<br>Tensor<[1, 193, 768]> other = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 201, 768]> self = ?,<br>Tensor<[1, 201, 768]> other = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                            | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1536]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1536]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[201, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[3129]> self = ?,<br>Tensor<[1, 1536]> mat1 = ?,<br>Tensor<[1536, 3129]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[201, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[201, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number end = 12,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | number end = 12,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | number end = 16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | number end = 16,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[12, 201, 201]> self = ?,<br>Tensor<[12, 201, 64]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[12, 201, 64]> self = ?,<br>Tensor<[12, 64, 201]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 768, 12, 16]>]                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[1, 8, 768]>, <[1, 193, 768]>],<br>int dim = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[Tensor] tensors = [<[1, 8]>, <[1, 193]>],<br>int dim = 1           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?                                                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 201, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 201, 768]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 768]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 3, 384, 512]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor other = 8.0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 193]> indices = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?     | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?    | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int] size = [1, 1, -1, -1, -1] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int] size = [1, 12, 201, 201]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int] size = [1, 12, 201, 64]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int] size = [1, 12, 64, 201]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 16]> self = ?,<br>List[int] size = [12, 16]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.full_like.default
|    | ATen Input Variations                                                                                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 193]> self = ?,<br>number fill_value = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1536]> self = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 201, 3072]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.max.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1]> self = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[12]> self = ?,<br>Tensor other = 32.0                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[16]> self = ?,<br>Tensor other = 32.0                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 201, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 201, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>number other = 1.0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 192]> self = ?,<br>number other = 1         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0        | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0        | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 201, 768]> self = ?,<br>int dim = 1,<br>int index = 0  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[192, 2]> self = ?,<br>int dim = 1,<br>int index = 0       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 201]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 4,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 12]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 144, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 201, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 201]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[192, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.stack.default
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[12, 16]>, <[12, 16]>],<br>int dim = -1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sum.dim_IntList
|    | ATen Input Variations                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [1] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [2] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1536, 768]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[3072, 768]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[3129, 1536]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768, 3072]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768, 768]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.tanh.default
|    | ATen Input Variations     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 768]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 201, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 201]> self = ?,<br>int dim = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 16, 2]> self = ?,<br>int dim = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 201]> self = ?,<br>int dim = 1       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[12, 16, 2]> self = ?,<br>int dim = 0    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[12]> self = ?,<br>int dim = -1          | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int] size = [1, 192, 2]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 12, 16]> self = ?,<br>List[int] size = [1, 192]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int] size = [12, 201, 201] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int] size = [12, 201, 64]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int] size = [12, 64, 201]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 201, 12, 64]> self = ?,<br>List[int] size = [1, 201, 768]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 201, 3072]> self = ?,<br>List[int] size = [201, 3072]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 201, 768]> self = ?,<br>List[int] size = [1, 201, 12, 64]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 201, 768]> self = ?,<br>List[int] size = [201, 768]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[12, 201, 201]> self = ?,<br>List[int] size = [1, 12, 201, 201] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[12, 201, 64]> self = ?,<br>List[int] size = [1, 12, 201, 64]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[16]> self = ?,<br>List[int] size = [1, -1]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[201, 3072]> self = ?,<br>List[int] size = [1, 201, 3072]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[201, 768]> self = ?,<br>List[int] size = [1, 201, 768]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.zeros_like.default
|    | ATen Input Variations                                                                                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 8]> self = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |

