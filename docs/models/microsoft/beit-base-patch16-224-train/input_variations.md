# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax_backward_data.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_view.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                         |                 13 |          13 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default                      |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.bmm.default                        |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default                        |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.clone.default                      |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.detach.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.div.Scalar                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.div.Tensor                         |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 13 | aten.expand.default                     |                  5 |           1 |         4 |          0 | ✅          |    1    |
| 14 | aten.gelu.default                       |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 15 | aten.gelu_backward.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.index.Tensor                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.index_put.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.mean.dim                           |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 19 | aten.mm.default                         |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 20 | aten.mul.Tensor                         |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 21 | aten.native_layer_norm.default          |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 22 | aten.native_layer_norm_backward.default |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.new_zeros.default                  |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 24 | aten.permute.default                    |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 25 | aten.rand.default                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.slice.Tensor                       |                  5 |           3 |         2 |          0 | ✅          |    1    |
| 27 | aten.slice_backward.default             |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.squeeze.dim                        |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 29 | aten.sum.dim_IntList                    |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.t.default                          |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 31 | aten.transpose.int                      |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 32 | aten.unsqueeze.default                  |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 33 | aten.view.default                       |                 21 |          20 |         0 |          0 | 🚧          |    0.95 |
| 34 | aten.zeros.default                      |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999589 |      0 |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 197, 197]> grad_output = ?,<br>Tensor<[1, 12, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768] | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839           | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9090909063816071           | Done     | Done       | 1        |      0 |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9181818142533302           | Done     | Done       | 1        |      0 |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9272727221250534           | Done     | Done       | 1        |      0 |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9363636374473572           | Done     | Done       | 1        |      0 |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.94545454159379             | Done     | Done       | 1        |      0 |
|  6 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9545454569160938           | Done     | Done       | 1        |      0 |
|  7 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.963636364787817            | Done     | Done       | 1        |      0 |
|  8 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9727272726595402           | Done     | Done       | 1        |      0 |
|  9 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9818181823939085           | Done     | Done       | 1        |      0 |
| 10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9909090911969543           | Done     | Done       | 1        |      0 |
| 11 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ? | Done     | Done       | 0.999998 |      0 |
| 12 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?         | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     | Done       | 0.999968 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[197, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999944 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999967 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
|  1 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?  | Done     | Done       | 0.999988 |      0 |
|  2 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 196, 768]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 197, 197]> self = ?                                                          | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  3 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 14, 14]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[List[int]] bias_sizes = [768],<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
### aten.detach.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 197, 197]> self = ? | None     | Fallback   |     1 |     -1 |
### aten.div.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>number other = 196 | None     | Fallback   |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0            | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.8999999985098839 | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9090909063816071 | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9181818142533302 | Done     | Done       | 0.999995 |      0 |
|  4 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9272727221250534 | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9363636374473572 | Done     | Done       | 0.999997 |      0 |
|  6 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.94545454159379   | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9545454569160938 | Done     | Done       | 0.999997 |      0 |
|  8 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.963636364787817  | Done     | Done       | 0.999998 |      0 |
|  9 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9727272726595402 | Done     | Done       | 0.999997 |      0 |
| 10 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9818181823939085 | Done     | Done       | 0.999996 |      0 |
| 11 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9909090911969543 | Done     | Done       | 0.999997 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 196, 768]           | Done     | Done       |     1 |      2 |
|  2 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 197, 3072]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 197, 3072]> grad_output = ?,<br>Tensor<[1, 197, 3072]> self = ? | None     | Fallback   |     1 |     -1 |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>] | None     | Fallback   |     1 |     -1 |
### aten.index_put.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>],<br>Tensor<[38809, 12]> values = ?,<br>bool accumulate = True | None     | Fallback   |     1 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Done     | Done       | 0.713954 |      0 |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 768]> mat2 = ?   | Done     | Done       | 0.999968 |      0 |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?      | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[197, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999944 |      0 |
|  3 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | 0.999968 |      0 |
|  4 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999968 |      0 |
|  5 | Tensor<[3072, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?  | Done     | Done       | 0.999971 |      0 |
|  6 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 3072]> mat2 = ?  | Done     | Done       | 0.999971 |      0 |
|  7 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?   | Done     | Done       | 0.999971 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?     | Done     | Done       | 0.999997 |      0 |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?         | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?         | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Done     | Done       | N/A   |      1 |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 197, 768]> grad_out = ?,<br>Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 197, 1]> mean = ?,<br>Tensor<[1, 197, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 768]> grad_out = ?,<br>Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 1]> mean = ?,<br>Tensor<[1, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True]                     | None     | Fallback   |     1 |      0 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [732, 12],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Removed  | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[12, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]      | Done     | Done       |     1 |      0 |
|  3 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]      | Done     | Done       |     1 |      0 |
### aten.rand.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                 | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Done     | Done       |     1 |     -1 |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 196, 768],<br>int dim = 2,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 196, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 1,<br>int start = 1,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 197, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
### aten.squeeze.dim
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[197, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[197, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1000, 768]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[197, 3072]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[197, 768]> self = ?  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[3072, 768]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[768, 1000]> self = ? | Done     | Done       |     1 |      0 |
|  6 | Tensor<[768, 3072]> self = ? | Done     | Done       |     1 |      0 |
|  7 | Tensor<[768, 768]> self = ?  | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
|  4 | Tensor<[12, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  5 | Tensor<[12, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
|  6 | Tensor<[12, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768]> self = ?,<br>int dim = 1       | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]                | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]   | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]   | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]                 | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14]   | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                   | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[197, 197, 12]> self = ?,<br>List[int] size = [38809, 12]       | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | None     | Fallback   |     1 |     -1 |
| 18 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | Done     | Done       |     1 |     -1 |
| 19 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | Done     | Done       |     1 |     -1 |
| 20 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]       | Done     | Done       |     1 |     -1 |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [732, 12],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Unknown    | N/A   | N/A    |

