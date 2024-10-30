# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                 18 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                                  |                  6 |           4 |         0 |          0 | 🚧          |    0.67 |
|  2 | aten.addmm.default                               |                  9 |           6 |         0 |          0 | 🚧          |    0.67 |
|  3 | aten.argmax.default                              |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.cat.default                                 |                 26 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.clone.default                               |                  8 |           5 |         0 |          0 | 🚧          |    0.62 |
|  6 | aten.convolution.default                         |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.embedding.default                           |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.gelu.default                                |                  5 |           4 |         0 |          0 | 🚧          |    0.8  |
|  9 | aten.mm.default                                  |                  5 |           3 |         0 |          0 | 🚧          |    0.6  |
| 10 | aten.mul.Tensor                                  |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
| 11 | aten.native_layer_norm.default                   |                  3 |           2 |         0 |          0 | 🚧          |    0.67 |
| 12 | aten.ones.default                                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.permute.default                             |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.select.int                                  |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.slice.Tensor                                |                  7 |           1 |         0 |          0 | 🚧          |    0.14 |
| 16 | aten.t.default                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 17 | aten.transpose.int                               |                  6 |           4 |         0 |          0 | 🚧          |    0.67 |
| 18 | aten.view.default                                |                 25 |          15 |         0 |          0 | 🚧          |    0.6  |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?                                                     | None     | Fallback   | True  |
|  1 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                               | None     | Fallback   | True  |
|  2 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?                                                     | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s10 + 1, 64]> key = ?,<br>Tensor<[1, 12, s11 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s12 + 1, 64]> key = ?,<br>Tensor<[1, 12, s13 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s14 + 1, 64]> key = ?,<br>Tensor<[1, 12, s15 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s16 + 1, 64]> key = ?,<br>Tensor<[1, 12, s17 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s18 + 1, 64]> key = ?,<br>Tensor<[1, 12, s19 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s2 + 1, 64]> key = ?,<br>Tensor<[1, 12, s3 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s20 + 1, 64]> key = ?,<br>Tensor<[1, 12, s21 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s22 + 1, 64]> key = ?,<br>Tensor<[1, 12, s23 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s24 + 1, 64]> key = ?,<br>Tensor<[1, 12, s25 + 1, 64]> value = ?                                         | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s4 + 1, 64]> key = ?,<br>Tensor<[1, 12, s5 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s6 + 1, 64]> key = ?,<br>Tensor<[1, 12, s7 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s8 + 1, 64]> key = ?,<br>Tensor<[1, 12, s9 + 1, 64]> value = ?                                           | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                            | None     | Fallback   | False |
| 16 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                               | Unknown  | Fallback   | False |
| 17 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>float dropout_p = 0.0,<br>bool is_causal = True | Unknown  | Fallback   | False |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?       | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?          | Done     | Done       | True  |
|  2 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?    | Done     | Done       | True  |
|  4 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?       | Unknown  | Done       | True  |
|  5 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?          | Unknown  | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Done     | Done       | True  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[4, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Unknown  | Done       | True  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Done     | Done       | True  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[1500, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  6 | Tensor<[768]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[4, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Unknown  | Done       | True  |
|  8 | Tensor<[768]> self = ?,<br>Tensor<[4, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Done       | True  |
### aten.argmax.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   | True  |
### aten.cat.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 12, 4, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2      | Unknown  | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  2 | List[Tensor] tensors = [<[1, 12, s11, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  3 | List[Tensor] tensors = [<[1, 12, s12, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  4 | List[Tensor] tensors = [<[1, 12, s13, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  5 | List[Tensor] tensors = [<[1, 12, s14, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  6 | List[Tensor] tensors = [<[1, 12, s15, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  7 | List[Tensor] tensors = [<[1, 12, s16, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  8 | List[Tensor] tensors = [<[1, 12, s17, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
|  9 | List[Tensor] tensors = [<[1, 12, s18, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 10 | List[Tensor] tensors = [<[1, 12, s19, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 11 | List[Tensor] tensors = [<[1, 12, s2, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 12 | List[Tensor] tensors = [<[1, 12, s20, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 13 | List[Tensor] tensors = [<[1, 12, s21, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 14 | List[Tensor] tensors = [<[1, 12, s22, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 15 | List[Tensor] tensors = [<[1, 12, s23, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 16 | List[Tensor] tensors = [<[1, 12, s24, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 17 | List[Tensor] tensors = [<[1, 12, s25, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2    | Unknown  | Unknown    | N/A   |
| 18 | List[Tensor] tensors = [<[1, 12, s3, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 19 | List[Tensor] tensors = [<[1, 12, s4, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 20 | List[Tensor] tensors = [<[1, 12, s5, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 21 | List[Tensor] tensors = [<[1, 12, s6, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 22 | List[Tensor] tensors = [<[1, 12, s7, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 23 | List[Tensor] tensors = [<[1, 12, s8, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 24 | List[Tensor] tensors = [<[1, 12, s9, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   |
| 25 | List[Tensor] tensors = [<[1, 1]>, <[1, 1]>, <[1, 1]>, <[1, 1]>],<br>int dim = -1 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                                | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 768]> self = ?                                                                 | Done     | Done       | True  |
|  2 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  3 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1500, 3072]> self = ?                                                             | Done     | Done       | True  |
|  5 | Tensor<[1, 1500, 768]> self = ?                                                              | Done     | Done       | True  |
|  6 | Tensor<[1, 4, 3072]> self = ?                                                                | Unknown  | Done       | True  |
|  7 | Tensor<[1, 4, 768]> self = ?                                                                 | Unknown  | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 3000]> input = ?,<br>Tensor<[768, 768, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [2],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | None     | Fallback   | True  |
|  1 | Tensor<[1, 80, 3000]> input = ?,<br>Tensor<[768, 80, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | None     | Fallback   | True  |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | None     | Fallback   | True  |
|  1 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?    | Done     | Done       | True  |
|  1 | Tensor<[1, 1500, 3072]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 4, 3072]> self = ?    | Unknown  | Done       | True  |
|  3 | Tensor<[1, 768, 1500]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[1, 768, 3000]> self = ?  | Done     | Done       | True  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?  | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     | Unknown    | N/A   |
|  2 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Done     | Unknown    | N/A   |
|  3 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?  | Unknown  | Done       | True  |
|  4 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258 | None     | Fallback   | True  |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50259 | Done     | Done       | True  |
|  2 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50359 | Done     | Done       | True  |
|  3 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50363 | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | N/A   |
|  1 | Tensor<[1, 1500, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  2 | Tensor<[1, 4, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  | Done       | N/A   |
### aten.ones.default
|    | ATen Input Variations                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.permute.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1] | Done     | Done       | True  |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1 | None     | Fallback   | True  |
|  1 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | Unknown  | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  3 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1                      | Done     | Done       | True  |
|  4 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 4                      | Unknown  | Done       | True  |
|  5 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 4,<br>Optional[int] end = 5                      | Unknown  | Done       | True  |
|  6 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ?          | Unknown  | Failed     | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072, 768]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[51865, 768]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[768, 3072]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[768, 768]> self = ?   | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  2 | Tensor<[1, 12, 1500, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  3 | Tensor<[1, 12, 4, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  5 | Tensor<[1, 4, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]       | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]           | Done     | Done       | True  |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Done     | Done       | True  |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]       | Done     | Done       | True  |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]             | Done     | Done       | True  |
|  5 | Tensor<[1, 1500, 12, 64]> self = ?,<br>List[int] size = [1, 1500, 768] | Done     | Done       | True  |
|  6 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]     | Done     | Done       | True  |
|  7 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]   | Done     | Done       | True  |
|  8 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, 1500, 12, 64] | Done     | Done       | True  |
|  9 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]       | Done     | Done       | True  |
| 10 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                   | None     | Fallback   | True  |
| 11 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]           | Done     | Done       | True  |
| 12 | Tensor<[1, 4, 12, 64]> self = ?,<br>List[int] size = [1, 4, 768]       | Unknown  | Done       | True  |
| 13 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]           | Unknown  | Done       | True  |
| 14 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Unknown  | Done       | True  |
| 15 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, 4, 12, 64]       | Unknown  | Done       | True  |
| 16 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]             | Unknown  | Done       | True  |
| 17 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                   | Unknown  | Done       | True  |
| 18 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]         | Done     | Done       | True  |
| 19 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]             | Done     | Done       | True  |
| 20 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]     | Done     | Done       | True  |
| 21 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]       | Done     | Done       | True  |
| 22 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]           | Unknown  | Done       | True  |
| 23 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]         | Unknown  | Done       | True  |
| 24 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]             | Unknown  | Done       | True  |

