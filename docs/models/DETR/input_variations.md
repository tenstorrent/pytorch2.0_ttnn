# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default                |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                      |                 27 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.addmm.default                   |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.baddbmm.default                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default                     |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.cat.default                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.convolution.default             |                 24 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.cos.default                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.div.Tensor                      |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.expand.default                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.masked_fill.Scalar              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.max_pool2d_with_indices.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mm.default                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mul.Tensor                      |                 19 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.native_layer_norm.default       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.permute.default                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.pow.Scalar                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.relu.default                    |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.repeat.default                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.rsqrt.default                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.select.int                      |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.sigmoid.default                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.sin.default                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.slice.Tensor                    |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.split.Tensor                    |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.stack.default                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.sub.Tensor                      |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.t.default                       |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.transpose.int                   |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.unsqueeze.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.view.default                    |                 26 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.zeros.default                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.zeros_like.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999598 |      0 |
|  1 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999585 |      0 |
|  2 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999588 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 23, 40]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                         | Unknown  | Done       | 1        |      0 |
|  1 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | Unknown  | Done       | 1        |      0 |
|  2 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Unknown  | Done       | 1        |      0 |
|  5 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Unknown  | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | Unknown  | Done       | 1        |      0 |
|  8 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  9 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
| 10 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                         | Unknown  | Done       | 1        |      0 |
| 11 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Unknown  | Done       | 1        |      0 |
| 12 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
| 13 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ? | Unknown  | Done       | 0.999998 |      0 |
| 14 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 15 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Unknown  | Done       | 0.999998 |      0 |
| 16 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Unknown  | Done       | 1        |      0 |
| 17 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 18 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 19 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Unknown  | Done       | 0.999998 |      0 |
| 20 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
| 21 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Unknown  | Done       | 1        |      0 |
| 22 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 23 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 24 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?           | Unknown  | Done       | 0.999998 |      0 |
| 25 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Unknown  | Done       | 0.293088 |      0 |
| 26 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?           | Unknown  | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[100, 256]> mat1 = ?,<br>Tensor<[256, 2048]> mat2 = ? | Unknown  | Done       | 0.999974 |      0 |
|  1 | Tensor<[2048]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 2048]> mat2 = ? | Unknown  | Done       | 0.999978 |      0 |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[100, 2048]> mat1 = ?,<br>Tensor<[2048, 256]> mat2 = ? | Unknown  | Done       | 0.99992  |      0 |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[100, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  | Done       | 0.999977 |      0 |
|  4 | Tensor<[256]> self = ?,<br>Tensor<[600, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  | Done       | 0.999974 |      0 |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[920, 2048]> mat1 = ?,<br>Tensor<[2048, 256]> mat2 = ? | Unknown  | Done       | 0.999954 |      0 |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  | Done       | 0.999974 |      0 |
|  7 | Tensor<[4]> self = ?,<br>Tensor<[600, 256]> mat1 = ?,<br>Tensor<[256, 4]> mat2 = ?       | Unknown  | Done       | 0.999976 |      0 |
|  8 | Tensor<[92]> self = ?,<br>Tensor<[600, 256]> mat1 = ?,<br>Tensor<[256, 92]> mat2 = ?     | Unknown  | Done       | 0.999974 |      0 |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 100, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ? | Unknown  | Done       | 0.999988 |      0 |
|  1 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 920, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ? | Unknown  | Done       | 0.999988 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ? | Unknown  | Done       | 0.999981 |      0 |
|  1 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?  | Unknown  | Done       | 0.999989 |      0 |
|  2 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ? | Unknown  | Done       | 0.999965 |      0 |
|  3 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 23, 40, 128]>, <[1, 23, 40, 128]>],<br>int dim = 3 | Unknown  | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[100, 1, 2048]> self = ?                                                         | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[100, 1, 256]> self = ?                                                          | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[920, 1, 2048]> self = ?                                                         | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[920, 1, 256]> self = ?                                                          | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 45, 80]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.9998390470176708 | 2      |
|  1 | Tensor<[1, 1024, 45, 80]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999656884509439 | 2      |
|  2 | Tensor<[1, 1024, 45, 80]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999656612762922 | 2      |
|  3 | Tensor<[1, 128, 180, 320]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Failed     | N/A                | N/A    |
|  4 | Tensor<[1, 128, 90, 160]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9998144857799989 | 2      |
|  5 | Tensor<[1, 128, 90, 160]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999798419062585 | 2      |
|  6 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.9999534175372403 | 3      |
|  7 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999551641560122 | 2      |
|  8 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999753785464047 | 2      |
|  9 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Fallback   | 1.0                | -1     |
| 10 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999754194248031 | 2      |
| 11 | Tensor<[1, 256, 45, 80]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999792884193589 | 2      |
| 12 | Tensor<[1, 256, 45, 80]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.999547408284761  | 2      |
| 13 | Tensor<[1, 256, 90, 160]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9995445014990083 | 2      |
| 14 | Tensor<[1, 3, 720, 1280]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  | Fallback   | 1.0                | -1     |
| 15 | Tensor<[1, 512, 23, 40]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999713324456078 | 2      |
| 16 | Tensor<[1, 512, 23, 40]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.9988589999873476 | 2      |
| 17 | Tensor<[1, 512, 45, 80]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.998857034237004  | 2      |
| 18 | Tensor<[1, 512, 90, 160]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999294272555228 | 2      |
| 19 | Tensor<[1, 512, 90, 160]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999713897245909 | 2      |
| 20 | Tensor<[1, 512, 90, 160]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999714006102397 | 2      |
| 21 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.9999863364149457 | 2      |
| 22 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.9999864953219345 | 2      |
| 23 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.9999197296603385 | 2      |
### aten.cos.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  | Done       | 0.999992 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 128                             | Unknown  | Unknown    | N/A                   | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 40]> other = ?                   | Unknown  | Unknown    | N/A                   | N/A    |
|  2 | Tensor self = ?,<br>Tensor<[1, 23, 1]> other = ?                   | Unknown  | Unknown    | N/A                   | N/A    |
|  3 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?        | Unknown  | Done       | 0.0004768621838454325 | 0      |
|  4 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  | Done       | 0.9999957561005907    | 0      |
|  5 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  | Done       | 0.9999958401214069    | 0      |
### aten.expand.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1] | Unknown  | Done       |     1 |      0 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 920]> self = ?,<br>Tensor mask = ?,<br>number value = -inf | Unknown  | Unknown    | N/A   | N/A    |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 360, 640]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  | Done       |     1 |      2 |
### aten.mm.default
|    | ATen Input Variations                                       | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ? | Unknown  | Done       | 0.999975 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Unknown  | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ? | Unknown  | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?  | Unknown  | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
|  6 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586        | Unknown  | Done       | 0.999996 |      0 |
|  8 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Unknown  | Done       | 0.999994 |      0 |
|  9 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Unknown  | Done       | 0.999996 |      0 |
| 10 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
| 11 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?  | Unknown  | Done       | 0.999996 |      0 |
| 12 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Unknown  | Done       | 0.999996 |      0 |
| 13 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
| 14 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
| 15 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?  | Unknown  | Done       | 0.999996 |      0 |
| 16 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Unknown  | Done       | 0.999994 |      0 |
| 17 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
| 18 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[100, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      1 |
|  1 | Tensor<[920, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]       | Unknown  | Done       |     1 |      0 |
### aten.pow.Scalar
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | number self = 10000,<br>Tensor<[128]> exponent = ? | Unknown  | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 45, 80]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 180, 320]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 90, 160]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 2048, 23, 40]> self = ?  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 180, 320]> self = ? | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 45, 80]> self = ?   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 90, 160]> self = ?  | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 512, 23, 40]> self = ?   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 512, 45, 80]> self = ?   | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 512, 90, 160]> self = ?  | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 64, 180, 320]> self = ?  | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 64, 360, 640]> self = ?  | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[100, 1, 2048]> self = ?     | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[6, 1, 100, 256]> self = ?   | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[920, 1, 2048]> self = ?     | Unknown  | Done       |     1 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Done       |     1 |     -1 |
### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ? | Unknown  | Done       | 0.999994 |      0 |
|  1 | Tensor<[1, 128, 1, 1]> self = ?  | Unknown  | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 2048, 1, 1]> self = ? | Unknown  | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 256, 1, 1]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  4 | Tensor<[1, 512, 1, 1]> self = ?  | Unknown  | Done       | 0.999995 |      0 |
|  5 | Tensor<[1, 64, 1, 1]> self = ?   | Unknown  | Done       | 0.999994 |      0 |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[6, 1, 100, 4]> self = ?,<br>int dim = 0,<br>int index = -1  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1 | Unknown  | Done       |     1 |     -1 |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[6, 1, 100, 4]> self = ? | Unknown  | Done       | 0.999763 |      0 |
### aten.sin.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  | Done       | 0.999997 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Done       | 1.0   | -1     |
### aten.split.Tensor
|    | ATen Input Variations                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[768, 256]> self = ?,<br>int split_size = 256 | Unknown  | Done       |     1 |      1 |
|  1 | Tensor<[768]> self = ?,<br>int split_size = 256      | Unknown  | Fallback   |     1 |     -3 |
### aten.stack.default
|    | ATen Input Variations                                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 23, 40, 64]>, <[1, 23, 40, 64]>],<br>int dim = 4                                                 | Unknown  | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>] | Unknown  | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  | Done       | 0.999997 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2048, 256]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[256, 2048]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[256, 256]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[4, 256]> self = ?    | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[92, 256]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[100, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1   | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1     | Unknown  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3 | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[100, 256]> self = ?,<br>int dim = 1  | Unknown  | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]      | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]          | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]             | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]          | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]            | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 8, 32]          | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]          | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]            | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[100, 8, 32]> self = ?,<br>List[int] size = [100, 256]             | Unknown  | Done       |     1 |     -1 |
| 10 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                | Unknown  | Done       |     1 |     -1 |
| 11 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                 | Unknown  | Done       |     1 |     -1 |
| 12 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                | Unknown  | Done       |     1 |     -1 |
| 13 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                 | Unknown  | Done       |     1 |     -1 |
| 14 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                 | Unknown  | Done       |     1 |     -1 |
| 15 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]         | Unknown  | Done       |     1 |     -1 |
| 16 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]         | Unknown  | Done       |     1 |     -1 |
| 17 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]             | Unknown  | Done       |     1 |     -1 |
| 18 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]           | Unknown  | Done       |     1 |     -1 |
| 19 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                  | Unknown  | Done       |     1 |     -1 |
| 20 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]          | Unknown  | Done       |     1 |     -1 |
| 21 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]            | Unknown  | Done       |     1 |     -1 |
| 22 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 8, 32]          | Unknown  | Done       |     1 |     -1 |
| 23 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]          | Unknown  | Done       |     1 |     -1 |
| 24 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]            | Unknown  | Done       |     1 |     -1 |
| 25 | Tensor<[920, 8, 32]> self = ?,<br>List[int] size = [920, 256]             | Unknown  | Done       |     1 |     -1 |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
### aten.zeros_like.default
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                           | Unknown  | Done       | 1.0   | 0      |

