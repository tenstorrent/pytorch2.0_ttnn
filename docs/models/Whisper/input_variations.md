# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                 18 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.add.Tensor                                  |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.addmm.default                               |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.argmax.default                              |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.cat.default                                 |                 26 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.clone.default                               |                  8 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.convolution.default                         |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.embedding.default                           |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.gelu.default                                |                  5 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.index_put.default                           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.mm.default                                  |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.native_layer_norm.default                   |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.ones_like.default                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.permute.default                             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.select.int                                  |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.select_scatter.default                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.slice.Tensor                                |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.slice_scatter.default                       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.t.default                                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.transpose.int                               |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.view.default                                |                 26 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?                                                     | Unknown  | Fallback   | N/A   | 0      |
|  1 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                               | Unknown  | Fallback   | N/A   | 0      |
|  2 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?                                                     | Unknown  | Fallback   | N/A   | 0      |
|  3 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s10 + 1, 64]> key = ?,<br>Tensor<[1, 12, s11 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s12 + 1, 64]> key = ?,<br>Tensor<[1, 12, s13 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s14 + 1, 64]> key = ?,<br>Tensor<[1, 12, s15 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s16 + 1, 64]> key = ?,<br>Tensor<[1, 12, s17 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s18 + 1, 64]> key = ?,<br>Tensor<[1, 12, s19 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s2 + 1, 64]> key = ?,<br>Tensor<[1, 12, s3 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s20 + 1, 64]> key = ?,<br>Tensor<[1, 12, s21 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s22 + 1, 64]> key = ?,<br>Tensor<[1, 12, s23 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s24 + 1, 64]> key = ?,<br>Tensor<[1, 12, s25 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s4 + 1, 64]> key = ?,<br>Tensor<[1, 12, s5 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s6 + 1, 64]> key = ?,<br>Tensor<[1, 12, s7 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s8 + 1, 64]> key = ?,<br>Tensor<[1, 12, s9 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                            | Unknown  | Fallback   | N/A   | 0      |
| 16 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                               | Unknown  | Fallback   | N/A   | 0      |
| 17 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>float dropout_p = 0.0,<br>bool is_causal = True | Unknown  | Fallback   | N/A   | 0      |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?       | Unknown  | Done       | 0.999999 |      0 |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?          | Unknown  | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?    | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?          | Unknown  | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | 0.9999620604815471 | 0      |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[4, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[1500, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[768]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.9999620695032664 | 0      |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[4, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[768]> self = ?,<br>Tensor<[4, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
### aten.argmax.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1 | Unknown  | Fallback   |     1 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 12, 4, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                        | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 12, s11, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 12, s12, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[1, 12, s13, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[1, 12, s14, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1, 12, s15, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[1, 12, s16, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[1, 12, s17, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
|  9 | List[Tensor] tensors = [<[1, 12, s18, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 10 | List[Tensor] tensors = [<[1, 12, s19, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 11 | List[Tensor] tensors = [<[1, 12, s2, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 12 | List[Tensor] tensors = [<[1, 12, s20, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 13 | List[Tensor] tensors = [<[1, 12, s21, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 14 | List[Tensor] tensors = [<[1, 12, s22, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 15 | List[Tensor] tensors = [<[1, 12, s23, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 16 | List[Tensor] tensors = [<[1, 12, s24, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 17 | List[Tensor] tensors = [<[1, 12, s25, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                      | Unknown  | Unknown    | N/A   | N/A    |
| 18 | List[Tensor] tensors = [<[1, 12, s3, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 19 | List[Tensor] tensors = [<[1, 12, s4, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 20 | List[Tensor] tensors = [<[1, 12, s5, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 21 | List[Tensor] tensors = [<[1, 12, s6, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 22 | List[Tensor] tensors = [<[1, 12, s7, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 23 | List[Tensor] tensors = [<[1, 12, s8, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 24 | List[Tensor] tensors = [<[1, 12, s9, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2                       | Unknown  | Unknown    | N/A   | N/A    |
| 25 | List[Tensor] tensors = [_folded_mul, _folded_mul_1, _folded_mul_2, _folded_mul_3],<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                                | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 768]> self = ?                                                                 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 1500, 3072]> self = ?                                                             | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 1500, 768]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 4, 3072]> self = ?                                                                | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 4, 768]> self = ?                                                                 | Unknown  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768, 3000]> input = ?,<br>Tensor<[768, 768, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [2],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[1, 80, 3000]> input = ?,<br>Tensor<[768, 80, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Done       | 0.999966 |      1 |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[51865, 768]> weight = ?,<br>Tensor indices = ?,<br>int padding_idx = 50257         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0   | 0      |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?    | Unknown  | Done       | 0.999992 |      0 |
|  1 | Tensor<[1, 1500, 3072]> self = ? | Unknown  | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 4, 3072]> self = ?    | Unknown  | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 768, 1500]> self = ?  | Unknown  | Done       | 0.999991 |      0 |
|  4 | Tensor<[1, 768, 3000]> self = ?  | Unknown  | Done       | 0.999991 |      0 |
### aten.index_put.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[51865]>],<br>Tensor values = ?                 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, _folded_lift_fresh_copy_1],<br>Tensor values = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, _folded_lift_fresh_copy_3],<br>Tensor values = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[51865]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_lift_fresh_copy_1],<br>Tensor values = ?          | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?  | Unknown  | Done       | 0.999969 |      0 |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.999966 |      0 |
|  2 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  | Done       | 0.999963 |      0 |
|  3 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?  | Unknown  | Done       | 0.999968 |      0 |
|  4 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.999969 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  | Done       | N/A   |      1 |
|  1 | Tensor<[1, 1500, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      1 |
|  2 | Tensor<[1, 4, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  | Done       | N/A   |      1 |
### aten.ones_like.default
|    | ATen Input Variations                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[51865]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1] | Unknown  | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 51865]> self = ?,<br>int dim = 0,<br>int index = 0     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | Unknown  | Done       | 1.0   | 0      |
### aten.select_scatter.default
|    | ATen Input Variations                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>Tensor<[1, 51865]> src = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1                      | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 4                      | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 4,<br>Optional[int] end = 5                      | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ?          | Unknown  | Failed     | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>Tensor<[1, 1, 51865]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 51865]> self = ?,<br>Tensor<[1, 51865]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3072, 768]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[51865, 768]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[768, 3072]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[768, 768]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 1500, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 12, 4, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 4, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]       | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 51865]> self = ?,<br>List[int] size = [1, 51865]         | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]       | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]             | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1500, 12, 64]> self = ?,<br>List[int] size = [1, 1500, 768] | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]     | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]   | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, 1500, 12, 64] | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]       | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                   | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]           | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 4, 12, 64]> self = ?,<br>List[int] size = [1, 4, 768]       | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]           | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, 4, 12, 64]       | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]             | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                   | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]         | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]             | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]     | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]       | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]           | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]         | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]             | Unknown  | Done       | 1.0   | 0      |

