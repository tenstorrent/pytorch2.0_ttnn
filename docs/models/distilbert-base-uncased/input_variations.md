# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default                                    |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default                                       |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  4 | aten.clone.default                                       |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  5 | aten.embedding.default                                   |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  6 | aten.expand.default                                      |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.gelu.default                                        |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  8 | aten.masked_fill.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.native_layer_norm.default                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.slice.Tensor                                        |                  4 |           0 |         4 |          0 | ✅          |       1 |
| 11 | aten.sub.Tensor                                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.t.default                                           |                  3 |           0 |         3 |          0 | ✅          |       1 |
| 13 | aten.transpose.int                                       |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 14 | aten.unsqueeze.default                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 15 | aten.view.default                                        |                  6 |           5 |         1 |          0 | ✅          |       1 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 16, 64]> query = ?,<br>Tensor<[1, 12, 16, 64]> key = ?,<br>Tensor<[1, 12, 16, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(masked_fill_scalar)   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 16, 64]> query = ?,<br>Tensor<[1, 12, 16, 64]> key = ?,<br>Tensor<[1, 12, 16, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 16, 16]> attn_mask = masked_fill | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bool     | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Removed  | Done       | 0.999967 |      0 |
|  1 | Tensor<[768]> self = ?,<br>Tensor<[16, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Removed  | Done       | 0.999942 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Removed  | Done       | 0.999967 |      0 |
### aten.clone.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 768]> self = ? | Removed  | Done       |     1 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                           | Removed  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 1, 16, 16] | Done     | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 3072]> self = ? | Removed  | Done       | 0.999991 |      0 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 16]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | 0.991771 |      3 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                       | Removed  | Done       | 1.0   | 0      |
### aten.sub.Tensor
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 16, 16]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3072, 768]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[768, 3072]> self = ? | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[768, 768]> self = ?  | Removed  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16]> self = ?,<br>int dim = 1    | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]     | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]       | Done     | Done       |     1 |      0 |
|  4 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]     | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]       | Done     | Done       |     1 |      0 |

