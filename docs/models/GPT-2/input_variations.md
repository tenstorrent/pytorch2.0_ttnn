# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                 24 |          12 |        12 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default                                    |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  2 | aten._unsafe_view.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.add.Tensor                                          |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  4 | aten.addmm.default                                       |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  5 | aten.argmax.default                                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.clone.default                                       |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  7 | aten.copy.default                                        |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  8 | aten.embedding.default                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  9 | aten.eq.Scalar                                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.expand.default                                      |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 11 | aten.full.default                                        |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 12 | aten.gt.Tensor                                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.index.Tensor                                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.masked_fill.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 15 | aten.mm.default                                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.mul.Tensor                                          |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 17 | aten.native_layer_norm.default                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.ne.Scalar                                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 19 | aten.pow.Tensor_Scalar                                   |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 20 | aten.slice.Tensor                                        |                  6 |           0 |         6 |          0 | ✅          |       1 |
| 21 | aten.slice_scatter.default                               |                  3 |           0 |         3 |          0 | ✅          |       1 |
| 22 | aten.split.Tensor                                        |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 23 | aten.t.default                                           |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 24 | aten.tanh.default                                        |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 25 | aten.transpose.int                                       |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 26 | aten.triu.default                                        |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 27 | aten.unsqueeze.default                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 28 | aten.view.default                                        |                 11 |          11 |         0 |          0 | ✅          |       1 |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_17) | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_20) | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_23) | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_26) | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_29) | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_32) | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_35) | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_38) | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_41) | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_44) | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_47) | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor] attn_mask = Proxy(slice_tensor_50) | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_26 | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_32 | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_38 | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_44 | Removed  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_50 | Removed  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_56 | Removed  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_62 | Removed  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_68 | Removed  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_74 | Removed  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_80 | Removed  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_86 | Removed  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 12, 7, 64]> query = ?,<br>Tensor<[1, 12, 7, 64]> key = ?,<br>Tensor<[1, 12, 7, 64]> value = ?,<br>Optional[Tensor]<[1, 1, 7, 7]> attn_mask = slice_92 | Removed  | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Removed  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2] | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ? | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0             | Done     | Done       | 0.9999947873840198 | 0      |
|  2 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ? | Done     | Done       | 0.9999979984475087 | 0      |
|  3 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?   | Done     | Done       | 0.9999981547716872 | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2304]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[7, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999944 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999968 |      0 |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   |     1 |     -1 |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?                                                             | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 7, 768]> self = ?                                                              | Removed  | Done       | 1.0   | 0      |
### aten.copy.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> src = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Done     | Done       | 1.0   | 0      |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>number other = 0 | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [1, 1, -1, -1] | Removed  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Unknown    | N/A   | N/A    |
### aten.gt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | None     | Unknown    | N/A   | N/A    |
### aten.index.Tensor
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 2]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange_3, <[1]>] | None     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ? | Done     | Done       | 0.999972 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 7]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715           | Done     | Done       | 0.9999952996894373 | 0      |
|  2 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                | Done     | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654 | Done     | Done       | 0.9999972097789044 | 0      |
|  4 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?    | Done     | Done       | 0.9999961414026098 | 0      |
|  5 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> other = ?                | Done     | Unknown    | N/A                | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.997545 |      3 |
### aten.ne.Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 50256 | Done     | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 3072]> self = ?,<br>number exponent = 3.0 | Done     | Done       | 0.999996 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       | 1.0   | -1     |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
### aten.split.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2 | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 768]> self = ? | Removed  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 3072]> self = ? | Done     | Done       | 0.999993 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.triu.default
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[7, 7]> self = ?,<br>int diagonal = 1 | Removed  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2 | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 7]> self = ?,<br>int dim = 1    | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, -1]  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]    | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 7, 768]   | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]      | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [1, 7, -1, 64] | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [7, 768]       | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]             | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 7]> self = ?,<br>List[int] size = [1, -1]             | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]     | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]     | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[7, 768]> self = ?,<br>List[int] size = [1, 7, 768]       | Done     | Done       | 1.0   | 0      |

