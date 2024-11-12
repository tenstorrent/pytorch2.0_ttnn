# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  1 | aten._softmax_backward_data.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_view.default               |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  3 | aten.add.Tensor                         |                 25 |           2 |         0 |         23 | 🚧          |    0.08 |
|  4 | aten.addmm.default                      |                  4 |           0 |         0 |          4 | ✘           |    0    |
|  5 | aten.bmm.default                        |                  3 |           1 |         0 |          2 | 🚧          |    0.33 |
|  6 | aten.cat.default                        |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default                      |                  4 |           2 |         0 |          2 | 🚧          |    0.5  |
|  8 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.detach.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.div.Scalar                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.div.Tensor                         |                 24 |          23 |         0 |          0 | 🚧          |    0.96 |
| 13 | aten.expand.default                     |                  5 |           0 |         4 |          1 | 🚧          |    0.8  |
| 14 | aten.gelu.default                       |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 15 | aten.gelu_backward.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.index.Tensor                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.index_put.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.mean.dim                           |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.mm.default                         |                  8 |           4 |         0 |          4 | 🚧          |    0.5  |
| 20 | aten.mul.Tensor                         |                  4 |           2 |         0 |          2 | 🚧          |    0.5  |
| 21 | aten.native_layer_norm.default          |                  2 |           0 |         0 |          2 | ✘           |    0    |
| 22 | aten.native_layer_norm_backward.default |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.new_zeros.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.permute.default                    |                  4 |           1 |         0 |          2 | 🚧          |    0.25 |
| 25 | aten.rand.default                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.slice.Tensor                       |                  5 |           1 |         2 |          2 | 🚧          |    0.6  |
| 27 | aten.slice_backward.default             |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.squeeze.dim                        |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 29 | aten.sum.dim_IntList                    |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.t.default                          |                  8 |           4 |         0 |          4 | 🚧          |    0.5  |
| 31 | aten.transpose.int                      |                  7 |           2 |         0 |          2 | 🚧          |    0.29 |
| 32 | aten.unsqueeze.default                  |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 33 | aten.view.default                       |                 21 |           0 |         0 |          7 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Fallback | Unknown    | N/A   |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> grad_output = ?,<br>Tensor<[1, 16, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | Unknown    | N/A   |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024] | Fallback | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839           | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9043478220701218           | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9086956530809402           | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9130434766411781           | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.917391300201416            | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9217391312122345           | Fallback | Unknown    | N/A   |
|  6 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9260869547724724           | Fallback | Unknown    | N/A   |
|  7 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9304347857832909           | Fallback | Unknown    | N/A   |
|  8 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9347826093435287           | Fallback | Unknown    | N/A   |
|  9 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9391304366290569           | Fallback | Unknown    | N/A   |
| 10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9434782639145851           | Fallback | Unknown    | N/A   |
| 11 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.947826087474823            | Fallback | Unknown    | N/A   |
| 12 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9521739110350609           | Fallback | Unknown    | N/A   |
| 13 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9565217345952988           | Fallback | Unknown    | N/A   |
| 14 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.960869561880827            | Fallback | Unknown    | N/A   |
| 15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9652173891663551           | Fallback | Unknown    | N/A   |
| 16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9695652164518833           | Fallback | Unknown    | N/A   |
| 17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9739130418747663           | Fallback | Unknown    | N/A   |
| 18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9782608672976494           | Fallback | Unknown    | N/A   |
| 19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9826086945831776           | Fallback | Unknown    | N/A   |
| 20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9869565209373832           | Fallback | Unknown    | N/A   |
| 21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9913043472915888           | Fallback | Unknown    | N/A   |
| 22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9956521736457944           | Fallback | Unknown    | N/A   |
| 23 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Done     | Unknown    | N/A   |
| 24 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?       | Done     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[197, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Fallback | Unknown    | N/A   |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ? | Fallback | Unknown    | N/A   |
|  1 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?  | Fallback | Unknown    | N/A   |
|  2 | Tensor<[16, 64, 197]> self = ?,<br>Tensor<[16, 197, 197]> mat2 = ? | Done     | Unknown    | N/A   |
### aten.cat.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 196, 1024]>],<br>int dim = 1 | None     | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?                                                          | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?                                                             | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   |
|  3 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Unknown    | N/A   |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Unknown    | N/A   |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 14, 14]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[List[int]] bias_sizes = [1024],<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Unknown    | N/A   |
### aten.detach.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ? | None     | Unknown    | N/A   |
### aten.div.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>number other = 196 | None     | Unknown    | N/A   |
### aten.div.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0             | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.8999999985098839 | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9043478220701218 | Done     | Unknown    | N/A   |
|  3 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9086956530809402 | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9130434766411781 | Done     | Unknown    | N/A   |
|  5 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.917391300201416  | Done     | Unknown    | N/A   |
|  6 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9217391312122345 | Done     | Unknown    | N/A   |
|  7 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9260869547724724 | Done     | Unknown    | N/A   |
|  8 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9304347857832909 | Done     | Unknown    | N/A   |
|  9 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9347826093435287 | Done     | Unknown    | N/A   |
| 10 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9391304366290569 | Done     | Unknown    | N/A   |
| 11 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9434782639145851 | Done     | Unknown    | N/A   |
| 12 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.947826087474823  | Done     | Unknown    | N/A   |
| 13 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9521739110350609 | Done     | Unknown    | N/A   |
| 14 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9565217345952988 | Done     | Unknown    | N/A   |
| 15 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.960869561880827  | Done     | Unknown    | N/A   |
| 16 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9652173891663551 | Done     | Unknown    | N/A   |
| 17 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9695652164518833 | Done     | Unknown    | N/A   |
| 18 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9739130418747663 | Done     | Unknown    | N/A   |
| 19 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9782608672976494 | Done     | Unknown    | N/A   |
| 20 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9826086945831776 | Done     | Unknown    | N/A   |
| 21 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9869565209373832 | Done     | Unknown    | N/A   |
| 22 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9913043472915888 | Done     | Unknown    | N/A   |
| 23 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9956521736457944 | Done     | Unknown    | N/A   |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]            | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 196, 1024]         | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | Removed  | Unknown    | N/A   |
|  3 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Removed  | Unknown    | N/A   |
|  4 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]   | Removed  | Unknown    | N/A   |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 4096]> self = ? | Fallback | Unknown    | N/A   |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 4096]> grad_output = ?,<br>Tensor<[1, 197, 4096]> self = ? | None     | Unknown    | N/A   |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>] | None     | Unknown    | N/A   |
### aten.index_put.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>],<br>Tensor<[38809, 16]> values = ?,<br>bool accumulate = True | None     | Unknown    | N/A   |
### aten.mean.dim
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1] | None     | Unknown    | N/A   |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1024]> mat2 = ?   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1024]> mat2 = ?      | Done     | Unknown    | N/A   |
|  2 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?  | Done     | Unknown    | N/A   |
|  3 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 4096]> mat2 = ?  | Done     | Unknown    | N/A   |
|  4 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
|  5 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Fallback | Unknown    | N/A   |
|  6 | Tensor<[197, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
|  7 | Tensor<[4096, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?  | Done     | Unknown    | N/A   |
### aten.mul.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?      | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ? | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?         | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?         | Done     | Unknown    | N/A   |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12      | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Fallback | Unknown    | N/A   |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024]> grad_out = ?,<br>Tensor<[1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Tensor<[1, 1]> mean = ?,<br>Tensor<[1, 1]> rstd = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[bool] output_mask = [True, True, True]                     | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> grad_out = ?,<br>Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Tensor<[1, 197, 1]> mean = ?,<br>Tensor<[1, 197, 1]> rstd = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | Unknown    | N/A   |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [732, 16],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | None     | Unknown    | N/A   |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Fallback | Unknown    | N/A   |
|  2 | Tensor<[16, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]      | None     | Unknown    | N/A   |
|  3 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]      | Done     | Unknown    | N/A   |
### aten.rand.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                 | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Fallback | Unknown    | N/A   |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 196, 1024]> grad_output = ?,<br>List[int] input_sizes = [1, 196, 1024],<br>int dim = 2,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 196, 1024]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 1024],<br>int dim = 1,<br>int start = 1,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 1024]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 1024],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Unknown    | N/A   |
### aten.squeeze.dim
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = 0 | Fallback | Unknown    | N/A   |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | None     | Unknown    | N/A   |
|  2 | Tensor<[197, 1024]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | Unknown    | N/A   |
|  3 | Tensor<[197, 4096]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?    | Done     | Unknown    | N/A   |
|  1 | Tensor<[1000, 1024]> self = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[1024, 1000]> self = ? | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1024, 1024]> self = ? | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1024, 4096]> self = ? | Fallback | Unknown    | N/A   |
|  5 | Tensor<[197, 1024]> self = ?  | Done     | Unknown    | N/A   |
|  6 | Tensor<[197, 4096]> self = ?  | Done     | Unknown    | N/A   |
|  7 | Tensor<[4096, 1024]> self = ? | Fallback | Unknown    | N/A   |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 196, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Unknown    | N/A   |
|  4 | Tensor<[16, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | None     | Unknown    | N/A   |
|  5 | Tensor<[16, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Unknown    | N/A   |
|  6 | Tensor<[16, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | None     | Unknown    | N/A   |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024]> self = ?,<br>int dim = 1      | Done     | Unknown    | N/A   |
|  1 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0 | Done     | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1024]              | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                 | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196] | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] size = [1, 1024, 14, 14] | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                 | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197] | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]   | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]   | None     | Unknown    | N/A   |
|  8 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [1, 197, 16, 64]  | None     | Unknown    | N/A   |
|  9 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]       | None     | Unknown    | N/A   |
| 10 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]  | None     | Unknown    | N/A   |
| 11 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]       | None     | Unknown    | N/A   |
| 12 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [4096]                 | Fallback | Unknown    | N/A   |
| 13 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | None     | Unknown    | N/A   |
| 14 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | None     | Unknown    | N/A   |
| 15 | Tensor<[16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]   | Fallback | Unknown    | N/A   |
| 16 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]       | None     | Unknown    | N/A   |
| 17 | Tensor<[197, 197, 16]> self = ?,<br>List[int] size = [38809, 16]       | Fallback | Unknown    | N/A   |
| 18 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | None     | Unknown    | N/A   |
| 19 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]       | None     | Unknown    | N/A   |
| 20 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]       | None     | Unknown    | N/A   |

