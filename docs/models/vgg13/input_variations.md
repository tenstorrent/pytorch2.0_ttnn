# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._adaptive_avg_pool2d.default    |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten.addmm.default                   |                  3 |           2 |         0 |          0 | 🚧          |    0.67 |
|  2 | aten.clone.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default             |                  9 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.max_pool2d_with_indices.default |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.relu.default                    |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  6 | aten.t.default                       |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  7 | aten.view.default                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._adaptive_avg_pool2d.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] output_size = [7, 7] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1000]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[4096]> self = ?,<br>Tensor<[1, 25088]> mat1 = ?,<br>Tensor<[25088, 4096]> mat2 = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4096]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 4096]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 128, 112, 112]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 64, 224, 224]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 128, 112, 112]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 56, 56]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 512, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 512, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 64, 224, 224]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.relu.default
|    | ATen Input Variations               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 128, 112, 112]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 56, 56]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 4096]> self = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 512, 14, 14]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 512, 28, 28]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 224, 224]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1000, 4096]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[4096, 25088]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4096, 4096]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] size = [1, 25088] | Done     | N/A                 | N/A          | N/A               | N/A                |

