# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 32 |          32 |         0 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default                             |                 16 |          16 |         0 |          0 | ✅          |     1   |
|  2 | aten._unsafe_index.Tensor                         |                 14 |           0 |         0 |          0 | ✘           |     0   |
|  3 | aten.add.Tensor                                   |                  6 |           6 |         0 |          0 | ✅          |     1   |
|  4 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  5 | aten.avg_pool2d.default                           |                  5 |           1 |         0 |          0 | 🚧          |     0.2 |
|  6 | aten.cat.default                                  |                 15 |          15 |         0 |          0 | ✅          |     1   |
|  7 | aten.clone.default                                |                  1 |           0 |         1 |          0 | ✅          |     1   |
|  8 | aten.convolution.default                          |                 87 |          87 |         0 |          0 | ✅          |     1   |
|  9 | aten.hardsigmoid.default                          |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 10 | aten.mean.dim                                     |                  7 |           7 |         0 |          0 | ✅          |     1   |
| 11 | aten.mul.Tensor                                   |                 14 |          14 |         0 |          0 | ✅          |     1   |
| 12 | aten.relu.default                                 |                 18 |          18 |         0 |          0 | ✅          |     1   |
| 13 | aten.sigmoid.default                              |                  8 |           8 |         0 |          0 | ✅          |     1   |
| 14 | aten.slice.Tensor                                 |                 45 |           0 |        45 |          0 | ✅          |     1   |
| 15 | aten.slice_scatter.default                        |                 18 |           0 |        18 |          0 | ✅          |     1   |
| 16 | aten.t.default                                    |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 17 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |     1   |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 100, 14, 14]> input = ?,<br>Optional[Tensor]<[100]> weight = ?,<br>Optional[Tensor]<[100]> bias = ?,<br>Tensor<[100]> running_mean = ?,<br>Tensor<[100]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  1 | Tensor<[1, 112, 14, 14]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 112, 7, 7]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999987 |      0 |
|  3 | Tensor<[1, 12, 56, 56]> input = ?,<br>Optional[Tensor]<[12]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>Tensor<[12]> running_mean = ?,<br>Tensor<[12]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      0 |
|  4 | Tensor<[1, 120, 14, 14]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  5 | Tensor<[1, 120, 28, 28]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  6 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999993 |      0 |
|  7 | Tensor<[1, 16, 56, 56]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      0 |
|  8 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999988 |      0 |
|  9 | Tensor<[1, 184, 7, 7]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.99999  |      0 |
| 10 | Tensor<[1, 20, 28, 28]> input = ?,<br>Optional[Tensor]<[20]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>Tensor<[20]> running_mean = ?,<br>Tensor<[20]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      0 |
| 11 | Tensor<[1, 200, 7, 7]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.99999  |      0 |
| 12 | Tensor<[1, 24, 112, 112]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |      0 |
| 13 | Tensor<[1, 24, 28, 28]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      0 |
| 14 | Tensor<[1, 24, 56, 56]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      0 |
| 15 | Tensor<[1, 240, 14, 14]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999992 |      0 |
| 16 | Tensor<[1, 336, 14, 14]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      0 |
| 17 | Tensor<[1, 36, 56, 56]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999992 |      0 |
| 18 | Tensor<[1, 40, 14, 14]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999986 |      0 |
| 19 | Tensor<[1, 40, 28, 28]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999985 |      0 |
| 20 | Tensor<[1, 48, 56, 56]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999992 |      0 |
| 21 | Tensor<[1, 480, 7, 7]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999991 |      0 |
| 22 | Tensor<[1, 56, 14, 14]> input = ?,<br>Optional[Tensor]<[56]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>Tensor<[56]> running_mean = ?,<br>Tensor<[56]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      0 |
| 23 | Tensor<[1, 60, 28, 28]> input = ?,<br>Optional[Tensor]<[60]> weight = ?,<br>Optional[Tensor]<[60]> bias = ?,<br>Tensor<[60]> running_mean = ?,<br>Tensor<[60]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      0 |
| 24 | Tensor<[1, 672, 7, 7]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999986 |      0 |
| 25 | Tensor<[1, 72, 28, 28]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      0 |
| 26 | Tensor<[1, 8, 112, 112]> input = ?,<br>Optional[Tensor]<[8]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>Tensor<[8]> running_mean = ?,<br>Tensor<[8]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999995 |      0 |
| 27 | Tensor<[1, 80, 14, 14]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999992 |      0 |
| 28 | Tensor<[1, 80, 7, 7]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05        | Done     | Done       | 0.999991 |      0 |
| 29 | Tensor<[1, 92, 14, 14]> input = ?,<br>Optional[Tensor]<[92]> weight = ?,<br>Optional[Tensor]<[92]> bias = ?,<br>Tensor<[92]> running_mean = ?,<br>Tensor<[92]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      0 |
| 30 | Tensor<[1, 960, 3, 3]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999975 |      0 |
| 31 | Tensor<[1, 960, 7, 7]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999989 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 184, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 184, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 200, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 200, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 240, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 240, 28, 28]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 480, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
| 10 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
| 11 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
| 12 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[int] dtype = torch.float32   | Done     | Fallback   |     1 |     -1 |
| 13 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Done     | Fallback   |     1 |     -1 |
| 14 | Tensor<[1, 960, 3, 3]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
| 15 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_10] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 184, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_22]   | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 184, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_26]   | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 200, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_18]   | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 240, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_3, _folded__to_copy_14] | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 480, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_30]   | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 672, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_34]   | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 672, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_38]   | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 72, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2]     | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 72, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_6]   | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_42]  | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_46]  | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_50]  | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_13, _folded__to_copy_54]  | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?       | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?     | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     | Done       | 0.999961 |      0 |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | None     | Fallback   | 1        |     -1 |
|  1 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]   | Done     | Done       | 0.999997 |      0 |
|  2 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Fallback   | 1        |     -1 |
|  3 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Fallback   | 1        |     -1 |
|  4 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Fallback   | 1        |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 100, 14, 14]>, <[1, 100, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 12, 56, 56]>, <[1, 12, 56, 56]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[1, 120, 28, 28]>, <[1, 120, 28, 28]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[1, 20, 28, 28]>, <[1, 20, 28, 28]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  4 | List[Tensor] tensors = [<[1, 24, 112, 112]>, <[1, 24, 112, 112]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  5 | List[Tensor] tensors = [<[1, 240, 14, 14]>, <[1, 240, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  6 | List[Tensor] tensors = [<[1, 336, 14, 14]>, <[1, 336, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  7 | List[Tensor] tensors = [<[1, 36, 56, 56]>, <[1, 36, 56, 56]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  8 | List[Tensor] tensors = [<[1, 40, 14, 14]>, <[1, 40, 14, 14]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  9 | List[Tensor] tensors = [<[1, 480, 7, 7]>, <[1, 480, 7, 7]>],<br>int dim = 1       | Done     | Done       |     1 |      0 |
| 10 | List[Tensor] tensors = [<[1, 56, 14, 14]>, <[1, 56, 14, 14]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
| 11 | List[Tensor] tensors = [<[1, 60, 28, 28]>, <[1, 60, 28, 28]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
| 12 | List[Tensor] tensors = [<[1, 8, 112, 112]>, <[1, 8, 112, 112]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
| 13 | List[Tensor] tensors = [<[1, 80, 7, 7]>, <[1, 80, 7, 7]>],<br>int dim = 1         | Done     | Done       |     1 |      0 |
| 14 | List[Tensor] tensors = [<[1, 92, 14, 14]>, <[1, 92, 14, 14]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280]> self = ? | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 100, 14, 14]> input = ?,<br>Tensor<[100, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 100        | Done     | Done       | 0.9999843765865176 | 0      |
|  1 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[112, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 112        | Done     | Done       | 0.9999613824372797 | 0      |
|  2 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[336, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.9999826767229842 | 0      |
|  3 | Tensor<[1, 112, 7, 7]> input = ?,<br>Tensor<[160, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999825518435573 | 0      |
|  4 | Tensor<[1, 112, 7, 7]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999826989051234 | 0      |
|  5 | Tensor<[1, 12, 56, 56]> input = ?,<br>Tensor<[12, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 12           | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999850608697448 | 1      |
|  7 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9999806330595208 | 1      |
|  8 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Done     | Done       | 0.9999898563348938 | 0      |
|  9 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Done     | Done       | 0.9999891231008233 | 0      |
| 10 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Done     | Done       | 0.999983932345007  | 0      |
| 11 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[20, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999802937457608 | 0      |
| 12 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[24, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[8, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 16, 56, 56]> input = ?,<br>Tensor<[24, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999943465900463 | 0      |
| 16 | Tensor<[1, 160, 3, 3]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999764435689773 | 0      |
| 17 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[480, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999769056774708 | 0      |
| 18 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999766749700008 | 0      |
| 19 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9999751264467311 | 1      |
| 20 | Tensor<[1, 184, 14, 14]> input = ?,<br>Tensor<[40, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999725670146475 | 0      |
| 21 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184          | Done     | Done       | 0.9999906012959251 | 0      |
| 22 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184          | Done     | Done       | 0.999990360605569  | 0      |
| 23 | Tensor<[1, 20, 1, 1]> input = ?,<br>Tensor<[72, 20, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9999874238197622 | 1      |
| 24 | Tensor<[1, 20, 28, 28]> input = ?,<br>Tensor<[20, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20           | Done     | Done       | 0.9999820260816584 | 0      |
| 25 | Tensor<[1, 200, 14, 14]> input = ?,<br>Tensor<[40, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999705492407693 | 0      |
| 26 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200          | Done     | Done       | 0.9999902401599909 | 0      |
| 27 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200          | Done     | Done       | 0.9999904367965703 | 0      |
| 28 | Tensor<[1, 24, 112, 112]> input = ?,<br>Tensor<[24, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24         | Done     | Unknown    | N/A                | N/A    |
| 29 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[40, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999910841496739 | 0      |
| 30 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999910277185986 | 0      |
| 31 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[24, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24           | Done     | Done       | 0.9999596873876915 | 0      |
| 32 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[36, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999911441728142 | 0      |
| 33 | Tensor<[1, 240, 1, 1]> input = ?,<br>Tensor<[960, 240, 1, 1]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9999662941857652 | 1      |
| 34 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Done     | Done       | 0.9999897501123023 | 0      |
| 35 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Done     | Done       | 0.9999842298931817 | 0      |
| 36 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Done     | Done       | 0.9999894147676345 | 0      |
| 37 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[40, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999965161194674  | 0      |
| 38 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Done     | Done       | 0.9999833497197307 | 0      |
| 39 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Unknown    | N/A                | N/A    |
| 40 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999895302906877 | 1      |
| 41 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336        | Done     | Done       | 0.9999839485812464 | 0      |
| 42 | Tensor<[1, 36, 56, 56]> input = ?,<br>Tensor<[36, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36           | Done     | Done       | 0.999984175659177  | 0      |
| 43 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999893618297274 | 0      |
| 44 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999989417155817  | 0      |
| 45 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40           | Done     | Done       | 0.9999840395278803 | 0      |
| 46 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[80, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999892931112854 | 0      |
| 47 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999891430693867 | 0      |
| 48 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40           | Done     | Done       | 0.9999829530056702 | 0      |
| 49 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[60, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999889115883299 | 0      |
| 50 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 48         | Done     | Unknown    | N/A                | N/A    |
| 51 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[12, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Unknown    | N/A                | N/A    |
| 52 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9999473077714941 | 1      |
| 53 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[56, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999329732673468 | 0      |
| 54 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | Done     | Done       | 0.9999901941518115 | 0      |
| 55 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | Done     | Done       | 0.999984830731613  | 0      |
| 56 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | Done     | Done       | 0.999990280027587  | 0      |
| 57 | Tensor<[1, 56, 14, 14]> input = ?,<br>Tensor<[56, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 56           | Done     | Done       | 0.9999841383886133 | 0      |
| 58 | Tensor<[1, 60, 28, 28]> input = ?,<br>Tensor<[60, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 60           | Done     | Done       | 0.9999835227568012 | 0      |
| 59 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9999003043954439 | 1      |
| 60 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[56, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999002275163691 | 0      |
| 61 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Done     | Done       | 0.9999622813255052 | 0      |
| 62 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672          | Done     | Done       | 0.999990128467903  | 0      |
| 63 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672          | Done     | Done       | 0.9999902861635462 | 0      |
| 64 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999042152475005 | 0      |
| 65 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9999887935500043 | 1      |
| 66 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999859540675128 | 0      |
| 67 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.9999895846187782 | 0      |
| 68 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.9999894220825064 | 0      |
| 69 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[12, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999848476109477 | 0      |
| 70 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Done     | Done       | 0.9999596843264503 | 0      |
| 71 | Tensor<[1, 8, 112, 112]> input = ?,<br>Tensor<[8, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8            | Done     | Unknown    | N/A                | N/A    |
| 72 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[100, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999861225500501 | 0      |
| 73 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[112, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999858448376922 | 0      |
| 74 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.9999860235317601 | 0      |
| 75 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80           | Done     | Done       | 0.9999837145932566 | 0      |
| 76 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[92, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9999863881543206 | 0      |
| 77 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.9999863709072258 | 0      |
| 78 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.9999859084072771 | 0      |
| 79 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.9999857627979066 | 0      |
| 80 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80             | Done     | Done       | 0.9999837950285207 | 0      |
| 81 | Tensor<[1, 92, 14, 14]> input = ?,<br>Tensor<[92, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 92           | Done     | Done       | 0.9999844739940976 | 0      |
| 82 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[1280, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.9998530752563063 | 1      |
| 83 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[240, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9998628892683098 | 1      |
| 84 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960          | Done     | Done       | 0.999992263019838  | 0      |
| 85 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960          | Done     | Done       | 0.9999924380086703 | 0      |
| 86 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[80, 960, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.9998497527657711 | 0      |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Done     | Done       | 0.99999  |      0 |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | Done     | Done       | 0.999984 |      0 |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | Done     | Done       | 0.999988 |      0 |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | Done     | Done       | 0.999993 |      0 |
|  4 | Tensor<[1, 960, 1, 1]> self = ? | Done     | Done       | 0.999988 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | Done     | Done       | 0.999997 |      0 |
|  5 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  6 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Done     | Done       | 0.999996 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  6 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  8 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  9 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?     | Done     | Done       | 0.999996 |      0 |
| 10 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?     | Done     | Done       | 0.999996 |      0 |
| 11 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     | Done       | 0.999996 |      0 |
| 12 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?     | Done     | Done       | 0.999996 |      0 |
| 13 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?     | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 120, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 120, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1280, 1, 1]> self = ?   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 16, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 168, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 20, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 24, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 240, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 240, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 32, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 336, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 36, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 480, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 60, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 8, 112, 112]> self = ?  | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 92, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 960, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 14, 14]> self = ? | Done     | Done       | 0.999755 |      0 |
|  1 | Tensor<[1, 184, 7, 7]> self = ?   | Done     | Done       | 0.999748 |      0 |
|  2 | Tensor<[1, 200, 7, 7]> self = ?   | Done     | Done       | 0.999759 |      0 |
|  3 | Tensor<[1, 240, 14, 14]> self = ? | Done     | Done       | 0.999756 |      0 |
|  4 | Tensor<[1, 480, 7, 7]> self = ?   | Done     | Done       | 0.999756 |      0 |
|  5 | Tensor<[1, 672, 7, 7]> self = ?   | Done     | Done       | 0.999758 |      0 |
|  6 | Tensor<[1, 72, 28, 28]> self = ?  | Done     | Done       | 0.999755 |      0 |
|  7 | Tensor<[1, 960, 3, 3]> self = ?   | Done     | Done       | 0.99975  |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 15 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 16 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 17 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 18 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 19 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 20 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 21 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 22 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 23 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 24 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 25 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 26 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 27 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
| 28 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
| 29 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
| 30 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 31 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 32 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 33 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 34 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 35 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
| 36 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 37 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 38 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 39 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 40 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 41 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
| 42 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
| 43 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
| 44 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 15 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 16 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
| 17 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1280]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Done     | Done       |     1 |      0 |

