# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 30 |          30 |         0 |          0 | ✅          |       1 |
|  1 | aten._unsafe_index.Tensor                         |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default                         |                 15 |          15 |         0 |          0 | ✅          |       1 |
|  3 | aten.add.Tensor                                   |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  4 | aten.cat.default                                  |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  5 | aten.clamp.default                                |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  6 | aten.clone.default                                |                 15 |           0 |        15 |          0 | ✅          |       1 |
|  7 | aten.convolution.default                          |                 71 |          71 |         0 |          0 | ✅          |       1 |
|  8 | aten.copy.default                                 |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  9 | aten.div.Tensor                                   |                 10 |          10 |         0 |          0 | ✅          |       1 |
| 10 | aten.exp.default                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.expand.default                               |                 11 |          10 |         1 |          0 | ✅          |       1 |
| 12 | aten.full.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.hardsigmoid.default                          |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 14 | aten.hardswish.default                            |                  9 |           9 |         0 |          0 | ✅          |       1 |
| 15 | aten.hardtanh.default                             |                 13 |          13 |         0 |          0 | ✅          |       1 |
| 16 | aten.mean.dim                                     |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 17 | aten.mul.Tensor                                   |                 15 |          15 |         0 |          0 | ✅          |       1 |
| 18 | aten.new_full.default                             |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 19 | aten.permute.default                              |                 12 |          12 |         0 |          0 | ✅          |       1 |
| 20 | aten.relu.default                                 |                 10 |          10 |         0 |          0 | ✅          |       1 |
| 21 | aten.repeat.default                               |                  6 |           5 |         1 |          0 | ✅          |       1 |
| 22 | aten.rsub.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 23 | aten.select.int                                   |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 24 | aten.select_scatter.default                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.slice.Tensor                                 |                 11 |           8 |         3 |          0 | ✅          |       1 |
| 26 | aten.stack.default                                |                  9 |           9 |         0 |          0 | ✅          |       1 |
| 27 | aten.sub.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 28 | aten.unbind.int                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.unsqueeze.default                            |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 30 | aten.view.default                                 |                 35 |          35 |         0 |          0 | ✅          |       1 |
| 31 | aten.zeros_like.default                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999983 |      0 |
|  1 | Tensor<[1, 120, 40, 40]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999987 |      0 |
|  2 | Tensor<[1, 128, 1, 1]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.99999  |      0 |
|  3 | Tensor<[1, 128, 2, 2]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999992 |      0 |
|  4 | Tensor<[1, 128, 3, 3]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999991 |      0 |
|  5 | Tensor<[1, 128, 5, 5]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999994 |      0 |
|  6 | Tensor<[1, 16, 160, 160]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Done     | Done       | 0.999992 |      0 |
|  7 | Tensor<[1, 184, 20, 20]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999989 |      0 |
|  8 | Tensor<[1, 200, 20, 20]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999989 |      0 |
|  9 | Tensor<[1, 24, 80, 80]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.99999  |      0 |
| 10 | Tensor<[1, 240, 20, 20]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999989 |      0 |
| 11 | Tensor<[1, 240, 40, 40]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.99999  |      0 |
| 12 | Tensor<[1, 256, 10, 10]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.99999  |      0 |
| 13 | Tensor<[1, 256, 2, 2]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999987 |      0 |
| 14 | Tensor<[1, 256, 3, 3]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999988 |      0 |
| 15 | Tensor<[1, 256, 5, 5]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999992 |      0 |
| 16 | Tensor<[1, 40, 40, 40]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.999989 |      0 |
| 17 | Tensor<[1, 480, 10, 10]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      0 |
| 18 | Tensor<[1, 480, 20, 20]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      0 |
| 19 | Tensor<[1, 512, 5, 5]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.999989 |      0 |
| 20 | Tensor<[1, 64, 1, 1]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Done     | Done       | 0.999984 |      0 |
| 21 | Tensor<[1, 64, 160, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Done     | Done       | 0.999992 |      0 |
| 22 | Tensor<[1, 64, 2, 2]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Done     | Done       | 0.999994 |      0 |
| 23 | Tensor<[1, 64, 80, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.999993 |      0 |
| 24 | Tensor<[1, 672, 10, 10]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      0 |
| 25 | Tensor<[1, 672, 20, 20]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999989 |      0 |
| 26 | Tensor<[1, 72, 40, 40]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.999991 |      0 |
| 27 | Tensor<[1, 72, 80, 80]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.99999  |      0 |
| 28 | Tensor<[1, 80, 10, 10]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.999989 |      0 |
| 29 | Tensor<[1, 80, 20, 20]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.999992 |      0 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_2] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_3] | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_2] | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_3] | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]       | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91] | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]       | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]     | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]      | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                       | Done     | Done       |     1 |      0 |
| 12 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                       | Done     | Done       |     1 |      0 |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                      | Done     | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?   | Done     | Done       | 0.9999980798061244 | 0      |
|  1 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ? | Done     | Done       | 0.9999979973720009 | 0      |
|  2 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?     | Done     | Done       | 0.9999980142731272 | 0      |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?   | Done     | Done       | 0.9999979879318891 | 0      |
|  4 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?     | Done     | Done       | 0.9999980041334185 | 0      |
|  5 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?     | Done     | Done       | 0.9999979458200444 | 0      |
|  6 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?     | Done     | Done       | 0.9999979842981962 | 0      |
|  7 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                 | Done     | Done       | 0.9999980481524241 | 0      |
|  9 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                       | Done     | Unknown    | N/A                | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 2400, 4]>, <[1, 600, 4]>, <[1, 150, 4]>, <[1, 54, 4]>, <[1, 24, 4]>, <[1, 6, 4]>],<br>int dim = 1       | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 2400, 91]>, <[1, 600, 91]>, <[1, 150, 91]>, <[1, 54, 91]>, <[1, 24, 91]>, <[1, 6, 91]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[150, 2]>, <[150, 2]>],<br>int dim = 1                                                                      | Done     | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[24, 2]>, <[24, 2]>],<br>int dim = 1                                                                        | Done     | Done       |     1 |      0 |
|  4 | List[Tensor] tensors = [<[2400, 2]>, <[2400, 2]>],<br>int dim = 1                                                                    | Done     | Done       |     1 |      0 |
|  5 | List[Tensor] tensors = [<[2400, 4]>, <[600, 4]>, <[150, 4]>, <[54, 4]>, <[24, 4]>, <[6, 4]>]                                         | Done     | Done       |     1 |      0 |
|  6 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = -1                                                                   | Done     | Done       |     1 |      0 |
|  7 | List[Tensor] tensors = [<[54, 2]>, <[54, 2]>],<br>int dim = 1                                                                        | Done     | Done       |     1 |      0 |
|  8 | List[Tensor] tensors = [<[6, 2]>, <[6, 2]>],<br>int dim = 1                                                                          | Done     | Done       |     1 |      0 |
|  9 | List[Tensor] tensors = [<[600, 2]>, <[600, 2]>],<br>int dim = 1                                                                      | Done     | Done       |     1 |      0 |
### aten.clamp.default
|    | ATen Input Variations                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3234, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3234, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 320               | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                    | Done     | Done       | 1.0   | 0      |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       |     1 |      0 |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
| 10 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       |     1 |      0 |
| 11 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Removed  | Done       |     1 |      0 |
| 12 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       |     1 |      0 |
| 13 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Removed  | Done       |     1 |      0 |
| 14 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999794476691413 | 1      |
|  2 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Done     | Done       | 0.99995928734061   | 0      |
|  4 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[40, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999805714470664 | 0      |
|  5 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[24, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[546, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 128, 2, 2]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Done     | Done       | 0.9999832274668431 | 0      |
| 13 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999943637024178 | 0      |
| 14 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[64, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999942995268889 | 0      |
| 15 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184        | Done     | Done       | 0.9999839207738052 | 0      |
| 17 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[80, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999729519222529 | 0      |
| 18 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200        | Done     | Done       | 0.9999837539332482 | 0      |
| 19 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[80, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999707418692827 | 0      |
| 20 | Tensor<[1, 24, 1, 1]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9999923228772689 | 1      |
| 21 | Tensor<[1, 24, 80, 80]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999912030497947 | 0      |
| 22 | Tensor<[1, 240, 20, 20]> input = ?,<br>Tensor<[80, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999669772055025 | 0      |
| 23 | Tensor<[1, 240, 40, 40]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Done     | Done       | 0.9999839367842367 | 0      |
| 24 | Tensor<[1, 256, 10, 10]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256        | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Done     | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 28 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Unknown    | N/A                | N/A    |
| 29 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
| 30 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 31 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Done     | Unknown    | N/A                | N/A    |
| 32 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 33 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
| 34 | Tensor<[1, 3, 320, 320]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999813818884336 | 0      |
| 35 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999909811638873 | 1      |
| 36 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999890547952387 | 0      |
| 37 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999891236554975 | 0      |
| 38 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9999376935912438 | 1      |
| 39 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[24, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 40 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[256, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A                | N/A    |
| 41 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Done     | Unknown    | N/A                | N/A    |
| 42 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Done     | Unknown    | N/A                | N/A    |
| 43 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[546, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
| 44 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[80, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A                | N/A    |
| 45 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[112, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A                | N/A    |
| 46 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Done     | Done       | 0.9999834315584281 | 0      |
| 47 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
| 48 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[24, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 49 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512          | Done     | Unknown    | N/A                | N/A    |
| 50 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[546, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 51 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Unknown    | N/A                | N/A    |
| 52 | Tensor<[1, 64, 160, 160]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64         | Done     | Done       | 0.999983018504133  | 0      |
| 53 | Tensor<[1, 64, 2, 2]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64             | Done     | Unknown    | N/A                | N/A    |
| 54 | Tensor<[1, 64, 80, 80]> input = ?,<br>Tensor<[24, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999875321055536 | 0      |
| 55 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 56 | Tensor<[1, 672, 10, 10]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A                | N/A    |
| 57 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[112, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A                | N/A    |
| 58 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[24, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 59 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[546, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
| 60 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Done     | Unknown    | N/A                | N/A    |
| 61 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Done     | Unknown    | N/A                | N/A    |
| 62 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9999828861744828 | 1      |
| 63 | Tensor<[1, 72, 40, 40]> input = ?,<br>Tensor<[40, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999855043561643 | 0      |
| 64 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999855515160457 | 0      |
| 65 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.9999829269515896 | 0      |
| 66 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.9999582945127763 | 0      |
| 67 | Tensor<[1, 80, 10, 10]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
| 68 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999859318291879 | 0      |
| 69 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999859512713646 | 0      |
| 70 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999986008356113  | 0      |
### aten.copy.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 320, 320]> src = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor self = ?,<br>Tensor other = 10                          | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor self = ?,<br>Tensor other = 20                          | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor self = ?,<br>Tensor other = 3                           | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor self = ?,<br>Tensor other = 5                           | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor self = ?,<br>Tensor other = ?                           | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     | Done       | 0.9999967045891478 | 0      |
|  8 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0             | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0              | Done     | Unknown    | N/A                | N/A    |
### aten.exp.default
|    | ATen Input Variations      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3234, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10, 10] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]    | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 20]> self = ?,<br>List[int] size = [20, 20] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2]> self = ?,<br>List[int] size = [2, 2]    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3, 3]    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 5]> self = ?,<br>List[int] size = [5, 5]    | Done     | Done       |     1 |      0 |
|  6 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10] | Done     | Done       |     1 |      0 |
|  7 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]    | Done     | Done       |     1 |      0 |
|  8 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20] | Done     | Done       |     1 |      0 |
|  9 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]    | Done     | Done       |     1 |      0 |
### aten.full.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.float32 | Done     | Unknown    | N/A   | N/A    |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Done     | Done       | 0.999969 |      0 |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | Done     | Done       | 0.999963 |      0 |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | Done     | Done       | 0.999961 |      0 |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | Done     | Done       | 0.999957 |      0 |
### aten.hardswish.default
|    | ATen Input Variations              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 160, 160]> self = ? | Done     | Done       | 0.999994 |      0 |
|  1 | Tensor<[1, 184, 20, 20]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  2 | Tensor<[1, 200, 20, 20]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  3 | Tensor<[1, 240, 20, 20]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  4 | Tensor<[1, 240, 40, 40]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  5 | Tensor<[1, 480, 10, 10]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  6 | Tensor<[1, 480, 20, 20]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  7 | Tensor<[1, 672, 10, 10]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  8 | Tensor<[1, 672, 20, 20]> self = ?  | Done     | Done       | 0.999994 |      0 |
### aten.hardtanh.default
|    | ATen Input Variations                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 128, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 480, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 512, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 64, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 64, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 672, 20, 20]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Done     | Done       |     1 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |      0 |
|  1 | Tensor<[1, 480, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 480, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 672, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |      0 |
|  4 | Tensor<[1, 672, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999998 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[3234, 1]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ? | Done     | Done       | 0.9999957604812811 | 0      |
|  2 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                 | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?       | Done     | Done       | 0.9999958434315228 | 0      |
|  4 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?          | Done     | Done       | 0.9999960036647445 | 0      |
|  5 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ? | Done     | Done       | 0.9999960952350109 | 0      |
|  6 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ? | Done     | Done       | 0.9999959414402644 | 0      |
|  7 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ? | Done     | Done       | 0.9999958528525971 | 0      |
|  8 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ? | Done     | Done       | 0.9999959783494172 | 0      |
|  9 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?   | Done     | Done       | 0.9999962078702594 | 0      |
| 10 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                      | Done     | Done       | 1.0                | 0      |
| 13 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                         | Done     | Unknown    | N/A                | N/A    |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 120, 40, 40]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 160, 160]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 168, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 24, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 32, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 64, 160, 160]> self = ? | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 64, 80, 80]> self = ?   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 72, 40, 40]> self = ?   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 72, 80, 80]> self = ?   | Done     | Done       |     1 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                    | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]   | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1] | Done     | Done       |     1 |      0 |
|  5 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]   | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 1        | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2        | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 3        | Done     | Unknown    | N/A   | N/A    |
### aten.select_scatter.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[3, 320, 320]> src = ?,<br>int dim = 0,<br>int index = 0 | None     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                             | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                                    | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807                  | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[3234]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Done     | Done       | 1.0   | 0      |
|  2 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Done     | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[300]>, <[300]>, <[300]>, <[300]>],<br>int dim = 1                                                                          | Done     | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[3234, 1]>, <[3234, 1]>, <[3234, 1]>, <[3234, 1]>],<br>int dim = 2                                                          | Done     | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = 2                                                                                    | Done     | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
|  7 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Done     | Done       | 1.0   | 0      |
|  8 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Done     | Done       | 1.0   | 0      |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     | Done       | 0.9999976840590764 | 0      |
|  1 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?     | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?     | Done     | Done       | 0.9999980133720862 | 0      |
|  3 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?           | Done     | Unknown    | N/A                | N/A    |
### aten.unbind.int
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[300, 4]> self = ?,<br>int dim = 1 | None     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[3234]> self = ?,<br>int dim = 1        | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[3]> self = ?,<br>int dim = 1           | Done     | Done       | 1.0   | 0      |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]           | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]         | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                          | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]       | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]   | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]       | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]   | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]       | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]       | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]     | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10] | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]     | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20] | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]     | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]     | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Done     | Done       | 1.0   | 0      |
| 17 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                         | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                         | Done     | Done       | 1.0   | 0      |
| 19 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       | 1.0   | 0      |
| 20 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       | 1.0   | 0      |
| 21 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                         | Done     | Done       | 1.0   | 0      |
| 22 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                         | Done     | Done       | 1.0   | 0      |
| 23 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                     | Done     | Done       | 1.0   | 0      |
| 24 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       | 1.0   | 0      |
| 25 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]               | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[3234, 2, 2]> self = ?,<br>List[int] size = [3234, 4]               | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       | 1.0   | 0      |
| 29 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       | 1.0   | 0      |
| 30 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Done     | Done       | 1.0   | 0      |
| 31 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Done     | Done       | 1.0   | 0      |
| 32 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       | 1.0   | 0      |
| 33 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       | 1.0   | 0      |
| 34 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Done     | Done       | 1.0   | 0      |
### aten.zeros_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[8381]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |

