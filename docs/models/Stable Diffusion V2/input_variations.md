# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._assert_async.msg                           |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._scaled_dot_product_flash_attention.default |                 12 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._to_copy.default                            |                 12 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten._unsafe_index.Tensor                        |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.add.Tensor                                  |                 24 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.addmm.default                               |                 22 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.arange.default                              |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.arange.start                                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.cat.default                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.clone.default                               |                 24 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.convolution.default                         |                 37 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.cos.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.div.Tensor                                  |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.exp.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.expand.default                              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.gelu.default                                |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.lift_fresh_copy.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.mm.default                                  |                  9 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.mul.Tensor                                  |                 13 |           3 |         0 |          0 | 🚧          |    0.23 |
| 19 | aten.native_group_norm.default                   |                 18 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.native_layer_norm.default                   |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.permute.default                             |                 12 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.scalar_tensor.default                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.silu.default                                |                 13 |           1 |         0 |          0 | 🚧          |    0.08 |
| 24 | aten.sin.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 25 | aten.slice.Tensor                                |                 10 |           2 |         0 |          0 | 🚧          |    0.2  |
| 26 | aten.split.Tensor                                |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.sym_size.int                                |                 20 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.t.default                                   |                 14 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.transpose.int                               |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.unsqueeze.default                           |                 11 |           2 |         0 |          0 | 🚧          |    0.18 |
| 31 | aten.view.default                                |                 54 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._assert_async.msg
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[]> self = ?,<br>str assert_msg = assertion error | Unknown  | Unknown    | N/A   |
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 4096, 40]> key = ?,<br>Tensor<[1, 8, 4096, 40]> value = ?       | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?             | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 8, s0*s1, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?         | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 8, s0*s1, 160]> query = ?,<br>Tensor<[1, 8, s0*s1, 160]> key = ?,<br>Tensor<[1, 8, s0*s1, 160]> value = ? | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 8, s0*s1, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?            | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 8, s0*s1, 80]> query = ?,<br>Tensor<[1, 8, s0*s1, 80]> key = ?,<br>Tensor<[1, 8, s0*s1, 80]> value = ?    | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 8, s1*s2, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?         | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 8, s1*s2, 160]> query = ?,<br>Tensor<[1, 8, s1*s2, 160]> key = ?,<br>Tensor<[1, 8, s1*s2, 160]> value = ? | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 8, s1*s2, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?            | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 8, s1*s2, 40]> query = ?,<br>Tensor<[1, 8, s1*s2, 40]> key = ?,<br>Tensor<[1, 8, s1*s2, 40]> value = ?    | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, 8, s1*s2, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?            | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 8, s1*s2, 80]> query = ?,<br>Tensor<[1, 8, s1*s2, 80]> key = ?,<br>Tensor<[1, 8, s1*s2, 80]> value = ?    | Unknown  | Unknown    | N/A   |
### aten._to_copy.default
|    | ATen Input Variations                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1280, 2*s0, 2*s1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] dtype = torch.float32        | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                 | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16              | None     | Fallback   | True  |
|  6 | Tensor<[1, s0, 2*s1, 2*s2]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, s0, s1, s2]> self = ?,<br>Optional[int] dtype = torch.float32        | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[16]> self = ?,<br>Optional[int] dtype = torch.int64                     | Unknown  | Fallback   | True  |
|  9 | Tensor<[2*s0]> self = ?,<br>Optional[int] dtype = torch.int64                   | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[2*s1]> self = ?,<br>Optional[int] dtype = torch.int64                   | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[2*s2]> self = ?,<br>Optional[int] dtype = torch.int64                   | Unknown  | Unknown    | N/A   |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                       | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[16, 1]>, <[16]>]       | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[2*s0, 1]>, <[2*s1]>] | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, s0, s1, s2]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[2*s1, 1]>, <[2*s2]>]   | Unknown  | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?     | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?     | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?   | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ? | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?   | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ? | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?     | Unknown  | Done       | True  |
|  7 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?   | Unknown  | Done       | True  |
|  8 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?     | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?   | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?       | Unknown  | Done       | True  |
| 11 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?     | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?   | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?     | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?   | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?   | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?     | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?   | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?     | Unknown  | Unknown    | N/A   |
| 19 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?     | Unknown  | Unknown    | N/A   |
| 20 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                               | Unknown  | Fallback   | True  |
| 21 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                             | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                             | Unknown  | Unknown    | N/A   |
| 23 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                             | Unknown  | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[10240]> self = ?,<br>Tensor<[s0*s1, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[10240]> self = ?,<br>Tensor<[s1*s2, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1280]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?       | Unknown  | Done       | True  |
|  3 | Tensor<[1280]> self = ?,<br>Tensor<[1, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ?         | Unknown  | Done       | True  |
|  4 | Tensor<[1280]> self = ?,<br>Tensor<[s0*s1, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1280]> self = ?,<br>Tensor<[s0*s1, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1280]> self = ?,<br>Tensor<[s1*s2, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1280]> self = ?,<br>Tensor<[s1*s2, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[2560]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 2560]> mat2 = ?      | Unknown  | Done       | True  |
|  9 | Tensor<[2560]> self = ?,<br>Tensor<[s1*s2, 320]> mat1 = ?,<br>Tensor<[320, 2560]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[320]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?         | Unknown  | Done       | True  |
| 11 | Tensor<[320]> self = ?,<br>Tensor<[4096, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?      | Unknown  | Done       | True  |
| 12 | Tensor<[320]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?        | Unknown  | Done       | True  |
| 13 | Tensor<[320]> self = ?,<br>Tensor<[s1*s2, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[320]> self = ?,<br>Tensor<[s1*s2, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?       | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[5120]> self = ?,<br>Tensor<[s0*s1, 640]> mat1 = ?,<br>Tensor<[640, 5120]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[5120]> self = ?,<br>Tensor<[s1*s2, 640]> mat1 = ?,<br>Tensor<[640, 5120]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[640]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 640]> mat2 = ?         | Unknown  | Done       | True  |
| 18 | Tensor<[640]> self = ?,<br>Tensor<[s0*s1, 2560]> mat1 = ?,<br>Tensor<[2560, 640]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 19 | Tensor<[640]> self = ?,<br>Tensor<[s0*s1, 640]> mat1 = ?,<br>Tensor<[640, 640]> mat2 = ?       | Unknown  | Unknown    | N/A   |
| 20 | Tensor<[640]> self = ?,<br>Tensor<[s1*s2, 2560]> mat1 = ?,<br>Tensor<[2560, 640]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 21 | Tensor<[640]> self = ?,<br>Tensor<[s1*s2, 640]> mat1 = ?,<br>Tensor<[640, 640]> mat2 = ?       | Unknown  | Unknown    | N/A   |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 16,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  | Fallback   | True  |
|  1 | number<2*s0> end = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
|  2 | number<2*s1> end = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
|  3 | number<2*s2> end = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
### aten.arange.start
|    | ATen Input Variations                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number start = 0,<br>number end = 160,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.cat.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 160]>, <[1, 160]>],<br>int dim = -1 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?                                                             | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?                                                           | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, s1, s2]> self = ?                                                           | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 320, 64, 64]> self = ?                                                            | Unknown  | Done       | True  |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       | True  |
|  7 | Tensor<[1, 320, s1, s2]> self = ?                                                            | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 320, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 4096, 1280]> self = ?                                                             | Unknown  | Done       | True  |
| 10 | Tensor<[1, 4096, 320]> self = ?                                                              | Unknown  | Done       | True  |
| 11 | Tensor<[1, 640, s0, s1]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 640, s0, s1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, 640, s1, s2]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 640, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, s0*s1, 1280]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, s0*s1, 2560]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, s0*s1, 5120]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1, s0*s1, 640]> self = ?                                                             | Unknown  | Unknown    | N/A   |
| 19 | Tensor<[1, s1*s2, 1280]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 20 | Tensor<[1, s1*s2, 2560]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 21 | Tensor<[1, s1*s2, 320]> self = ?                                                             | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[1, s1*s2, 5120]> self = ?                                                            | Unknown  | Unknown    | N/A   |
| 23 | Tensor<[1, s1*s2, 640]> self = ?                                                             | Unknown  | Unknown    | N/A   |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[640, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[640, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[1280, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[1280, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[640, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[640, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, 2560, s0, s1]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, 2560, s0, s1]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Unknown    | N/A   |
| 19 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 20 | Tensor<[1, 320, s0, s1]> input = ?,<br>Tensor<[640, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 21 | Tensor<[1, 320, s0, s1]> input = ?,<br>Tensor<[640, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[1, 320, s1, s2]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 23 | Tensor<[1, 320, s1, s2]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 24 | Tensor<[1, 640, s0, s1]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 25 | Tensor<[1, 640, s0, s1]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 26 | Tensor<[1, 640, s0, s1]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 27 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[1280, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
| 28 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[1280, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   |
| 29 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[320, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 30 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[320, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 31 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 32 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 33 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 34 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[320, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 35 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[640, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
| 36 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[640, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   |
### aten.cos.default
|    | ATen Input Variations     | Status   | Isolated   | PCC   |
|---:|:--------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 160]> self = ? | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0   | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1   | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1.0 | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor other = 1.0 | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0  | Unknown  | Done       | True  |
|  5 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0    | Unknown  | Done       | True  |
|  7 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor other = 1.0   | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor other = 1.0   | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor other = 1.0   | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[160]> self = ?,<br>Tensor other = 160             | None     | Fallback   | True  |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[160]> self = ?  | Done     | Done       | True  |
### aten.expand.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1]> self = ?,<br>List[int] size = [1] | None     | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 4096, 1280]> self = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[1, s0*s1, 2560]> self = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, s0*s1, 5120]> self = ? | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, s1*s2, 1280]> self = ? | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, s1*s2, 2560]> self = ? | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, s1*s2, 5120]> self = ? | Unknown  | Unknown    | N/A   |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor self = ?         | None     | Unknown    | N/A   |
### aten.mm.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[4096, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?     | Unknown  | Done       | True  |
|  1 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 1280]> mat2 = ?       | Unknown  | Done       | True  |
|  2 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 320]> mat2 = ?        | Unknown  | Done       | True  |
|  3 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 640]> mat2 = ?        | Unknown  | Done       | True  |
|  4 | Tensor<[s0*s1, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[s0*s1, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[s1*s2, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[s1*s2, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?    | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[s1*s2, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A   |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                           | Done     | Done       | True  |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                   | Done     | Done       | True  |
|  2 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?   | Unknown  | Done       | True  |
|  3 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ? | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ? | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ? | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ? | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ? | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[160]> self = ?,<br>Tensor other = -9.210340371976184             | Done     | Done       | True  |
|  9 | Tensor<[16]> self = ?,<br>Tensor other = 0.5                             | Unknown  | Done       | True  |
| 10 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?          | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?          | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?          | Unknown  | Unknown    | N/A   |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05         | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-06 | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-06 | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int N = 1,<br>int C = 1920,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05         | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 2560, s0, s1]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05         | None     | Fallback   | True  |
|  9 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-06         | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 320, s0, s1]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 320, s1, s2]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 320, s1, s2]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-06     | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, 640, s0, s1]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 640, s0, s1]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-06     | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, 640, s1, s2]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, 640, s1, s2]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-06     | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, 960, s1, s2]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int N = 1,<br>int C = 960,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 4096, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05      | Unknown  | Done       | N/A   |
|  1 | Tensor<[1, s0*s1, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, s0*s1, 640]> input = ?,<br>List[int] normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, s1*s2, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, s1*s2, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, s1*s2, 640]> input = ?,<br>List[int] normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 1280, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Done       | True  |
|  3 | Tensor<[1, 320, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Done       | True  |
|  5 | Tensor<[1, 640, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 640, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Unknown    | N/A   |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                             | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number<Eq(s0, 640)> s = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
### aten.silu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?   | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1280, s0, s1]> self = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s1, s2]> self = ? | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280]> self = ?         | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1920, s1, s2]> self = ? | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 2560, 8, 8]> self = ?   | Unknown  | Done       | True  |
|  6 | Tensor<[1, 2560, s0, s1]> self = ? | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 320, 64, 64]> self = ?  | Done     | Done       | True  |
|  8 | Tensor<[1, 320, s0, s1]> self = ?  | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 320, s1, s2]> self = ?  | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, 640, s0, s1]> self = ?  | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 640, s1, s2]> self = ?  | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 960, s1, s2]> self = ?  | Unknown  | Unknown    | N/A   |
### aten.sin.default
|    | ATen Input Variations     | Status   | Isolated   | PCC   |
|---:|:--------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 160]> self = ? | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                   | Done     | Done       | True  |
|  5 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 9223372036854775807 | Done     | Done       | True  |
|  7 | Tensor<[1, 640]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 640]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  9 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Fallback   | True  |
### aten.split.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1   | Unknown  | Done       | True  |
|  1 | Tensor<[1, s0*s1, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, s0*s1, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1  | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, s1*s2, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, s1*s2, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1  | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, s1*s2, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1  | Unknown  | Unknown    | N/A   |
### aten.sym_size.int
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, s0, s1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?,<br>int dim = 3 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s1, s2]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280, s1, s2]> self = ?,<br>int dim = 3 | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 320, s1, s2]> self = ?,<br>int dim = 2  | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 320, s1, s2]> self = ?,<br>int dim = 3  | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 640, s0, s1]> self = ?,<br>int dim = 2  | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 640, s0, s1]> self = ?,<br>int dim = 3  | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 640, s1, s2]> self = ?,<br>int dim = 2  | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 640, s1, s2]> self = ?,<br>int dim = 3  | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, s0*s1, 10240]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, s0*s1, 1280]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, s0*s1, 5120]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, s0*s1, 640]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, s1*s2, 10240]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, s1*s2, 1280]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, s1*s2, 2560]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, s1*s2, 320]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1, s1*s2, 5120]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   |
| 19 | Tensor<[1, s1*s2, 640]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[10240, 1280]> self = ? | Unknown  | Done       | True  |
|  1 | Tensor<[1280, 1280]> self = ?  | Unknown  | Done       | True  |
|  2 | Tensor<[1280, 320]> self = ?   | Unknown  | Done       | True  |
|  3 | Tensor<[1280, 5120]> self = ?  | Unknown  | Done       | True  |
|  4 | Tensor<[1280, 768]> self = ?   | Unknown  | Done       | True  |
|  5 | Tensor<[2560, 320]> self = ?   | Unknown  | Done       | True  |
|  6 | Tensor<[320, 1280]> self = ?   | Unknown  | Done       | True  |
|  7 | Tensor<[320, 320]> self = ?    | Unknown  | Done       | True  |
|  8 | Tensor<[320, 768]> self = ?    | Unknown  | Done       | True  |
|  9 | Tensor<[5120, 640]> self = ?   | Unknown  | Done       | True  |
| 10 | Tensor<[640, 1280]> self = ?   | Unknown  | Done       | True  |
| 11 | Tensor<[640, 2560]> self = ?   | Unknown  | Done       | True  |
| 12 | Tensor<[640, 640]> self = ?    | Unknown  | Done       | True  |
| 13 | Tensor<[640, 768]> self = ?    | Unknown  | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | True  |
|  1 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | True  |
|  2 | Tensor<[1, 8, s0*s1, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 8, s0*s1, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 8, s1*s2, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 8, s1*s2, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 8, s1*s2, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | True  |
|  8 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | True  |
|  9 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | True  |
| 10 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 1]> self = ?,<br>int dim = 3 | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 2    | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 320, 1]> self = ?,<br>int dim = 3  | Unknown  | Done       | True  |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 2     | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 640, 1]> self = ?,<br>int dim = 3  | Unknown  | Done       | True  |
|  5 | Tensor<[1, 640]> self = ?,<br>int dim = 2     | Unknown  | Fallback   | True  |
|  6 | Tensor<[160]> self = ?,<br>int dim = 0        | Done     | Done       | True  |
|  7 | Tensor<[16]> self = ?,<br>int dim = -1        | Unknown  | Fallback   | True  |
|  8 | Tensor<[1]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  9 | Tensor<[2*s0]> self = ?,<br>int dim = -1      | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[2*s1]> self = ?,<br>int dim = -1      | Unknown  | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]           | Unknown  | Done       | True  |
|  1 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]          | Unknown  | Done       | True  |
|  2 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]        | Unknown  | Done       | True  |
|  3 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]             | Unknown  | Done       | True  |
|  4 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]          | Unknown  | Done       | False |
|  5 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]        | Unknown  | Done       | True  |
|  6 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]           | Unknown  | Done       | True  |
|  7 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]             | Unknown  | Done       | True  |
|  8 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]             | Unknown  | Done       | True  |
|  9 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                   | Unknown  | Done       | True  |
| 10 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]       | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 1280] | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [<s0*s1>, 1280]       | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, s0*s1, 2560]> self = ?,<br>List[int] size = [<s0*s1>, 2560]       | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, s0*s1, 5120]> self = ?,<br>List[int] size = [<s0*s1>, 5120]       | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]         | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 640]   | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [<s0*s1>, 640]         | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]       | Unknown  | Unknown    | N/A   |
| 19 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]         | Unknown  | Unknown    | N/A   |
| 20 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]   | Unknown  | Unknown    | N/A   |
| 21 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]     | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]       | Unknown  | Unknown    | N/A   |
| 23 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 1280] | Unknown  | Unknown    | N/A   |
| 24 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [<s1*s2>, 1280]       | Unknown  | Unknown    | N/A   |
| 25 | Tensor<[1, s1*s2, 2560]> self = ?,<br>List[int] size = [<s1*s2>, 2560]       | Unknown  | Unknown    | N/A   |
| 26 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]         | Unknown  | Unknown    | N/A   |
| 27 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 320]   | Unknown  | Unknown    | N/A   |
| 28 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [<s1*s2>, 320]         | Unknown  | Unknown    | N/A   |
| 29 | Tensor<[1, s1*s2, 5120]> self = ?,<br>List[int] size = [<s1*s2>, 5120]       | Unknown  | Unknown    | N/A   |
| 30 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]         | Unknown  | Unknown    | N/A   |
| 31 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 640]   | Unknown  | Unknown    | N/A   |
| 32 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [<s1*s2>, 640]         | Unknown  | Unknown    | N/A   |
| 33 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]       | Unknown  | Unknown    | N/A   |
| 34 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]         | Unknown  | Unknown    | N/A   |
| 35 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]         | Unknown  | Unknown    | N/A   |
| 36 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]   | Unknown  | Unknown    | N/A   |
| 37 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]     | Unknown  | Unknown    | N/A   |
| 38 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]     | Unknown  | Unknown    | N/A   |
| 39 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]           | Unknown  | Done       | True  |
| 40 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]             | Unknown  | Done       | True  |
| 41 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]                 | Unknown  | Done       | True  |
| 42 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]                   | Unknown  | Done       | True  |
| 43 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]                   | Unknown  | Done       | True  |
| 44 | Tensor<[s0*s1, 10240]> self = ?,<br>List[int] size = [1, <s0*s1>, 10240]     | Unknown  | Unknown    | N/A   |
| 45 | Tensor<[s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]       | Unknown  | Unknown    | N/A   |
| 46 | Tensor<[s0*s1, 5120]> self = ?,<br>List[int] size = [1, <s0*s1>, 5120]       | Unknown  | Unknown    | N/A   |
| 47 | Tensor<[s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]         | Unknown  | Unknown    | N/A   |
| 48 | Tensor<[s1*s2, 10240]> self = ?,<br>List[int] size = [1, <s1*s2>, 10240]     | Unknown  | Unknown    | N/A   |
| 49 | Tensor<[s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]       | Unknown  | Unknown    | N/A   |
| 50 | Tensor<[s1*s2, 2560]> self = ?,<br>List[int] size = [1, <s1*s2>, 2560]       | Unknown  | Unknown    | N/A   |
| 51 | Tensor<[s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]         | Unknown  | Unknown    | N/A   |
| 52 | Tensor<[s1*s2, 5120]> self = ?,<br>List[int] size = [1, <s1*s2>, 5120]       | Unknown  | Unknown    | N/A   |
| 53 | Tensor<[s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]         | Unknown  | Unknown    | N/A   |

