# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._to_copy.default                             |                 12 |           0 |         9 |          0 | 🚧          |    0.75 |
|  2 | aten._unsafe_index.Tensor                         |                  6 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten.add.Tensor                                   |                 12 |           9 |         0 |          0 | 🚧          |    0.75 |
|  4 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.arange.default                               |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.convolution.default                          |                 47 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.mul.Tensor                                   |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.relu.default                                 |                 19 |          19 |         0 |          0 | ✅          |    1    |
| 11 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.unsqueeze.default                            |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
|  3 | Tensor<[1, 144, 7, 7]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Fallback   | True  |
|  4 | Tensor<[1, 18, 14, 14]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
|  5 | Tensor<[1, 18, 28, 28]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
|  6 | Tensor<[1, 18, 56, 56]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
|  7 | Tensor<[1, 18, 7, 7]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | None     | Fallback   | True  |
|  8 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  9 | Tensor<[1, 256, 28, 28]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
| 10 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
| 11 | Tensor<[1, 256, 7, 7]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Fallback   | True  |
| 12 | Tensor<[1, 32, 56, 56]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
| 13 | Tensor<[1, 36, 14, 14]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
| 14 | Tensor<[1, 36, 28, 28]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
| 15 | Tensor<[1, 36, 7, 7]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | None     | Fallback   | True  |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
| 17 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05       | None     | Fallback   | True  |
| 18 | Tensor<[1, 64, 28, 28]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
| 19 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
| 20 | Tensor<[1, 72, 14, 14]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   | True  |
| 21 | Tensor<[1, 72, 7, 7]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | None     | Fallback   | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 18, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 18, 28, 28]> self = ?,<br>Optional[int] dtype = torch.float32  | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 18, 56, 56]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 18, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Fallback   | True  |
|  4 | Tensor<[1, 36, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 36, 28, 28]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Fallback   | True  |
|  6 | Tensor<[1, 36, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Fallback   | True  |
|  7 | Tensor<[1, 72, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  | Fallback   | True  |
|  8 | Tensor<[1, 72, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Removed  | Fallback   | True  |
|  9 | Tensor<[14]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Fallback   | True  |
| 10 | Tensor<[28]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Fallback   | True  |
| 11 | Tensor<[56]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Fallback   | True  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>] | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>] | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>]   | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]   | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?   | Done     | Done       | True  |
|  1 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?     | Done     | Done       | True  |
|  3 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?   | Done     | Done       | True  |
|  4 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ? | Done     | Done       | True  |
|  5 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ? | Done     | Done       | True  |
|  6 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?   | Done     | Done       | True  |
|  7 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ? | Done     | Done       | True  |
|  8 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?   | Done     | Done       | True  |
|  9 | Tensor<[14]> self = ?,<br>Tensor other = 0.0                             | None     | Fallback   | True  |
| 10 | Tensor<[28]> self = ?,<br>Tensor other = 0.0                             | None     | Fallback   | True  |
| 11 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                             | None     | Fallback   | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ? | Done     | Done       | True  |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 14,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  1 | number end = 28,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  2 | number end = 56,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   | PCC   |
|---:|:---------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048]> self = ? | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Fallback   | True  |
|  2 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | Fallback   | True  |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
|  4 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[1024, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Fallback   | True  |
|  5 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[144, 144, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
|  6 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[18, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
|  7 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[256, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
|  8 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[36, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
|  9 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[72, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 10 | Tensor<[1, 18, 14, 14]> input = ?,<br>Tensor<[144, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 11 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 12 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[72, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 13 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[128, 18, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 14 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 15 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 16 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[32, 18, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 17 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[36, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 18 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 19 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[18, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Fallback   | True  |
| 20 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Fallback   | True  |
| 21 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Fallback   | True  |
| 22 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Fallback   | True  |
| 23 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 24 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 25 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[128, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 26 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 27 | Tensor<[1, 36, 14, 14]> input = ?,<br>Tensor<[144, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 28 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[18, 36, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 29 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[256, 36, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 30 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 31 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 32 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[64, 36, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 33 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[72, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 34 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
| 35 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | Fallback   | True  |
| 36 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 37 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 38 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 39 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 40 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 41 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[128, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 42 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[144, 72, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 43 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[18, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 44 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[36, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
| 45 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[512, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | True  |
| 46 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[72, 72, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | None     | Fallback   | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[14]> self = ?,<br>Tensor other = 0.5   | None     | Fallback   | True  |
|  1 | Tensor<[28]> self = ?,<br>Tensor other = 0.25  | None     | Fallback   | True  |
|  2 | Tensor<[28]> self = ?,<br>Tensor other = 0.5   | None     | Fallback   | True  |
|  3 | Tensor<[56]> self = ?,<br>Tensor other = 0.125 | None     | Fallback   | True  |
|  4 | Tensor<[56]> self = ?,<br>Tensor other = 0.25  | None     | Fallback   | True  |
|  5 | Tensor<[56]> self = ?,<br>Tensor other = 0.5   | None     | Fallback   | True  |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?   | Done     | Done       | True  |
|  1 | Tensor<[1, 128, 14, 14]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 128, 56, 56]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 144, 7, 7]> self = ?    | Done     | Done       | True  |
|  4 | Tensor<[1, 18, 14, 14]> self = ?   | Done     | Done       | True  |
|  5 | Tensor<[1, 18, 28, 28]> self = ?   | Done     | Done       | True  |
|  6 | Tensor<[1, 18, 56, 56]> self = ?   | Done     | Done       | True  |
|  7 | Tensor<[1, 2048, 7, 7]> self = ?   | Done     | Done       | True  |
|  8 | Tensor<[1, 256, 28, 28]> self = ?  | Done     | Done       | True  |
|  9 | Tensor<[1, 256, 56, 56]> self = ?  | Done     | Done       | True  |
| 10 | Tensor<[1, 256, 7, 7]> self = ?    | Done     | Done       | True  |
| 11 | Tensor<[1, 32, 56, 56]> self = ?   | Done     | Done       | True  |
| 12 | Tensor<[1, 36, 14, 14]> self = ?   | Done     | Done       | True  |
| 13 | Tensor<[1, 36, 28, 28]> self = ?   | Done     | Done       | True  |
| 14 | Tensor<[1, 512, 14, 14]> self = ?  | Done     | Done       | True  |
| 15 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Done       | True  |
| 16 | Tensor<[1, 64, 28, 28]> self = ?   | Done     | Done       | True  |
| 17 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Done       | True  |
| 18 | Tensor<[1, 72, 14, 14]> self = ?   | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 2048]> self = ? | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[14]> self = ?,<br>int dim = -1 | None     | Fallback   | True  |
|  1 | Tensor<[28]> self = ?,<br>int dim = -1 | None     | Fallback   | True  |
|  2 | Tensor<[56]> self = ?,<br>int dim = -1 | None     | Fallback   | True  |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048] | Done     | Done       | True  |

