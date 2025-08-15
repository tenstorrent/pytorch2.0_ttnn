# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_functional.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._softmax.default                            |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten._softmax_backward_data.default              |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten._to_copy.default                            |                 11 |          10 |         0 |          0 | 🚧          |    0.91 |
|  4 | aten._unsafe_index.Tensor                        |                 16 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten._unsafe_index_put.default                   |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten._unsafe_view.default                        |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  7 | aten.add.Tensor                                  |                 26 |          26 |         0 |          0 | ✅          |    1    |
|  8 | aten.addmm.default                               |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  9 | aten.bmm.default                                 |                 15 |          15 |         0 |          0 | ✅          |    1    |
| 10 | aten.cat.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.clone.default                               |                 23 |           0 |        23 |          0 | ✅          |    1    |
| 12 | aten.convolution.default                         |                 13 |          13 |         0 |          0 | ✅          |    1    |
| 13 | aten.convolution_backward.default                |                 13 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.detach.default                              |                  5 |           0 |         5 |          0 | ✅          |    1    |
| 15 | aten.div.Tensor                                  |                 11 |          11 |         0 |          0 | ✅          |    1    |
| 16 | aten.expand.default                              |                 15 |           0 |        15 |          0 | ✅          |    1    |
| 17 | aten.floor.default                               |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 18 | aten.gelu.default                                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 19 | aten.gelu_backward.default                       |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.mm.default                                  |                 35 |          35 |         0 |          0 | ✅          |    1    |
| 21 | aten.mul.Tensor                                  |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 22 | aten.native_batch_norm_backward.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.native_layer_norm.default                   |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 24 | aten.native_layer_norm_backward.default          |                  7 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.new_zeros.default                           |                  4 |           0 |         4 |          0 | ✅          |    1    |
| 26 | aten.permute.default                             |                 41 |          41 |         0 |          0 | ✅          |    1    |
| 27 | aten.rand.default                                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.relu.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 29 | aten.rsub.Scalar                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 30 | aten.slice.Tensor                                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 31 | aten.sum.dim_IntList                             |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 32 | aten.t.default                                   |                 26 |          26 |         0 |          0 | ✅          |    1    |
| 33 | aten.threshold_backward.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 34 | aten.transpose.int                               |                 37 |          37 |         0 |          0 | ✅          |    1    |
| 35 | aten.view.default                                |                112 |         112 |         0 |          0 | ✅          |    1    |
| 36 | aten.zeros.default                               |                  4 |           4 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   |     1 |      0 |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999595 |      0 |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999591 |      0 |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999598 |      0 |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999597 |      0 |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> grad_output = ?,<br>Tensor<[1, 1, 16384, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 2, 4096, 256]> grad_output = ?,<br>Tensor<[1, 2, 4096, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 5, 1024, 256]> grad_output = ?,<br>Tensor<[1, 5, 1024, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 8, 256, 256]> grad_output = ?,<br>Tensor<[1, 8, 256, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16     | None     | Fallback   |     1 |     -1 |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu  | Done     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Done     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Done     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 256, 64, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 256, 64, 64]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Done     | Fallback   |     1 |     -1 |
| 10 | Tensor<[256]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided                                                | None     | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_3] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_4] | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_3] | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_4] | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_21] | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_22] | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_21] | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_22] | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_15]  | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_16]  | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_15]  | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_16]  | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_10]  | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_9]   | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_10]  | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_9]   | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_index_put.default
|    | ATen Input Variations                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True   | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True   | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True   | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]  | Done     | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839             | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032             | Done     | Done       | 1        |      0 |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226             | Done     | Done       | 1        |      0 |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323             | Done     | Done       | 1        |      0 |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516             | Done     | Done       | 1        |      0 |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161             | Done     | Done       | 1        |      0 |
|  6 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581             | Done     | Done       | 1        |      0 |
|  7 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?         | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.999998 |      0 |
|  9 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 10 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                 | Done     | Done       | 0.999998 |      0 |
| 11 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?         | Done     | Done       | 0.999998 |      0 |
| 12 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     | Done       | 0.999998 |      0 |
| 13 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 14 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?           | Done     | Done       | 0.999998 |      0 |
| 15 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?           | Done     | Done       | 0.999998 |      0 |
| 16 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.999998 |      0 |
| 17 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 18 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?             | Done     | Done       | 0.999998 |      0 |
| 19 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 20 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?             | Done     | Done       | 0.999998 |      0 |
| 21 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?   | Done     | Done       | 0.999998 |      0 |
| 22 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.999998 |      0 |
| 23 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?           | Done     | Done       | 0.999998 |      0 |
| 24 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 25 | Tensor<[]> self = ?,<br>Tensor other = 1                                     | Done     | Done       | 1        |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Done     | Done       | 0.999974 |      0 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 128]> mat2 = ?   | Done     | Done       | 0.999988 |      0 |
|  2 | Tensor<[160]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?  | Done     | Done       | 0.999981 |      0 |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 160]> mat2 = ?  | Done     | Done       | 0.999968 |      0 |
|  4 | Tensor<[160]> self = ?,<br>Tensor<[256, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?   | Done     | Done       | 0.999981 |      0 |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Done     | Done       | 0.999954 |      0 |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | Done       | 0.999978 |      0 |
|  7 | Tensor<[256]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     | Done       | 0.999985 |      0 |
|  8 | Tensor<[32]> self = ?,<br>Tensor<[16384, 128]> mat1 = ?,<br>Tensor<[128, 32]> mat2 = ?   | Done     | Done       | 0.999978 |      0 |
|  9 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?     | Done     | Done       | 0.999988 |      0 |
| 10 | Tensor<[32]> self = ?,<br>Tensor<[256, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     | Done       | 0.999988 |      0 |
| 11 | Tensor<[640]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 640]> mat2 = ?  | Done     | Done       | 0.999981 |      0 |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[256, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?       | Done     | Done       | 0.999986 |      0 |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[4096, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | Done       | 0.999974 |      0 |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | Done       | 0.999985 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                                | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?    | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ? | Done     | Done       | 0.999799 |      0 |
|  3 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ? | Done     | Done       | 0.999799 |      0 |
|  4 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?   | Done     | Done       | 0.999936 |      0 |
|  5 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?   | Done     | Done       | 0.999933 |      0 |
|  6 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
|  7 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?     | Done     | Done       | 0.999989 |      0 |
|  8 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
|  9 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?     | Done     | Done       | 0.999989 |      0 |
| 10 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?   | Done     | Done       | 0.999966 |      0 |
| 11 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?   | Done     | Done       | 0.999966 |      0 |
| 12 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?     | Done     | Done       | 0.999975 |      0 |
| 13 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?      | Done     | Done       | 0.999989 |      0 |
| 14 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?     | Done     | Done       | 0.999975 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 256, 128, 128]>, <[1, 256, 128, 128]>, <[1, 256, 128, 128]>, <[1, 256, 128, 128]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                          | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1024, 160]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 1024, 640]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[1, 16384, 128]> self = ?                                                             | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[1, 16384, 32]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[1, 2, 4096, 256]> self = ?                                                           | Removed  | Done       |     1 |      0 |
|  8 | Tensor<[1, 256, 1024]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  9 | Tensor<[1, 256, 128, 128]> self = ?                                                          | Removed  | Done       |     1 |      0 |
| 10 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last    | Removed  | Done       |     1 |      0 |
| 11 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
| 12 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 13 | Tensor<[1, 256, 256]> self = ?                                                               | Removed  | Done       |     1 |      0 |
| 14 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 15 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 16 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
| 17 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
| 18 | Tensor<[1, 4096, 256]> self = ?                                                              | Removed  | Done       |     1 |      0 |
| 19 | Tensor<[1, 4096, 64]> self = ?                                                               | Removed  | Done       |     1 |      0 |
| 20 | Tensor<[1, 5, 1024, 256]> self = ?                                                           | Removed  | Done       |     1 |      0 |
| 21 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 22 | Tensor<[1, 8, 256, 256]> self = ?                                                            | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999839 |      0 |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Done     | Done       | 0.999984 |      1 |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Done     | Done       | 0.999983 |      1 |
|  3 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999909 |      1 |
|  4 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999757 |      1 |
|  5 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999964 |      1 |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | Done     | Done       | 0.999983 |      1 |
|  7 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999   |      1 |
|  8 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999606 |      1 |
|  9 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.99996  |      1 |
| 10 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999919 |      1 |
| 11 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999841 |      1 |
| 12 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | Done     | Done       | 0.999983 |      1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                     | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1024, 16, 16]> grad_output = ?,<br>Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [1024],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   | 1.0   |      0 |
|  1 | Tensor<[1, 128, 128, 128]> grad_output = ?,<br>Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [128],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128,<br>List[bool] output_mask = [True, True, True]  | None     | Fallback   | 1.0   |      0 |
|  2 | Tensor<[1, 150, 128, 128]> grad_output = ?,<br>Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [150],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]  | None     | Fallback   | 1.0   |      0 |
|  3 | Tensor<[1, 160, 16, 16]> grad_output = ?,<br>Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[List[int]] bias_sizes = [160],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
|  4 | Tensor<[1, 160, 32, 32]> grad_output = ?,<br>Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [160],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]        | None     | Fallback   | 1.0   |      0 |
|  5 | Tensor<[1, 256, 128, 128]> grad_output = ?,<br>Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   | N/A   |      0 |
|  6 | Tensor<[1, 256, 16, 16]> grad_output = ?,<br>Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [256],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
|  7 | Tensor<[1, 256, 64, 64]> grad_output = ?,<br>Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [256],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
|  8 | Tensor<[1, 32, 128, 128]> grad_output = ?,<br>Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[List[int]] bias_sizes = [32],<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]         | None     | Fallback   | 1.0   |      0 |
|  9 | Tensor<[1, 32, 16, 16]> grad_output = ?,<br>Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[List[int]] bias_sizes = [32],<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]         | None     | Fallback   | 1.0   |      0 |
| 10 | Tensor<[1, 64, 16, 16]> grad_output = ?,<br>Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[List[int]] bias_sizes = [64],<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]           | None     | Fallback   | 1.0   |      0 |
| 11 | Tensor<[1, 64, 64, 64]> grad_output = ?,<br>Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [64],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]         | None     | Fallback   | 1.0   |      0 |
| 12 | Tensor<[1, 640, 32, 32]> grad_output = ?,<br>Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [640],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
### aten.detach.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ? | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 256, 128, 128]> self = ? | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 5, 1024, 256]> self = ?  | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 8, 256, 256]> self = ?   | Removed  | Done       |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.999996 |      0 |
|  6 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.999997 |      0 |
|  8 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.999997 |      0 |
|  9 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999996 |      0 |
| 10 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.999996 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]       | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]       | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]       | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]       | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]       | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]       | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]       | Removed  | Done       |     1 |     -1 |
### aten.floor.default
|    | ATen Input Variations      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 640]> self = ?  | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 16384, 128]> self = ? | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 256, 1024]> self = ?  | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 4096, 256]> self = ?  | Done     | Done       | 0.999991 |      0 |
### aten.gelu_backward.default
|    | ATen Input Variations                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 640]> grad_output = ?,<br>Tensor<[1, 1024, 640]> self = ?   | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 16384, 128]> grad_output = ?,<br>Tensor<[1, 16384, 128]> self = ? | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 1024]> grad_output = ?,<br>Tensor<[1, 256, 1024]> self = ?   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 4096, 256]> grad_output = ?,<br>Tensor<[1, 4096, 256]> self = ?   | None     | Fallback   |     1 |     -1 |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?   | Done     | Done       | 0.999982 |      0 |
|  1 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ?   | Done     | Done       | 0.999982 |      0 |
|  2 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 640]> mat2 = ?   | Done     | Done       | 0.999982 |      0 |
|  3 | Tensor<[1024, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
|  4 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 160]> mat2 = ?   | Done     | Done       | 0.99997  |      0 |
|  5 | Tensor<[128, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ? | Done     | Done       | 0.999799 |      0 |
|  6 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?  | Done     | Done       | 0.999955 |      0 |
|  7 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 640]> mat2 = ?  | Done     | Done       | 0.999966 |      0 |
|  8 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
|  9 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 160]> mat2 = ?    | Done     | Done       | 0.999979 |      0 |
| 10 | Tensor<[16384, 128]> self = ?,<br>Tensor<[128, 32]> mat2 = ?   | Done     | Done       | 0.99998  |      0 |
| 11 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 128]> mat2 = ?    | Done     | Done       | 0.999989 |      0 |
| 12 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?    | Done     | Done       | 0.999989 |      0 |
| 13 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?     | Done     | Done       | 0.999989 |      0 |
| 14 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?  | Done     | Done       | 0.999955 |      0 |
| 15 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 256]> mat2 = ?  | Done     | Done       | 0.999955 |      0 |
| 16 | Tensor<[256, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
| 17 | Tensor<[256, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ? | Done     | Done       | 0.999801 |      0 |
| 18 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
| 19 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?    | Done     | Done       | 0.999979 |      0 |
| 20 | Tensor<[256, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     | Done       | 0.99999  |      0 |
| 21 | Tensor<[256, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?   | Done     | Done       | 0.999845 |      0 |
| 22 | Tensor<[256, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?       | Done     | Done       | 0.999986 |      0 |
| 23 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 128]> mat2 = ? | Done     | Done       | 0.999801 |      0 |
| 24 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?  | Done     | Done       | 0.999815 |      0 |
| 25 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 16384]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
| 26 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 32]> mat2 = ?      | Done     | Done       | 0.999973 |      0 |
| 27 | Tensor<[4096, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
| 28 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?     | Done     | Done       | 0.999986 |      0 |
| 29 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | Done       | 0.999986 |      0 |
| 30 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 4096]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
| 31 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?      | Done     | Done       | 0.999979 |      0 |
| 32 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 256]> mat2 = ?   | Done     | Done       | 0.999846 |      0 |
| 33 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?    | Done     | Done       | 0.999839 |      0 |
| 34 | Tensor<[640, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?  | Done     | Done       | 0.999965 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?    | Done     | Done       | 0.9999949595371787 | 0      |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?    | Done     | Done       | 0.9999966287111733 | 0      |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?           | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     | Done       | 0.9999964134646159 | 0      |
|  4 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?    | Done     | Done       | 0.9999957314051086 | 0      |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?     | Done     | Done       | 0.9999952484665113 | 0      |
|  6 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?     | Done     | Done       | 0.9999949930846385 | 0      |
### aten.native_batch_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> grad_out = ?,<br>Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> running_mean = ?,<br>Optional[Tensor]<[256]> running_var = ?,<br>Optional[Tensor]<[256]> save_mean = ?,<br>Optional[Tensor]<[256]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.999398 |      3 |
|  1 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | 0.999898 |      3 |
|  2 | Tensor<[1, 256, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.99944  |      3 |
|  3 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.999379 |      3 |
|  4 | Tensor<[1, 256, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | 0.999895 |      3 |
|  5 | Tensor<[1, 256, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | 0.999785 |      3 |
|  6 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | 0.999791 |      3 |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 160]> grad_out = ?,<br>Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Tensor<[1, 1024, 1]> mean = ?,<br>Tensor<[1, 1024, 1]> rstd = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 16384, 32]> grad_out = ?,<br>Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Tensor<[1, 16384, 1]> mean = ?,<br>Tensor<[1, 16384, 1]> rstd = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[bool] output_mask = [True, True, True]  | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 256, 160]> grad_out = ?,<br>Tensor<[1, 256, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 256, 256]> grad_out = ?,<br>Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | None     | Fallback   |     1 |      0 |
|  4 | Tensor<[1, 256, 32]> grad_out = ?,<br>Tensor<[1, 256, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[bool] output_mask = [True, True, True]          | None     | Fallback   |     1 |      0 |
|  5 | Tensor<[1, 256, 64]> grad_out = ?,<br>Tensor<[1, 256, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[bool] output_mask = [True, True, True]          | None     | Fallback   |     1 |      0 |
|  6 | Tensor<[1, 4096, 64]> grad_out = ?,<br>Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Tensor<[1, 4096, 1]> mean = ?,<br>Tensor<[1, 4096, 1]> rstd = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   |     1 |      0 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 128, 128],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 32, 32],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 64, 64],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Removed  | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 19 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | Done       |     1 |      0 |
| 20 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 21 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 22 | Tensor<[1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 23 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 24 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 25 | Tensor<[1, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 26 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 27 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Done     | Done       |     1 |      0 |
| 28 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 29 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 30 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
| 31 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 32 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 33 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 34 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 35 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 36 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 37 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 38 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]   | Done     | Done       |     1 |      0 |
| 39 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]   | Done     | Done       |     1 |      0 |
| 40 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
### aten.rand.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Done       |     1 |     -1 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> self = ? | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512  | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 768  | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 1024 | Done     | Done       | 1.0   | 0      |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True  | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 16384, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 4096, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True  | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1024, 160]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1024, 640]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[16384, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[16384, 32]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[256, 1024]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   |     1 |     -1 |
|  9 | Tensor<[256, 160]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   |     1 |     -1 |
| 10 | Tensor<[256, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   |     1 |     -1 |
| 11 | Tensor<[256, 32]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   |     1 |     -1 |
| 12 | Tensor<[256, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   |     1 |     -1 |
| 13 | Tensor<[4096, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   |     1 |     -1 |
| 14 | Tensor<[4096, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 160]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1024, 256]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1024, 640]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[128, 32]> self = ?    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[160, 1024]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[160, 160]> self = ?   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[160, 256]> self = ?   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[160, 640]> self = ?   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[16384, 128]> self = ? | Done     | Done       |     1 |      0 |
|  9 | Tensor<[16384, 256]> self = ? | Done     | Done       |     1 |      0 |
| 10 | Tensor<[16384, 32]> self = ?  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[256, 1024]> self = ?  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[256, 160]> self = ?   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[256, 256]> self = ?   | Done     | Done       |     1 |      0 |
| 14 | Tensor<[256, 32]> self = ?    | Done     | Done       |     1 |      0 |
| 15 | Tensor<[256, 64]> self = ?    | Done     | Done       |     1 |      0 |
| 16 | Tensor<[32, 128]> self = ?    | Done     | Done       |     1 |      0 |
| 17 | Tensor<[32, 16384]> self = ?  | Done     | Done       |     1 |      0 |
| 18 | Tensor<[32, 256]> self = ?    | Done     | Done       |     1 |      0 |
| 19 | Tensor<[32, 32]> self = ?     | Done     | Done       |     1 |      0 |
| 20 | Tensor<[4096, 256]> self = ?  | Done     | Done       |     1 |      0 |
| 21 | Tensor<[4096, 64]> self = ?   | Done     | Done       |     1 |      0 |
| 22 | Tensor<[64, 256]> self = ?    | Done     | Done       |     1 |      0 |
| 23 | Tensor<[64, 4096]> self = ?   | Done     | Done       |     1 |      0 |
| 24 | Tensor<[64, 64]> self = ?     | Done     | Done       |     1 |      0 |
| 25 | Tensor<[640, 160]> self = ?   | Done     | Done       |     1 |      0 |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> grad_output = ?,<br>Tensor<[1, 256, 128, 128]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 16384, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 16384, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 2, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 19 | Tensor<[1, 4096, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 20 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 21 | Tensor<[1, 5, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 22 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 23 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 24 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 25 | Tensor<[1, 8, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 26 | Tensor<[2, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 27 | Tensor<[2, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 28 | Tensor<[2, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 29 | Tensor<[2, 4096, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 30 | Tensor<[5, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 31 | Tensor<[5, 1024, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 32 | Tensor<[5, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 33 | Tensor<[5, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 34 | Tensor<[8, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 35 | Tensor<[8, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
| 36 | Tensor<[8, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       |     1 |      0 |
### aten.view.default
|     | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|   0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256] | Done     | Done       |     1 |      0 |
|   1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       |     1 |      0 |
|   2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]       | Done     | Done       |     1 |      0 |
|   3 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [256]                  | Done     | Done       |     1 |      0 |
|   4 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | Done       |     1 |      0 |
|   5 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]   | Done     | Done       |     1 |      0 |
|   6 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]    | Done     | Done       |     1 |      0 |
|   7 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]     | Done     | Done       |     1 |      0 |
|   8 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]         | Done     | Done       |     1 |      0 |
|   9 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]   | Done     | Done       |     1 |      0 |
|  10 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1024, 256]         | Done     | Done       |     1 |      0 |
|  11 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]    | Done     | Done       |     1 |      0 |
|  12 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]         | Done     | Done       |     1 |      0 |
|  13 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                   | Done     | Done       |     1 |      0 |
|  14 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384] | Done     | Done       |     1 |      0 |
|  15 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       |     1 |      0 |
|  16 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128] | Done     | Done       |     1 |      0 |
|  17 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]                     | Done     | Done       |     1 |      0 |
|  18 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] size = [1, 256, 256]     | Done     | Done       |     1 |      0 |
|  19 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]    | Done     | Done       |     1 |      0 |
|  20 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]     | Done     | Done       |     1 |      0 |
|  21 | Tensor<[1, 160, 256]> self = ?,<br>List[int] size = [1, 160, 16, 16]     | Done     | Done       |     1 |      0 |
|  22 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]    | Done     | Done       |     1 |      0 |
|  23 | Tensor<[1, 160]> self = ?,<br>List[int] size = [160]                     | Done     | Done       |     1 |      0 |
|  24 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       |     1 |      0 |
|  25 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]       | Done     | Done       |     1 |      0 |
|  26 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Done     | Done       |     1 |      0 |
|  27 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [16384, 256]       | Done     | Done       |     1 |      0 |
|  28 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Done     | Done       |     1 |      0 |
|  29 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]   | Done     | Done       |     1 |      0 |
|  30 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]   | Done     | Done       |     1 |      0 |
|  31 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]         | Done     | Done       |     1 |      0 |
|  32 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]       | Done     | Done       |     1 |      0 |
|  33 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]       | Done     | Done       |     1 |      0 |
|  34 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]   | Done     | Done       |     1 |      0 |
|  35 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]     | Done     | Done       |     1 |      0 |
|  36 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] size = [1, 256, 32]       | Done     | Done       |     1 |      0 |
|  37 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]    | Done     | Done       |     1 |      0 |
|  38 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]         | Done     | Done       |     1 |      0 |
|  39 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16384] | Done     | Done       |     1 |      0 |
|  40 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]     | Done     | Done       |     1 |      0 |
|  41 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]      | Done     | Done       |     1 |      0 |
|  42 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]           | Done     | Done       |     1 |      0 |
|  43 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128] | Done     | Done       |     1 |      0 |
|  44 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]       | Done     | Done       |     1 |      0 |
|  45 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]      | Done     | Done       |     1 |      0 |
|  46 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]     | Done     | Done       |     1 |      0 |
|  47 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]      | Done     | Done       |     1 |      0 |
|  48 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]           | Done     | Done       |     1 |      0 |
|  49 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[int] size = [1, 256, 1024]    | Done     | Done       |     1 |      0 |
|  50 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]       | Done     | Done       |     1 |      0 |
|  51 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]       | Done     | Done       |     1 |      0 |
|  52 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]             | Done     | Done       |     1 |      0 |
|  53 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]    | Done     | Done       |     1 |      0 |
|  54 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]      | Done     | Done       |     1 |      0 |
|  55 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]    | Done     | Done       |     1 |      0 |
|  56 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]       | Done     | Done       |     1 |      0 |
|  57 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]             | Done     | Done       |     1 |      0 |
|  58 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]      | Done     | Done       |     1 |      0 |
|  59 | Tensor<[1, 256]> self = ?,<br>List[int] size = [256]                     | Done     | Done       |     1 |      0 |
|  60 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]   | Done     | Done       |     1 |      0 |
|  61 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | Done       |     1 |      0 |
|  62 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]   | Done     | Done       |     1 |      0 |
|  63 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]       | Done     | Done       |     1 |      0 |
|  64 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 16, 16]       | Done     | Done       |     1 |      0 |
|  65 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] size = [1, 1024, 160]    | Done     | Done       |     1 |      0 |
|  66 | Tensor<[1, 32]> self = ?,<br>List[int] size = [32]                       | Done     | Done       |     1 |      0 |
|  67 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]     | Done     | Done       |     1 |      0 |
|  68 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]         | Done     | Done       |     1 |      0 |
|  69 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]     | Done     | Done       |     1 |      0 |
|  70 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]      | Done     | Done       |     1 |      0 |
|  71 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]           | Done     | Done       |     1 |      0 |
|  72 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]   | Done     | Done       |     1 |      0 |
|  73 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]     | Done     | Done       |     1 |      0 |
|  74 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]       | Done     | Done       |     1 |      0 |
|  75 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]       | Done     | Done       |     1 |      0 |
|  76 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]       | Done     | Done       |     1 |      0 |
|  77 | Tensor<[1, 64, 256]> self = ?,<br>List[int] size = [1, 64, 16, 16]       | Done     | Done       |     1 |      0 |
|  78 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]      | Done     | Done       |     1 |      0 |
|  79 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 4096, 64]      | Done     | Done       |     1 |      0 |
|  80 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]      | Done     | Done       |     1 |      0 |
|  81 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]    | Done     | Done       |     1 |      0 |
|  82 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]    | Done     | Done       |     1 |      0 |
|  83 | Tensor<[1, 640]> self = ?,<br>List[int] size = [640]                     | Done     | Done       |     1 |      0 |
|  84 | Tensor<[1, 64]> self = ?,<br>List[int] size = [64]                       | Done     | Done       |     1 |      0 |
|  85 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]     | Done     | Done       |     1 |      0 |
|  86 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]       | Done     | Done       |     1 |      0 |
|  87 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]       | Done     | Done       |     1 |      0 |
|  88 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]         | Done     | Done       |     1 |      0 |
|  89 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]         | Done     | Done       |     1 |      0 |
|  90 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]         | Done     | Done       |     1 |      0 |
|  91 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]       | Done     | Done       |     1 |      0 |
|  92 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | Done       |     1 |      0 |
|  93 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       |     1 |      0 |
|  94 | Tensor<[2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]       | Done     | Done       |     1 |      0 |
|  95 | Tensor<[2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]       | Done     | Done       |     1 |      0 |
|  96 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Done     | Done       |     1 |      0 |
|  97 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Done     | Done       |     1 |      0 |
|  98 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]         | Done     | Done       |     1 |      0 |
|  99 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]           | Done     | Done       |     1 |      0 |
| 100 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Done       |     1 |      0 |
| 101 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       |     1 |      0 |
| 102 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]             | Done     | Done       |     1 |      0 |
| 103 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]         | Done     | Done       |     1 |      0 |
| 104 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | Done       |     1 |      0 |
| 105 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Done     | Done       |     1 |      0 |
| 106 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Done     | Done       |     1 |      0 |
| 107 | Tensor<[5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]       | Done     | Done       |     1 |      0 |
| 108 | Tensor<[5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]       | Done     | Done       |     1 |      0 |
| 109 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Done     | Done       |     1 |      0 |
| 110 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Done     | Done       |     1 |      0 |
| 111 | Tensor<[8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]       | Done     | Done       |     1 |      0 |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 256, 128, 128],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1, 256, 16, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1, 256, 32, 32],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
|  3 | List[int] size = [1, 256, 64, 64],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |

