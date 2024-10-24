# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default          |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  2 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  3 | aten.add.Tensor                |                  5 |           5 |         0 |          0 | ✅          |     1   |
|  4 | aten.addmm.default             |                  5 |           5 |         0 |          0 | ✅          |     1   |
|  5 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  6 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  7 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  8 | aten.embedding.default         |                  3 |           0 |         0 |          0 | ✘           |     0   |
|  9 | aten.expand.default            |                  3 |           0 |         0 |          0 | ✘           |     0   |
| 10 | aten.mul.Tensor                |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 11 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 12 | aten.permute.default           |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 13 | aten.pow.Tensor_Scalar         |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 14 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 15 | aten.slice.Tensor              |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
| 16 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 17 | aten.tanh.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 18 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 19 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 20 | aten.view.default              |                 12 |          12 |         0 |          0 | ✅          |     1   |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 768] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2]> self = ?,<br>Tensor<[12, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[12, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[12, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[12, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[12, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?                                                           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 128]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 768]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                             | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                           | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 3072]> self = ?,<br>number exponent = 3.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 12                  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2, 768]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[3072, 768]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[768, 128]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12]> self = ?,<br>int dim = 1    | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [1, 12, 12, 64] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]       | Done     | N/A                 | N/A          | N/A               | N/A                |
