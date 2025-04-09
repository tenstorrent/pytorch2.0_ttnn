# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_functional.default |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default                            |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                                  |                 12 |          12 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default                               |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.cat.default                                 |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  5 | aten.clone.default                               |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  6 | aten.convolution.default                         |                 25 |          25 |         0 |          0 | ✅          |       1 |
|  7 | aten.convolution_backward.default                |                 25 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.detach.default                              |                 10 |           0 |        10 |          0 | ✅          |       1 |
|  9 | aten.div.Scalar                                  |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default                              |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 11 | aten.hardsigmoid.default                         |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 12 | aten.hardsigmoid_backward.default                |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.max_pool2d_with_indices.default             |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.max_pool2d_with_indices_backward.default    |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mean.dim                                    |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 16 | aten.mm.default                                  |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 17 | aten.mul.Tensor                                  |                  8 |           8 |         0 |          0 | ✅          |       1 |
| 18 | aten.native_batch_norm_backward.default          |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.relu.default                                |                 10 |          10 |         0 |          0 | ✅          |       1 |
| 20 | aten.slice.Tensor                                |                 16 |          16 |         0 |          0 | ✅          |       1 |
| 21 | aten.sum.dim_IntList                             |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.t.default                                   |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 23 | aten.threshold_backward.default                  |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.view.default                                |                  3 |           3 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 160, 28, 28]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 192, 14, 14]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
|  4 | Tensor<[1, 224, 7, 7]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Fallback   |     1 |      0 |
|  5 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
|  6 | Tensor<[1, 512, 28, 28]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
|  7 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05       | None     | Fallback   |     1 |      0 |
|  8 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Fallback   |     1 |      0 |
|  9 | Tensor<[1, 768, 14, 14]> input = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>Tensor<[768]> running_mean = ?,<br>Tensor<[768]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[160]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[192]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[224]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[256]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[512]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[64]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided   | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[768]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ? | Done     | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  9 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
| 10 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
| 11 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 256, 28, 28]>, <[1, 160, 28, 28]>, <[1, 160, 28, 28]>, <[1, 160, 28, 28]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 512, 14, 14]>, <[1, 192, 14, 14]>, <[1, 192, 14, 14]>, <[1, 192, 14, 14]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[1, 64, 56, 56]>, <[1, 128, 56, 56]>, <[1, 128, 56, 56]>, <[1, 128, 56, 56]>],<br>int dim = 1  | Done     | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[1, 768, 7, 7]>, <[1, 224, 7, 7]>, <[1, 224, 7, 7]>, <[1, 224, 7, 7]>],<br>int dim = 1         | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024]> self = ? | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999965 |      1 |
|  1 | Tensor<[1, 1088, 14, 14]> input = ?,<br>Tensor<[768, 1088, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999965 |      0 |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Done     | Done       | 0.999983 |      0 |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99998  |      0 |
|  4 | Tensor<[1, 1440, 7, 7]> input = ?,<br>Tensor<[1024, 1440, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999953 |      0 |
|  5 | Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 160          | Done     | Done       | 0.999983 |      0 |
|  6 | Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999982 |      0 |
|  7 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192          | Done     | Done       | 0.999984 |      0 |
|  8 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999981 |      0 |
|  9 | Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 224            | Done     | Done       | 0.999985 |      0 |
| 10 | Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999981 |      0 |
| 11 | Tensor<[1, 256, 1, 1]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999981 |      1 |
| 12 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[160, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999975 |      0 |
| 13 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999981 |      0 |
| 14 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[256, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999972 |      0 |
| 15 | Tensor<[1, 512, 1, 1]> input = ?,<br>Tensor<[512, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999969 |      1 |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[192, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999971 |      0 |
| 17 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64           | Done     | Done       | 0.999983 |      0 |
| 18 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64           | Done     | Done       | 0.999984 |      0 |
| 19 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999987 |      0 |
| 20 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999986 |      0 |
| 21 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999986 |      0 |
| 22 | Tensor<[1, 736, 28, 28]> input = ?,<br>Tensor<[512, 736, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999968 |      0 |
| 23 | Tensor<[1, 768, 1, 1]> input = ?,<br>Tensor<[768, 768, 1, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999964 |      1 |
| 24 | Tensor<[1, 768, 7, 7]> input = ?,<br>Tensor<[224, 768, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999964 |      0 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> grad_output = ?,<br>Tensor<[1, 1024, 1, 1]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [1024],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   | 1.0   |      0 |
|  1 | Tensor<[1, 1024, 7, 7]> grad_output = ?,<br>Tensor<[1, 1440, 7, 7]> input = ?,<br>Tensor<[1024, 1440, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  2 | Tensor<[1, 128, 56, 56]> grad_output = ?,<br>Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  3 | Tensor<[1, 128, 56, 56]> grad_output = ?,<br>Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  4 | Tensor<[1, 128, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]     | None     | Fallback   | N/A   |      0 |
|  5 | Tensor<[1, 160, 28, 28]> grad_output = ?,<br>Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 160,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  6 | Tensor<[1, 160, 28, 28]> grad_output = ?,<br>Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 160, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  7 | Tensor<[1, 160, 28, 28]> grad_output = ?,<br>Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[160, 256, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  8 | Tensor<[1, 192, 14, 14]> grad_output = ?,<br>Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
|  9 | Tensor<[1, 192, 14, 14]> grad_output = ?,<br>Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 192, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
| 10 | Tensor<[1, 192, 14, 14]> grad_output = ?,<br>Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[192, 512, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
| 11 | Tensor<[1, 224, 7, 7]> grad_output = ?,<br>Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 224,<br>List[bool] output_mask = [True, True, False]       | None     | Fallback   | N/A   |      0 |
| 12 | Tensor<[1, 224, 7, 7]> grad_output = ?,<br>Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]       | None     | Fallback   | N/A   |      0 |
| 13 | Tensor<[1, 224, 7, 7]> grad_output = ?,<br>Tensor<[1, 768, 7, 7]> input = ?,<br>Tensor<[224, 768, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]       | None     | Fallback   | N/A   |      0 |
| 14 | Tensor<[1, 256, 1, 1]> grad_output = ?,<br>Tensor<[1, 256, 1, 1]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [256],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
| 15 | Tensor<[1, 256, 56, 56]> grad_output = ?,<br>Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[256, 448, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
| 16 | Tensor<[1, 512, 1, 1]> grad_output = ?,<br>Tensor<[1, 512, 1, 1]> input = ?,<br>Tensor<[512, 512, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [512],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
| 17 | Tensor<[1, 512, 28, 28]> grad_output = ?,<br>Tensor<[1, 736, 28, 28]> input = ?,<br>Tensor<[512, 736, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
| 18 | Tensor<[1, 64, 112, 112]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]     | None     | Fallback   | N/A   |      0 |
| 19 | Tensor<[1, 64, 112, 112]> grad_output = ?,<br>Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
| 20 | Tensor<[1, 64, 112, 112]> grad_output = ?,<br>Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   | N/A   |      0 |
| 21 | Tensor<[1, 64, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64,<br>List[bool] output_mask = [True, True, False]     | None     | Fallback   | N/A   |      0 |
| 22 | Tensor<[1, 64, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]       | None     | Fallback   | N/A   |      0 |
| 23 | Tensor<[1, 768, 1, 1]> grad_output = ?,<br>Tensor<[1, 768, 1, 1]> input = ?,<br>Tensor<[768, 768, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [768],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | None     | Fallback   | 1.0   |      0 |
| 24 | Tensor<[1, 768, 14, 14]> grad_output = ?,<br>Tensor<[1, 1088, 14, 14]> input = ?,<br>Tensor<[768, 1088, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   | N/A   |      0 |
### aten.detach.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?   | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 128, 56, 56]> self = ?  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 160, 28, 28]> self = ?  | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 192, 14, 14]> self = ?  | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 224, 7, 7]> self = ?    | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 256, 56, 56]> self = ?  | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 512, 28, 28]> self = ?  | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 64, 112, 112]> self = ? | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 64, 56, 56]> self = ?   | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 768, 14, 14]> self = ?  | Removed  | Done       |     1 |     -1 |
### aten.div.Scalar
|    | ATen Input Variations                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>number other = 49    | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 56, 56]> self = ?,<br>number other = 3136 | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 512, 28, 28]> self = ?,<br>number other = 784  | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 768, 14, 14]> self = ?,<br>number other = 196  | None     | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 7, 7] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 1, 1]> self = ?,<br>List[int] size = [1, 256, 56, 56] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512, 28, 28] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 14, 14] | Done     | Done       |     1 |      0 |
### aten.hardsigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ? | Done     | Done       | 0.999988 |      0 |
|  1 | Tensor<[1, 256, 1, 1]> self = ?  | Done     | Done       | 0.999988 |      0 |
|  2 | Tensor<[1, 512, 1, 1]> self = ?  | Done     | Done       | 0.999989 |      0 |
|  3 | Tensor<[1, 768, 1, 1]> self = ?  | Done     | Done       | 0.999986 |      0 |
### aten.hardsigmoid_backward.default
|    | ATen Input Variations                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> grad_output = ?,<br>Tensor<[1, 1024, 1, 1]> self = ? | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 1, 1]> grad_output = ?,<br>Tensor<[1, 256, 1, 1]> self = ?   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 512, 1, 1]> grad_output = ?,<br>Tensor<[1, 512, 1, 1]> self = ?   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 768, 1, 1]> grad_output = ?,<br>Tensor<[1, 768, 1, 1]> self = ?   | None     | Fallback   |     1 |     -1 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 56, 56]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 512, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | None     | Fallback   |     1 |      0 |
### aten.max_pool2d_with_indices_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 28, 28]> grad_output = ?,<br>Tensor<[1, 256, 56, 56]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True,<br>Tensor<[1, 256, 28, 28]> indices = ? | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 512, 14, 14]> grad_output = ?,<br>Tensor<[1, 512, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True,<br>Tensor<[1, 512, 14, 14]> indices = ? | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 768, 7, 7]> grad_output = ?,<br>Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True,<br>Tensor<[1, 768, 7, 7]> indices = ?     | None     | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 512, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 768, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | Done     | Done       | 0.999997 |      0 |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1024]> mat2 = ? | Done     | Done       | 0.999969 |      0 |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1024]> mat2 = ?    | Done     | Done       | 0.999992 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ? | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  6 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
### aten.native_batch_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> grad_out = ?,<br>Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> running_mean = ?,<br>Optional[Tensor]<[1024]> running_var = ?,<br>Optional[Tensor]<[1024]> save_mean = ?,<br>Optional[Tensor]<[1024]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 128, 56, 56]> grad_out = ?,<br>Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> running_mean = ?,<br>Optional[Tensor]<[128]> running_var = ?,<br>Optional[Tensor]<[128]> save_mean = ?,<br>Optional[Tensor]<[128]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 160, 28, 28]> grad_out = ?,<br>Tensor<[1, 160, 28, 28]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> running_mean = ?,<br>Optional[Tensor]<[160]> running_var = ?,<br>Optional[Tensor]<[160]> save_mean = ?,<br>Optional[Tensor]<[160]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 192, 14, 14]> grad_out = ?,<br>Tensor<[1, 192, 14, 14]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> running_mean = ?,<br>Optional[Tensor]<[192]> running_var = ?,<br>Optional[Tensor]<[192]> save_mean = ?,<br>Optional[Tensor]<[192]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  4 | Tensor<[1, 224, 7, 7]> grad_out = ?,<br>Tensor<[1, 224, 7, 7]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> running_mean = ?,<br>Optional[Tensor]<[224]> running_var = ?,<br>Optional[Tensor]<[224]> save_mean = ?,<br>Optional[Tensor]<[224]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]        | None     | Fallback   |     1 |      0 |
|  5 | Tensor<[1, 256, 56, 56]> grad_out = ?,<br>Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> running_mean = ?,<br>Optional[Tensor]<[256]> running_var = ?,<br>Optional[Tensor]<[256]> save_mean = ?,<br>Optional[Tensor]<[256]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  6 | Tensor<[1, 512, 28, 28]> grad_out = ?,<br>Tensor<[1, 512, 28, 28]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> running_mean = ?,<br>Optional[Tensor]<[512]> running_var = ?,<br>Optional[Tensor]<[512]> save_mean = ?,<br>Optional[Tensor]<[512]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  7 | Tensor<[1, 64, 112, 112]> grad_out = ?,<br>Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> running_mean = ?,<br>Optional[Tensor]<[64]> running_var = ?,<br>Optional[Tensor]<[64]> save_mean = ?,<br>Optional[Tensor]<[64]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]       | None     | Fallback   |     1 |      0 |
|  8 | Tensor<[1, 64, 56, 56]> grad_out = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> running_mean = ?,<br>Optional[Tensor]<[64]> running_var = ?,<br>Optional[Tensor]<[64]> save_mean = ?,<br>Optional[Tensor]<[64]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]           | None     | Fallback   |     1 |      0 |
|  9 | Tensor<[1, 768, 14, 14]> grad_out = ?,<br>Tensor<[1, 768, 14, 14]> input = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> running_mean = ?,<br>Optional[Tensor]<[768]> running_var = ?,<br>Optional[Tensor]<[768]> save_mean = ?,<br>Optional[Tensor]<[768]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?   | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 128, 56, 56]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 160, 28, 28]> self = ?  | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 192, 14, 14]> self = ?  | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 224, 7, 7]> self = ?    | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 256, 56, 56]> self = ?  | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 512, 28, 28]> self = ?  | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 768, 14, 14]> self = ?  | Done     | Done       | 1.0   | 0      |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 704  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 704,<br>Optional[int] end = 896  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 896,<br>Optional[int] end = 1088 | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 768      | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1216,<br>Optional[int] end = 1440  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 992    | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 992,<br>Optional[int] end = 1216   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64      | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 320   | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 448   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 192    | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256     | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 416   | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 416,<br>Optional[int] end = 576   | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 576,<br>Optional[int] end = 736   | Done     | Done       |     1 |      0 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True           | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 512, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 768, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1000, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1024, 1000]> self = ? | Done     | Done       |     1 |      0 |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> grad_output = ?,<br>Tensor<[1, 1024, 7, 7]> self = ?,<br>number threshold = 0     | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 128, 56, 56]> grad_output = ?,<br>Tensor<[1, 128, 56, 56]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 160, 28, 28]> grad_output = ?,<br>Tensor<[1, 160, 28, 28]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 192, 14, 14]> grad_output = ?,<br>Tensor<[1, 192, 14, 14]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 224, 7, 7]> grad_output = ?,<br>Tensor<[1, 224, 7, 7]> self = ?,<br>number threshold = 0       | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 256, 56, 56]> grad_output = ?,<br>Tensor<[1, 256, 56, 56]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 512, 28, 28]> grad_output = ?,<br>Tensor<[1, 512, 28, 28]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 64, 112, 112]> grad_output = ?,<br>Tensor<[1, 64, 112, 112]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 64, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> self = ?,<br>number threshold = 0     | None     | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 768, 14, 14]> grad_output = ?,<br>Tensor<[1, 768, 14, 14]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]          | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1024, 1, 1] | Done     | Done       |     1 |      0 |

