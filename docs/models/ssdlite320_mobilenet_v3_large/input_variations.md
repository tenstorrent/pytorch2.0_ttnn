# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 30 |          30 |         0 |          0 | ✅          |       1 |
|  1 | aten._unsafe_index.Tensor                         |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default                         |                 15 |          15 |         0 |          0 | ✅          |       1 |
|  3 | aten.add.Tensor                                   |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  4 | aten.cat.default                                  |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  5 | aten.clamp.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.clone.default                                |                 15 |           0 |        15 |          0 | ✅          |       1 |
|  7 | aten.convolution.default                          |                 71 |          71 |         0 |          0 | ✅          |       1 |
|  8 | aten.copy.default                                 |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  9 | aten.div.Tensor                                   |                  7 |           7 |         0 |          0 | ✅          |       1 |
| 10 | aten.expand.default                               |                 11 |          10 |         1 |          0 | ✅          |       1 |
| 11 | aten.full.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.hardsigmoid.default                          |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 13 | aten.hardswish.default                            |                  9 |           9 |         0 |          0 | ✅          |       1 |
| 14 | aten.hardtanh.default                             |                 13 |          13 |         0 |          0 | ✅          |       1 |
| 15 | aten.mean.dim                                     |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 16 | aten.mul.Tensor                                   |                 11 |          11 |         0 |          0 | ✅          |       1 |
| 17 | aten.new_full.default                             |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 18 | aten.permute.default                              |                 12 |          12 |         0 |          0 | ✅          |       1 |
| 19 | aten.relu.default                                 |                 10 |          10 |         0 |          0 | ✅          |       1 |
| 20 | aten.repeat.default                               |                  6 |           5 |         1 |          0 | ✅          |       1 |
| 21 | aten.rsub.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 22 | aten.select.int                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 23 | aten.select_scatter.default                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.slice.Tensor                                 |                  4 |           2 |         2 |          0 | ✅          |       1 |
| 25 | aten.stack.default                                |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 26 | aten.sub.Tensor                                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 27 | aten.unsqueeze.default                            |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 28 | aten.view.default                                 |                 33 |          33 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 120, 40, 40]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 128, 1, 1]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999957820762986 | -1     |
|  3 | Tensor<[1, 128, 2, 2]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999900097733684 | -1     |
|  4 | Tensor<[1, 128, 3, 3]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999895744113978 | -1     |
|  5 | Tensor<[1, 128, 5, 5]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999903597993173 | -1     |
|  6 | Tensor<[1, 16, 160, 160]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 184, 20, 20]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 200, 20, 20]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 24, 80, 80]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 240, 20, 20]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 240, 40, 40]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 256, 10, 10]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.9999890892680195 | -1     |
| 13 | Tensor<[1, 256, 2, 2]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999935243950774 | -1     |
| 14 | Tensor<[1, 256, 3, 3]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999915880326641 | -1     |
| 15 | Tensor<[1, 256, 5, 5]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999891610861474 | -1     |
| 16 | Tensor<[1, 40, 40, 40]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 480, 10, 10]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.9999895439421985 | -1     |
| 18 | Tensor<[1, 480, 20, 20]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
| 19 | Tensor<[1, 512, 5, 5]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Done     | Done       | 0.9999871014749222 | -1     |
| 20 | Tensor<[1, 64, 1, 1]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Done     | Done       | 0.9999981750941819 | -1     |
| 21 | Tensor<[1, 64, 160, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Done     | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 64, 2, 2]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Done     | Done       | 0.9999886146507596 | -1     |
| 23 | Tensor<[1, 64, 80, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 672, 10, 10]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999988051481502  | -1     |
| 25 | Tensor<[1, 672, 20, 20]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 72, 40, 40]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 72, 80, 80]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Unknown    | N/A                | N/A    |
| 28 | Tensor<[1, 80, 10, 10]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Done       | 0.9999905698483934 | -1     |
| 29 | Tensor<[1, 80, 20, 20]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Done     | Unknown    | N/A                | N/A    |
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
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]    | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]       | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]     | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]   | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91] | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]       | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]     | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]      | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]    | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                   | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                       | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                   | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                       | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                      | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?   | Done     | Done       | 0.999998 |     -1 |
|  1 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ? | Done     | Done       | 0.999998 |     -1 |
|  2 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?     | Done     | Done       | 0.999998 |     -1 |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?   | Done     | Done       | 0.999998 |     -1 |
|  4 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?     | Done     | Done       | 0.999998 |     -1 |
|  5 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?     | Done     | Done       | 0.999998 |     -1 |
|  6 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?     | Done     | Done       | 0.999998 |     -1 |
|  7 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                 | Done     | Done       | 0.999998 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 2400, 4]>, <[1, 600, 4]>, <[1, 150, 4]>, <[1, 54, 4]>, <[1, 24, 4]>, <[1, 6, 4]>],<br>int dim = 1       | Done     | Done       |     1 |     -1 |
|  1 | List[Tensor] tensors = [<[1, 2400, 91]>, <[1, 600, 91]>, <[1, 150, 91]>, <[1, 54, 91]>, <[1, 24, 91]>, <[1, 6, 91]>],<br>int dim = 1 | Done     | Done       |     1 |     -1 |
|  2 | List[Tensor] tensors = [<[150, 2]>, <[150, 2]>],<br>int dim = 1                                                                      | Done     | Done       |     1 |     -1 |
|  3 | List[Tensor] tensors = [<[24, 2]>, <[24, 2]>],<br>int dim = 1                                                                        | Done     | Done       |     1 |     -1 |
|  4 | List[Tensor] tensors = [<[2400, 2]>, <[2400, 2]>],<br>int dim = 1                                                                    | Done     | Done       |     1 |     -1 |
|  5 | List[Tensor] tensors = [<[2400, 4]>, <[600, 4]>, <[150, 4]>, <[54, 4]>, <[24, 4]>, <[6, 4]>]                                         | Done     | Done       |     1 |     -1 |
|  6 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = -1                                                                   | Done     | Done       |     1 |     -1 |
|  7 | List[Tensor] tensors = [<[54, 2]>, <[54, 2]>],<br>int dim = 1                                                                        | Done     | Done       |     1 |     -1 |
|  8 | List[Tensor] tensors = [<[6, 2]>, <[6, 2]>],<br>int dim = 1                                                                          | Done     | Done       |     1 |     -1 |
|  9 | List[Tensor] tensors = [<[600, 2]>, <[600, 2]>],<br>int dim = 1                                                                      | Done     | Done       |     1 |     -1 |
### aten.clamp.default
|    | ATen Input Variations                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1 | Done     | Done       |     1 |     -1 |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Removed  | Done       |     1 |     -1 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999982 |     -1 |
|  1 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999959 |     -1 |
|  2 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999977 |     -1 |
|  3 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Done     | Done       | 0.999959 |     -1 |
|  4 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[40, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999979 |     -1 |
|  5 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Done       | 0.999996 |     -1 |
|  6 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[24, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999988 |     -1 |
|  7 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[546, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999978 |     -1 |
|  8 | Tensor<[1, 128, 2, 2]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99998  |     -1 |
|  9 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Done       | 0.999992 |     -1 |
| 10 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999981 |     -1 |
| 11 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Done       | 0.99999  |     -1 |
| 12 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Done     | Done       | 0.999983 |     -1 |
| 13 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999992 |     -1 |
| 14 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[64, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999992 |     -1 |
| 15 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999978 |     -1 |
| 16 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184        | Done     | Done       | 0.999984 |     -1 |
| 17 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[80, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999981 |     -1 |
| 18 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200        | Done     | Done       | 0.999984 |     -1 |
| 19 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[80, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999982 |     -1 |
| 20 | Tensor<[1, 24, 1, 1]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999989 |     -1 |
| 21 | Tensor<[1, 24, 80, 80]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999989 |     -1 |
| 22 | Tensor<[1, 240, 20, 20]> input = ?,<br>Tensor<[80, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999981 |     -1 |
| 23 | Tensor<[1, 240, 40, 40]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Done     | Done       | 0.999984 |     -1 |
| 24 | Tensor<[1, 256, 10, 10]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256        | Done     | Done       | 0.999985 |     -1 |
| 25 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.99997  |     -1 |
| 26 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Done     | Done       | 0.99999  |     -1 |
| 27 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999975 |     -1 |
| 28 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999977 |     -1 |
| 29 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999978 |     -1 |
| 30 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999977 |     -1 |
| 31 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Done     | Done       | 0.999988 |     -1 |
| 32 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999972 |     -1 |
| 33 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999976 |     -1 |
| 34 | Tensor<[1, 3, 320, 320]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999981 |     -1 |
| 35 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999991 |     -1 |
| 36 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999988 |     -1 |
| 37 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999988 |     -1 |
| 38 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999969 |     -1 |
| 39 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[24, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999972 |     -1 |
| 40 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[256, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999974 |     -1 |
| 41 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Done     | Done       | 0.999985 |     -1 |
| 42 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Done     | Done       | 0.999964 |     -1 |
| 43 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[546, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999973 |     -1 |
| 44 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[80, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999974 |     -1 |
| 45 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[112, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999974 |     -1 |
| 46 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Done     | Done       | 0.999984 |     -1 |
| 47 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999972 |     -1 |
| 48 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[24, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999968 |     -1 |
| 49 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512          | Done     | Done       | 0.999986 |     -1 |
| 50 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[546, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99997  |     -1 |
| 51 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999985 |     -1 |
| 52 | Tensor<[1, 64, 160, 160]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64         | Done     | Done       | 0.999983 |     -1 |
| 53 | Tensor<[1, 64, 2, 2]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64             | Done     | Done       | 0.99999  |     -1 |
| 54 | Tensor<[1, 64, 80, 80]> input = ?,<br>Tensor<[24, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999986 |     -1 |
| 55 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999975 |     -1 |
| 56 | Tensor<[1, 672, 10, 10]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999971 |     -1 |
| 57 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[112, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99997  |     -1 |
| 58 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[24, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999969 |     -1 |
| 59 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[546, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999969 |     -1 |
| 60 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Done     | Done       | 0.999984 |     -1 |
| 61 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Done     | Done       | 0.999962 |     -1 |
| 62 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999977 |     -1 |
| 63 | Tensor<[1, 72, 40, 40]> input = ?,<br>Tensor<[40, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999986 |     -1 |
| 64 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999986 |     -1 |
| 65 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.999983 |     -1 |
| 66 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.999958 |     -1 |
| 67 | Tensor<[1, 80, 10, 10]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999986 |     -1 |
| 68 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999986 |     -1 |
| 69 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999986 |     -1 |
| 70 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999986 |     -1 |
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
|  6 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     | Done       | 0.9999956698498013 | -1     |
### aten.expand.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10, 10] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]    | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 20]> self = ?,<br>List[int] size = [20, 20] | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2]> self = ?,<br>List[int] size = [2, 2]    | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3, 3]    | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 5]> self = ?,<br>List[int] size = [5, 5]    | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10] | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]    | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20] | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]    | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]    | Done     | Done       |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.float32 | Done     | Unknown    | N/A   | N/A    |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Done     | Done       | 0.999987 |     -1 |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | Done     | Done       | 0.999984 |     -1 |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | Done     | Done       | 0.999981 |     -1 |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | Done     | Done       | 0.999986 |     -1 |
### aten.hardswish.default
|    | ATen Input Variations              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 160, 160]> self = ? | Done     | Done       | 0.999993 |     -1 |
|  1 | Tensor<[1, 184, 20, 20]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  2 | Tensor<[1, 200, 20, 20]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  3 | Tensor<[1, 240, 20, 20]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  4 | Tensor<[1, 240, 40, 40]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  5 | Tensor<[1, 480, 10, 10]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  6 | Tensor<[1, 480, 20, 20]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  7 | Tensor<[1, 672, 10, 10]> self = ?  | Done     | Done       | 0.999993 |     -1 |
|  8 | Tensor<[1, 672, 20, 20]> self = ?  | Done     | Done       | 0.999993 |     -1 |
### aten.hardtanh.default
|    | ATen Input Variations                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 128, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 128, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 128, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 256, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 256, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 256, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 256, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 480, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 512, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[1, 64, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1, 64, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[1, 672, 20, 20]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Done     | Done       |     1 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |     -1 |
|  1 | Tensor<[1, 480, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |     -1 |
|  2 | Tensor<[1, 480, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |     -1 |
|  3 | Tensor<[1, 672, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999995 |     -1 |
|  4 | Tensor<[1, 672, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999995 |     -1 |
|  5 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999994 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ? | Done     | Done       | 0.9999960530641604 | -1     |
|  1 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                 | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?       | Done     | Done       | 0.9999959385031927 | -1     |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?          | Done     | Done       | 0.9999959913433208 | -1     |
|  4 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ? | Done     | Done       | 0.9999960296193582 | -1     |
|  5 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ? | Done     | Done       | 0.999995864435108  | -1     |
|  6 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ? | Done     | Done       | 0.999996037322124  | -1     |
|  7 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ? | Done     | Done       | 0.9999958637149765 | -1     |
|  8 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?   | Done     | Done       | 0.9999959252171917 | -1     |
|  9 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                      | Done     | Done       | 1.0                | -1     |
| 10 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                | N/A    |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |     -1 |
### aten.permute.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |     -1 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ?    | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 120, 40, 40]> self = ?  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 16, 160, 160]> self = ? | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 168, 1, 1]> self = ?    | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 24, 1, 1]> self = ?     | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 32, 1, 1]> self = ?     | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 64, 160, 160]> self = ? | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 64, 80, 80]> self = ?   | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 72, 40, 40]> self = ?   | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 72, 80, 80]> self = ?   | Done     | Done       |     1 |     -1 |
### aten.repeat.default
|    | ATen Input Variations                                    | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]   | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]  | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1] | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]   | Done     | Done       |     1 |     -1 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
### aten.select_scatter.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[3, 320, 320]> src = ?,<br>int dim = 0,<br>int index = 0 | None     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                   | Done     | Done       | 1.0   | -1     |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807 | Done     | Done       | 1.0   | -1     |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Done     | Done       | 1        |     -1 |
|  1 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Done     | Done       | 0.124025 |     -1 |
|  2 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Done     | Done       | 1        |     -1 |
|  3 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Done     | Done       | 1        |     -1 |
|  4 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Done     | Done       | 1        |     -1 |
|  5 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Done     | Done       | 1        |     -1 |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     | Done       | 0.999998 |     -1 |
|  1 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?     | Done     | Done       | 0.999998 |     -1 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[3]> self = ?,<br>int dim = 1           | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]           | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]         | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                          | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]       | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]   | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]       | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]   | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]       | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]       | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]     | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10] | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]     | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20] | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]     | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]     | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                         | Done     | Done       |     1 |     -1 |
| 18 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                         | Done     | Done       |     1 |     -1 |
| 19 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       |     1 |     -1 |
| 20 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       |     1 |     -1 |
| 21 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                         | Done     | Done       |     1 |     -1 |
| 22 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                         | Done     | Done       |     1 |     -1 |
| 23 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                     | Done     | Done       |     1 |     -1 |
| 24 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       |     1 |     -1 |
| 25 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       |     1 |     -1 |
| 26 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       |     1 |     -1 |
| 27 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       |     1 |     -1 |
| 28 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Done     | Done       |     1 |     -1 |
| 29 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Done     | Done       |     1 |     -1 |
| 30 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                          | Done     | Done       |     1 |     -1 |
| 31 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                          | Done     | Done       |     1 |     -1 |
| 32 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Done     | Done       |     1 |     -1 |

