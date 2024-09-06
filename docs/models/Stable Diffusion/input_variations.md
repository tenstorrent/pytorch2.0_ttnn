# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |
|---:|:-------------------------------------------------|-------------------:|------------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  8 |           0 |
|  1 | aten._to_copy.default                            |                  4 |           0 |
|  2 | aten._unsafe_index.Tensor                        |                  3 |           0 |
|  3 | aten.add.Tensor                                  |                 15 |          15 |
|  4 | aten.addmm.default                               |                 16 |          16 |
|  5 | aten.arange.default                              |                  3 |           0 |
|  6 | aten.arange.start                                |                  1 |           0 |
|  7 | aten.cat.default                                 |                  9 |           0 |
|  8 | aten.clone.default                               |                 16 |          12 |
|  9 | aten.convolution.default                         |                 35 |           0 |
| 10 | aten.cos.default                                 |                  1 |           1 |
| 11 | aten.div.Tensor                                  |                 10 |           9 |
| 12 | aten.exp.default                                 |                  1 |           1 |
| 13 | aten.expand.default                              |                  1 |           0 |
| 14 | aten.gelu.default                                |                  4 |           4 |
| 15 | aten.lift_fresh_copy.default                     |                  1 |           0 |
| 16 | aten.mm.default                                  |                  7 |           7 |
| 17 | aten.mul.Tensor                                  |                 10 |          10 |
| 18 | aten.native_group_norm.default                   |                 18 |           0 |
| 19 | aten.native_layer_norm.default                   |                  4 |           4 |
| 20 | aten.permute.default                             |                  8 |           8 |
| 21 | aten.silu.default                                |                 15 |          15 |
| 22 | aten.sin.default                                 |                  1 |           1 |
| 23 | aten.slice.Tensor                                |                 10 |           0 |
| 24 | aten.split.Tensor                                |                  4 |           0 |
| 25 | aten.t.default                                   |                 14 |          14 |
| 26 | aten.transpose.int                               |                 11 |          11 |
| 27 | aten.unsqueeze.default                           |                 11 |           5 |
| 28 | aten.view.default                                |                 39 |           0 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 1024, 80]> key = ?,<br>Tensor<[1, 8, 1024, 80]> value = ? | Unknown  |
|  1 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?       | Unknown  |
|  2 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 256, 160]> key = ?,<br>Tensor<[1, 8, 256, 160]> value = ? | Unknown  |
|  3 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?     | Unknown  |
|  4 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 4096, 40]> key = ?,<br>Tensor<[1, 8, 4096, 40]> value = ? | Unknown  |
|  5 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?       | Unknown  |
|  6 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 64, 160]> key = ?,<br>Tensor<[1, 8, 64, 160]> value = ?    | Unknown  |
|  7 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?      | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
|  1 | Tensor<[16]> self = ?,<br>Optional[int] dtype = torch.int64     | Unknown  |
|  2 | Tensor<[32]> self = ?,<br>Optional[int] dtype = torch.int64     | Unknown  |
|  3 | Tensor<[64]> self = ?,<br>Optional[int] dtype = torch.int64     | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, 'torch.Size([32, 1])', 'torch.Size([32])'] | Unknown  |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, 'torch.Size([16, 1])', 'torch.Size([16])']   | Unknown  |
|  2 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, 'torch.Size([64, 1])', 'torch.Size([64])']  | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor<[1, 1024, 640]> other = ?       | Done     |
|  1 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?   | Done     |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<[1, 1280, 16, 16]> other = ? | Done     |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?     | Done     |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?     | Done     |
|  5 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?       | Done     |
|  6 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?     | Done     |
|  7 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?   | Done     |
|  8 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?       | Done     |
|  9 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor<[1, 64, 1280]> other = ?         | Done     |
| 10 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?     | Done     |
| 11 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<[1, 640, 32, 32]> other = ?   | Done     |
| 12 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                               | Done     |
| 13 | Tensor<[32]> self = ?,<br>Tensor other = 0.0                               | Done     |
| 14 | Tensor<[64]> self = ?,<br>Tensor other = 0.0                               | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[10240]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ? | Done     |
|  1 | Tensor<[10240]> self = ?,<br>Tensor<[64, 1280]> mat1 = ?,<br>Tensor<[1280, 10240]> mat2 = ?  | Done     |
|  2 | Tensor<[1280]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?     | Done     |
|  3 | Tensor<[1280]> self = ?,<br>Tensor<[1, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ?       | Done     |
|  4 | Tensor<[1280]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?   | Done     |
|  5 | Tensor<[1280]> self = ?,<br>Tensor<[256, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?   | Done     |
|  6 | Tensor<[1280]> self = ?,<br>Tensor<[64, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ?    | Done     |
|  7 | Tensor<[1280]> self = ?,<br>Tensor<[64, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ?    | Done     |
|  8 | Tensor<[2560]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 2560]> mat2 = ?    | Done     |
|  9 | Tensor<[320]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?       | Done     |
| 10 | Tensor<[320]> self = ?,<br>Tensor<[4096, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ?    | Done     |
| 11 | Tensor<[320]> self = ?,<br>Tensor<[4096, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?      | Done     |
| 12 | Tensor<[5120]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 5120]> mat2 = ?    | Done     |
| 13 | Tensor<[640]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 640]> mat2 = ?       | Done     |
| 14 | Tensor<[640]> self = ?,<br>Tensor<[1024, 2560]> mat1 = ?,<br>Tensor<[2560, 640]> mat2 = ?    | Done     |
| 15 | Tensor<[640]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 640]> mat2 = ?      | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 16,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | number end = 32,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  2 | number end = 64,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 160,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = ['torch.Size([1, 1280, 16, 16])', 'torch.Size([1, 1280, 16, 16])'],<br>int dim = 1 | Unknown  |
|  1 | List[Tensor] tensors = ['torch.Size([1, 1280, 16, 16])', 'torch.Size([1, 640, 16, 16])'],<br>int dim = 1  | Unknown  |
|  2 | List[Tensor] tensors = ['torch.Size([1, 1280, 32, 32])', 'torch.Size([1, 640, 32, 32])'],<br>int dim = 1  | Unknown  |
|  3 | List[Tensor] tensors = ['torch.Size([1, 1280, 8, 8])', 'torch.Size([1, 1280, 8, 8])'],<br>int dim = 1     | Unknown  |
|  4 | List[Tensor] tensors = ['torch.Size([1, 160])', 'torch.Size([1, 160])'],<br>int dim = -1                  | Unknown  |
|  5 | List[Tensor] tensors = ['torch.Size([1, 320, 64, 64])', 'torch.Size([1, 320, 64, 64])'],<br>int dim = 1   | Unknown  |
|  6 | List[Tensor] tensors = ['torch.Size([1, 640, 32, 32])', 'torch.Size([1, 320, 32, 32])'],<br>int dim = 1   | Unknown  |
|  7 | List[Tensor] tensors = ['torch.Size([1, 640, 32, 32])', 'torch.Size([1, 640, 32, 32])'],<br>int dim = 1   | Unknown  |
|  8 | List[Tensor] tensors = ['torch.Size([1, 640, 64, 64])', 'torch.Size([1, 320, 64, 64])'],<br>int dim = 1   | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 2560]> self = ?                                                             | Done     |
|  1 | Tensor<[1, 1024, 640]> self = ?                                                              | Unknown  |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?                                                           | Done     |
|  3 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?                                                             | Done     |
|  5 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  6 | Tensor<[1, 256, 1280]> self = ?                                                              | Unknown  |
|  7 | Tensor<[1, 256, 5120]> self = ?                                                              | Done     |
|  8 | Tensor<[1, 320, 64, 64]> self = ?                                                            | Done     |
|  9 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     |
| 10 | Tensor<[1, 4096, 1280]> self = ?                                                             | Done     |
| 11 | Tensor<[1, 4096, 320]> self = ?                                                              | Unknown  |
| 12 | Tensor<[1, 64, 1280]> self = ?                                                               | Unknown  |
| 13 | Tensor<[1, 64, 5120]> self = ?                                                               | Done     |
| 14 | Tensor<[1, 640, 32, 32]> self = ?                                                            | Done     |
| 15 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  1 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  2 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  3 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  4 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[640, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  5 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[640, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  6 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  7 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  8 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Tensor<[1280, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  9 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Tensor<[1280, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 10 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Tensor<[640, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 11 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Tensor<[640, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 12 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 13 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 14 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 15 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 16 | Tensor<[1, 320, 32, 32]> input = ?,<br>Tensor<[640, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 17 | Tensor<[1, 320, 32, 32]> input = ?,<br>Tensor<[640, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 18 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 19 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 20 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 21 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[4, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[4]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 22 | Tensor<[1, 4, 64, 64]> input = ?,<br>Tensor<[320, 4, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 23 | Tensor<[1, 640, 16, 16]> input = ?,<br>Tensor<[1280, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 24 | Tensor<[1, 640, 16, 16]> input = ?,<br>Tensor<[1280, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 25 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 26 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 27 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 28 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[320, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 29 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[320, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 30 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 31 | Tensor<[1, 960, 32, 32]> input = ?,<br>Tensor<[640, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 32 | Tensor<[1, 960, 32, 32]> input = ?,<br>Tensor<[640, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 33 | Tensor<[1, 960, 64, 64]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 34 | Tensor<[1, 960, 64, 64]> input = ?,<br>Tensor<[320, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
### aten.cos.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[1, 160]> self = ? | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor other = 1.0    | Done     |
|  1 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor other = 1.0 | Done     |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1     | Done     |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0   | Done     |
|  4 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor other = 1.0    | Done     |
|  5 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0  | Done     |
|  6 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0    | Done     |
|  7 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor other = 1.0     | Done     |
|  8 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor other = 1.0  | Done     |
|  9 | Tensor<[160]> self = ?,<br>Tensor other = 160             | Unknown  |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[160]> self = ?  | Done     |
### aten.expand.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>List[int] size = [1] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1024, 2560]> self = ? | Done     |
|  1 | Tensor<[1, 256, 5120]> self = ?  | Done     |
|  2 | Tensor<[1, 4096, 1280]> self = ? | Done     |
|  3 | Tensor<[1, 64, 5120]> self = ?   | Done     |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?   | Done     |
|  1 | Tensor<[256, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Done     |
|  2 | Tensor<[4096, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?   | Done     |
|  3 | Tensor<[64, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ?  | Done     |
|  4 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 1280]> mat2 = ?     | Done     |
|  5 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 320]> mat2 = ?      | Done     |
|  6 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 640]> mat2 = ?      | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 2560]> self = ?,<br>Tensor<[1, 1024, 2560]> other = ? | Done     |
|  1 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                         | Done     |
|  2 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                 | Done     |
|  3 | Tensor<[1, 256, 5120]> self = ?,<br>Tensor<[1, 256, 5120]> other = ?   | Done     |
|  4 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ? | Done     |
|  5 | Tensor<[1, 64, 5120]> self = ?,<br>Tensor<[1, 64, 5120]> other = ?     | Done     |
|  6 | Tensor<[160]> self = ?,<br>Tensor other = -9.210340371976184           | Done     |
|  7 | Tensor<[16]> self = ?,<br>Tensor other = 0.5                           | Done     |
|  8 | Tensor<[32]> self = ?,<br>Tensor other = 0.5                           | Done     |
|  9 | Tensor<[64]> self = ?,<br>Tensor other = 0.5                           | Done     |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05  | Unknown  |
|  1 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-06  | Unknown  |
|  2 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05 | Unknown  |
|  3 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
|  4 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int N = 1,<br>int C = 1280,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-06     | Unknown  |
|  5 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int N = 1,<br>int C = 1920,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05  | Unknown  |
|  6 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int N = 1,<br>int C = 1920,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05 | Unknown  |
|  7 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05  | Unknown  |
|  8 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int N = 1,<br>int C = 2560,<br>int HxW = 64,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
|  9 | Tensor<[1, 320, 32, 32]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
| 10 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
| 11 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-06     | Unknown  |
| 12 | Tensor<[1, 640, 16, 16]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 256,<br>int group = 32,<br>float eps = 1e-05      | Unknown  |
| 13 | Tensor<[1, 640, 32, 32]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
| 14 | Tensor<[1, 640, 32, 32]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-06     | Unknown  |
| 15 | Tensor<[1, 640, 64, 64]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int N = 1,<br>int C = 640,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
| 16 | Tensor<[1, 960, 32, 32]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int N = 1,<br>int C = 960,<br>int HxW = 1024,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
| 17 | Tensor<[1, 960, 64, 64]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int N = 1,<br>int C = 960,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05     | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 640]> input = ?,<br>List[int] normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float eps = 1e-05    | Done     |
|  1 | Tensor<[1, 256, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Done     |
|  2 | Tensor<[1, 4096, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05    | Done     |
|  3 | Tensor<[1, 64, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05  | Done     |
### aten.permute.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Done     |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 3, 1]   | Done     |
|  2 | Tensor<[1, 16, 16, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     |
|  3 | Tensor<[1, 32, 32, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     |
|  4 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Done     |
|  5 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     |
|  6 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Done     |
|  7 | Tensor<[1, 8, 8, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2]   | Done     |
### aten.silu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ? | Done     |
|  1 | Tensor<[1, 1280, 32, 32]> self = ? | Done     |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?   | Done     |
|  3 | Tensor<[1, 1280]> self = ?         | Done     |
|  4 | Tensor<[1, 1920, 16, 16]> self = ? | Done     |
|  5 | Tensor<[1, 1920, 32, 32]> self = ? | Done     |
|  6 | Tensor<[1, 2560, 16, 16]> self = ? | Done     |
|  7 | Tensor<[1, 2560, 8, 8]> self = ?   | Done     |
|  8 | Tensor<[1, 320, 32, 32]> self = ?  | Done     |
|  9 | Tensor<[1, 320, 64, 64]> self = ?  | Done     |
| 10 | Tensor<[1, 640, 16, 16]> self = ?  | Done     |
| 11 | Tensor<[1, 640, 32, 32]> self = ?  | Done     |
| 12 | Tensor<[1, 640, 64, 64]> self = ?  | Done     |
| 13 | Tensor<[1, 960, 32, 32]> self = ?  | Done     |
| 14 | Tensor<[1, 960, 64, 64]> self = ?  | Done     |
### aten.sin.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[1, 160]> self = ? | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1  | Unknown  |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1  | Unknown  |
|  2 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1   | Unknown  |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1   | Unknown  |
|  4 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1   | Unknown  |
|  5 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160  | Unknown  |
|  6 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = -1 | Unknown  |
|  7 | Tensor<[1, 640]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1   | Unknown  |
|  8 | Tensor<[1, 640]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1   | Unknown  |
|  9 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1        | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1 | Unknown  |
|  1 | Tensor<[1, 256, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  |
|  2 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1 | Unknown  |
|  3 | Tensor<[1, 64, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1  | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[10240, 1280]> self = ? | Done     |
|  1 | Tensor<[1280, 1280]> self = ?  | Done     |
|  2 | Tensor<[1280, 320]> self = ?   | Done     |
|  3 | Tensor<[1280, 5120]> self = ?  | Done     |
|  4 | Tensor<[1280, 768]> self = ?   | Done     |
|  5 | Tensor<[2560, 320]> self = ?   | Done     |
|  6 | Tensor<[320, 1280]> self = ?   | Done     |
|  7 | Tensor<[320, 320]> self = ?    | Done     |
|  8 | Tensor<[320, 768]> self = ?    | Done     |
|  9 | Tensor<[5120, 640]> self = ?   | Done     |
| 10 | Tensor<[640, 1280]> self = ?   | Done     |
| 11 | Tensor<[640, 2560]> self = ?   | Done     |
| 12 | Tensor<[640, 640]> self = ?    | Done     |
| 13 | Tensor<[640, 768]> self = ?    | Done     |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  1 | Tensor<[1, 256, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  2 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  3 | Tensor<[1, 64, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     |
|  4 | Tensor<[1, 8, 1024, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  5 | Tensor<[1, 8, 256, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  6 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  7 | Tensor<[1, 8, 64, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     |
|  8 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     |
|  9 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     |
| 10 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1]> self = ?,<br>int dim = 3 | Done     |
|  1 | Tensor<[1, 1280]> self = ?,<br>int dim = 2    | Unknown  |
|  2 | Tensor<[1, 320, 1]> self = ?,<br>int dim = 3  | Done     |
|  3 | Tensor<[1, 320]> self = ?,<br>int dim = 2     | Unknown  |
|  4 | Tensor<[1, 640, 1]> self = ?,<br>int dim = 3  | Done     |
|  5 | Tensor<[1, 640]> self = ?,<br>int dim = 2     | Unknown  |
|  6 | Tensor<[160]> self = ?,<br>int dim = 0        | Done     |
|  7 | Tensor<[16]> self = ?,<br>int dim = -1        | Unknown  |
|  8 | Tensor<[1]> self = ?,<br>int dim = 1          | Done     |
|  9 | Tensor<[32]> self = ?,<br>int dim = -1        | Unknown  |
| 10 | Tensor<[64]> self = ?,<br>int dim = -1        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 2560]> self = ?,<br>List[int] size = [1024, 2560]     | Unknown  |
|  1 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]    | Unknown  |
|  2 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1, 32, 32, 640]  | Unknown  |
|  3 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]       | Unknown  |
|  4 | Tensor<[1, 1024, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]    | Unknown  |
|  5 | Tensor<[1, 16, 16, 1280]> self = ?,<br>List[int] size = [1, 256, 1280] | Unknown  |
|  6 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]   | Unknown  |
|  7 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 16, 16, 1280] | Unknown  |
|  8 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]       | Unknown  |
|  9 | Tensor<[1, 256, 5120]> self = ?,<br>List[int] size = [256, 5120]       | Unknown  |
| 10 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]   | Unknown  |
| 11 | Tensor<[1, 32, 32, 640]> self = ?,<br>List[int] size = [1, 1024, 640]  | Unknown  |
| 12 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]     | Unknown  |
| 13 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]    | Unknown  |
| 14 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]  | Unknown  |
| 15 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]       | Unknown  |
| 16 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]    | Unknown  |
| 17 | Tensor<[1, 64, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]    | Unknown  |
| 18 | Tensor<[1, 64, 1280]> self = ?,<br>List[int] size = [1, 8, 8, 1280]    | Unknown  |
| 19 | Tensor<[1, 64, 1280]> self = ?,<br>List[int] size = [64, 1280]         | Unknown  |
| 20 | Tensor<[1, 64, 5120]> self = ?,<br>List[int] size = [64, 5120]         | Unknown  |
| 21 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]  | Unknown  |
| 22 | Tensor<[1, 64, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]    | Unknown  |
| 23 | Tensor<[1, 8, 8, 1280]> self = ?,<br>List[int] size = [1, 64, 1280]    | Unknown  |
| 24 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]     | Unknown  |
| 25 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]       | Unknown  |
| 26 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]       | Unknown  |
| 27 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]             | Unknown  |
| 28 | Tensor<[1024, 5120]> self = ?,<br>List[int] size = [1, 1024, 5120]     | Unknown  |
| 29 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]       | Unknown  |
| 30 | Tensor<[256, 10240]> self = ?,<br>List[int] size = [1, 256, 10240]     | Unknown  |
| 31 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]       | Unknown  |
| 32 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]     | Unknown  |
| 33 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]       | Unknown  |
| 34 | Tensor<[64, 10240]> self = ?,<br>List[int] size = [1, 64, 10240]       | Unknown  |
| 35 | Tensor<[64, 1280]> self = ?,<br>List[int] size = [1, 64, 1280]         | Unknown  |
| 36 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]           | Unknown  |
| 37 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]             | Unknown  |
| 38 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]             | Unknown  |

