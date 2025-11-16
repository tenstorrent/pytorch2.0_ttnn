# High Level Operations Status
|    | Operations                                               |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:---------------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention_for_cpu.default |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default                                    |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  2 | aten._unsafe_index.Tensor                                |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten._unsafe_view.default                                |                  7 |           7 |         0 |          0 | ✅          |    1    |
|  4 | aten.add.Tensor                                          |                 12 |          12 |         0 |          0 | ✅          |    1    |
|  5 | aten.addmm.default                                       |                 16 |           4 |        12 |          0 | ✅          |    1    |
|  6 | aten.cat.default                                         |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  7 | aten.clone.default                                       |                 16 |           0 |        16 |          0 | ✅          |    1    |
|  8 | aten.convolution.default                                 |                 35 |          34 |         0 |          0 | 🚧          |    0.97 |
|  9 | aten.cos.default                                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.div.Tensor                                          |                 10 |          10 |         0 |          0 | ✅          |    1    |
| 11 | aten.exp.default                                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.gelu.default                                        |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 13 | aten.mm.default                                          |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 14 | aten.mul.Tensor                                          |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 15 | aten.native_group_norm.default                           |                 18 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.native_layer_norm.default                           |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 17 | aten.permute.default                                     |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 18 | aten.silu.default                                        |                 15 |          15 |         0 |          0 | ✅          |    1    |
| 19 | aten.sin.default                                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 20 | aten.slice.Tensor                                        |                 10 |           2 |         8 |          0 | ✅          |    1    |
| 21 | aten.split.Tensor                                        |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 22 | aten.t.default                                           |                 14 |           0 |        14 |          0 | ✅          |    1    |
| 23 | aten.transpose.int                                       |                 11 |          11 |         0 |          0 | ✅          |    1    |
| 24 | aten.unsqueeze.default                                   |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 25 | aten.view.default                                        |                 36 |          36 |         0 |          0 | ✅          |    1    |
***
### aten._scaled_dot_product_flash_attention_for_cpu.default
|    | ATen Input Variations                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 1024, 80]> key = ?,<br>Tensor<[1, 8, 1024, 80]> value = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?       | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 256, 160]> key = ?,<br>Tensor<[1, 8, 256, 160]> value = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 4096, 40]> key = ?,<br>Tensor<[1, 8, 4096, 40]> value = ? | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 64, 160]> key = ?,<br>Tensor<[1, 8, 64, 160]> value = ?    | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?      | Done     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32             | Done     | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16          | Done     | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32   | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 640, 64, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Done     | Unknown    | N/A   | N/A    |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_35, _folded__to_copy_8] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_28, _folded__to_copy_4]   | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_42, _folded__to_copy_12] | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320] | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[64, 1280]> self = ?,<br>List[int] size = [1, 64, 1280]   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]     | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]       | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor<[1, 1024, 640]> other = ?       | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?   | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<[1, 1280, 16, 16]> other = ? | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?     | Done     | Done       | 0.9999979780730145 | 0      |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?     | Done     | Done       | 0.9999980042404504 | 0      |
|  5 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?       | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?     | Done     | Done       | 0.9999980031160945 | 0      |
|  7 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?   | Done     | Done       | 0.9999979872919947 | 0      |
|  8 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?       | Done     | Done       | 0.9999979839732381 | 0      |
|  9 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor<[1, 64, 1280]> other = ?         | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<[1, 640, 32, 32]> other = ?   | Done     | Unknown    | N/A                | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[10240]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ? | Removed  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[10240]> self = ?,<br>Tensor<[64, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ?  | Removed  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1280]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?     | Done     | Done       | 0.9999612978357579 | 0      |
|  3 | Tensor<[1280]> self = ?,<br>Tensor<[1, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ?       | Done     | Done       | 0.9999696758167204 | 0      |
|  4 | Tensor<[1280]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?   | Removed  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1280]> self = ?,<br>Tensor<[256, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?   | Removed  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1280]> self = ?,<br>Tensor<[64, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?    | Removed  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1280]> self = ?,<br>Tensor<[64, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?    | Removed  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[2560]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 2560]> mat2 = ?    | Removed  | Done       | 0.9999763546023326 | 0      |
|  9 | Tensor<[320]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?       | Done     | Done       | 0.9999614166878024 | 0      |
| 10 | Tensor<[320]> self = ?,<br>Tensor<[4096, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?    | Removed  | Done       | 0.9999618496443158 | 0      |
| 11 | Tensor<[320]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?      | Removed  | Done       | 0.9999728366145555 | 0      |
| 12 | Tensor<[5120]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 5120]> mat2 = ?    | Removed  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[640]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 640]> mat2 = ?       | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[640]> self = ?,<br>Tensor<[1024, 2560]> mat1 = ?,<br>Tensor<[2560, 640]> mat2 = ?    | Removed  | Unknown    | N/A                | N/A    |
| 15 | Tensor<[640]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 640]> mat2 = ?      | Removed  | Unknown    | N/A                | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1280, 16, 16]>, <[1, 1280, 16, 16]>],<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 1280, 16, 16]>, <[1, 640, 16, 16]>],<br>int dim = 1  | Done     | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 1280, 32, 32]>, <[1, 640, 32, 32]>],<br>int dim = 1  | Done     | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, 1280, 8, 8]>, <[1, 1280, 8, 8]>],<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[1, 160]>, <[1, 160]>],<br>int dim = -1                  | Done     | Done       | 1.0   | 0      |
|  5 | List[Tensor] tensors = [<[1, 320, 64, 64]>, <[1, 320, 64, 64]>],<br>int dim = 1   | Done     | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1, 640, 32, 32]>, <[1, 320, 32, 32]>],<br>int dim = 1   | Done     | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[1, 640, 32, 32]>, <[1, 640, 32, 32]>],<br>int dim = 1   | Done     | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[1, 640, 64, 64]>, <[1, 320, 64, 64]>],<br>int dim = 1   | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 2560]> self = ?                                                             | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1024, 640]> self = ?                                                              | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?                                                           | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?                                                             | Removed  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 256, 1280]> self = ?                                                              | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 256, 5120]> self = ?                                                              | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 320, 64, 64]> self = ?                                                            | Removed  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 4096, 1280]> self = ?                                                             | Removed  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 4096, 320]> self = ?                                                              | Removed  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 64, 1280]> self = ?                                                               | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 64, 5120]> self = ?                                                               | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 640, 32, 32]> self = ?                                                            | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.9956851302334657 | 1      |
|  2 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[640, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[640, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9959475170662695 | 1      |
|  8 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Tensor<[1280, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Tensor<[1280, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Tensor<[640, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Tensor<[640, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.9994689048539944 | 1      |
| 15 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.987056258805129  | 1      |
| 16 | Tensor<[1, 320, 32, 32]> input = ?,<br>Tensor<[640, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 320, 32, 32]> input = ?,<br>Tensor<[640, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 18 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999557488191481 | 1      |
| 19 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Fallback   | 1.0                | -1     |
| 20 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9993885765596    | 1      |
| 21 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[4, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[4]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 4, 64, 64]> input = ?,<br>Tensor<[320, 4, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 640, 16, 16]> input = ?,<br>Tensor<[1280, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 640, 16, 16]> input = ?,<br>Tensor<[1280, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 28 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[320, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 29 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[320, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 30 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 31 | Tensor<[1, 960, 32, 32]> input = ?,<br>Tensor<[640, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 32 | Tensor<[1, 960, 32, 32]> input = ?,<br>Tensor<[640, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 33 | Tensor<[1, 960, 64, 64]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
| 34 | Tensor<[1, 960, 64, 64]> input = ?,<br>Tensor<[320, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A                | N/A    |
### aten.cos.default
|    | ATen Input Variations     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 160]> self = ? | Done     | Done       | 0.999988 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 160                    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor other = 1.0    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor other = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0   | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor other = 1.0    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0  | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0    | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor other = 1.0     | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor other = 1.0  | Done     | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[160]> self = ?  | Done     | Done       | 0.999997 |      0 |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 2560]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 256, 5120]> self = ?  | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 4096, 1280]> self = ? | Done     | Done       | 0.9999913379124985 | 0      |
|  3 | Tensor<[1, 64, 5120]> self = ?   | Done     | Unknown    | N/A                | N/A    |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?   | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[256, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[4096, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?   | Done     | Done       | 0.99997416966312   | 0      |
|  3 | Tensor<[64, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ?  | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 1280]> mat2 = ?     | Done     | Done       | 0.9999687177519623 | 0      |
|  5 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 320]> mat2 = ?      | Done     | Done       | 0.9999697198176881 | 0      |
|  6 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 640]> mat2 = ?      | Done     | Done       | 0.9999690778420982 | 0      |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 2560]> self = ?,<br>Tensor<[1, 1024, 2560]> other = ? | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                         | Done     | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                 | Done     | Done       | 0.9999949620654826 | 0      |
|  3 | Tensor<[1, 256, 5120]> self = ?,<br>Tensor<[1, 256, 5120]> other = ?   | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ? | Done     | Done       | 0.9999959613130432 | 0      |
|  5 | Tensor<[1, 64, 5120]> self = ?,<br>Tensor<[1, 64, 5120]> other = ?     | Done     | Unknown    | N/A                | N/A    |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05  | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-06  | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05 | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05     | None     | Fallback   | 1.0   | 0      |
|  4 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-06     | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int N = 1,<br>int C = 1920,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05  | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int N = 1,<br>int C = 1920,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05 | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05  | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05     | None     | Fallback   | 1.0   | 0      |
|  9 | Tensor<[1, 320, 32, 32]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05     | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05     | None     | Fallback   | 1.0   | 0      |
| 11 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-06     | None     | Fallback   | 1.0   | 0      |
| 12 | Tensor<[1, 640, 16, 16]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05      | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 640, 32, 32]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05     | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 640, 32, 32]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-06     | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 640, 64, 64]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05     | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 960, 32, 32]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int N = 1,<br>int C = 960,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05     | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 960, 64, 64]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int N = 1,<br>int C = 960,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05     | None     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 640]> input = ?,<br>List[int] normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float eps = 1e-05    | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 256, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 4096, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | 0.9993518530304687 | 3      |
|  3 | Tensor<[1, 64, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05  | Done     | Unknown    | N/A                | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 3, 1]   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 16, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 32, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 8, 8, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2]   | Done     | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1280, 32, 32]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?   | Done     | Done       | 0.9999882925407249 | 0      |
|  3 | Tensor<[1, 1280]> self = ?         | Done     | Done       | 0.9999873068113269 | 0      |
|  4 | Tensor<[1, 1920, 16, 16]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 1920, 32, 32]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 2560, 16, 16]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 2560, 8, 8]> self = ?   | Done     | Done       | 0.9999880961698088 | 0      |
|  8 | Tensor<[1, 320, 32, 32]> self = ?  | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 320, 64, 64]> self = ?  | Done     | Done       | 0.9999882863664363 | 0      |
| 10 | Tensor<[1, 640, 16, 16]> self = ?  | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 640, 32, 32]> self = ?  | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 640, 64, 64]> self = ?  | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 960, 32, 32]> self = ?  | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 960, 64, 64]> self = ?  | Done     | Unknown    | N/A                | N/A    |
### aten.sin.default
|    | ATen Input Variations     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 160]> self = ? | Done     | Done       | 0.999997 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1280]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                   | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 9223372036854775807 | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 640]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 640]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       | 1.0   | -1     |
### aten.split.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 64, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1  | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10240, 1280]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1280, 1280]> self = ?  | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1280, 320]> self = ?   | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1280, 5120]> self = ?  | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[1280, 768]> self = ?   | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[2560, 320]> self = ?   | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[320, 1280]> self = ?   | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[320, 320]> self = ?    | Removed  | Done       |     1 |      0 |
|  8 | Tensor<[320, 768]> self = ?    | Removed  | Done       |     1 |      0 |
|  9 | Tensor<[5120, 640]> self = ?   | Removed  | Done       |     1 |      0 |
| 10 | Tensor<[640, 1280]> self = ?   | Removed  | Done       |     1 |      0 |
| 11 | Tensor<[640, 2560]> self = ?   | Removed  | Done       |     1 |      0 |
| 12 | Tensor<[640, 640]> self = ?    | Removed  | Done       |     1 |      0 |
| 13 | Tensor<[640, 768]> self = ?    | Removed  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 64, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 8, 1024, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 8, 256, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 8, 64, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | 1.0   | 0      |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280, 1]> self = ?,<br>int dim = 3 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 2    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 320, 1]> self = ?,<br>int dim = 3  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 2     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 640, 1]> self = ?,<br>int dim = 3  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 640]> self = ?,<br>int dim = 2     | Done     | Done       |     1 |      0 |
|  6 | Tensor<[160]> self = ?,<br>int dim = 0        | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1]> self = ?,<br>int dim = 1          | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 2560]> self = ?,<br>List[int] size = [1024, 2560]     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1, 32, 32, 640]  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1024, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 16, 16, 1280]> self = ?,<br>List[int] size = [1, 256, 1280] | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]   | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 16, 16, 1280] | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]       | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 256, 5120]> self = ?,<br>List[int] size = [256, 5120]       | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]   | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 32, 32, 640]> self = ?,<br>List[int] size = [1, 1024, 640]  | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]     | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]    | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]  | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]       | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]    | Done     | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 64, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]    | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 64, 1280]> self = ?,<br>List[int] size = [1, 8, 8, 1280]    | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 64, 1280]> self = ?,<br>List[int] size = [64, 1280]         | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 64, 5120]> self = ?,<br>List[int] size = [64, 5120]         | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]  | Done     | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 64, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]    | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 8, 8, 1280]> self = ?,<br>List[int] size = [1, 64, 1280]    | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]     | Done     | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]       | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]       | Done     | Done       | 1.0   | 0      |
| 27 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]             | Done     | Done       | 1.0   | 0      |
| 28 | Tensor<[1024, 5120]> self = ?,<br>List[int] size = [1, 1024, 5120]     | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]       | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[256, 10240]> self = ?,<br>List[int] size = [1, 256, 10240]     | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]       | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]     | Done     | Done       | 1.0   | 0      |
| 33 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]       | Done     | Done       | 1.0   | 0      |
| 34 | Tensor<[64, 10240]> self = ?,<br>List[int] size = [1, 64, 10240]       | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[64, 1280]> self = ?,<br>List[int] size = [1, 64, 1280]         | Done     | Unknown    | N/A   | N/A    |

