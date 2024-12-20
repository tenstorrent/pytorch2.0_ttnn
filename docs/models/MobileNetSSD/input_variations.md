# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 30 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._unsafe_index.Tensor                         |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default                         |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                                   |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.cat.default                                  |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.clamp.default                                |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.clone.default                                |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.convolution.default                          |                 71 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.div.Tensor                                   |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.exp.default                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default                               |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.hardsigmoid.default                          |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.hardswish.default                            |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.hardtanh.default                             |                 13 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mean.dim                                     |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mul.Tensor                                   |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.new_full.default                             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.permute.default                              |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.relu.default                                 |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.repeat.default                               |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.rsub.Scalar                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.select.int                                   |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.slice.Tensor                                 |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.stack.default                                |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.sub.Tensor                                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.unbind.int                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.unsqueeze.default                            |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.view.default                                 |                 35 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.zeros_like.default                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999986 |      5 |
|  1 | Tensor<[1, 120, 40, 40]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999988 |      5 |
|  2 | Tensor<[1, 128, 1, 1]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999993 |      5 |
|  3 | Tensor<[1, 128, 2, 2]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999981 |      5 |
|  4 | Tensor<[1, 128, 3, 3]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999995 |      5 |
|  5 | Tensor<[1, 128, 5, 5]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999989 |      5 |
|  6 | Tensor<[1, 16, 160, 160]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Unknown  | Done       | 0.99999  |      5 |
|  7 | Tensor<[1, 184, 20, 20]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999988 |      5 |
|  8 | Tensor<[1, 200, 20, 20]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.99999  |      5 |
|  9 | Tensor<[1, 24, 80, 80]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.999991 |      5 |
| 10 | Tensor<[1, 240, 20, 20]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.99999  |      5 |
| 11 | Tensor<[1, 240, 40, 40]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999988 |      5 |
| 12 | Tensor<[1, 256, 10, 10]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999991 |      5 |
| 13 | Tensor<[1, 256, 2, 2]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999985 |      5 |
| 14 | Tensor<[1, 256, 3, 3]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.99999  |      5 |
| 15 | Tensor<[1, 256, 5, 5]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999988 |      5 |
| 16 | Tensor<[1, 40, 40, 40]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.999988 |      5 |
| 17 | Tensor<[1, 480, 10, 10]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999988 |      5 |
| 18 | Tensor<[1, 480, 20, 20]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.99999  |      5 |
| 19 | Tensor<[1, 512, 5, 5]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  | Done       | 0.999991 |      5 |
| 20 | Tensor<[1, 64, 1, 1]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Unknown  | Done       | 0.999989 |      5 |
| 21 | Tensor<[1, 64, 160, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Unknown  | Done       | 0.999989 |      5 |
| 22 | Tensor<[1, 64, 2, 2]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Unknown  | Done       | 0.99998  |      5 |
| 23 | Tensor<[1, 64, 80, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.999992 |      5 |
| 24 | Tensor<[1, 672, 10, 10]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999987 |      5 |
| 25 | Tensor<[1, 672, 20, 20]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Done       | 0.999987 |      5 |
| 26 | Tensor<[1, 72, 40, 40]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.999989 |      5 |
| 27 | Tensor<[1, 72, 80, 80]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.999989 |      5 |
| 28 | Tensor<[1, 80, 10, 10]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.999986 |      5 |
| 29 | Tensor<[1, 80, 20, 20]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Done       | 0.99999  |      5 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_2] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 320, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_3] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 320, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_2] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_3] | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]    | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]  | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]       | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]     | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]   | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91] | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]       | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]     | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]      | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]    | Unknown  | Done       |     1 |     -1 |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                   | Unknown  | Done       |     1 |     -1 |
| 11 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                       | Unknown  | Done       |     1 |     -1 |
| 12 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                   | Unknown  | Done       |     1 |     -1 |
| 13 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                       | Unknown  | Done       |     1 |     -1 |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                      | Unknown  | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  7 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                 | Unknown  | Done       | 0.999998 |      0 |
|  8 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                 | Unknown  | Done       | 0.999998 |      0 |
|  9 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                       | Unknown  | Done       | 0.999998 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 2400, 4]>, <[1, 600, 4]>, <[1, 150, 4]>, <[1, 54, 4]>, <[1, 24, 4]>, <[1, 6, 4]>],<br>int dim = 1       | Unknown  | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 2400, 91]>, <[1, 600, 91]>, <[1, 150, 91]>, <[1, 54, 91]>, <[1, 24, 91]>, <[1, 6, 91]>],<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[150, 2]>, <[150, 2]>],<br>int dim = 1                                                                      | Unknown  | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[24, 2]>, <[24, 2]>],<br>int dim = 1                                                                        | Unknown  | Done       |     1 |      0 |
|  4 | List[Tensor] tensors = [<[2400, 2]>, <[2400, 2]>],<br>int dim = 1                                                                    | Unknown  | Done       |     1 |      0 |
|  5 | List[Tensor] tensors = [<[2400, 4]>, <[600, 4]>, <[150, 4]>, <[54, 4]>, <[24, 4]>, <[6, 4]>]                                         | Unknown  | Done       |     1 |      0 |
|  6 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = -1                                                                   | Unknown  | Done       |     1 |      0 |
|  7 | List[Tensor] tensors = [<[54, 2]>, <[54, 2]>],<br>int dim = 1                                                                        | Unknown  | Done       |     1 |      0 |
|  8 | List[Tensor] tensors = [<[6, 2]>, <[6, 2]>],<br>int dim = 1                                                                          | Unknown  | Done       |     1 |      0 |
|  9 | List[Tensor] tensors = [<[600, 2]>, <[600, 2]>],<br>int dim = 1                                                                      | Unknown  | Done       |     1 |      0 |
### aten.clamp.default
|    | ATen Input Variations                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3234, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[3234, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 320               | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                    | Unknown  | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.999982 |      4 |
|  1 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999979 |      6 |
|  2 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.99998  |      6 |
|  3 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Unknown  | Done       | 0.999959 |      4 |
|  4 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[40, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.99998  |      4 |
|  5 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Unknown  | Done       | 0.999999 |      4 |
|  6 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[24, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999988 |      6 |
|  7 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[546, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999979 |      6 |
|  8 | Tensor<[1, 128, 2, 2]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.99998  |      4 |
|  9 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Unknown  | Done       | 0.999992 |      4 |
| 10 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.99998  |      4 |
| 11 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Unknown  | Done       | 0.999989 |      4 |
| 12 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Unknown  | Done       | 0.999984 |      4 |
| 13 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999994 |      4 |
| 14 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[64, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999994 |      4 |
| 15 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999976 |      6 |
| 16 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184        | Unknown  | Done       | 0.999984 |      4 |
| 17 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[80, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999972 |      4 |
| 18 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200        | Unknown  | Done       | 0.999984 |      4 |
| 19 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[80, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.99997  |      4 |
| 20 | Tensor<[1, 24, 1, 1]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999987 |      6 |
| 21 | Tensor<[1, 24, 80, 80]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999991 |      4 |
| 22 | Tensor<[1, 240, 20, 20]> input = ?,<br>Tensor<[80, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999967 |      4 |
| 23 | Tensor<[1, 240, 40, 40]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Unknown  | Done       | 0.999983 |      4 |
| 24 | Tensor<[1, 256, 10, 10]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256        | Unknown  | Done       | 0.999985 |      4 |
| 25 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999946 |      6 |
| 26 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Unknown  | Done       | 0.999991 |      4 |
| 27 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999973 |      6 |
| 28 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999969 |      4 |
| 29 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999963 |      4 |
| 30 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999968 |      6 |
| 31 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Unknown  | Done       | 0.999988 |      4 |
| 32 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999973 |      6 |
| 33 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999964 |      4 |
| 34 | Tensor<[1, 3, 320, 320]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999981 |      4 |
| 35 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999988 |      6 |
| 36 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999988 |      4 |
| 37 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999988 |      4 |
| 38 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.99994  |      6 |
| 39 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[24, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999932 |      6 |
| 40 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[256, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.999933 |      4 |
| 41 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Unknown  | Done       | 0.999984 |      4 |
| 42 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Unknown  | Done       | 0.999964 |      4 |
| 43 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[546, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.999933 |      6 |
| 44 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[80, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999932 |      4 |
| 45 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[112, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.999934 |      4 |
| 46 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Unknown  | Done       | 0.999984 |      4 |
| 47 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999929 |      4 |
| 48 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[24, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999928 |      6 |
| 49 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512          | Unknown  | Done       | 0.999986 |      4 |
| 50 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[546, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999969 |      6 |
| 51 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  | Done       | 0.999987 |      4 |
| 52 | Tensor<[1, 64, 160, 160]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64         | Unknown  | Done       | 0.999983 |      4 |
| 53 | Tensor<[1, 64, 2, 2]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64             | Unknown  | Done       | 0.999987 |      4 |
| 54 | Tensor<[1, 64, 80, 80]> input = ?,<br>Tensor<[24, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999988 |      4 |
| 55 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999908 |      6 |
| 56 | Tensor<[1, 672, 10, 10]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999903 |      4 |
| 57 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[112, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.999903 |      4 |
| 58 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[24, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999904 |      6 |
| 59 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[546, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.999902 |      6 |
| 60 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Unknown  | Done       | 0.999984 |      4 |
| 61 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Unknown  | Done       | 0.99996  |      4 |
| 62 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999984 |      6 |
| 63 | Tensor<[1, 72, 40, 40]> input = ?,<br>Tensor<[40, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999985 |      4 |
| 64 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999986 |      4 |
| 65 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Unknown  | Done       | 0.999983 |      4 |
| 66 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Unknown  | Done       | 0.999958 |      4 |
| 67 | Tensor<[1, 80, 10, 10]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999986 |      4 |
| 68 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999986 |      4 |
| 69 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999986 |      4 |
| 70 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999986 |      4 |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 1                           | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor self = ?,<br>Tensor other = 10                          | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor self = ?,<br>Tensor other = 2                           | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor self = ?,<br>Tensor other = 20                          | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor self = ?,<br>Tensor other = 3                           | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor self = ?,<br>Tensor other = 5                           | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor self = ?,<br>Tensor other = ?                           | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  | Done       | 0.9999947755701295 | 0      |
|  8 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0             | Unknown  | Done       | 0.9999958121615513 | 0      |
|  9 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0              | Unknown  | Done       | 0.9999958153313703 | 0      |
### aten.exp.default
|    | ATen Input Variations      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3234, 1]> self = ? | Unknown  | Done       | 0.999966 |      0 |
### aten.expand.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10, 10] | Unknown  | Done       |     1 |      2 |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]    | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 20]> self = ?,<br>List[int] size = [20, 20] | Unknown  | Done       |     1 |      2 |
|  3 | Tensor<[1, 2]> self = ?,<br>List[int] size = [2, 2]    | Unknown  | Done       |     1 |      2 |
|  4 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3, 3]    | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 5]> self = ?,<br>List[int] size = [5, 5]    | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10] | Unknown  | Fallback   |     1 |     -1 |
|  7 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  8 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20] | Unknown  | Fallback   |     1 |     -1 |
|  9 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]    | Unknown  | Fallback   |     1 |     -1 |
| 10 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]    | Unknown  | Fallback   |     1 |     -1 |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Unknown  | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | Unknown  | Done       | 0.999983 |      0 |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | Unknown  | Done       | 0.999985 |      0 |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | Unknown  | Done       | 0.999983 |      0 |
### aten.hardswish.default
|    | ATen Input Variations              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 160, 160]> self = ? | Unknown  | Done       | 0.999993 |      0 |
|  1 | Tensor<[1, 184, 20, 20]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  2 | Tensor<[1, 200, 20, 20]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  3 | Tensor<[1, 240, 20, 20]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  4 | Tensor<[1, 240, 40, 40]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  5 | Tensor<[1, 480, 10, 10]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  6 | Tensor<[1, 480, 20, 20]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  7 | Tensor<[1, 672, 10, 10]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  8 | Tensor<[1, 672, 20, 20]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
### aten.hardtanh.default
|    | ATen Input Variations                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 128, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 480, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 512, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 64, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 64, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[1, 672, 20, 20]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  | Done       |     1 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  | Done       | 0.346369 |      0 |
|  1 | Tensor<[1, 480, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  | Done       | 0.321627 |      0 |
|  2 | Tensor<[1, 480, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  | Done       | 0.309661 |      0 |
|  3 | Tensor<[1, 672, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  | Done       | 0.28222  |      0 |
|  4 | Tensor<[1, 672, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  | Done       | 0.32632  |      0 |
|  5 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Unknown  | Done       | 0.335955 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[3234, 1]> other = ?                        | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ? | Unknown  | Done       | 0.9999957119619659 | 0      |
|  2 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?       | Unknown  | Done       | 0.9999958514254714 | 0      |
|  4 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?          | Unknown  | Done       | 0.9999959979153369 | 0      |
|  5 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ? | Unknown  | Done       | 0.9999961590950545 | 0      |
|  6 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ? | Unknown  | Done       | 0.9999959845345281 | 0      |
|  7 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ? | Unknown  | Done       | 0.9999958938499198 | 0      |
|  8 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ? | Unknown  | Done       | 0.9999960073521945 | 0      |
|  9 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?   | Unknown  | Done       | 0.999996571601195  | 0      |
| 10 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                        | Unknown  | Fallback   | 1.0                | -1     |
| 11 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | 0.9999963574110621 | 0      |
| 12 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                      | Unknown  | Done       | 1.0                | 0      |
| 13 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                         | Unknown  | Done       | 1.0                | 0      |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  | Fallback   |     1 |     -1 |
### aten.permute.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Unknown  | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  | Fallback   |     1 |     -1 |
| 10 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
| 11 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ?    | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 120, 40, 40]> self = ?  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 160, 160]> self = ? | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 168, 1, 1]> self = ?    | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 24, 1, 1]> self = ?     | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 32, 1, 1]> self = ?     | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 64, 160, 160]> self = ? | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 64, 80, 80]> self = ?   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 72, 40, 40]> self = ?   | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 72, 80, 80]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                    | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]   | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1] | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1] | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]   | Unknown  | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 1        | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2        | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 3        | Unknown  | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                                    | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  9 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[3234]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Done       | 1.0   | -1     |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Unknown  | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Unknown  | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[300]>, <[300]>, <[300]>, <[300]>],<br>int dim = 1                                                                          | Unknown  | Done       |     1 |      0 |
|  4 | List[Tensor] tensors = [<[3234, 1]>, <[3234, 1]>, <[3234, 1]>, <[3234, 1]>],<br>int dim = 2                                                          | Unknown  | Done       |     1 |      0 |
|  5 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = 2                                                                                    | Unknown  | Done       |     1 |      0 |
|  6 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
|  7 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Unknown  | Done       |     1 |      0 |
|  8 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Unknown  | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  2 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?           | Unknown  | Done       | 0.999998 |      0 |
### aten.unbind.int
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[300, 4]> self = ?,<br>int dim = 1 | Unknown  | Fallback   |     1 |     -4 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[3, 320, 320]> self = ?,<br>int dim = 0 | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[3234]> self = ?,<br>int dim = 1        | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[3]> self = ?,<br>int dim = 1           | Unknown  | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]         | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                          | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]       | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]   | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]       | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]   | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]       | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]       | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]     | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10] | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]     | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20] | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]     | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]     | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                         | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                         | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                     | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]               | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[3234, 2, 2]> self = ?,<br>List[int] size = [3234, 4]               | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros_like.default
|    | ATen Input Variations                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[13685]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  | Fallback   |     1 |     -1 |

