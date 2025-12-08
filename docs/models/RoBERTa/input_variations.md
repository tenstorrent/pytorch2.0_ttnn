# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default                                    |                  5 |           2 |         3 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                                          |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default                                       |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  4 | aten.clone.default                                       |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  5 | aten.cumsum.default                                      |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.embedding.default                                   |                  3 |           2 |         1 |          0 | ✅          |       1 |
|  7 | aten.expand.default                                      |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  8 | aten.gelu.default                                        |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  9 | aten.masked_fill.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.mul.Tensor                                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.native_layer_norm.default                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.ne.Scalar                                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.permute.default                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.slice.Tensor                                        |                  4 |           0 |         4 |          0 | ✅          |       1 |
| 15 | aten.sub.Tensor                                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.t.default                                           |                  4 |           0 |         4 |          0 | ✅          |       1 |
| 17 | aten.transpose.int                                       |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.unsqueeze.default                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 19 | aten.view.default                                        |                  7 |           6 |         1 |          0 | ✅          |       1 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 10, 64]> query = ?,<br>Tensor<[1, 12, 10, 64]> key = ?,<br>Tensor<[1, 12, 10, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(masked_fill_scalar)   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 10, 64]> query = ?,<br>Tensor<[1, 12, 10, 64]> key = ?,<br>Tensor<[1, 12, 10, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 10, 10]> attn_mask = masked_fill | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 10, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 10, 10]> self = ?,<br>Optional[int] dtype = torch.bool                                                                      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32                                                                            | Removed  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Removed  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                            | Removed  | Fallback   | 1.0   | -1     |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                    | Done     | Done       | 1        |      0 |
|  2 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.999999 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[250002]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 250002]> mat2 = ? | Removed  | Done       | 0.999967 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Removed  | Done       | 0.999967 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[10, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Removed  | Done       | 0.999944 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Removed  | Done       | 0.999967 |      0 |
### aten.clone.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 768]> self = ? | Removed  | Done       |     1 |      0 |
### aten.cumsum.default
|    | ATen Input Variations                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1 | Done     | Done       | 0.999977 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                              | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1    | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>List[int] size = [1, 1, 10, 10] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]              | Removed  | Done       | 1.0   | -1     |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10, 3072]> self = ? | Removed  | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 10, 768]> self = ?  | Removed  | Done       | 0.999991 |      0 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 10, 10]> self = ?,<br>Tensor<[1, 1, 10, 10]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ? | Done     | Done       |     1 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |     PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[1, 10, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.99975 |      3 |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>number other = 1 | Done     | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 514]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 10                       | Removed  | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 10, 10]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[250002, 768]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[3072, 768]> self = ?   | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[768, 3072]> self = ?   | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[768, 768]> self = ?    | Removed  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, 10, 768] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]     | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, 10, 12, 64] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]       | Done     | Done       |     1 |      0 |
|  4 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002] | Done     | Done       |     1 |      0 |
|  5 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]     | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]       | Done     | Done       |     1 |      0 |

