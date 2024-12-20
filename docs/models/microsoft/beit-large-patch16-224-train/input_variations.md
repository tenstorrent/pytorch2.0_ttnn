# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax_backward_data.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_view.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                         |                 25 |          25 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default                      |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.bmm.default                        |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default                        |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.clone.default                      |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.detach.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.div.Scalar                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.div.Tensor                         |                 24 |          24 |         0 |          0 | ✅          |    1    |
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
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999584 |      0 |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> grad_output = ?,<br>Tensor<[1, 16, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024] | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839           | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9043478220701218           | Done     | Done       | 1        |      0 |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9086956530809402           | Done     | Done       | 1        |      0 |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9130434766411781           | Done     | Done       | 1        |      0 |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.917391300201416            | Done     | Done       | 1        |      0 |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9217391312122345           | Done     | Done       | 1        |      0 |
|  6 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9260869547724724           | Done     | Done       | 1        |      0 |
|  7 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9304347857832909           | Done     | Done       | 1        |      0 |
|  8 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9347826093435287           | Done     | Done       | 1        |      0 |
|  9 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9391304366290569           | Done     | Done       | 1        |      0 |
| 10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9434782639145851           | Done     | Done       | 1        |      0 |
| 11 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.947826087474823            | Done     | Done       | 1        |      0 |
| 12 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9521739110350609           | Done     | Done       | 1        |      0 |
| 13 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9565217345952988           | Done     | Done       | 1        |      0 |
| 14 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.960869561880827            | Done     | Done       | 1        |      0 |
| 15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9652173891663551           | Done     | Done       | 1        |      0 |
| 16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9695652164518833           | Done     | Done       | 1        |      0 |
| 17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9739130418747663           | Done     | Done       | 1        |      0 |
| 18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9782608672976494           | Done     | Done       | 1        |      0 |
| 19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9826086945831776           | Done     | Done       | 1        |      0 |
| 20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9869565209373832           | Done     | Done       | 1        |      0 |
| 21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9913043472915888           | Done     | Done       | 1        |      0 |
| 22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9956521736457944           | Done     | Done       | 1        |      0 |
| 23 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Done     | Done       | 0.999998 |      0 |
| 24 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?       | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?   | Done     | Done       | 0.99996  |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[197, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999932 |      0 |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
|  1 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?  | Done     | Done       | 0.999988 |      0 |
|  2 | Tensor<[16, 64, 197]> self = ?,<br>Tensor<[16, 197, 197]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 196, 1024]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?                                                          | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 197, 1024]> self = ?                                                             | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  3 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 14, 14]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[List[int]] bias_sizes = [1024],<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
### aten.detach.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ? | None     | Fallback   |     1 |     -1 |
### aten.div.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>number other = 196 | None     | Fallback   |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0             | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.8999999985098839 | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9043478220701218 | Done     | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9086956530809402 | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9130434766411781 | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.917391300201416  | Done     | Done       | 0.999995 |      0 |
|  6 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9217391312122345 | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9260869547724724 | Done     | Done       | 0.999995 |      0 |
|  8 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9304347857832909 | Done     | Done       | 0.999996 |      0 |
|  9 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9347826093435287 | Done     | Done       | 0.999997 |      0 |
| 10 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9391304366290569 | Done     | Done       | 0.999996 |      0 |
| 11 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9434782639145851 | Done     | Done       | 0.999996 |      0 |
| 12 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.947826087474823  | Done     | Done       | 0.999995 |      0 |
| 13 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9521739110350609 | Done     | Done       | 0.999996 |      0 |
| 14 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9565217345952988 | Done     | Done       | 0.999997 |      0 |
| 15 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.960869561880827  | Done     | Done       | 0.999996 |      0 |
| 16 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9652173891663551 | Done     | Done       | 0.999997 |      0 |
| 17 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9695652164518833 | Done     | Done       | 0.999999 |      0 |
| 18 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9739130418747663 | Done     | Done       | 0.999996 |      0 |
| 19 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9782608672976494 | Done     | Done       | 0.999998 |      0 |
| 20 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9826086945831776 | Done     | Done       | 0.999996 |      0 |
| 21 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9869565209373832 | Done     | Done       | 0.999999 |      0 |
| 22 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9913043472915888 | Done     | Done       | 0.999998 |      0 |
| 23 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9956521736457944 | Done     | Done       | 0.999999 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]            | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 196, 1024]         | Done     | Done       |     1 |      2 |
|  2 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]   | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 197, 4096]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 197, 4096]> grad_output = ?,<br>Tensor<[1, 197, 4096]> self = ? | None     | Fallback   |     1 |     -1 |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>] | None     | Fallback   |     1 |     -1 |
### aten.index_put.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>],<br>Tensor<[38809, 16]> values = ?,<br>bool accumulate = True | None     | Fallback   |     1 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1] | Done     | Done       | 0.717433 |      0 |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1024]> mat2 = ?   | Done     | Done       | 0.999966 |      0 |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1024]> mat2 = ?      | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?  | Done     | Done       | 0.999971 |      0 |
|  3 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 4096]> mat2 = ?  | Done     | Done       | 0.999971 |      0 |
|  4 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
|  5 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
|  6 | Tensor<[197, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999933 |      0 |
|  7 | Tensor<[4096, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?  | Done     | Done       | 0.999971 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?      | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?         | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?         | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12      | Done     | Done       | N/A   |      1 |
|  1 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024]> grad_out = ?,<br>Tensor<[1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Tensor<[1, 1]> mean = ?,<br>Tensor<[1, 1]> rstd = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[bool] output_mask = [True, True, True]                     | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 197, 1024]> grad_out = ?,<br>Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Tensor<[1, 197, 1]> mean = ?,<br>Tensor<[1, 197, 1]> rstd = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [732, 16],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Removed  | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]      | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]      | Done     | Unknown    | N/A   | N/A    |
### aten.rand.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                 | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Done     | Done       |     1 |     -1 |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 1024]> grad_output = ?,<br>List[int] input_sizes = [1, 196, 1024],<br>int dim = 2,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 196, 1024]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 1024],<br>int dim = 1,<br>int start = 1,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 197, 1024]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 1024],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   |     1 |     -1 |
### aten.squeeze.dim
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[197, 1024]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[197, 4096]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1000, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1024, 1000]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1024, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1024, 4096]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[197, 1024]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[197, 4096]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[4096, 1024]> self = ? | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 196, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[16, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  5 | Tensor<[16, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
|  6 | Tensor<[16, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>int dim = 1      | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1024]              | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196] | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] size = [1, 1024, 14, 14] | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                 | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197] | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]   | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]   | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [1, 197, 16, 64]  | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]       | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]  | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]       | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [4096]                 | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]   | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]       | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[197, 197, 16]> self = ?,<br>List[int] size = [38809, 16]       | Done     | Done       |     1 |     -1 |
| 18 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | None     | Fallback   |     1 |     -1 |
| 19 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]       | Done     | Done       |     1 |     -1 |
| 20 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]       | Done     | Done       |     1 |     -1 |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [732, 16],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Unknown    | N/A   | N/A    |

