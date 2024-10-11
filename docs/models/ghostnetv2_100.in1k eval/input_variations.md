# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 32 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default                             |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_index.Tensor                         |                  8 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                                   |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  4 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.arange.default                               |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.avg_pool2d.default                           |                  5 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.cat.default                                  |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.convolution.default                          |                 87 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.hardsigmoid.default                          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.mean.dim                                     |                  7 |           7 |         0 |          0 | ✅          |       1 |
| 12 | aten.mul.Tensor                                   |                 18 |          18 |         0 |          0 | ✅          |       1 |
| 13 | aten.relu.default                                 |                 18 |          18 |         0 |          0 | ✅          |       1 |
| 14 | aten.sigmoid.default                              |                  8 |           8 |         0 |          0 | ✅          |       1 |
| 15 | aten.slice.Tensor                                 |                 45 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.slice_scatter.default                        |                 18 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.unsqueeze.default                            |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 14, 14]> input = ?,<br>Optional[Tensor]<[100]> weight = ?,<br>Optional[Tensor]<[100]> bias = ?,<br>Tensor<[100]> running_mean = ?,<br>Tensor<[100]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
|  1 | Tensor<[1, 112, 14, 14]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
|  2 | Tensor<[1, 112, 7, 7]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
|  3 | Tensor<[1, 12, 56, 56]> input = ?,<br>Optional[Tensor]<[12]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>Tensor<[12]> running_mean = ?,<br>Tensor<[12]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
|  4 | Tensor<[1, 120, 14, 14]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
|  5 | Tensor<[1, 120, 28, 28]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
|  6 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     |
|  7 | Tensor<[1, 16, 56, 56]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
|  8 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
|  9 | Tensor<[1, 184, 7, 7]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
| 10 | Tensor<[1, 20, 28, 28]> input = ?,<br>Optional[Tensor]<[20]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>Tensor<[20]> running_mean = ?,<br>Tensor<[20]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 11 | Tensor<[1, 200, 7, 7]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
| 12 | Tensor<[1, 24, 112, 112]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     |
| 13 | Tensor<[1, 24, 28, 28]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 14 | Tensor<[1, 24, 56, 56]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 15 | Tensor<[1, 240, 14, 14]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
| 16 | Tensor<[1, 336, 14, 14]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
| 17 | Tensor<[1, 36, 56, 56]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 18 | Tensor<[1, 40, 14, 14]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 19 | Tensor<[1, 40, 28, 28]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 20 | Tensor<[1, 48, 56, 56]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 21 | Tensor<[1, 480, 7, 7]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
| 22 | Tensor<[1, 56, 14, 14]> input = ?,<br>Optional[Tensor]<[56]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>Tensor<[56]> running_mean = ?,<br>Tensor<[56]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 23 | Tensor<[1, 60, 28, 28]> input = ?,<br>Optional[Tensor]<[60]> weight = ?,<br>Optional[Tensor]<[60]> bias = ?,<br>Tensor<[60]> running_mean = ?,<br>Tensor<[60]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 24 | Tensor<[1, 672, 7, 7]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
| 25 | Tensor<[1, 72, 28, 28]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 26 | Tensor<[1, 8, 112, 112]> input = ?,<br>Optional[Tensor]<[8]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>Tensor<[8]> running_mean = ?,<br>Tensor<[8]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     |
| 27 | Tensor<[1, 80, 14, 14]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 28 | Tensor<[1, 80, 7, 7]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05        | None     |
| 29 | Tensor<[1, 92, 14, 14]> input = ?,<br>Optional[Tensor]<[92]> weight = ?,<br>Optional[Tensor]<[92]> bias = ?,<br>Tensor<[92]> running_mean = ?,<br>Tensor<[92]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
| 30 | Tensor<[1, 960, 3, 3]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
| 31 | Tensor<[1, 960, 7, 7]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
### aten._to_copy.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[14]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
|  1 | Tensor<[28]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
|  2 | Tensor<[56]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
|  3 | Tensor<[7]> self = ?,<br>Optional[int] dtype = torch.int64  | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>] | None     |
|  1 | Tensor<[1, 184, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     |
|  2 | Tensor<[1, 200, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     |
|  3 | Tensor<[1, 240, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>] | None     |
|  4 | Tensor<[1, 480, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     |
|  5 | Tensor<[1, 672, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     |
|  6 | Tensor<[1, 72, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]  | None     |
|  7 | Tensor<[1, 960, 3, 3]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[7, 1]>, <[7]>]     | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?   | Done     |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ? | Done     |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?       | Done     |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Done     |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?     | Done     |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?     | Done     |
|  6 | Tensor<[14]> self = ?,<br>Tensor other = 0.0                               | Done     |
|  7 | Tensor<[28]> self = ?,<br>Tensor other = 0.0                               | Done     |
|  8 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                               | Done     |
|  9 | Tensor<[7]> self = ?,<br>Tensor other = 0.0                                | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 14,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     |
|  1 | number end = 28,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     |
|  2 | number end = 56,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     |
|  3 | number end = 7,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | None     |
|  1 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]   | None     |
|  2 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     |
|  3 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     |
|  4 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   |
|---:|:----------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [<[1, 100, 14, 14]>, <[1, 100, 14, 14]>],<br>int dim = 1   | None     |
|  1 | List[Tensor] tensors = [<[1, 12, 56, 56]>, <[1, 12, 56, 56]>],<br>int dim = 1     | None     |
|  2 | List[Tensor] tensors = [<[1, 120, 28, 28]>, <[1, 120, 28, 28]>],<br>int dim = 1   | None     |
|  3 | List[Tensor] tensors = [<[1, 20, 28, 28]>, <[1, 20, 28, 28]>],<br>int dim = 1     | None     |
|  4 | List[Tensor] tensors = [<[1, 24, 112, 112]>, <[1, 24, 112, 112]>],<br>int dim = 1 | None     |
|  5 | List[Tensor] tensors = [<[1, 240, 14, 14]>, <[1, 240, 14, 14]>],<br>int dim = 1   | None     |
|  6 | List[Tensor] tensors = [<[1, 336, 14, 14]>, <[1, 336, 14, 14]>],<br>int dim = 1   | None     |
|  7 | List[Tensor] tensors = [<[1, 36, 56, 56]>, <[1, 36, 56, 56]>],<br>int dim = 1     | None     |
|  8 | List[Tensor] tensors = [<[1, 40, 14, 14]>, <[1, 40, 14, 14]>],<br>int dim = 1     | None     |
|  9 | List[Tensor] tensors = [<[1, 480, 7, 7]>, <[1, 480, 7, 7]>],<br>int dim = 1       | None     |
| 10 | List[Tensor] tensors = [<[1, 56, 14, 14]>, <[1, 56, 14, 14]>],<br>int dim = 1     | None     |
| 11 | List[Tensor] tensors = [<[1, 60, 28, 28]>, <[1, 60, 28, 28]>],<br>int dim = 1     | None     |
| 12 | List[Tensor] tensors = [<[1, 8, 112, 112]>, <[1, 8, 112, 112]>],<br>int dim = 1   | None     |
| 13 | List[Tensor] tensors = [<[1, 80, 7, 7]>, <[1, 80, 7, 7]>],<br>int dim = 1         | None     |
| 14 | List[Tensor] tensors = [<[1, 92, 14, 14]>, <[1, 92, 14, 14]>],<br>int dim = 1     | None     |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 1280]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 14, 14]> input = ?,<br>Tensor<[100, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 100        | None     |
|  1 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[112, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 112        | None     |
|  2 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[336, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
|  3 | Tensor<[1, 112, 7, 7]> input = ?,<br>Tensor<[160, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
|  4 | Tensor<[1, 112, 7, 7]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
|  5 | Tensor<[1, 12, 56, 56]> input = ?,<br>Tensor<[12, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 12           | None     |
|  6 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
|  7 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
|  8 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | None     |
|  9 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | None     |
| 10 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | None     |
| 11 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[20, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 12 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | None     |
| 13 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[24, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 14 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[8, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 15 | Tensor<[1, 16, 56, 56]> input = ?,<br>Tensor<[24, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 16 | Tensor<[1, 160, 3, 3]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 17 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[480, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 18 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 19 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 20 | Tensor<[1, 184, 14, 14]> input = ?,<br>Tensor<[40, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 21 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184          | None     |
| 22 | Tensor<[1, 184, 7, 7]> input = ?,<br>Tensor<[184, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184          | None     |
| 23 | Tensor<[1, 20, 1, 1]> input = ?,<br>Tensor<[72, 20, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 24 | Tensor<[1, 20, 28, 28]> input = ?,<br>Tensor<[20, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20           | None     |
| 25 | Tensor<[1, 200, 14, 14]> input = ?,<br>Tensor<[40, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 26 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200          | None     |
| 27 | Tensor<[1, 200, 7, 7]> input = ?,<br>Tensor<[200, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200          | None     |
| 28 | Tensor<[1, 24, 112, 112]> input = ?,<br>Tensor<[24, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24         | None     |
| 29 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[40, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 30 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 31 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[24, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24           | None     |
| 32 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[36, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 33 | Tensor<[1, 240, 1, 1]> input = ?,<br>Tensor<[960, 240, 1, 1]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 34 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     |
| 35 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     |
| 36 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     |
| 37 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[40, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 38 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | None     |
| 39 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 40 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 41 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336        | None     |
| 42 | Tensor<[1, 36, 56, 56]> input = ?,<br>Tensor<[36, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36           | None     |
| 43 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 44 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 45 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40           | None     |
| 46 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[80, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 47 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 48 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[40, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 40           | None     |
| 49 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[60, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 50 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 48         | None     |
| 51 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[12, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 52 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 53 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[56, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 54 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | None     |
| 55 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | None     |
| 56 | Tensor<[1, 480, 7, 7]> input = ?,<br>Tensor<[480, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480          | None     |
| 57 | Tensor<[1, 56, 14, 14]> input = ?,<br>Tensor<[56, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 56           | None     |
| 58 | Tensor<[1, 60, 28, 28]> input = ?,<br>Tensor<[60, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 60           | None     |
| 59 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 60 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[56, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     |
| 61 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | None     |
| 62 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672          | None     |
| 63 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[672, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672          | None     |
| 64 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 65 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[20]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 66 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[20, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 67 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | None     |
| 68 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[72, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | None     |
| 69 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[12, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 70 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | None     |
| 71 | Tensor<[1, 8, 112, 112]> input = ?,<br>Tensor<[8, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8            | None     |
| 72 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[100, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 73 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[112, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 74 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     |
| 75 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80           | None     |
| 76 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[92, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 77 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     |
| 78 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     |
| 79 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     |
| 80 | Tensor<[1, 80, 7, 7]> input = ?,<br>Tensor<[80, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 80             | None     |
| 81 | Tensor<[1, 92, 14, 14]> input = ?,<br>Tensor<[92, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 92           | None     |
| 82 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[1280, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
| 83 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[240, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 84 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 1, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960          | None     |
| 85 | Tensor<[1, 960, 3, 3]> input = ?,<br>Tensor<[960, 1, 5, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960          | None     |
| 86 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[80, 960, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | None     |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | None     |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | None     |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | None     |
|  4 | Tensor<[1, 960, 1, 1]> self = ? | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Done     |
|  1 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Done     |
|  2 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | Done     |
|  3 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Done     |
|  4 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | Done     |
|  5 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  6 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?   | Done     |
|  1 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ? | Done     |
|  2 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ? | Done     |
|  3 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ? | Done     |
|  4 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ? | Done     |
|  5 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?   | Done     |
|  6 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ? | Done     |
|  7 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?   | Done     |
|  8 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ? | Done     |
|  9 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?     | Done     |
| 10 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?     | Done     |
| 11 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     |
| 12 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?     | Done     |
| 13 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?     | Done     |
| 14 | Tensor<[14]> self = ?,<br>Tensor other = 0.5                             | Done     |
| 15 | Tensor<[28]> self = ?,<br>Tensor other = 0.5                             | Done     |
| 16 | Tensor<[56]> self = ?,<br>Tensor other = 0.5                             | Done     |
| 17 | Tensor<[7]> self = ?,<br>Tensor other = 0.42857142857142855              | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 100, 14, 14]> self = ?  | Done     |
|  1 | Tensor<[1, 120, 1, 1]> self = ?    | Done     |
|  2 | Tensor<[1, 120, 28, 28]> self = ?  | Done     |
|  3 | Tensor<[1, 1280, 1, 1]> self = ?   | Done     |
|  4 | Tensor<[1, 16, 112, 112]> self = ? | Done     |
|  5 | Tensor<[1, 168, 1, 1]> self = ?    | Done     |
|  6 | Tensor<[1, 20, 1, 1]> self = ?     | Done     |
|  7 | Tensor<[1, 24, 112, 112]> self = ? | Done     |
|  8 | Tensor<[1, 240, 1, 1]> self = ?    | Done     |
|  9 | Tensor<[1, 240, 14, 14]> self = ?  | Done     |
| 10 | Tensor<[1, 32, 1, 1]> self = ?     | Done     |
| 11 | Tensor<[1, 336, 14, 14]> self = ?  | Done     |
| 12 | Tensor<[1, 36, 56, 56]> self = ?   | Done     |
| 13 | Tensor<[1, 480, 7, 7]> self = ?    | Done     |
| 14 | Tensor<[1, 60, 28, 28]> self = ?   | Done     |
| 15 | Tensor<[1, 8, 112, 112]> self = ?  | Done     |
| 16 | Tensor<[1, 92, 14, 14]> self = ?   | Done     |
| 17 | Tensor<[1, 960, 7, 7]> self = ?    | Done     |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 120, 14, 14]> self = ? | Done     |
|  1 | Tensor<[1, 184, 7, 7]> self = ?   | Done     |
|  2 | Tensor<[1, 200, 7, 7]> self = ?   | Done     |
|  3 | Tensor<[1, 240, 14, 14]> self = ? | Done     |
|  4 | Tensor<[1, 480, 7, 7]> self = ?   | Done     |
|  5 | Tensor<[1, 672, 7, 7]> self = ?   | Done     |
|  6 | Tensor<[1, 72, 28, 28]> self = ?  | Done     |
|  7 | Tensor<[1, 960, 3, 3]> self = ?   | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  3 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  4 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  5 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  6 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  7 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  8 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  9 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  |
| 10 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  |
| 11 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  |
| 12 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 13 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 14 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 15 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 16 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 17 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 18 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 19 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 20 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 21 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 22 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 23 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 24 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 25 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 26 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 27 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
| 28 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
| 29 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
| 30 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 31 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 32 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 33 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 34 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 35 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
| 36 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 37 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 38 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 39 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 40 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 41 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  |
| 42 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  |
| 43 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  |
| 44 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | None     |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | None     |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | None     |
|  3 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | None     |
|  4 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | None     |
|  5 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | None     |
|  6 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | None     |
|  7 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | None     |
|  8 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | None     |
|  9 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 10 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 11 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 12 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 13 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 14 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 15 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 16 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
| 17 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | None     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ? | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   |
|---:|:---------------------------------------|:---------|
|  0 | Tensor<[14]> self = ?,<br>int dim = -1 | None     |
|  1 | Tensor<[28]> self = ?,<br>int dim = -1 | None     |
|  2 | Tensor<[56]> self = ?,<br>int dim = -1 | None     |
|  3 | Tensor<[7]> self = ?,<br>int dim = -1  | None     |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Done     |

