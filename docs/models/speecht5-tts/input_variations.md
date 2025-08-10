# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._softmax.default                             |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._to_copy.default                             |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten._unsafe_view.default                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.add.Tensor                                   |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.addmm.default                                |                 14 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.bernoulli.p                                  |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.bmm.default                                  |                 21 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.cat.default                                  |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.clamp_min.default                            |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.clone.default                                |                 19 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.convolution.default                          |                 45 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.div.Tensor                                   |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.embedding.default                            |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.eq.Scalar                                    |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.expand.default                               |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.ge.Scalar                                    |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.gelu.default                                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.index_put.default                            |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.leaky_relu.default                           |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.linalg_vector_norm.default                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.lt.Scalar                                    |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.masked_fill.Scalar                           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.mul.Tensor                                   |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.native_layer_norm.default                    |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.relu.default                                 |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.repeat.default                               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.rsub.Scalar                                  |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.scalar_tensor.default                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.select.int                                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.slice.Tensor                                 |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.squeeze.dim                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.sub.Tensor                                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.sym_size.int                                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.t.default                                    |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.tanh.default                                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.transpose.int                                |                 20 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.unsqueeze.default                            |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 38 | aten.view.default                                 |                 43 |           0 |         0 |          0 | ✘           |       0 |
| 39 | aten.where.self                                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 96]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 80, 96]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  | Unknown    | N/A   | N/A    |
### aten._softmax.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[12, 1, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[12, 1, s2 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[12, 1, s4 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[12, 1, s6 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[12, 1, s8 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996470573032951 | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bool      | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.bool     | Unknown  | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int] size = [1, 24, 768] | Unknown  | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 12, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ? | Unknown  | Done       | 0.9999981830921401 | 0      |
|  3 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor<[1, 128, 1536]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?      | Unknown  | Done       | 0.9999980384356956 | 0      |
|  5 | Tensor<[1, 256, 384]> self = ?,<br>Tensor<[1, 256, 384]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor<[1, 32, 24576]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor<[1, 64, 6144]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 96, 80]> self = ?,<br>Tensor<[1, 96, 80]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, s0, 768]> self = ?,<br>Tensor<[1, s0, 768]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?      | Unknown  | Done       | 0.9999979574133198 | 0      |
| 11 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                      | Unknown  | Done       | 0.974454708272439  | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[256]> self = ?,<br>Tensor<[1, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[256]> self = ?,<br>Tensor<[1, 80]> mat1 = ?,<br>Tensor<[80, 256]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[s0, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[s0, 80]> mat1 = ?,<br>Tensor<[80, 256]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[3072]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | 0.999967350838087  | 0      |
|  6 | Tensor<[768]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[1, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[768]> self = ?,<br>Tensor<[24, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | 0.9999441684650849 | 0      |
| 11 | Tensor<[768]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.9999672199057917 | 0      |
| 12 | Tensor<[768]> self = ?,<br>Tensor<[s0, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[s0, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
### aten.bernoulli.p
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256]> self = ?,<br>float p = 0.5  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[s0, 256]> self = ?,<br>float p = 0.5 | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[12, 1, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?           | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?           | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s2 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s4 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s6 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s8 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[12, 1, s2 + 1]> self = ?,<br>Tensor<[12, s2 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 15 | Tensor<[12, 1, s4 + 1]> self = ?,<br>Tensor<[12, s4 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[12, 1, s6 + 1]> self = ?,<br>Tensor<[12, s6 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[12, 1, s8 + 1]> self = ?,<br>Tensor<[12, s8 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 18 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Unknown  | Done       | 0.9999892422935462 | 0      |
| 19 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Unknown  | Done       | 0.999986179927007  | 0      |
| 20 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Unknown  | Done       | 0.9999860133509236 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 1, 512]>],<br>int dim = -1        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 12, 1, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 12, s0, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[1, 12, s2, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[1, 12, s4, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1, 12, s6, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[1, 12, s8, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[1, s0, 768]>, <[1, s0, 512]>],<br>int dim = -1      | Unknown  | Unknown    | N/A   | N/A    |
### aten.clamp_min.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number min = 1e-12 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 24, 3072]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 24, 768]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 256, 96]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 80, 96]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, s0, 768]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[12, 1, 1]> self = ?                                                                | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[12, 1, 24]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[12, 1, 2]> self = ?                                                                | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[12, 1, s0 + 1]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[12, 1, s10 + 1]> self = ?                                                          | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[12, 1, s2 + 1]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[12, 1, s4 + 1]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[12, 1, s6 + 1]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[12, 1, s8 + 1]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[12, 24, 24]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 64, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 128, 8]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 256, 96]> input = ?,<br>Tensor<[256, 256, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1            | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 256, 96]> input = ?,<br>Tensor<[80, 256, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1             | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[1, 32, 7]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 512, 96]> input = ?,<br>Tensor<[512, 256, 8]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 32, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 80, 96]> input = ?,<br>Tensor<[256, 80, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1              | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 80, 96]> input = ?,<br>Tensor<[512, 80, 7]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 0.5      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor other = 3     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 256, 384]> self = ?,<br>Tensor other = 3      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor other = 3     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor other = 3      | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 0.5     | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?     | Unknown  | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                        | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1 | Unknown  | Done       |     1 |      0 |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>number other = 1  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>number other = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 1, 24]  | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24] | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [-1, 1, -1]      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [-1, <s0>, -1]   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 512]              | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]    | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]    | Unknown  | Done       | 1.0   | -1     |
### aten.ge.Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[24, 24]> self = ?,<br>number other = 160 | Unknown  | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 24, 3072]> self = ? | Unknown  | Done       | 0.9999911996681277 | 0      |
### aten.index_put.default
|    | ATen Input Variations                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[24, 24]> self = ?,<br>List[Optional[Tensor]] indices = [<[24, 24]>],<br>Tensor values = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.leaky_relu.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128, 1536]> self = ?,<br>number negative_slope = 0.1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 384]> self = ?,<br>number negative_slope = 0.1  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 24576]> self = ?                                 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 24576]> self = ?,<br>number negative_slope = 0.1 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 512, 96]> self = ?,<br>number negative_slope = 0.1   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 6144]> self = ?,<br>number negative_slope = 0.1  | Unknown  | Unknown    | N/A   | N/A    |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True | Unknown  | Unknown    | N/A   | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[24, 24]> self = ?,<br>number other = -160 | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> mask = ?,<br>number value = -3.3895313892515355e+38   | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Done       |     1 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1      | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125  | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125 | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1     | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ? | Unknown  | Done       | 0.9999960183255797 | 0      |
|  6 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05  | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 24, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.9955531592332004 | 3      |
### aten.relu.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 256]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 768]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0, 256]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, s0, 768]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.repeat.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0  | Unknown  | Done       | 0.999994 |      0 |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0 | Unknown  | Done       | 0.999993 |      0 |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number s = 0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 0,<br>int index = 0  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int]<s0> end = ?               | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                   | Unknown  | Done       | 1.0   | 0      |
### aten.squeeze.dim
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 24576]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ? | Unknown  | Done       | 0.9999983021675521 | 0      |
|  1 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
### aten.sym_size.int
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0, 768]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[256, 256]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[256, 80]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[3072, 768]> self = ? | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[768, 1280]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[768, 256]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[768, 3072]> self = ? | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[768, 768]> self = ?  | Unknown  | Done       | 1.0   | 0      |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 24576]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 96]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 24576]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 80, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 96, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 96, 80]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1       | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[12, 2, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1      | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[12, s0 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[12, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[12, s2 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[12, s4 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[12, s6 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[12, s8 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[24, 12, 24]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1      | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1    | Unknown  | Done       | 1.0   | 0      |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2 | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 24]> self = ?,<br>int dim = 1    | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 256]> self = ?,<br>int dim = 0   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[24]> self = ?,<br>int dim = 1       | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[96, 80]> self = ?,<br>int dim = 0   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[s0, 256]> self = ?,<br>int dim = 0  | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, 1280]            | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [1, 256]              | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]            | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]        | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]              | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 80]> self = ?,<br>List[int] size = [1, 80]                | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 12, 1, 24]> self = ?,<br>List[int] size = [12, 1, 24]        | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]       | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, -1, 64]       | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]      | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]      | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 12, s2 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 12, s4 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 12, s6 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 12, s8 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]          | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, 24, 12, 64]      | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]            | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 256]> self = ?,<br>List[int] size = [1, 1, 256]              | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]            | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]              | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, s0, 1280]> self = ?,<br>List[int] size = [<s0>, 1280]        | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, s0, 256]> self = ?,<br>List[int] size = [<s0>, 256]          | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, s0, 80]> self = ?,<br>List[int] size = [<s0>, 80]            | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[12, 1, 24]> self = ?,<br>List[int] size = [1, 12, 1, 24]        | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]        | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [1, 12, 24, 24]      | Unknown  | Done       | 1.0   | 0      |
| 32 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]         | Unknown  | Done       | 1.0   | 0      |
| 33 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]      | Unknown  | Done       | 1.0   | 0      |
| 34 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  | Done       | 1.0   | 0      |
| 35 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]         | Unknown  | Done       | 1.0   | 0      |
| 36 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]         | Unknown  | Done       | 1.0   | 0      |
| 37 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]          | Unknown  | Done       | 1.0   | 0      |
| 38 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]         | Unknown  | Done       | 1.0   | 0      |
| 39 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]            | Unknown  | Done       | 1.0   | 0      |
| 40 | Tensor<[24576, 1]> self = ?,<br>List[int] size = [-1]                   | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[s0, 256]> self = ?,<br>List[int] size = [1, <s0>, 256]          | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[s0, 768]> self = ?,<br>List[int] size = [1, <s0>, 768]          | Unknown  | Unknown    | N/A   | N/A    |
### aten.where.self
|    | ATen Input Variations                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 256]> condition = ?,<br>Tensor<[1, 1, 256]> self = ?,<br>Tensor<[]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0, 256]> condition = ?,<br>Tensor<[1, s0, 256]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   | N/A    |

