# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._assert_async.msg         |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  1 | aten._to_copy.default          |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
|  2 | aten.cat.default               |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  3 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  4 | aten.cos.default               |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  5 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  6 | aten.exp.default               |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  7 | aten.mul.Tensor                |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  8 | aten.native_group_norm.default |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  9 | aten.scalar_tensor.default     |                  2 |           0 |         0 |          0 | ✘           |     0   |
| 10 | aten.silu.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 11 | aten.sin.default               |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 12 | aten.slice.Tensor              |                  5 |           2 |         3 |          0 | ✅          |     1   |
| 13 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |     1   |
***
### aten._assert_async.msg
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[]> self = ?,<br>str assert_msg = assertion error | None     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | None     | Fallback   |     1 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 160]>, <[1, 160]>],<br>int dim = -1 | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.cos.default
|    | ATen Input Variations     | Status   | Isolated   |     PCC |   Host |
|---:|:--------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[1, 160]> self = ? | Done     | Done       | 0.99999 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 160 | Done     | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[160]> self = ?  | Done     | Done       | 0.999959 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1         | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ? | Done     | Done       | 0.999996 |      0 |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05 | None     | Fallback   |     1 |      0 |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<Eq(s0, 1280)> s = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  1 | number<Eq(s0, 640)> s = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations             | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 320, 64, 64]> self = ? | Done     | Done       | 0.999982 |      0 |
### aten.sin.default
|    | ATen Input Variations     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 160]> self = ? | Done     | Done       | 0.999997 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                   | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 9223372036854775807 | Done     | Done       | 1.0   | 0      |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[160]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1]> self = ?,<br>int dim = 1   | Done     | Done       |     1 |      0 |

