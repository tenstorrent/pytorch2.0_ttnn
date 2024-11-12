# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 32 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._to_copy.default                             |                 20 |           0 |        16 |          0 | 🚧          |    0.8  |
|  2 | aten._unsafe_index.Tensor                         |                  8 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten.add.Tensor                                   |                 10 |           0 |         0 |          6 | ✘           |    0    |
|  4 | aten.addmm.default                                |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  5 | aten.arange.default                               |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.avg_pool2d.default                           |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.cat.default                                  |                 15 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.convolution.default                          |                 87 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.hardsigmoid.default                          |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.mean.dim                                     |                  7 |           0 |         0 |          7 | ✘           |    0    |
| 12 | aten.mul.Tensor                                   |                 18 |           3 |         0 |         11 | 🚧          |    0.17 |
| 13 | aten.relu.default                                 |                 18 |           2 |         0 |         16 | 🚧          |    0.11 |
| 14 | aten.sigmoid.default                              |                  8 |           0 |         0 |          8 | ✘           |    0    |
| 15 | aten.slice.Tensor                                 |                 45 |           0 |        45 |          0 | ✅          |    1    |
| 16 | aten.slice_scatter.default                        |                 18 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 18 | aten.unsqueeze.default                            |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 100, 14, 14]> input = ?,<br>Optional[Tensor]<[100]> weight = ?,<br>Optional[Tensor]<[100]> bias = ?,<br>Tensor<[100]> running_mean = ?,<br>Tensor<[100]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 112, 14, 14]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 112, 7, 7]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 12, 56, 56]> input = ?,<br>Optional[Tensor]<[12]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>Tensor<[12]> running_mean = ?,<br>Tensor<[12]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 120, 14, 14]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 120, 28, 28]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 16, 56, 56]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
|  8 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
|  9 | Tensor<[1, 184, 7, 7]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
| 10 | Tensor<[1, 20, 28, 28]> input = ?,<br>Optional[Tensor]<[20]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>Tensor<[20]> running_mean = ?,<br>Tensor<[20]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 11 | Tensor<[1, 200, 7, 7]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
| 12 | Tensor<[1, 24, 112, 112]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Unknown    | N/A   |
| 13 | Tensor<[1, 24, 28, 28]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 14 | Tensor<[1, 24, 56, 56]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 15 | Tensor<[1, 240, 14, 14]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
| 16 | Tensor<[1, 336, 14, 14]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
| 17 | Tensor<[1, 36, 56, 56]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 18 | Tensor<[1, 40, 14, 14]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 19 | Tensor<[1, 40, 28, 28]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 20 | Tensor<[1, 48, 56, 56]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 21 | Tensor<[1, 480, 7, 7]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
| 22 | Tensor<[1, 56, 14, 14]> input = ?,<br>Optional[Tensor]<[56]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>Tensor<[56]> running_mean = ?,<br>Tensor<[56]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 23 | Tensor<[1, 60, 28, 28]> input = ?,<br>Optional[Tensor]<[60]> weight = ?,<br>Optional[Tensor]<[60]> bias = ?,<br>Tensor<[60]> running_mean = ?,<br>Tensor<[60]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 24 | Tensor<[1, 672, 7, 7]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
| 25 | Tensor<[1, 72, 28, 28]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 26 | Tensor<[1, 8, 112, 112]> input = ?,<br>Optional[Tensor]<[8]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>Tensor<[8]> running_mean = ?,<br>Tensor<[8]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Unknown    | N/A   |
| 27 | Tensor<[1, 80, 14, 14]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 28 | Tensor<[1, 80, 7, 7]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05        | None     | Unknown    | N/A   |
| 29 | Tensor<[1, 92, 14, 14]> input = ?,<br>Optional[Tensor]<[92]> weight = ?,<br>Optional[Tensor]<[92]> bias = ?,<br>Tensor<[92]> running_mean = ?,<br>Tensor<[92]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
| 30 | Tensor<[1, 960, 3, 3]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
| 31 | Tensor<[1, 960, 7, 7]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 184, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Unknown    | N/A   |
|  3 | Tensor<[1, 184, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Unknown    | N/A   |
|  4 | Tensor<[1, 200, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Unknown    | N/A   |
|  5 | Tensor<[1, 200, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Unknown    | N/A   |
|  6 | Tensor<[1, 240, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Removed  | Unknown    | N/A   |
|  7 | Tensor<[1, 240, 28, 28]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Unknown    | N/A   |
|  8 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Unknown    | N/A   |
|  9 | Tensor<[1, 480, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Unknown    | N/A   |
| 10 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Unknown    | N/A   |
| 11 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Unknown    | N/A   |
| 12 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[int] dtype = torch.float32   | Removed  | Unknown    | N/A   |
| 13 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Removed  | Unknown    | N/A   |
| 14 | Tensor<[1, 960, 3, 3]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Unknown    | N/A   |
| 15 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Removed  | Unknown    | N/A   |
| 16 | Tensor<[14]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   |
| 17 | Tensor<[28]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   |
| 18 | Tensor<[56]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   |
| 19 | Tensor<[7]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Unknown    | N/A   |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 184, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 200, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 240, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>] | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 480, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 672, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 72, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]  | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[7, 1]>, <[7]>]     | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ? | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?       | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?     | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?     | Fallback | Unknown    | N/A   |
|  6 | Tensor<[14]> self = ?,<br>Tensor other = 0.0                               | None     | Unknown    | N/A   |
|  7 | Tensor<[28]> self = ?,<br>Tensor other = 0.0                               | None     | Unknown    | N/A   |
|  8 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                               | None     | Unknown    | N/A   |
|  9 | Tensor<[7]> self = ?,<br>Tensor other = 0.0                                | None     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Fallback | Unknown    | N/A   |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 14,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   |
|  1 | number end = 28,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   |
|  2 | number end = 56,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   |
|  3 | number end = 7,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Unknown    | N/A   |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Unknown    | N/A   |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 100, 14, 14]>, <[1, 100, 14, 14]>],<br>int dim = 1   | None     | Unknown    | N/A   |
|  1 | List[Tensor] tensors = [<[1, 12, 56, 56]>, <[1, 12, 56, 56]>],<br>int dim = 1     | None     | Unknown    | N/A   |
|  2 | List[Tensor] tensors = [<[1, 120, 28, 28]>, <[1, 120, 28, 28]>],<br>int dim = 1   | None     | Unknown    | N/A   |
|  3 | List[Tensor] tensors = [<[1, 20, 28, 28]>, <[1, 20, 28, 28]>],<br>int dim = 1     | None     | Unknown    | N/A   |
|  4 | List[Tensor] tensors = [<[1, 24, 112, 112]>, <[1, 24, 112, 112]>],<br>int dim = 1 | None     | Unknown    | N/A   |
|  5 | List[Tensor] tensors = [<[1, 240, 14, 14]>, <[1, 240, 14, 14]>],<br>int dim = 1   | None     | Unknown    | N/A   |
|  6 | List[Tensor] tensors = [<[1, 336, 14, 14]>, <[1, 336, 14, 14]>],<br>int dim = 1   | None     | Unknown    | N/A   |
|  7 | List[Tensor] tensors = [<[1, 36, 56, 56]>, <[1, 36, 56, 56]>],<br>int dim = 1     | None     | Unknown    | N/A   |
|  8 | List[Tensor] tensors = [<[1, 40, 14, 14]>, <[1, 40, 14, 14]>],<br>int dim = 1     | None     | Unknown    | N/A   |
|  9 | List[Tensor] tensors = [<[1, 480, 7, 7]>, <[1, 480, 7, 7]>],<br>int dim = 1       | None     | Unknown    | N/A   |
| 10 | List[Tensor] tensors = [<[1, 56, 14, 14]>, <[1, 56, 14, 14]>],<br>int dim = 1     | None     | Unknown    | N/A   |
| 11 | List[Tensor] tensors = [<[1, 60, 28, 28]>, <[1, 60, 28, 28]>],<br>int dim = 1     | None     | Unknown    | N/A   |
| 12 | List[Tensor] tensors = [<[1, 8, 112, 112]>, <[1, 8, 112, 112]>],<br>int dim = 1   | None     | Unknown    | N/A   |
| 13 | List[Tensor] tensors = [<[1, 80, 7, 7]>, <[1, 80, 7, 7]>],<br>int dim = 1         | None     | Unknown    | N/A   |
| 14 | List[Tensor] tensors = [<[1, 92, 14, 14]>, <[1, 92, 14, 14]>],<br>int dim = 1     | None     | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   | PCC   |
|---:|:---------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280]> self = ? | Done     | Unknown    | N/A   |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 100, 14, 14]> input = ?,<br>Tensor<[100, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 100        | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[112, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 112        | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[336, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 112, 7, 7]> input = ?,<br>Tensor<[160, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 112, 7, 7]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 12, 56, 56]> input = ?,<br>Tensor<[12, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 12           | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
|  8 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | None     | Unknown    | N/A   |
|  9 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | None     | Unknown    | N/A   |
| 10 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | None     | Unknown    | N/A   |
| 11 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[20, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 12 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | None     | Unknown    | N/A   |
| 13 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[24, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 14 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[8, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 15 | Tensor<[1, 16, 56, 56]> input = ?,<br>Tensor<[24, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 16 | Tensor<[1, 160, 3, 3]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 17 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[480, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 18 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 19 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 20 | Tensor<[1, 184, 14, 14]> input = ?,<br>Tensor<[40, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 21 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184          | None     | Unknown    | N/A   |
| 22 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184          | None     | Unknown    | N/A   |
| 23 | Tensor<[1, 20, 1, 1]> input = ?,<br>Tensor<[72, 20, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Unknown    | N/A   |
| 24 | Tensor<[1, 20, 28, 28]> input = ?,<br>Tensor<[20, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20           | None     | Unknown    | N/A   |
| 25 | Tensor<[1, 200, 14, 14]> input = ?,<br>Tensor<[40, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 26 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200          | None     | Unknown    | N/A   |
| 27 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200          | None     | Unknown    | N/A   |
| 28 | Tensor<[1, 24, 112, 112]> input = ?,<br>Tensor<[24, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24         | None     | Unknown    | N/A   |
| 29 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[40, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 30 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 31 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[24, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24           | None     | Unknown    | N/A   |
| 32 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[36, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 33 | Tensor<[1, 240, 1, 1]> input = ?,<br>Tensor<[960, 240, 1, 1]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 34 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     | Unknown    | N/A   |
| 35 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     | Unknown    | N/A   |
| 36 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     | Unknown    | N/A   |
| 37 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[40, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 38 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     | Unknown    | N/A   |
| 39 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 40 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Unknown    | N/A   |
| 41 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336        | None     | Unknown    | N/A   |
| 42 | Tensor<[1, 36, 56, 56]> input = ?,<br>Tensor<[36, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36           | None     | Unknown    | N/A   |
| 43 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 44 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 45 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40           | None     | Unknown    | N/A   |
| 46 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[80, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 47 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 48 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40           | None     | Unknown    | N/A   |
| 49 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[60, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 50 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 48         | None     | Unknown    | N/A   |
| 51 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[12, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 52 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 53 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[56, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 54 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | None     | Unknown    | N/A   |
| 55 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | None     | Unknown    | N/A   |
| 56 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | None     | Unknown    | N/A   |
| 57 | Tensor<[1, 56, 14, 14]> input = ?,<br>Tensor<[56, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 56           | None     | Unknown    | N/A   |
| 58 | Tensor<[1, 60, 28, 28]> input = ?,<br>Tensor<[60, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 60           | None     | Unknown    | N/A   |
| 59 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 60 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[56, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   |
| 61 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | None     | Unknown    | N/A   |
| 62 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672          | None     | Unknown    | N/A   |
| 63 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672          | None     | Unknown    | N/A   |
| 64 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 65 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Unknown    | N/A   |
| 66 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 67 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | None     | Unknown    | N/A   |
| 68 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | None     | Unknown    | N/A   |
| 69 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[12, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 70 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | None     | Unknown    | N/A   |
| 71 | Tensor<[1, 8, 112, 112]> input = ?,<br>Tensor<[8, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8            | None     | Unknown    | N/A   |
| 72 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[100, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 73 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[112, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 74 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Unknown    | N/A   |
| 75 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80           | None     | Unknown    | N/A   |
| 76 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[92, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
| 77 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Unknown    | N/A   |
| 78 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Unknown    | N/A   |
| 79 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Unknown    | N/A   |
| 80 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80             | None     | Unknown    | N/A   |
| 81 | Tensor<[1, 92, 14, 14]> input = ?,<br>Tensor<[92, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 92           | None     | Unknown    | N/A   |
| 82 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[1280, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Unknown    | N/A   |
| 83 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[240, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 84 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960          | None     | Unknown    | N/A   |
| 85 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960          | None     | Unknown    | N/A   |
| 86 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[80, 960, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Unknown    | N/A   |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 960, 1, 1]> self = ? | None     | Unknown    | N/A   |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Fallback | Unknown    | N/A   |
|  6 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Fallback | Unknown    | N/A   |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ? | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ? | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ? | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?   | Fallback | Unknown    | N/A   |
|  6 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ? | Done     | Unknown    | N/A   |
|  7 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?   | Fallback | Unknown    | N/A   |
|  8 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ? | Fallback | Unknown    | N/A   |
|  9 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?     | Fallback | Unknown    | N/A   |
| 10 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?     | Fallback | Unknown    | N/A   |
| 11 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Fallback | Unknown    | N/A   |
| 12 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?     | Fallback | Unknown    | N/A   |
| 13 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?     | Done     | Unknown    | N/A   |
| 14 | Tensor<[14]> self = ?,<br>Tensor other = 0.5                             | None     | Unknown    | N/A   |
| 15 | Tensor<[28]> self = ?,<br>Tensor other = 0.5                             | None     | Unknown    | N/A   |
| 16 | Tensor<[56]> self = ?,<br>Tensor other = 0.5                             | None     | Unknown    | N/A   |
| 17 | Tensor<[7]> self = ?,<br>Tensor other = 0.42857142857142855              | None     | Unknown    | N/A   |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 100, 14, 14]> self = ?  | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 120, 1, 1]> self = ?    | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 120, 28, 28]> self = ?  | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, 1, 1]> self = ?   | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 16, 112, 112]> self = ? | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 168, 1, 1]> self = ?    | Fallback | Unknown    | N/A   |
|  6 | Tensor<[1, 20, 1, 1]> self = ?     | Fallback | Unknown    | N/A   |
|  7 | Tensor<[1, 24, 112, 112]> self = ? | Fallback | Unknown    | N/A   |
|  8 | Tensor<[1, 240, 1, 1]> self = ?    | Fallback | Unknown    | N/A   |
|  9 | Tensor<[1, 240, 14, 14]> self = ?  | Fallback | Unknown    | N/A   |
| 10 | Tensor<[1, 32, 1, 1]> self = ?     | Fallback | Unknown    | N/A   |
| 11 | Tensor<[1, 336, 14, 14]> self = ?  | Fallback | Unknown    | N/A   |
| 12 | Tensor<[1, 36, 56, 56]> self = ?   | Fallback | Unknown    | N/A   |
| 13 | Tensor<[1, 480, 7, 7]> self = ?    | Fallback | Unknown    | N/A   |
| 14 | Tensor<[1, 60, 28, 28]> self = ?   | Fallback | Unknown    | N/A   |
| 15 | Tensor<[1, 8, 112, 112]> self = ?  | Fallback | Unknown    | N/A   |
| 16 | Tensor<[1, 92, 14, 14]> self = ?   | Fallback | Unknown    | N/A   |
| 17 | Tensor<[1, 960, 7, 7]> self = ?    | Done     | Unknown    | N/A   |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 14, 14]> self = ? | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 184, 7, 7]> self = ?   | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 200, 7, 7]> self = ?   | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 240, 14, 14]> self = ? | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 480, 7, 7]> self = ?   | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 672, 7, 7]> self = ?   | Fallback | Unknown    | N/A   |
|  6 | Tensor<[1, 72, 28, 28]> self = ?  | Fallback | Unknown    | N/A   |
|  7 | Tensor<[1, 960, 3, 3]> self = ?   | Fallback | Unknown    | N/A   |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
|  3 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
|  4 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
|  5 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
|  6 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  7 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  8 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  9 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   |
| 10 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   |
| 11 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   |
| 12 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 13 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 14 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 15 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 16 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 17 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 18 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 19 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 20 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 21 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 22 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 23 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 24 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 25 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 26 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 27 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
| 28 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
| 29 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
| 30 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 31 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 32 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 33 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 34 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 35 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   |
| 36 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 37 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 38 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 39 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 40 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 41 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   |
| 42 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   |
| 43 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   |
| 44 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | None     | Unknown    | N/A   |
|  8 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | None     | Unknown    | N/A   |
|  9 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 10 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 11 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 12 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 13 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 14 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 15 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 16 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
| 17 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 1280]> self = ? | Done     | Unknown    | N/A   |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[14]> self = ?,<br>int dim = -1 | None     | Unknown    | N/A   |
|  1 | Tensor<[28]> self = ?,<br>int dim = -1 | None     | Unknown    | N/A   |
|  2 | Tensor<[56]> self = ?,<br>int dim = -1 | None     | Unknown    | N/A   |
|  3 | Tensor<[7]> self = ?,<br>int dim = -1  | None     | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Done     | Unknown    | N/A   |

