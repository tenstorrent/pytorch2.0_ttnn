# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  6 |           0 |
|  1 | aten._softmax.default                             |                  4 |           4 |
|  2 | aten._to_copy.default                             |                 10 |           0 |
|  3 | aten._unsafe_index.Tensor                         |                  5 |           0 |
|  4 | aten.add.Tensor                                   |                 19 |          19 |
|  5 | aten.addmm.default                                |                 15 |          15 |
|  6 | aten.arange.default                               |                 10 |           0 |
|  7 | aten.bmm.default                                  |                  8 |           8 |
|  8 | aten.cat.default                                  |                  3 |           0 |
|  9 | aten.ceil.default                                 |                 10 |           0 |
| 10 | aten.clamp.default                                |                 20 |          20 |
| 11 | aten.clone.default                                |                 19 |          15 |
| 12 | aten.convolution.default                          |                 25 |           0 |
| 13 | aten.div.Tensor                                   |                  4 |           0 |
| 14 | aten.expand.default                               |                 15 |           0 |
| 15 | aten.gelu.default                                 |                  4 |           4 |
| 16 | aten.mul.Tensor                                   |                 24 |          24 |
| 17 | aten.native_layer_norm.default                    |                  7 |           7 |
| 18 | aten.permute.default                              |                 21 |          21 |
| 19 | aten.relu.default                                 |                  7 |           7 |
| 20 | aten.rsub.Scalar                                  |                 10 |           0 |
| 21 | aten.select.int                                   |                  6 |           0 |
| 22 | aten.sigmoid.default                              |                  4 |           4 |
| 23 | aten.slice.Tensor                                 |                  9 |           0 |
| 24 | aten.squeeze.dim                                  |                  1 |           0 |
| 25 | aten.sub.Tensor                                   |                 20 |          20 |
| 26 | aten.t.default                                    |                 12 |          12 |
| 27 | aten.transpose.int                                |                 16 |          16 |
| 28 | aten.unsqueeze.default                            |                  8 |           3 |
| 29 | aten.view.default                                 |                 78 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 120, 160]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 32, 30, 40]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
|  2 | Tensor<[1, 32, 60, 80]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
|  3 | Tensor<[1, 64, 120, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  4 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
|  5 | Tensor<[1, 64, 60, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Done     |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Done     |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False   | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[120]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  1 | Tensor<[160]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  2 | Tensor<[240]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  3 | Tensor<[30]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
|  4 | Tensor<[320]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  5 | Tensor<[40]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
|  6 | Tensor<[480]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  7 | Tensor<[60]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
|  8 | Tensor<[640]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  9 | Tensor<[80]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([240, 1])', 'torch.Size([320])'] | Unknown  |
|  1 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([30, 1])', 'torch.Size([40])']     | Unknown  |
|  2 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([480, 1])', 'torch.Size([640])'] | Unknown  |
|  3 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([60, 1])', 'torch.Size([80])']     | Unknown  |
|  4 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([120, 1])', 'torch.Size([160])']   | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?       | Done     |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Done     |
|  2 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?         | Done     |
|  3 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?       | Done     |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ? | Done     |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ? | Done     |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?     | Done     |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ? | Done     |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?     | Done     |
|  9 | Tensor<[120]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 10 | Tensor<[160]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 11 | Tensor<[240]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 12 | Tensor<[30]> self = ?,<br>Tensor<> other = 0.5                             | Done     |
| 13 | Tensor<[320]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 14 | Tensor<[40]> self = ?,<br>Tensor<> other = 0.5                             | Done     |
| 15 | Tensor<[480]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 16 | Tensor<[60]> self = ?,<br>Tensor<> other = 0.5                             | Done     |
| 17 | Tensor<[640]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 18 | Tensor<[80]> self = ?,<br>Tensor<> other = 0.5                             | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ? | Done     |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[300, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?    | Done     |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     |
|  3 | Tensor<[128]> self = ?,<br>Tensor<[4800, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     |
|  4 | Tensor<[2048]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     |
|  6 | Tensor<[320]> self = ?,<br>Tensor<[1200, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ? | Done     |
|  7 | Tensor<[320]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?   | Done     |
|  8 | Tensor<[320]> self = ?,<br>Tensor<[300, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?    | Done     |
|  9 | Tensor<[512]> self = ?,<br>Tensor<[300, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     |
| 10 | Tensor<[512]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[19200, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[300, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 120,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | number<> end = 160,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  2 | number<> end = 240,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  3 | number<> end = 30,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  4 | number<> end = 320,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  5 | number<> end = 40,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  6 | number<> end = 480,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  7 | number<> end = 60,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  8 | number<> end = 640,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  9 | number<> end = 80,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ? | Done     |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?  | Done     |
|  2 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?  | Done     |
|  3 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?   | Done     |
|  4 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?  | Done     |
|  5 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?   | Done     |
|  6 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?   | Done     |
|  7 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?    | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 64, 120, 160])', 'torch.Size([1, 64, 120, 160])'],<br>int<> dim = 1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 64, 30, 40])', 'torch.Size([1, 64, 30, 40])'],<br>int<> dim = 1     | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 64, 60, 80])', 'torch.Size([1, 64, 60, 80])'],<br>int<> dim = 1     | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[120]> self = ?  | Unknown  |
|  1 | Tensor<[160]> self = ?  | Unknown  |
|  2 | Tensor<[240]> self = ?  | Unknown  |
|  3 | Tensor<[30]> self = ?   | Unknown  |
|  4 | Tensor<[320]> self = ?  | Unknown  |
|  5 | Tensor<[40]> self = ?   | Unknown  |
|  6 | Tensor<[480]> self = ?  | Unknown  |
|  7 | Tensor<[60]> self = ?   | Unknown  |
|  8 | Tensor<[640]> self = ?  | Unknown  |
|  9 | Tensor<[80]> self = ?   | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[120]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
|  1 | Tensor<[120]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 59  | Done     |
|  2 | Tensor<[160]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
|  3 | Tensor<[160]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 79  | Done     |
|  4 | Tensor<[240]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
|  5 | Tensor<[240]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 119 | Done     |
|  6 | Tensor<[30]> self = ?,<br>Optional[number]<> min = 0.0                                 | Done     |
|  7 | Tensor<[30]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 14   | Done     |
|  8 | Tensor<[320]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
|  9 | Tensor<[320]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 159 | Done     |
| 10 | Tensor<[40]> self = ?,<br>Optional[number]<> min = 0.0                                 | Done     |
| 11 | Tensor<[40]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 19   | Done     |
| 12 | Tensor<[480]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
| 13 | Tensor<[480]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 239 | Done     |
| 14 | Tensor<[60]> self = ?,<br>Optional[number]<> min = 0.0                                 | Done     |
| 15 | Tensor<[60]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 29   | Done     |
| 16 | Tensor<[640]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
| 17 | Tensor<[640]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 319 | Done     |
| 18 | Tensor<[80]> self = ?,<br>Optional[number]<> min = 0.0                                 | Done     |
| 19 | Tensor<[80]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 39   | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?                                                            | Done     |
|  1 | Tensor<[1, 1200, 1280]> self = ?                                                               | Done     |
|  2 | Tensor<[1, 1200, 320]> self = ?                                                                | Unknown  |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  4 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  5 | Tensor<[1, 19200, 256]> self = ?                                                               | Done     |
|  6 | Tensor<[1, 19200, 64]> self = ?                                                                | Unknown  |
|  7 | Tensor<[1, 2, 4800, 300]> self = ?                                                             | Done     |
|  8 | Tensor<[1, 300, 2048]> self = ?                                                                | Done     |
|  9 | Tensor<[1, 300, 512]> self = ?                                                                 | Unknown  |
| 10 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
| 11 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 12 | Tensor<[1, 4800, 128]> self = ?                                                                | Unknown  |
| 13 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 14 | Tensor<[1, 4800, 512]> self = ?                                                                | Done     |
| 15 | Tensor<[1, 5, 1200, 300]> self = ?                                                             | Done     |
| 16 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 17 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
| 18 | Tensor<[1, 8, 300, 300]> self = ?                                                              | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 120, 160]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  1 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  2 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  3 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[320, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  4 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  5 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  6 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1280 | Unknown  |
|  7 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2048 | Unknown  |
|  8 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 256   | Unknown  |
|  9 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [3, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 10 | Tensor<[1, 32, 120, 160]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 11 | Tensor<[1, 32, 30, 40]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Unknown  |
| 12 | Tensor<[1, 32, 60, 80]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Unknown  |
| 13 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 14 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[512, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 15 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[64, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 16 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 17 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 512     | Unknown  |
| 18 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 19 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 20 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [8, 8],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 21 | Tensor<[1, 64, 30, 40]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 22 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[1, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 23 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 24 | Tensor<[1, 64, 60, 80]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor<> other = 8.0 | Unknown  |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor<> other = 8.0  | Unknown  |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor<> other = 8.0  | Unknown  |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor<> other = 8.0   | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int]<> size = [1, 1, 19200, 300] | Unknown  |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int]<> size = [1, 1, 19200, 64]   | Unknown  |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int]<> size = [1, 1, 300, 64]       | Unknown  |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int]<> size = [1, 1, 64, 300]       | Unknown  |
|  4 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int]<> size = [1, 2, 300, 64]       | Unknown  |
|  5 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int]<> size = [1, 2, 4800, 300]   | Unknown  |
|  6 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int]<> size = [1, 2, 4800, 64]     | Unknown  |
|  7 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int]<> size = [1, 2, 64, 300]       | Unknown  |
|  8 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int]<> size = [1, 5, 1200, 300]   | Unknown  |
|  9 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int]<> size = [1, 5, 1200, 64]     | Unknown  |
| 10 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int]<> size = [1, 5, 300, 64]       | Unknown  |
| 11 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int]<> size = [1, 5, 64, 300]       | Unknown  |
| 12 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int]<> size = [1, 8, 300, 300]     | Unknown  |
| 13 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int]<> size = [1, 8, 300, 64]       | Unknown  |
| 14 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int]<> size = [1, 8, 64, 300]       | Unknown  |
### aten.gelu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1200, 1280]> self = ? | Done     |
|  1 | Tensor<[1, 19200, 256]> self = ? | Done     |
|  2 | Tensor<[1, 300, 2048]> self = ?  | Done     |
|  3 | Tensor<[1, 4800, 512]> self = ?  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor<> other = 10                 | Done     |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ? | Done     |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?         | Done     |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?            | Done     |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?         | Done     |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?            | Done     |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?     | Done     |
|  7 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?            | Done     |
|  8 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?               | Done     |
|  9 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?         | Done     |
| 10 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?            | Done     |
| 11 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?     | Done     |
| 12 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?            | Done     |
| 13 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?               | Done     |
| 14 | Tensor<[120]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 15 | Tensor<[160]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 16 | Tensor<[240]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 17 | Tensor<[30]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 18 | Tensor<[320]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 19 | Tensor<[40]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 20 | Tensor<[480]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 21 | Tensor<[60]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 22 | Tensor<[640]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 23 | Tensor<[80]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1200, 320]> input = ?,<br>List[int]<> normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 19200, 64]> input = ?,<br>List[int]<> normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float<> eps = 1e-05    | Done     |
|  2 | Tensor<[1, 300, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-05  | Done     |
|  3 | Tensor<[1, 300, 320]> input = ?,<br>List[int]<> normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float<> eps = 1e-05  | Done     |
|  4 | Tensor<[1, 300, 512]> input = ?,<br>List[int]<> normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float<> eps = 1e-05  | Done     |
|  5 | Tensor<[1, 300, 64]> input = ?,<br>List[int]<> normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float<> eps = 1e-05      | Done     |
|  6 | Tensor<[1, 4800, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-05 | Done     |
### aten.permute.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2] | Done     |
|  2 | Tensor<[1, 1200, 320]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
|  4 | Tensor<[1, 128, 300]> self = ?,<br>List[int]<> dims = [0, 2, 1]        | Done     |
|  5 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
|  6 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  7 | Tensor<[1, 19200, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
|  8 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
|  9 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
| 10 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 11 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 12 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 13 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 14 | Tensor<[1, 320, 300]> self = ?,<br>List[int]<> dims = [0, 2, 1]        | Done     |
| 15 | Tensor<[1, 4800, 128]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
| 16 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
| 17 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
| 18 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
| 19 | Tensor<[1, 64, 300]> self = ?,<br>List[int]<> dims = [0, 2, 1]         | Done     |
| 20 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 32, 120, 160]> self = ? | Done     |
|  1 | Tensor<[1, 32, 30, 40]> self = ?   | Done     |
|  2 | Tensor<[1, 32, 60, 80]> self = ?   | Done     |
|  3 | Tensor<[1, 64, 120, 160]> self = ? | Done     |
|  4 | Tensor<[1, 64, 30, 40]> self = ?   | Done     |
|  5 | Tensor<[1, 64, 480, 640]> self = ? | Done     |
|  6 | Tensor<[1, 64, 60, 80]> self = ?   | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[120, 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  1 | Tensor<[160]> self = ?,<br>number<> other = 1.0    | Unknown  |
|  2 | Tensor<[240, 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  3 | Tensor<[30, 1]> self = ?,<br>number<> other = 1.0  | Unknown  |
|  4 | Tensor<[320]> self = ?,<br>number<> other = 1.0    | Unknown  |
|  5 | Tensor<[40]> self = ?,<br>number<> other = 1.0     | Unknown  |
|  6 | Tensor<[480, 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  7 | Tensor<[60, 1]> self = ?,<br>number<> other = 1.0  | Unknown  |
|  8 | Tensor<[640]> self = ?,<br>number<> other = 1.0    | Unknown  |
|  9 | Tensor<[80]> self = ?,<br>number<> other = 1.0     | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 120, 160]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
|  1 | Tensor<[1, 2, 120, 160]> self = ?,<br>int<> dim = 1,<br>int<> index = 1 | Unknown  |
|  2 | Tensor<[1, 2, 30, 40]> self = ?,<br>int<> dim = 1,<br>int<> index = 0   | Unknown  |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int<> dim = 1,<br>int<> index = 1   | Unknown  |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int<> dim = 1,<br>int<> index = 0   | Unknown  |
|  5 | Tensor<[1, 2, 60, 80]> self = ?,<br>int<> dim = 1,<br>int<> index = 1   | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 1, 480, 640]> self = ? | Done     |
|  1 | Tensor<[1, 2, 120, 160]> self = ? | Done     |
|  2 | Tensor<[1, 2, 30, 40]> self = ?   | Done     |
|  3 | Tensor<[1, 2, 60, 80]> self = ?   | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1    | Unknown  |
|  1 | Tensor<[1, 120, 160]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1    | Unknown  |
|  2 | Tensor<[1, 2, 120, 160]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Unknown  |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Unknown  |
|  5 | Tensor<[1, 30, 40]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
|  6 | Tensor<[1, 30, 40]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
|  7 | Tensor<[1, 60, 80]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
|  8 | Tensor<[1, 60, 80]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                               | Status   |
|---:|:----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int<> dim = 1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ? | Done     |
|  1 | Tensor<[120]> self = ?,<br>Tensor<> other = 0.5          | Done     |
|  2 | Tensor<[160]> self = ?,<br>Tensor<> other = 0.5          | Done     |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?       | Done     |
|  4 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ? | Done     |
|  5 | Tensor<[240]> self = ?,<br>Tensor<> other = 0.5          | Done     |
|  6 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?   | Done     |
|  7 | Tensor<[30]> self = ?,<br>Tensor<> other = 0.5           | Done     |
|  8 | Tensor<[320]> self = ?,<br>Tensor<> other = 0.5          | Done     |
|  9 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?       | Done     |
| 10 | Tensor<[40]> self = ?,<br>Tensor<> other = 0.5           | Done     |
| 11 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?         | Done     |
| 12 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ? | Done     |
| 13 | Tensor<[480]> self = ?,<br>Tensor<> other = 0.5          | Done     |
| 14 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?   | Done     |
| 15 | Tensor<[60]> self = ?,<br>Tensor<> other = 0.5           | Done     |
| 16 | Tensor<[640]> self = ?,<br>Tensor<> other = 0.5          | Done     |
| 17 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?       | Done     |
| 18 | Tensor<[80]> self = ?,<br>Tensor<> other = 0.5           | Done     |
| 19 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?         | Done     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[128, 128]> self = ?  | Done     |
|  1 | Tensor<[128, 512]> self = ?  | Done     |
|  2 | Tensor<[1280, 320]> self = ? | Done     |
|  3 | Tensor<[2048, 512]> self = ? | Done     |
|  4 | Tensor<[256, 64]> self = ?   | Done     |
|  5 | Tensor<[320, 1280]> self = ? | Done     |
|  6 | Tensor<[320, 320]> self = ?  | Done     |
|  7 | Tensor<[512, 128]> self = ?  | Done     |
|  8 | Tensor<[512, 2048]> self = ? | Done     |
|  9 | Tensor<[512, 512]> self = ?  | Done     |
| 10 | Tensor<[64, 256]> self = ?   | Done     |
| 11 | Tensor<[64, 64]> self = ?    | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 300, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  1 | Tensor<[1, 1200, 1280]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  2 | Tensor<[1, 128, 4800]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  3 | Tensor<[1, 1280, 1200]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[1, 19200, 256]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  5 | Tensor<[1, 2, 300, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  6 | Tensor<[1, 2048, 300]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  7 | Tensor<[1, 256, 19200]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  8 | Tensor<[1, 300, 2048]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  9 | Tensor<[1, 320, 1200]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 10 | Tensor<[1, 4800, 512]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 11 | Tensor<[1, 5, 300, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
| 12 | Tensor<[1, 512, 300]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
| 13 | Tensor<[1, 512, 4800]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 14 | Tensor<[1, 64, 19200]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 15 | Tensor<[1, 8, 300, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int<> dim = 1 | Done     |
|  1 | Tensor<[1, 30, 40]> self = ?,<br>int<> dim = 1   | Done     |
|  2 | Tensor<[1, 60, 80]> self = ?,<br>int<> dim = 1   | Done     |
|  3 | Tensor<[120]> self = ?,<br>int<> dim = 1         | Unknown  |
|  4 | Tensor<[240]> self = ?,<br>int<> dim = 1         | Unknown  |
|  5 | Tensor<[30]> self = ?,<br>int<> dim = 1          | Unknown  |
|  6 | Tensor<[480]> self = ?,<br>int<> dim = 1         | Unknown  |
|  7 | Tensor<[60]> self = ?,<br>int<> dim = 1          | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int]<> size = [1, 19200, 300] | Unknown  |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int]<> size = [1, 19200, 64]   | Unknown  |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int]<> size = [1, 300, 64]       | Unknown  |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int]<> size = [1, 64, 300]       | Unknown  |
|  4 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int]<> size = [1200, 1280]       | Unknown  |
|  5 | Tensor<[1, 1200, 320]> self = ?,<br>List[int]<> size = [1, 1200, 5, 64]    | Unknown  |
|  6 | Tensor<[1, 1200, 320]> self = ?,<br>List[int]<> size = [1, 30, 40, -1]     | Unknown  |
|  7 | Tensor<[1, 1200, 320]> self = ?,<br>List[int]<> size = [1200, 320]         | Unknown  |
|  8 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int]<> size = [1, 1200, 320]    | Unknown  |
|  9 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int]<> size = [1, 128, 300]     | Unknown  |
| 10 | Tensor<[1, 128, 4800]> self = ?,<br>List[int]<> size = [1, 128, 60, 80]    | Unknown  |
| 11 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int]<> size = [1, 128, 4800]    | Unknown  |
| 12 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int]<> size = [1, 1280, 30, 40]  | Unknown  |
| 13 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int]<> size = [1, 1280, 1200]  | Unknown  |
| 14 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int]<> size = [1, 19200, 64]   | Unknown  |
| 15 | Tensor<[1, 19200, 256]> self = ?,<br>List[int]<> size = [19200, 256]       | Unknown  |
| 16 | Tensor<[1, 19200, 300]> self = ?,<br>List[int]<> size = [1, 1, 19200, 300] | Unknown  |
| 17 | Tensor<[1, 19200, 64]> self = ?,<br>List[int]<> size = [1, 1, 19200, 64]   | Unknown  |
| 18 | Tensor<[1, 19200, 64]> self = ?,<br>List[int]<> size = [1, 120, 160, -1]   | Unknown  |
| 19 | Tensor<[1, 19200, 64]> self = ?,<br>List[int]<> size = [1, 19200, 1, 64]   | Unknown  |
| 20 | Tensor<[1, 19200, 64]> self = ?,<br>List[int]<> size = [19200, 64]         | Unknown  |
| 21 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int]<> size = [2, 300, 64]       | Unknown  |
| 22 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int]<> size = [2, 4800, 300]   | Unknown  |
| 23 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int]<> size = [2, 4800, 64]     | Unknown  |
| 24 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int]<> size = [2, 64, 300]       | Unknown  |
| 25 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int]<> size = [1, 2048, 300]   | Unknown  |
| 26 | Tensor<[1, 2048, 300]> self = ?,<br>List[int]<> size = [1, 2048, 15, 20]   | Unknown  |
| 27 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int]<> size = [1, 256, 19200] | Unknown  |
| 28 | Tensor<[1, 256, 19200]> self = ?,<br>List[int]<> size = [1, 256, 120, 160] | Unknown  |
| 29 | Tensor<[1, 300, 128]> self = ?,<br>List[int]<> size = [1, 300, 2, 64]      | Unknown  |
| 30 | Tensor<[1, 300, 128]> self = ?,<br>List[int]<> size = [300, 128]           | Unknown  |
| 31 | Tensor<[1, 300, 2048]> self = ?,<br>List[int]<> size = [300, 2048]         | Unknown  |
| 32 | Tensor<[1, 300, 320]> self = ?,<br>List[int]<> size = [1, 300, 5, 64]      | Unknown  |
| 33 | Tensor<[1, 300, 320]> self = ?,<br>List[int]<> size = [300, 320]           | Unknown  |
| 34 | Tensor<[1, 300, 512]> self = ?,<br>List[int]<> size = [1, 15, 20, -1]      | Unknown  |
| 35 | Tensor<[1, 300, 512]> self = ?,<br>List[int]<> size = [1, 300, 8, 64]      | Unknown  |
| 36 | Tensor<[1, 300, 512]> self = ?,<br>List[int]<> size = [300, 512]           | Unknown  |
| 37 | Tensor<[1, 300, 64]> self = ?,<br>List[int]<> size = [1, 300, 1, 64]       | Unknown  |
| 38 | Tensor<[1, 300, 64]> self = ?,<br>List[int]<> size = [300, 64]             | Unknown  |
| 39 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int]<> size = [1, 300, 512]      | Unknown  |
| 40 | Tensor<[1, 320, 1200]> self = ?,<br>List[int]<> size = [1, 320, 30, 40]    | Unknown  |
| 41 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int]<> size = [1, 320, 300]     | Unknown  |
| 42 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int]<> size = [1, 320, 1200]    | Unknown  |
| 43 | Tensor<[1, 4800, 128]> self = ?,<br>List[int]<> size = [1, 4800, 2, 64]    | Unknown  |
| 44 | Tensor<[1, 4800, 128]> self = ?,<br>List[int]<> size = [1, 60, 80, -1]     | Unknown  |
| 45 | Tensor<[1, 4800, 128]> self = ?,<br>List[int]<> size = [4800, 128]         | Unknown  |
| 46 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int]<> size = [1, 4800, 128]    | Unknown  |
| 47 | Tensor<[1, 4800, 512]> self = ?,<br>List[int]<> size = [4800, 512]         | Unknown  |
| 48 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int]<> size = [5, 1200, 300]   | Unknown  |
| 49 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int]<> size = [5, 1200, 64]     | Unknown  |
| 50 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int]<> size = [5, 300, 64]       | Unknown  |
| 51 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int]<> size = [5, 64, 300]       | Unknown  |
| 52 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int]<> size = [1, 512, 300]     | Unknown  |
| 53 | Tensor<[1, 512, 4800]> self = ?,<br>List[int]<> size = [1, 512, 60, 80]    | Unknown  |
| 54 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int]<> size = [1, 512, 4800]    | Unknown  |
| 55 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int]<> size = [1, 64, 19200]   | Unknown  |
| 56 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int]<> size = [1, 64, 300]       | Unknown  |
| 57 | Tensor<[1, 64, 19200]> self = ?,<br>List[int]<> size = [1, 64, 120, 160]   | Unknown  |
| 58 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int]<> size = [8, 300, 300]     | Unknown  |
| 59 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int]<> size = [8, 300, 64]       | Unknown  |
| 60 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int]<> size = [8, 64, 300]       | Unknown  |
| 61 | Tensor<[1200, 1280]> self = ?,<br>List[int]<> size = [1, 1200, 1280]       | Unknown  |
| 62 | Tensor<[1200, 320]> self = ?,<br>List[int]<> size = [1, 1200, 320]         | Unknown  |
| 63 | Tensor<[19200, 256]> self = ?,<br>List[int]<> size = [1, 19200, 256]       | Unknown  |
| 64 | Tensor<[19200, 64]> self = ?,<br>List[int]<> size = [1, 19200, 64]         | Unknown  |
| 65 | Tensor<[2, 4800, 300]> self = ?,<br>List[int]<> size = [1, 2, 4800, 300]   | Unknown  |
| 66 | Tensor<[2, 4800, 64]> self = ?,<br>List[int]<> size = [1, 2, 4800, 64]     | Unknown  |
| 67 | Tensor<[300, 128]> self = ?,<br>List[int]<> size = [1, 300, 128]           | Unknown  |
| 68 | Tensor<[300, 2048]> self = ?,<br>List[int]<> size = [1, 300, 2048]         | Unknown  |
| 69 | Tensor<[300, 320]> self = ?,<br>List[int]<> size = [1, 300, 320]           | Unknown  |
| 70 | Tensor<[300, 512]> self = ?,<br>List[int]<> size = [1, 300, 512]           | Unknown  |
| 71 | Tensor<[300, 64]> self = ?,<br>List[int]<> size = [1, 300, 64]             | Unknown  |
| 72 | Tensor<[4800, 128]> self = ?,<br>List[int]<> size = [1, 4800, 128]         | Unknown  |
| 73 | Tensor<[4800, 512]> self = ?,<br>List[int]<> size = [1, 4800, 512]         | Unknown  |
| 74 | Tensor<[5, 1200, 300]> self = ?,<br>List[int]<> size = [1, 5, 1200, 300]   | Unknown  |
| 75 | Tensor<[5, 1200, 64]> self = ?,<br>List[int]<> size = [1, 5, 1200, 64]     | Unknown  |
| 76 | Tensor<[8, 300, 300]> self = ?,<br>List[int]<> size = [1, 8, 300, 300]     | Unknown  |
| 77 | Tensor<[8, 300, 64]> self = ?,<br>List[int]<> size = [1, 8, 300, 64]       | Unknown  |

