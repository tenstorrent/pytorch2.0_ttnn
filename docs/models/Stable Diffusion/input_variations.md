# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |
|---:|:-------------------------------------------------|-------------------:|------------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  8 |           8 |
|  1 | aten._to_copy.default                            |                  4 |           4 |
|  2 | aten._unsafe_index.Tensor                        |                  6 |           3 |
|  3 | aten.add.Tensor                                  |                 15 |          15 |
|  4 | aten.addmm.default                               |                 16 |          16 |
|  5 | aten.arange.default                              |                  3 |           3 |
|  6 | aten.arange.start                                |                  1 |           1 |
|  7 | aten.cat.default                                 |                 23 |          14 |
|  8 | aten.clone.default                               |                 16 |          16 |
|  9 | aten.convolution.default                         |                 35 |          35 |
| 10 | aten.cos.default                                 |                  1 |           1 |
| 11 | aten.div.Tensor                                  |                 10 |          10 |
| 12 | aten.exp.default                                 |                  1 |           1 |
| 13 | aten.expand.default                              |                  1 |           1 |
| 14 | aten.gelu.default                                |                  4 |           4 |
| 15 | aten.lift_fresh_copy.default                     |                  1 |           1 |
| 16 | aten.mm.default                                  |                  7 |           7 |
| 17 | aten.mul.Tensor                                  |                 10 |          10 |
| 18 | aten.native_group_norm.default                   |                 18 |          18 |
| 19 | aten.native_layer_norm.default                   |                  4 |           4 |
| 20 | aten.permute.default                             |                  8 |           8 |
| 21 | aten.silu.default                                |                 15 |          15 |
| 22 | aten.sin.default                                 |                  1 |           1 |
| 23 | aten.slice.Tensor                                |                 10 |          10 |
| 24 | aten.split.Tensor                                |                  4 |           4 |
| 25 | aten.t.default                                   |                 14 |          14 |
| 26 | aten.transpose.int                               |                 11 |          11 |
| 27 | aten.unsqueeze.default                           |                 11 |          11 |
| 28 | aten.view.default                                |                 39 |          39 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 1024, 80]> key = ?,<br>Tensor<[1, 8, 1024, 80]> value = ? | Done     |
|  1 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?       | Done     |
|  2 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 256, 160]> key = ?,<br>Tensor<[1, 8, 256, 160]> value = ? | Done     |
|  3 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?     | Done     |
|  4 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 4096, 40]> key = ?,<br>Tensor<[1, 8, 4096, 40]> value = ? | Done     |
|  5 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?       | Done     |
|  6 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 64, 160]> key = ?,<br>Tensor<[1, 8, 64, 160]> value = ?    | Done     |
|  7 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?      | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Done     |
|  1 | Tensor<[16]> self = ?,<br>Optional[int]<> dtype = torch.int64     | Done     |
|  2 | Tensor<[32]> self = ?,<br>Optional[int]<> dtype = torch.int64     | Done     |
|  3 | Tensor<[64]> self = ?,<br>Optional[int]<> dtype = torch.int64     | Done     |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([32, 1])', 'torch.Size([32])']              | Unknown  |
|  1 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_35), Proxy(_to_copy_default_4)] | Done     |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([16, 1])', 'torch.Size([16])']                | Unknown  |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_28), Proxy(_to_copy_default_2)]   | Done     |
|  4 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([64, 1])', 'torch.Size([64])']               | Unknown  |
|  5 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_42), Proxy(_to_copy_default_6)]  | Done     |
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
| 12 | Tensor<[16]> self = ?,<br>Tensor<> other = 0.0                             | Done     |
| 13 | Tensor<[32]> self = ?,<br>Tensor<> other = 0.0                             | Done     |
| 14 | Tensor<[64]> self = ?,<br>Tensor<> other = 0.0                             | Done     |
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
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 16,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
|  1 | number<> end = 32,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
|  2 | number<> end = 64,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.arange.start
|    | ATen Input Variations                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> start = 0,<br>number<> end = 160,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 1280, 16, 16])', 'torch.Size([1, 1280, 16, 16])'],<br>int<> dim = 1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 1280, 16, 16])', 'torch.Size([1, 640, 16, 16])'],<br>int<> dim = 1  | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 1280, 32, 32])', 'torch.Size([1, 640, 32, 32])'],<br>int<> dim = 1  | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, 1280, 8, 8])', 'torch.Size([1, 1280, 8, 8])'],<br>int<> dim = 1     | Unknown  |
|  4 | List[Tensor]<> tensors = ['torch.Size([1, 160])', 'torch.Size([1, 160])'],<br>int<> dim = -1                  | Unknown  |
|  5 | List[Tensor]<> tensors = ['torch.Size([1, 320, 64, 64])', 'torch.Size([1, 320, 64, 64])'],<br>int<> dim = 1   | Unknown  |
|  6 | List[Tensor]<> tensors = ['torch.Size([1, 640, 32, 32])', 'torch.Size([1, 320, 32, 32])'],<br>int<> dim = 1   | Unknown  |
|  7 | List[Tensor]<> tensors = ['torch.Size([1, 640, 32, 32])', 'torch.Size([1, 640, 32, 32])'],<br>int<> dim = 1   | Unknown  |
|  8 | List[Tensor]<> tensors = ['torch.Size([1, 640, 64, 64])', 'torch.Size([1, 320, 64, 64])'],<br>int<> dim = 1   | Unknown  |
|  9 | List[Tensor]<> tensors = [Proxy(convolution_default_49), Proxy(ttnn_add_67)],<br>int<> dim = 1                | Done     |
| 10 | List[Tensor]<> tensors = [Proxy(convolution_default_65), Proxy(ttnn_add_45)],<br>int<> dim = 1                | Done     |
| 11 | List[Tensor]<> tensors = [Proxy(convolution_default_81), Proxy(ttnn_add_23)],<br>int<> dim = 1                | Done     |
| 12 | List[Tensor]<> tensors = [Proxy(div_tensor_24), Proxy(div_tensor_20)],<br>int<> dim = 1                       | Done     |
| 13 | List[Tensor]<> tensors = [Proxy(div_tensor_25), Proxy(div_tensor_19)],<br>int<> dim = 1                       | Done     |
| 14 | List[Tensor]<> tensors = [Proxy(div_tensor_26), Proxy(convolution_default_29)],<br>int<> dim = 1              | Done     |
| 15 | List[Tensor]<> tensors = [Proxy(slice_tensor_3), Proxy(slice_tensor_5)],<br>int<> dim = -1                    | Done     |
| 16 | List[Tensor]<> tensors = [Proxy(ttnn_add_109), Proxy(ttnn_add_56)],<br>int<> dim = 1                          | Done     |
| 17 | List[Tensor]<> tensors = [Proxy(ttnn_add_120), Proxy(convolution_default_19)],<br>int<> dim = 1               | Done     |
| 18 | List[Tensor]<> tensors = [Proxy(ttnn_add_144), Proxy(ttnn_add_34)],<br>int<> dim = 1                          | Done     |
| 19 | List[Tensor]<> tensors = [Proxy(ttnn_add_155), Proxy(convolution_default_9)],<br>int<> dim = 1                | Done     |
| 20 | List[Tensor]<> tensors = [Proxy(ttnn_add_179), Proxy(ttnn_add_12)],<br>int<> dim = 1                          | Done     |
| 21 | List[Tensor]<> tensors = [Proxy(ttnn_add_190), Proxy(convolution_default)],<br>int<> dim = 1                  | Done     |
| 22 | List[Tensor]<> tensors = [Proxy(ttnn_sin), Proxy(ttnn_cos)],<br>int<> dim = -1                                | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 2560]> self = ?                                                               | Done     |
|  1 | Tensor<[1, 1024, 640]> self = ?                                                                | Done     |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?                                                             | Done     |
|  3 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?                                                               | Done     |
|  5 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
|  6 | Tensor<[1, 256, 1280]> self = ?                                                                | Done     |
|  7 | Tensor<[1, 256, 5120]> self = ?                                                                | Done     |
|  8 | Tensor<[1, 320, 64, 64]> self = ?                                                              | Done     |
|  9 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 10 | Tensor<[1, 4096, 1280]> self = ?                                                               | Done     |
| 11 | Tensor<[1, 4096, 320]> self = ?                                                                | Done     |
| 12 | Tensor<[1, 64, 1280]> self = ?                                                                 | Done     |
| 13 | Tensor<[1, 64, 5120]> self = ?                                                                 | Done     |
| 14 | Tensor<[1, 640, 32, 32]> self = ?                                                              | Done     |
| 15 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  1 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  2 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  3 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  4 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[640, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  5 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Tensor<[640, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  6 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  7 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Tensor<[1280, 1280, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  8 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Tensor<[1280, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  9 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Tensor<[1280, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 10 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Tensor<[640, 1920, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 11 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Tensor<[640, 1920, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 12 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 13 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 14 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 15 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Tensor<[1280, 2560, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 16 | Tensor<[1, 320, 32, 32]> input = ?,<br>Tensor<[640, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 17 | Tensor<[1, 320, 32, 32]> input = ?,<br>Tensor<[640, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 18 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 19 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 20 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 21 | Tensor<[1, 320, 64, 64]> input = ?,<br>Tensor<[4, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[4]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 22 | Tensor<[1, 4, 64, 64]> input = ?,<br>Tensor<[320, 4, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 23 | Tensor<[1, 640, 16, 16]> input = ?,<br>Tensor<[1280, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 24 | Tensor<[1, 640, 16, 16]> input = ?,<br>Tensor<[1280, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 25 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 26 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 27 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 28 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[320, 640, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 29 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[320, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 30 | Tensor<[1, 640, 64, 64]> input = ?,<br>Tensor<[640, 640, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 31 | Tensor<[1, 960, 32, 32]> input = ?,<br>Tensor<[640, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 32 | Tensor<[1, 960, 32, 32]> input = ?,<br>Tensor<[640, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 33 | Tensor<[1, 960, 64, 64]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 34 | Tensor<[1, 960, 64, 64]> input = ?,<br>Tensor<[320, 960, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
### aten.cos.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[1, 160]> self = ? | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor<> other = 1.0    | Done     |
|  1 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<> other = 1.0 | Done     |
|  2 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<> other = 1     | Done     |
|  3 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<> other = 1.0   | Done     |
|  4 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<> other = 1.0    | Done     |
|  5 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<> other = 1.0  | Done     |
|  6 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<> other = 1.0    | Done     |
|  7 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor<> other = 1.0     | Done     |
|  8 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<> other = 1.0  | Done     |
|  9 | Tensor<[160]> self = ?,<br>Tensor<> other = 160             | Done     |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[160]> self = ?  | Done     |
### aten.expand.default
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>List[int]<> size = [1] | Done     |
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
|  0 | Tensor<> self = ?       | Done     |
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
|  1 | Tensor<[1, 160]> self = ?,<br>Tensor<> other = 1                       | Done     |
|  2 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                 | Done     |
|  3 | Tensor<[1, 256, 5120]> self = ?,<br>Tensor<[1, 256, 5120]> other = ?   | Done     |
|  4 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ? | Done     |
|  5 | Tensor<[1, 64, 5120]> self = ?,<br>Tensor<[1, 64, 5120]> other = ?     | Done     |
|  6 | Tensor<[160]> self = ?,<br>Tensor<> other = -9.210340371976184         | Done     |
|  7 | Tensor<[16]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
|  8 | Tensor<[32]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
|  9 | Tensor<[64]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int<> N = 1,<br>int<> C = 1280,<br>int<> HxW = 256,<br>int<> group = 32,<br>float<> eps = 1e-05  | Done     |
|  1 | Tensor<[1, 1280, 16, 16]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int<> N = 1,<br>int<> C = 1280,<br>int<> HxW = 256,<br>int<> group = 32,<br>float<> eps = 1e-06  | Done     |
|  2 | Tensor<[1, 1280, 32, 32]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int<> N = 1,<br>int<> C = 1280,<br>int<> HxW = 1024,<br>int<> group = 32,<br>float<> eps = 1e-05 | Done     |
|  3 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int<> N = 1,<br>int<> C = 1280,<br>int<> HxW = 64,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
|  4 | Tensor<[1, 1280, 8, 8]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>int<> N = 1,<br>int<> C = 1280,<br>int<> HxW = 64,<br>int<> group = 32,<br>float<> eps = 1e-06     | Done     |
|  5 | Tensor<[1, 1920, 16, 16]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int<> N = 1,<br>int<> C = 1920,<br>int<> HxW = 256,<br>int<> group = 32,<br>float<> eps = 1e-05  | Done     |
|  6 | Tensor<[1, 1920, 32, 32]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>int<> N = 1,<br>int<> C = 1920,<br>int<> HxW = 1024,<br>int<> group = 32,<br>float<> eps = 1e-05 | Done     |
|  7 | Tensor<[1, 2560, 16, 16]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int<> N = 1,<br>int<> C = 2560,<br>int<> HxW = 256,<br>int<> group = 32,<br>float<> eps = 1e-05  | Done     |
|  8 | Tensor<[1, 2560, 8, 8]> input = ?,<br>Optional[Tensor]<[2560]> weight = ?,<br>Optional[Tensor]<[2560]> bias = ?,<br>int<> N = 1,<br>int<> C = 2560,<br>int<> HxW = 64,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
|  9 | Tensor<[1, 320, 32, 32]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int<> N = 1,<br>int<> C = 320,<br>int<> HxW = 1024,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
| 10 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int<> N = 1,<br>int<> C = 320,<br>int<> HxW = 4096,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
| 11 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int<> N = 1,<br>int<> C = 320,<br>int<> HxW = 4096,<br>int<> group = 32,<br>float<> eps = 1e-06     | Done     |
| 12 | Tensor<[1, 640, 16, 16]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int<> N = 1,<br>int<> C = 640,<br>int<> HxW = 256,<br>int<> group = 32,<br>float<> eps = 1e-05      | Done     |
| 13 | Tensor<[1, 640, 32, 32]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int<> N = 1,<br>int<> C = 640,<br>int<> HxW = 1024,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
| 14 | Tensor<[1, 640, 32, 32]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int<> N = 1,<br>int<> C = 640,<br>int<> HxW = 1024,<br>int<> group = 32,<br>float<> eps = 1e-06     | Done     |
| 15 | Tensor<[1, 640, 64, 64]> input = ?,<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>int<> N = 1,<br>int<> C = 640,<br>int<> HxW = 4096,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
| 16 | Tensor<[1, 960, 32, 32]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int<> N = 1,<br>int<> C = 960,<br>int<> HxW = 1024,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
| 17 | Tensor<[1, 960, 64, 64]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>int<> N = 1,<br>int<> C = 960,<br>int<> HxW = 4096,<br>int<> group = 32,<br>float<> eps = 1e-05     | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 640]> input = ?,<br>List[int]<> normalized_shape = [640],<br>Optional[Tensor]<[640]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>float<> eps = 1e-05    | Done     |
|  1 | Tensor<[1, 256, 1280]> input = ?,<br>List[int]<> normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float<> eps = 1e-05 | Done     |
|  2 | Tensor<[1, 4096, 320]> input = ?,<br>List[int]<> normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float<> eps = 1e-05    | Done     |
|  3 | Tensor<[1, 64, 1280]> input = ?,<br>List[int]<> normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float<> eps = 1e-05  | Done     |
### aten.permute.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 16, 16]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1] | Done     |
|  1 | Tensor<[1, 1280, 8, 8]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]   | Done     |
|  2 | Tensor<[1, 16, 16, 1280]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2] | Done     |
|  3 | Tensor<[1, 32, 32, 640]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
|  4 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]  | Done     |
|  5 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
|  6 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int]<> dims = [0, 2, 3, 1]  | Done     |
|  7 | Tensor<[1, 8, 8, 1280]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]   | Done     |
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
|    | ATen Input Variations                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1  | Done     |
|  1 | Tensor<[1, 1280]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1  | Done     |
|  2 | Tensor<[1, 160]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Done     |
|  3 | Tensor<[1, 320]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Done     |
|  4 | Tensor<[1, 320]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Done     |
|  5 | Tensor<[1, 320]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 160  | Done     |
|  6 | Tensor<[1, 320]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 160,<br>Optional[int]<> end = -1 | Done     |
|  7 | Tensor<[1, 640]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Done     |
|  8 | Tensor<[1, 640]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Done     |
|  9 | Tensor<[1]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1        | Done     |
### aten.split.Tensor
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 5120]> self = ?,<br>int<> split_size = 2560,<br>int<> dim = -1 | Done     |
|  1 | Tensor<[1, 256, 10240]> self = ?,<br>int<> split_size = 5120,<br>int<> dim = -1 | Done     |
|  2 | Tensor<[1, 4096, 2560]> self = ?,<br>int<> split_size = 1280,<br>int<> dim = -1 | Done     |
|  3 | Tensor<[1, 64, 10240]> self = ?,<br>int<> split_size = 5120,<br>int<> dim = -1  | Done     |
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
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 8, 80]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  1 | Tensor<[1, 256, 8, 160]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  2 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  3 | Tensor<[1, 64, 8, 160]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Done     |
|  4 | Tensor<[1, 8, 1024, 80]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  5 | Tensor<[1, 8, 256, 160]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  6 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  7 | Tensor<[1, 8, 64, 160]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Done     |
|  8 | Tensor<[1, 9, 8, 160]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  9 | Tensor<[1, 9, 8, 40]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 10 | Tensor<[1, 9, 8, 80]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1]> self = ?,<br>int<> dim = 3 | Done     |
|  1 | Tensor<[1, 1280]> self = ?,<br>int<> dim = 2    | Done     |
|  2 | Tensor<[1, 320, 1]> self = ?,<br>int<> dim = 3  | Done     |
|  3 | Tensor<[1, 320]> self = ?,<br>int<> dim = 2     | Done     |
|  4 | Tensor<[1, 640, 1]> self = ?,<br>int<> dim = 3  | Done     |
|  5 | Tensor<[1, 640]> self = ?,<br>int<> dim = 2     | Done     |
|  6 | Tensor<[160]> self = ?,<br>int<> dim = 0        | Done     |
|  7 | Tensor<[16]> self = ?,<br>int<> dim = -1        | Done     |
|  8 | Tensor<[1]> self = ?,<br>int<> dim = 1          | Done     |
|  9 | Tensor<[32]> self = ?,<br>int<> dim = -1        | Done     |
| 10 | Tensor<[64]> self = ?,<br>int<> dim = -1        | Done     |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 2560]> self = ?,<br>List[int]<> size = [1024, 2560]     | Done     |
|  1 | Tensor<[1, 1024, 640]> self = ?,<br>List[int]<> size = [1, -1, 8, 80]    | Done     |
|  2 | Tensor<[1, 1024, 640]> self = ?,<br>List[int]<> size = [1, 32, 32, 640]  | Done     |
|  3 | Tensor<[1, 1024, 640]> self = ?,<br>List[int]<> size = [1024, 640]       | Done     |
|  4 | Tensor<[1, 1024, 8, 80]> self = ?,<br>List[int]<> size = [1, -1, 640]    | Done     |
|  5 | Tensor<[1, 16, 16, 1280]> self = ?,<br>List[int]<> size = [1, 256, 1280] | Done     |
|  6 | Tensor<[1, 256, 1280]> self = ?,<br>List[int]<> size = [1, -1, 8, 160]   | Done     |
|  7 | Tensor<[1, 256, 1280]> self = ?,<br>List[int]<> size = [1, 16, 16, 1280] | Done     |
|  8 | Tensor<[1, 256, 1280]> self = ?,<br>List[int]<> size = [256, 1280]       | Done     |
|  9 | Tensor<[1, 256, 5120]> self = ?,<br>List[int]<> size = [256, 5120]       | Done     |
| 10 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int]<> size = [1, -1, 1280]   | Done     |
| 11 | Tensor<[1, 32, 32, 640]> self = ?,<br>List[int]<> size = [1, 1024, 640]  | Done     |
| 12 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int]<> size = [4096, 1280]     | Done     |
| 13 | Tensor<[1, 4096, 320]> self = ?,<br>List[int]<> size = [1, -1, 8, 40]    | Done     |
| 14 | Tensor<[1, 4096, 320]> self = ?,<br>List[int]<> size = [1, 64, 64, 320]  | Done     |
| 15 | Tensor<[1, 4096, 320]> self = ?,<br>List[int]<> size = [4096, 320]       | Done     |
| 16 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int]<> size = [1, -1, 320]    | Done     |
| 17 | Tensor<[1, 64, 1280]> self = ?,<br>List[int]<> size = [1, -1, 8, 160]    | Done     |
| 18 | Tensor<[1, 64, 1280]> self = ?,<br>List[int]<> size = [1, 8, 8, 1280]    | Done     |
| 19 | Tensor<[1, 64, 1280]> self = ?,<br>List[int]<> size = [64, 1280]         | Done     |
| 20 | Tensor<[1, 64, 5120]> self = ?,<br>List[int]<> size = [64, 5120]         | Done     |
| 21 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int]<> size = [1, 4096, 320]  | Done     |
| 22 | Tensor<[1, 64, 8, 160]> self = ?,<br>List[int]<> size = [1, -1, 1280]    | Done     |
| 23 | Tensor<[1, 8, 8, 1280]> self = ?,<br>List[int]<> size = [1, 64, 1280]    | Done     |
| 24 | Tensor<[1, 9, 1280]> self = ?,<br>List[int]<> size = [1, -1, 8, 160]     | Done     |
| 25 | Tensor<[1, 9, 320]> self = ?,<br>List[int]<> size = [1, -1, 8, 40]       | Done     |
| 26 | Tensor<[1, 9, 640]> self = ?,<br>List[int]<> size = [1, -1, 8, 80]       | Done     |
| 27 | Tensor<[1, 9, 768]> self = ?,<br>List[int]<> size = [9, 768]             | Done     |
| 28 | Tensor<[1024, 5120]> self = ?,<br>List[int]<> size = [1, 1024, 5120]     | Done     |
| 29 | Tensor<[1024, 640]> self = ?,<br>List[int]<> size = [1, 1024, 640]       | Done     |
| 30 | Tensor<[256, 10240]> self = ?,<br>List[int]<> size = [1, 256, 10240]     | Done     |
| 31 | Tensor<[256, 1280]> self = ?,<br>List[int]<> size = [1, 256, 1280]       | Done     |
| 32 | Tensor<[4096, 2560]> self = ?,<br>List[int]<> size = [1, 4096, 2560]     | Done     |
| 33 | Tensor<[4096, 320]> self = ?,<br>List[int]<> size = [1, 4096, 320]       | Done     |
| 34 | Tensor<[64, 10240]> self = ?,<br>List[int]<> size = [1, 64, 10240]       | Done     |
| 35 | Tensor<[64, 1280]> self = ?,<br>List[int]<> size = [1, 64, 1280]         | Done     |
| 36 | Tensor<[9, 1280]> self = ?,<br>List[int]<> size = [1, 9, 1280]           | Done     |
| 37 | Tensor<[9, 320]> self = ?,<br>List[int]<> size = [1, 9, 320]             | Done     |
| 38 | Tensor<[9, 640]> self = ?,<br>List[int]<> size = [1, 9, 640]             | Done     |

