# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default                |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_index.Tensor            |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten.add.Tensor                      |                 29 |          22 |         0 |          0 | 🚧          |    0.76 |
|  4 | aten.addmm.default                   |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  5 | aten.arange.default                  |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.baddbmm.default                 |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  7 | aten.bitwise_not.default             |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.bmm.default                     |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  9 | aten.cat.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.clone.default                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 11 | aten.convolution.default             |                 24 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.cos.default                     |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.cumsum.default                  |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.div.Tensor                      |                  6 |           2 |         0 |          0 | 🚧          |    0.33 |
| 15 | aten.expand.default                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.floor_divide.default            |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.masked_fill.Scalar              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.max_pool2d_with_indices.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.mm.default                      |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 20 | aten.mul.Tensor                      |                 22 |          22 |         0 |          0 | ✅          |    1    |
| 21 | aten.native_layer_norm.default       |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 22 | aten.ones.default                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 23 | aten.permute.default                 |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 24 | aten.pow.Scalar                      |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.relu.default                    |                 15 |          15 |         0 |          0 | ✅          |    1    |
| 26 | aten.repeat.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.rsqrt.default                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 28 | aten.select.int                      |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.sigmoid.default                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 30 | aten.sin.default                     |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 31 | aten.slice.Tensor                    |                 11 |           2 |         0 |          0 | 🚧          |    0.18 |
| 32 | aten.split.Tensor                    |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 33 | aten.stack.default                   |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 34 | aten.sub.Tensor                      |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 35 | aten.t.default                       |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 36 | aten.transpose.int                   |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 37 | aten.unsqueeze.default               |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 38 | aten.view.default                    |                 27 |          27 |         0 |          0 | ✅          |    1    |
| 39 | aten.zeros.default                   |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 40 | aten.zeros_like.default              |                  2 |           2 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 23, 40]> self = ?,<br>Optional[int] dtype = torch.bool       | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 720, 1280]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 23, 40]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[23]> self = ?,<br>Optional[int] dtype = torch.int64                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[40]> self = ?,<br>Optional[int] dtype = torch.int64                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 720, 1280]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[23, 1]>, <[40]>] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | None     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | None     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | None     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[40]> self = ?,<br>Tensor other = 0.0                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                   | None     | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[100, 256]> mat1 = ?,<br>Tensor<[256, 2048]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[2048]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 2048]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[100, 2048]> mat1 = ?,<br>Tensor<[2048, 256]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[100, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[256]> self = ?,<br>Tensor<[600, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[920, 2048]> mat1 = ?,<br>Tensor<[2048, 256]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[4]> self = ?,<br>Tensor<[600, 256]> mat1 = ?,<br>Tensor<[256, 4]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[92]> self = ?,<br>Tensor<[600, 256]> mat1 = ?,<br>Tensor<[256, 92]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number end = 128,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | number end = 23,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | number end = 40,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 100, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 920, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.bitwise_not.default
|    | ATen Input Variations        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40]> self = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 23, 40, 128]>, <[1, 23, 40, 128]>],<br>int dim = 3 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[100, 1, 2048]> self = ?                                                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[100, 1, 256]> self = ?                                                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[920, 1, 2048]> self = ?                                                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[920, 1, 256]> self = ?                                                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 45, 80]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 45, 80]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 45, 80]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 128, 180, 320]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 128, 90, 160]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 128, 90, 160]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 256, 45, 80]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 256, 45, 80]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 256, 90, 160]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 3, 720, 1280]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 512, 23, 40]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 512, 23, 40]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 512, 45, 80]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 512, 90, 160]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 512, 90, 160]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 512, 90, 160]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | None     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.cos.default
|    | ATen Input Variations            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] dtype = torch.float32 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?        | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?      | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?      | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[128]> self = ?,<br>Tensor other = 128                      | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.floor_divide.default
|    | ATen Input Variations                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128]> self = ?,<br>Tensor other = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 920]> self = ?,<br>Tensor<[1, 920]> mask = ?,<br>number value = -inf | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 64, 360, 640]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[128]> self = ?,<br>Tensor other = 2                              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                            | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[100, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[920, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.ones.default
|    | ATen Input Variations                                                                                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [1, 720, 1280],<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]       | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.pow.Scalar
|    | ATen Input Variations                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number self = 10000,<br>Tensor<[128]> exponent = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.relu.default
|    | ATen Input Variations               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 45, 80]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 180, 320]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 128, 90, 160]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 2048, 23, 40]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 256, 180, 320]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 45, 80]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 90, 160]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 512, 23, 40]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 512, 45, 80]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 512, 90, 160]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 64, 180, 320]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 64, 360, 640]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[100, 1, 2048]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[6, 1, 100, 256]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[920, 1, 2048]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.repeat.default
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 1, 1]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 2048, 1, 1]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 1, 1]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 512, 1, 1]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 1, 1]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0   | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[6, 1, 100, 4]> self = ?,<br>int dim = 0,<br>int index = -1  | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[6, 1, 100, 4]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.sin.default
|    | ATen Input Variations            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.split.Tensor
|    | ATen Input Variations                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[768, 256]> self = ?,<br>int split_size = 256 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[768]> self = ?,<br>int split_size = 256      | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.stack.default
|    | ATen Input Variations                                                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 23, 40, 64]>, <[1, 23, 40, 64]>],<br>int dim = 4                                                 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2048, 256]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[256, 2048]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256, 256]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[4, 256]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[92, 256]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[100, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3    | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 720, 1280]> self = ?,<br>int dim = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[100, 256]> self = ?,<br>int dim = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[23]> self = ?,<br>int dim = -1          | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 8, 32]          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[100, 8, 32]> self = ?,<br>List[int] size = [100, 256]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 8, 32]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[920, 8, 32]> self = ?,<br>List[int] size = [920, 256]             | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.zeros_like.default
|    | ATen Input Variations                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 920]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[bool] pin_memory = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                                     | Done     | N/A                 | N/A          | N/A               | N/A                |

