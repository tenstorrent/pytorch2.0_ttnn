# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default                                    |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                                          |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default                                       |                  6 |           0 |         6 |          0 | ✅          |       1 |
|  4 | aten.clone.default                                       |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  5 | aten.embedding.default                                   |                  3 |           2 |         1 |          0 | ✅          |       1 |
|  6 | aten.expand.default                                      |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.masked_fill.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.mul.Tensor                                          |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  9 | aten.native_layer_norm.default                           |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 10 | aten.permute.default                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.pow.Tensor_Scalar                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 12 | aten.slice.Tensor                                        |                  4 |           0 |         4 |          0 | ✅          |       1 |
| 13 | aten.sub.Tensor                                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.t.default                                           |                  6 |           0 |         6 |          0 | ✅          |       1 |
| 15 | aten.tanh.default                                        |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 16 | aten.transpose.int                                       |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 17 | aten.unsqueeze.default                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 18 | aten.view.default                                        |                  9 |           9 |         0 |          0 | ✅          |       1 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 9, 64]> query = ?,<br>Tensor<[1, 12, 9, 64]> key = ?,<br>Tensor<[1, 12, 9, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(masked_fill_scalar) | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 9, 64]> query = ?,<br>Tensor<[1, 12, 9, 64]> key = ?,<br>Tensor<[1, 12, 9, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 9, 9]> attn_mask = masked_fill | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 9, 9]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 9, 9]> self = ?,<br>Optional[int] dtype = torch.bool     | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0              | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0             | Done     | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ? | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[128]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 128]> mat2 = ?     | Removed  | Done       | 0.999968 |      0 |
|  1 | Tensor<[30000]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 30000]> mat2 = ? | Removed  | Done       | 0.999979 |      0 |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?   | Removed  | Done       | 0.999967 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?     | Removed  | Done       | 0.999978 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[9, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?   | Removed  | Done       | 0.999939 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Removed  | Done       | 0.999966 |      0 |
### aten.clone.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 128]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 9, 768]> self = ? | Removed  | Done       |     1 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                             | Done     | Done       |     1 |      0 |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                           | Removed  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>List[int] size = [1, 1, 9, 9] | Done     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 9, 9]> self = ?,<br>Tensor<[1, 1, 9, 9]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715            | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                 | Done     | Done       | 1        |      0 |
|  2 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654  | Done     | Done       | 0.999997 |      0 |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?      | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715           | Done     | Done       | 0.999995 |      0 |
|  5 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                | Done     | Done       | 1        |      0 |
|  6 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654 | Done     | Done       | 0.999997 |      0 |
|  7 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?    | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 9, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | 0.999602 |      3 |
|  1 | Tensor<[1, 9, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | 0.997964 |      3 |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 9, 128]> self = ?,<br>number exponent = 3.0  | Done     | Done       | 0.999997 |      0 |
|  1 | Tensor<[1, 9, 3072]> self = ?,<br>number exponent = 3.0 | Done     | Done       | 0.999996 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9                       | Removed  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 9]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 9, 9]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[128, 768]> self = ?   | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[30000, 128]> self = ? | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[3072, 768]> self = ?  | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[768, 128]> self = ?   | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[768, 3072]> self = ?  | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[768, 768]> self = ?   | Removed  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 9, 128]> self = ?  | Done     | Done       | 0.999993 |      0 |
|  1 | Tensor<[1, 9, 3072]> self = ? | Done     | Done       | 0.999993 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 9]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] size = [1, 9, 768] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]       | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]     | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [1, 9, 12, 64] | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]       | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]       | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]   | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]     | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]       | Done     | Done       | 1.0   | 0      |

