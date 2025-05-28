# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.add.Tensor                                   |                  7 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.cat.default                                  |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.clone.default                                |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.convolution.default                          |                 28 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.mul.Tensor                                   |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.permute.default                              |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.pow.Tensor_Scalar                            |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.select.int                                   |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.sigmoid.default                              |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.silu.default                                 |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.split_with_sizes.default                     |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.view.default                                 |                  6 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 128, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 128, s1, s2]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                               | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 256, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 256, s0, s1]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                               | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 256, s1, s2]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                               | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                                  | Unknown  | Done       | 0.9999890755655048 | 0      |
|  6 | Tensor<[1, 32, s0, s1]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                                    | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 512, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 512, s1, s2]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                               | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 64, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 64, s0, s1]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                                    | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 64, s1, s2]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001                                    | Unknown  | Unknown    | N/A                | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128, s1, s2]> self = ?,<br>Tensor<[1, 128, s1, s2]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, s1, s2]> self = ?,<br>Tensor<[1, 256, s1, s2]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, s0, s1]> self = ?,<br>Tensor<[1, 32, s0, s1]> other = ?     | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, s1, s2]> self = ?,<br>Tensor<[1, 64, s1, s2]> other = ?     | Unknown  | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 12288, 85]>, <[1, 3072, 85]>, <[1, 768, 85]>],<br>int dim = 1              | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 128, s1, s2]>, <[1, 128, s1, s2]>],<br>int dim = 1                         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 256, 32, 32]>, <[1, 256, 32, 32]>],<br>int dim = 1                         | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 256, s1, s2]>, <[1, 256, s1, s2]>],<br>int dim = 1                         | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[1, 3, 16, 16, 2]>, <[1, 3, 16, 16, 2]>, <[1, 3, 16, 16, 81]>],<br>int dim = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[1, 3, 32, 32, 2]>, <[1, 3, 32, 32, 2]>, <[1, 3, 32, 32, 81]>],<br>int dim = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1, 3, 64, 64, 2]>, <[1, 3, 64, 64, 2]>, <[1, 3, 64, 64, 81]>],<br>int dim = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[1, 32, s0, s1]>, <[1, 32, s0, s1]>],<br>int dim = 1                           | Unknown  | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[1, 64, s1, s2]>, <[1, 64, s1, s2]>],<br>int dim = 1                           | Unknown  | Unknown    | N/A   | N/A    |
|  9 | List[Tensor] tensors = [<[1, s0, s1, s2]>, <[1, s3, s1, s2]>],<br>int dim = 1                           | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 16, 16, 85]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 32, 32, 85]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 64, 64, 85]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, s1, s2]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 128, 64, 64]> input = ?,<br>Tensor<[255, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 128, s1, s2]> input = ?,<br>Tensor<[128, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 128, s1, s2]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 128, s1, s2]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 128, s1, s2]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 128, s1, s2]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[255, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 256, s1, s2]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 256, s1, s2]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 256, s1, s2]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 256, s1, s2]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 256, s1, s2]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 256, s1, s2]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 6, 6]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.9999289795030138 | 0      |
| 15 | Tensor<[1, 32, s0, s1]> input = ?,<br>Tensor<[32, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 32, s0, s1]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 32, s1, s2]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 18 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[255, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
| 19 | Tensor<[1, 512, s0, s1]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 20 | Tensor<[1, 512, s1, s2]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[1, 512, s1, s2]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 512, s1, s2]> input = ?,<br>Tensor<[512, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 64, s0, s1]> input = ?,<br>Tensor<[32, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 64, s0, s1]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 64, s1, s2]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 64, s1, s2]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 64, s1, s2]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor other = 2                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor other = 2                    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor other = 2                    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 85, 16, 16]> self = ?,<br>List[int] dims = [0, 1, 3, 4, 2] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 85, 32, 32]> self = ?,<br>List[int] dims = [0, 1, 3, 4, 2] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 85, 64, 64]> self = ?,<br>List[int] dims = [0, 1, 3, 4, 2] | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>number exponent = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>number exponent = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>number exponent = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3]> self = ?,<br>int dim = 0,<br>int index = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[3]> self = ?,<br>int dim = 0,<br>int index = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.sigmoid.default
|    | ATen Input Variations               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 16, 16, 85]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 32, 32, 85]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 64, 64, 85]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 128, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 128, s1, s2]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 256, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 256, s0, s1]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 256, s1, s2]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 32, 256, 256]> self = ?                              | Unknown  | Done       | 0.9999823979497721 | 0      |
|  6 | Tensor<[1, 32, s0, s1]> self = ?                                | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 512, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 512, s1, s2]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 64, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 64, s0, s1]> self = ?                                | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 64, s1, s2]> self = ?                                | Unknown  | Unknown    | N/A                | N/A    |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 16, 16, 85]> self = ?,<br>List[int] split_sizes = [2, 2, 81],<br>int dim = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 3, 32, 32, 85]> self = ?,<br>List[int] split_sizes = [2, 2, 81],<br>int dim = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 64, 64, 85]> self = ?,<br>List[int] split_sizes = [2, 2, 81],<br>int dim = 4 | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 255, 16, 16]> self = ?,<br>List[int] size = [1, 3, 85, 16, 16] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 255, 32, 32]> self = ?,<br>List[int] size = [1, 3, 85, 32, 32] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 255, 64, 64]> self = ?,<br>List[int] size = [1, 3, 85, 64, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 16, 16, 85]> self = ?,<br>List[int] size = [1, 768, 85]     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 32, 32, 85]> self = ?,<br>List[int] size = [1, 3072, 85]    | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 3, 64, 64, 85]> self = ?,<br>List[int] size = [1, 12288, 85]   | Unknown  | Unknown    | N/A   | N/A    |

