# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._assert_async.msg                           |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._scaled_dot_product_flash_attention.default |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._to_copy.default                            |                 11 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten._unsafe_index.Tensor                        |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.add.Tensor                                  |                 23 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.addmm.default                               |                 22 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.arange.default                              |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.cat.default                                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.clone.default                               |                 24 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.convolution.default                         |                 37 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.cos.default                                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.div.Tensor                                  |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.exp.default                                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.gelu.default                                |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mm.default                                  |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mul.Tensor                                  |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.native_group_norm.default                   |                 18 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.native_layer_norm.default                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.permute.default                             |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.scalar_tensor.default                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.silu.default                                |                 13 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.sin.default                                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.slice.Tensor                                |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.split.Tensor                                |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.sym_size.int                                |                 20 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.t.default                                   |                 14 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.transpose.int                               |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.unsqueeze.default                           |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.view.default                                |                 54 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._assert_async.msg
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[]> self = ?,<br>str assert_msg = assertion error | Unknown  | Unknown    | N/A   | N/A    |
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 4096, 40]> key = ?,<br>Tensor<[1, 8, 4096, 40]> value = ?       | Unknown  | Fallback   | 0.8571428656578064 | 0      |
|  1 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?             | Unknown  | Fallback   | 0.7142857313156128 | 0      |
|  2 | Tensor<[1, 8, s0*s1, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?         | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 8, s0*s1, 160]> query = ?,<br>Tensor<[1, 8, s0*s1, 160]> key = ?,<br>Tensor<[1, 8, s0*s1, 160]> value = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 8, s0*s1, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 8, s0*s1, 80]> query = ?,<br>Tensor<[1, 8, s0*s1, 80]> key = ?,<br>Tensor<[1, 8, s0*s1, 80]> value = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 8, s1*s2, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?         | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 8, s1*s2, 160]> query = ?,<br>Tensor<[1, 8, s1*s2, 160]> key = ?,<br>Tensor<[1, 8, s1*s2, 160]> value = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 8, s1*s2, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 8, s1*s2, 40]> query = ?,<br>Tensor<[1, 8, s1*s2, 40]> key = ?,<br>Tensor<[1, 8, s1*s2, 40]> value = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 8, s1*s2, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 8, s1*s2, 80]> query = ?,<br>Tensor<[1, 8, s1*s2, 80]> key = ?,<br>Tensor<[1, 8, s1*s2, 80]> value = ?    | Unknown  | Unknown    | N/A                | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1280, 2*s0, 2*s1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] dtype = torch.float32        | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                 | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16              | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, s0, 2*s1, 2*s2]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, s0, s1, s2]> self = ?,<br>Optional[int] dtype = torch.float32        | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[2*s0]> self = ?,<br>Optional[int] dtype = torch.int64                   | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2*s1]> self = ?,<br>Optional[int] dtype = torch.int64                   | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[2*s2]> self = ?,<br>Optional[int] dtype = torch.int64                   | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[2*s0, 1]>, <[2*s1]>]               | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0, s1, s2]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[2*s1, 1]>, <[2*s2]>]                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?     | Unknown  | Done       | 0.9999979619644205 | 0      |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?     | Unknown  | Done       | 0.9999979560355953 | 0      |
|  2 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?     | Unknown  | Done       | 0.9999979494240899 | 0      |
|  7 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?   | Unknown  | Done       | 0.9999979944035525 | 0      |
|  8 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?       | Unknown  | Done       | 0.9999979910172134 | 0      |
| 11 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 18 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 19 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 20 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                             | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                             | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                             | Unknown  | Unknown    | N/A                | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[10240]> self = ?,<br>Tensor<[s0*s1, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[10240]> self = ?,<br>Tensor<[s1*s2, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1280]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?       | Unknown  | Done       | 0.999962630128045  | 0      |
|  3 | Tensor<[1280]> self = ?,<br>Tensor<[1, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ?         | Unknown  | Done       | 0.9999745771520074 | 0      |
|  4 | Tensor<[1280]> self = ?,<br>Tensor<[s0*s1, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1280]> self = ?,<br>Tensor<[s0*s1, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1280]> self = ?,<br>Tensor<[s1*s2, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1280]> self = ?,<br>Tensor<[s1*s2, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[2560]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 2560]> mat2 = ?      | Unknown  | Done       | 0.999976330890746  | 0      |
|  9 | Tensor<[2560]> self = ?,<br>Tensor<[s1*s2, 320]> mat1 = ?,<br>Tensor<[320, 2560]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[320]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?         | Unknown  | Done       | 0.9997677219760441 | 0      |
| 11 | Tensor<[320]> self = ?,<br>Tensor<[4096, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?      | Unknown  | Done       | 0.9999616078513479 | 0      |
| 12 | Tensor<[320]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?        | Unknown  | Done       | 0.9999727483456324 | 0      |
| 13 | Tensor<[320]> self = ?,<br>Tensor<[s1*s2, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[320]> self = ?,<br>Tensor<[s1*s2, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 15 | Tensor<[5120]> self = ?,<br>Tensor<[s0*s1, 640]> mat1 = ?,<br>Tensor<[640, 5120]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[5120]> self = ?,<br>Tensor<[s1*s2, 640]> mat1 = ?,<br>Tensor<[640, 5120]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[640]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 640]> mat2 = ?         | Unknown  | Done       | 0.9999634636559308 | 0      |
| 18 | Tensor<[640]> self = ?,<br>Tensor<[s0*s1, 2560]> mat1 = ?,<br>Tensor<[2560, 640]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 19 | Tensor<[640]> self = ?,<br>Tensor<[s0*s1, 640]> mat1 = ?,<br>Tensor<[640, 640]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 20 | Tensor<[640]> self = ?,<br>Tensor<[s1*s2, 2560]> mat1 = ?,<br>Tensor<[2560, 640]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[640]> self = ?,<br>Tensor<[s1*s2, 640]> mat1 = ?,<br>Tensor<[640, 640]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<2*s0> end = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | number<2*s1> end = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  2 | number<2*s2> end = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 160]>, <[1, 160]>],<br>int dim = -1 | Unknown  | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, s1, s2]> self = ?                                                           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 320, 64, 64]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 320, s1, s2]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 320, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 4096, 1280]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 4096, 320]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 640, s0, s1]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 640, s0, s1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 640, s1, s2]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 640, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, s0*s1, 1280]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, s0*s1, 2560]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, s0*s1, 5120]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, s0*s1, 640]> self = ?                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, s1*s2, 1280]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, s1*s2, 2560]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, s1*s2, 320]> self = ?                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, s1*s2, 5120]> self = ?                                                            | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, s1*s2, 640]> self = ?                                                             | Unknown  | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.9956649266937674 | 6      |
|  1 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9958647649544358 | 6      |
|  2 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[640, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Tensor<[640, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[1280, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[1280, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[640, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Tensor<[640, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9999488765591639 | 6      |
| 14 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9870563836989875 | 6      |
| 15 | Tensor<[1, 2560, s0, s1]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 2560, s0, s1]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.9999727874569225 | 6      |
| 18 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Fallback   | 1.0                | -1     |
| 19 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.9993868989833645 | 6      |
| 20 | Tensor<[1, 320, s0, s1]> input = ?,<br>Tensor<[640, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[1, 320, s0, s1]> input = ?,<br>Tensor<[640, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 320, s1, s2]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 320, s1, s2]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 640, s0, s1]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 640, s0, s1]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 640, s0, s1]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[1280, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A                | N/A    |
| 28 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[1280, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A                | N/A    |
| 29 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[320, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 30 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[320, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 31 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 32 | Tensor<[1, 640, s1, s2]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 33 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 34 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[320, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 35 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[640, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
| 36 | Tensor<[1, 960, s1, s2]> input = ?,<br>Tensor<[640, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A                | N/A    |
### aten.cos.default
|    | ATen Input Variations     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 160]> self = ? | Unknown  | Done       | 0.999993 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 160                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0   | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0  | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0    | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor other = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor other = 1.0  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor other = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor other = 1.0   | Unknown  | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[160]> self = ?  | Unknown  | Done       | 0.999961 |      0 |
### aten.gelu.default
|    | ATen Input Variations             | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 4096, 1280]> self = ?  | Unknown  | Done       | 0.9999913267350212 | 0      |
|  1 | Tensor<[1, s0*s1, 2560]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, s0*s1, 5120]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, s1*s2, 1280]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, s1*s2, 2560]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, s1*s2, 5120]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.mm.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[4096, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?     | Unknown  | Done       | 0.9999739659619848 | 0      |
|  1 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 1280]> mat2 = ?       | Unknown  | Done       | 0.9999681833273466 | 0      |
|  2 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 320]> mat2 = ?        | Unknown  | Done       | 0.9998860098279143 | 0      |
|  3 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 640]> mat2 = ?        | Unknown  | Done       | 0.9999694523112039 | 0      |
|  4 | Tensor<[s0*s1, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[s0*s1, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[s1*s2, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[s1*s2, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[s1*s2, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                   | Unknown  | Done       | 0.9999954112073149 | 0      |
|  2 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?   | Unknown  | Done       | 0.9999959395448531 | 0      |
|  3 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05         | Unknown  | Fallback   | 1.0   | 0      |
|  1 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, s0, s1]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-06 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1280, s1, s2]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-06 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1920, s1, s2]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int N = 1,<br>int C = 1920,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05         | Unknown  | Fallback   | 1.0   | 0      |
|  7 | Tensor<[1, 2560, s0, s1]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05         | Unknown  | Fallback   | 1.0   | 0      |
|  9 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-06         | Unknown  | Fallback   | 1.0   | 0      |
| 10 | Tensor<[1, 320, s0, s1]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 320, s1, s2]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 320, s1, s2]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-06     | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 640, s0, s1]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 640, s0, s1]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s0*s1> HxW = ?,<br>int group = 32,<br>float eps = 1e-06     | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 640, s1, s2]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 640, s1, s2]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-06     | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 960, s1, s2]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int N = 1,<br>int C = 960,<br>int<s1*s2> HxW = ?,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 4096, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05      | Unknown  | Done       | N/A   | 1      |
|  1 | Tensor<[1, s0*s1, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0*s1, 640]> input = ?,<br>List[int] normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, s1*s2, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1*s2, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, s1*s2, 640]> input = ?,<br>List[int] normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 320, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 640, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 640, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Unknown    | N/A   | N/A    |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<Eq(s0, 640)> s = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?   | Unknown  | Done       | 0.9999826566059398 | 0      |
|  1 | Tensor<[1, 1280, s0, s1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1280, s1, s2]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280]> self = ?         | Unknown  | Done       | 0.9999805643943921 | 0      |
|  4 | Tensor<[1, 1920, s1, s2]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 2560, 8, 8]> self = ?   | Unknown  | Done       | 0.9999823586153632 | 0      |
|  6 | Tensor<[1, 2560, s0, s1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 320, 64, 64]> self = ?  | Unknown  | Done       | 0.9999823607042638 | 0      |
|  8 | Tensor<[1, 320, s0, s1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 320, s1, s2]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 640, s0, s1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 640, s1, s2]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 960, s1, s2]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
### aten.sin.default
|    | ATen Input Variations     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 160]> self = ? | Unknown  | Done       | 0.999997 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1280]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                   | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 640]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 640]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       | 1.0   | -1     |
### aten.split.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1   | Unknown  | Done       | 1.0   | 1      |
|  1 | Tensor<[1, s0*s1, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0*s1, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, s1*s2, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1*s2, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, s1*s2, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1  | Unknown  | Unknown    | N/A   | N/A    |
### aten.sym_size.int
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, s0, s1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, s0, s1]> self = ?,<br>int dim = 3 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, s1, s2]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, s1, s2]> self = ?,<br>int dim = 3 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 320, s1, s2]> self = ?,<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 320, s1, s2]> self = ?,<br>int dim = 3  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 640, s0, s1]> self = ?,<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 640, s0, s1]> self = ?,<br>int dim = 3  | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 640, s1, s2]> self = ?,<br>int dim = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 640, s1, s2]> self = ?,<br>int dim = 3  | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s0*s1, 10240]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0*s1, 1280]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s0*s1, 5120]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s0*s1, 640]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, s1*s2, 10240]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, s1*s2, 1280]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, s1*s2, 2560]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, s1*s2, 320]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, s1*s2, 5120]> self = ?,<br>int dim = 1  | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, s1*s2, 640]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10240, 1280]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1280, 1280]> self = ?  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1280, 320]> self = ?   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1280, 5120]> self = ?  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1280, 768]> self = ?   | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[2560, 320]> self = ?   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[320, 1280]> self = ?   | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[320, 320]> self = ?    | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[320, 768]> self = ?    | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[5120, 640]> self = ?   | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[640, 1280]> self = ?   | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[640, 2560]> self = ?   | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[640, 640]> self = ?    | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[640, 768]> self = ?    | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 8, s0*s1, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 8, s0*s1, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 8, s1*s2, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 8, s1*s2, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 8, s1*s2, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 1]> self = ?,<br>int dim = 3 | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 2    | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 320, 1]> self = ?,<br>int dim = 3  | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 640, 1]> self = ?,<br>int dim = 3  | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 640]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[160]> self = ?,<br>int dim = 0        | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1]> self = ?,<br>int dim = 1          | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[2*s0]> self = ?,<br>int dim = -1      | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[2*s1]> self = ?,<br>int dim = -1      | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]          | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]        | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]          | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]        | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]           | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]             | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                   | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]       | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 1280] | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [<s0*s1>, 1280]       | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s0*s1, 2560]> self = ?,<br>List[int] size = [<s0*s1>, 2560]       | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, s0*s1, 5120]> self = ?,<br>List[int] size = [<s0*s1>, 5120]       | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]         | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 640]   | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [<s0*s1>, 640]         | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]       | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]         | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]   | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]     | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]       | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 1280] | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [<s1*s2>, 1280]       | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, s1*s2, 2560]> self = ?,<br>List[int] size = [<s1*s2>, 2560]       | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]         | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 320]   | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [<s1*s2>, 320]         | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, s1*s2, 5120]> self = ?,<br>List[int] size = [<s1*s2>, 5120]       | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]         | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 640]   | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [<s1*s2>, 640]         | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]       | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]         | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]         | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]   | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]     | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]     | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]           | Unknown  | Done       | 1.0   | -1     |
| 40 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]             | Unknown  | Done       | 1.0   | -1     |
| 41 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]                 | Unknown  | Done       | 1.0   | -1     |
| 42 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]                   | Unknown  | Done       | 1.0   | -1     |
| 43 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]                   | Unknown  | Done       | 1.0   | -1     |
| 44 | Tensor<[s0*s1, 10240]> self = ?,<br>List[int] size = [1, <s0*s1>, 10240]     | Unknown  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]       | Unknown  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[s0*s1, 5120]> self = ?,<br>List[int] size = [1, <s0*s1>, 5120]       | Unknown  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]         | Unknown  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[s1*s2, 10240]> self = ?,<br>List[int] size = [1, <s1*s2>, 10240]     | Unknown  | Unknown    | N/A   | N/A    |
| 49 | Tensor<[s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]       | Unknown  | Unknown    | N/A   | N/A    |
| 50 | Tensor<[s1*s2, 2560]> self = ?,<br>List[int] size = [1, <s1*s2>, 2560]       | Unknown  | Unknown    | N/A   | N/A    |
| 51 | Tensor<[s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]         | Unknown  | Unknown    | N/A   | N/A    |
| 52 | Tensor<[s1*s2, 5120]> self = ?,<br>List[int] size = [1, <s1*s2>, 5120]       | Unknown  | Unknown    | N/A   | N/A    |
| 53 | Tensor<[s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]         | Unknown  | Unknown    | N/A   | N/A    |

