# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._softmax.default                             |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten._to_copy.default                             |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten._unsafe_index.Tensor                         |                 16 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.add.Tensor                                   |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  5 | aten.addmm.default                                |                 15 |           0 |        15 |          0 | ✅          |       1 |
|  6 | aten.bmm.default                                  |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  7 | aten.cat.default                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.clone.default                                |                 21 |           0 |        21 |          0 | ✅          |       1 |
|  9 | aten.convolution.default                          |                 13 |          13 |         0 |          0 | ✅          |       1 |
| 10 | aten.div.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 11 | aten.expand.default                               |                 15 |           0 |        15 |          0 | ✅          |       1 |
| 12 | aten.gelu.default                                 |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 13 | aten.mm.default                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 14 | aten.mul.Tensor                                   |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 15 | aten.native_layer_norm.default                    |                  7 |           7 |         0 |          0 | ✅          |       1 |
| 16 | aten.permute.default                              |                 25 |          25 |         0 |          0 | ✅          |       1 |
| 17 | aten.relu.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.rsub.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 19 | aten.t.default                                    |                 14 |           0 |        14 |          0 | ✅          |       1 |
| 20 | aten.transpose.int                                |                 16 |          16 |         0 |          0 | ✅          |       1 |
| 21 | aten.view.default                                 |                 83 |          83 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      0 |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999595 |      0 |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999593 |      0 |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.99959  |      0 |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999593 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 256, 64, 64]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
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
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?         | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                 | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?         | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?           | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?           | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Removed  | Done       | 0.999974 |      0 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 128]> mat2 = ?   | Removed  | Done       | 0.999988 |      0 |
|  2 | Tensor<[160]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?  | Removed  | Done       | 0.999981 |      0 |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 160]> mat2 = ?  | Removed  | Done       | 0.999968 |      0 |
|  4 | Tensor<[160]> self = ?,<br>Tensor<[256, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?   | Removed  | Done       | 0.999981 |      0 |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Removed  | Done       | 0.999954 |      0 |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Removed  | Done       | 0.999978 |      0 |
|  7 | Tensor<[256]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Removed  | Done       | 0.999985 |      0 |
|  8 | Tensor<[32]> self = ?,<br>Tensor<[16384, 128]> mat1 = ?,<br>Tensor<[128, 32]> mat2 = ?   | Removed  | Done       | 0.999979 |      0 |
|  9 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?     | Removed  | Done       | 0.999988 |      0 |
| 10 | Tensor<[32]> self = ?,<br>Tensor<[256, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?       | Removed  | Done       | 0.999988 |      0 |
| 11 | Tensor<[640]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 640]> mat2 = ?  | Removed  | Done       | 0.999981 |      0 |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[256, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?       | Removed  | Done       | 0.999985 |      0 |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[4096, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Removed  | Done       | 0.999974 |      0 |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Removed  | Done       | 0.999985 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ? | Done     | Done       | 0.999975 |      0 |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?  | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?  | Done     | Done       | 0.999975 |      0 |
|  3 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?   | Done     | Done       | 0.999989 |      0 |
|  4 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?  | Done     | Done       | 0.999975 |      0 |
|  5 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?   | Done     | Done       | 0.99999  |      0 |
|  6 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
|  7 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?    | Done     | Done       | 0.999989 |      0 |
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
| 12 | Tensor<[1, 256, 256]> self = ?                                                               | Removed  | Done       |     1 |      0 |
| 13 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 14 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
| 15 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
| 16 | Tensor<[1, 4096, 256]> self = ?                                                              | Removed  | Done       |     1 |      0 |
| 17 | Tensor<[1, 4096, 64]> self = ?                                                               | Removed  | Done       |     1 |      0 |
| 18 | Tensor<[1, 5, 1024, 256]> self = ?                                                           | Removed  | Done       |     1 |      0 |
| 19 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 20 | Tensor<[1, 8, 256, 256]> self = ?                                                            | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999839 |      0 |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Done     | Done       | 0.999984 |      1 |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Done     | Done       | 0.999984 |      1 |
|  3 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999907 |      1 |
|  4 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999756 |      1 |
|  5 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999964 |      1 |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | Done     | Done       | 0.999983 |      1 |
|  7 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999899 |      1 |
|  8 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999596 |      1 |
|  9 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.99996  |      1 |
| 10 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999918 |      1 |
| 11 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999837 |      1 |
| 12 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | Done     | Done       | 0.999983 |      1 |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.999996 |      0 |
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
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 640]> self = ?  | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 16384, 128]> self = ? | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 256, 1024]> self = ?  | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 4096, 256]> self = ?  | Done     | Done       | 0.999991 |      0 |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ? | Done     | Done       | 0.999982 |      0 |
|  1 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?  | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?  | Done     | Done       | 0.99998  |      0 |
|  3 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?   | Done     | Done       | 0.999986 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?           | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     | Done       | 0.9999961335672274 | 0      |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?    | Done     | Done       | 0.9999961099507492 | 0      |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.999369 |      3 |
|  1 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | 0.999899 |      3 |
|  2 | Tensor<[1, 256, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.999466 |      3 |
|  3 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.999173 |      3 |
|  4 | Tensor<[1, 256, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | 0.999893 |      3 |
|  5 | Tensor<[1, 256, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | 0.999803 |      3 |
|  6 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | 0.999795 |      3 |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 19 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 20 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 21 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 22 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 23 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]   | Done     | Done       |     1 |      0 |
| 24 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 128, 128]> self = ? | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 256]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[128, 32]> self = ?   | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[160, 160]> self = ?  | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[160, 640]> self = ?  | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[256, 1024]> self = ? | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[256, 160]> self = ?  | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[256, 256]> self = ?  | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[256, 32]> self = ?   | Removed  | Done       |     1 |      0 |
|  8 | Tensor<[256, 64]> self = ?   | Removed  | Done       |     1 |      0 |
|  9 | Tensor<[32, 128]> self = ?   | Removed  | Done       |     1 |      0 |
| 10 | Tensor<[32, 32]> self = ?    | Removed  | Done       |     1 |      0 |
| 11 | Tensor<[64, 256]> self = ?   | Removed  | Done       |     1 |      0 |
| 12 | Tensor<[64, 64]> self = ?    | Removed  | Done       |     1 |      0 |
| 13 | Tensor<[640, 160]> self = ?  | Removed  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256] | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]       | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]     | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]         | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]   | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]    | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]         | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384] | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128] | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]    | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]     | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]    | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]       | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Done     | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Done     | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]   | Done     | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]   | Done     | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]         | Done     | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]       | Done     | Done       | 1.0   | 0      |
| 24 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]       | Done     | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]   | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]     | Done     | Done       | 1.0   | 0      |
| 27 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]    | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]         | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]     | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]      | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]           | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128] | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]      | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]     | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]      | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]           | Done     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]       | Done     | Done       | 1.0   | 0      |
| 38 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]             | Done     | Done       | 1.0   | 0      |
| 39 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]    | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]    | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]       | Done     | Done       | 1.0   | 0      |
| 42 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]             | Done     | Done       | 1.0   | 0      |
| 43 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]      | Done     | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]   | Done     | Done       | 1.0   | 0      |
| 45 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | Done       | 1.0   | 0      |
| 46 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]   | Done     | Done       | 1.0   | 0      |
| 47 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]     | Done     | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]         | Done     | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]     | Done     | Done       | 1.0   | 0      |
| 50 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]      | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]           | Done     | Done       | 1.0   | 0      |
| 52 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]   | Done     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]     | Done     | Unknown    | N/A   | N/A    |
| 54 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]       | Done     | Unknown    | N/A   | N/A    |
| 55 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]       | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]       | Done     | Done       | 1.0   | 0      |
| 57 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]      | Done     | Done       | 1.0   | 0      |
| 58 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]      | Done     | Done       | 1.0   | 0      |
| 59 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]    | Done     | Unknown    | N/A   | N/A    |
| 60 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]    | Done     | Unknown    | N/A   | N/A    |
| 61 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]     | Done     | Unknown    | N/A   | N/A    |
| 62 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]       | Done     | Unknown    | N/A   | N/A    |
| 63 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]       | Done     | Unknown    | N/A   | N/A    |
| 64 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]         | Done     | Unknown    | N/A   | N/A    |
| 65 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]         | Done     | Unknown    | N/A   | N/A    |
| 66 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]         | Done     | Unknown    | N/A   | N/A    |
| 67 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]       | Done     | Done       | 1.0   | 0      |
| 68 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | Unknown    | N/A   | N/A    |
| 69 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | 0      |
| 70 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Done     | Done       | 1.0   | 0      |
| 71 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Done     | Done       | 1.0   | 0      |
| 72 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]         | Done     | Unknown    | N/A   | N/A    |
| 73 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]           | Done     | Unknown    | N/A   | N/A    |
| 74 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Unknown    | N/A   | N/A    |
| 75 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | 1.0   | 0      |
| 76 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]             | Done     | Done       | 1.0   | 0      |
| 77 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]         | Done     | Unknown    | N/A   | N/A    |
| 78 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | Done       | 1.0   | 0      |
| 79 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Done     | Unknown    | N/A   | N/A    |
| 80 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Done     | Unknown    | N/A   | N/A    |
| 81 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Done     | Unknown    | N/A   | N/A    |
| 82 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Done     | Unknown    | N/A   | N/A    |

