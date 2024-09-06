# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 30 |           0 |
|  1 | aten._to_copy.default                             |                  1 |           0 |
|  2 | aten._unsafe_index.Tensor                         |                  1 |           0 |
|  3 | aten._unsafe_view.default                         |                 15 |           0 |
|  4 | aten.add.Tensor                                   |                 17 |          15 |
|  5 | aten.arange.default                               |                  1 |           0 |
|  6 | aten.arange.start                                 |                  6 |           0 |
|  7 | aten.cat.default                                  |                 10 |           0 |
|  8 | aten.ceil.default                                 |                  1 |           0 |
|  9 | aten.clamp.default                                |                  6 |           4 |
| 10 | aten.clone.default                                |                 15 |          15 |
| 11 | aten.convolution.default                          |                 71 |           0 |
| 12 | aten.div.Tensor                                   |                 10 |           1 |
| 13 | aten.exp.default                                  |                  1 |           0 |
| 14 | aten.expand.default                               |                 11 |           0 |
| 15 | aten.hardsigmoid.default                          |                  4 |           0 |
| 16 | aten.hardswish.default                            |                  9 |           0 |
| 17 | aten.hardtanh.default                             |                 13 |           0 |
| 18 | aten.lift_fresh_copy.default                      |                  1 |           0 |
| 19 | aten.mean.dim                                     |                  6 |           6 |
| 20 | aten.mul.Tensor                                   |                 16 |          12 |
| 21 | aten.new_full.default                             |                  1 |           0 |
| 22 | aten.permute.default                              |                 12 |          12 |
| 23 | aten.relu.default                                 |                 10 |          10 |
| 24 | aten.repeat.default                               |                  6 |           0 |
| 25 | aten.rsub.Scalar                                  |                  2 |           0 |
| 26 | aten.select.int                                   |                  6 |           0 |
| 27 | aten.slice.Tensor                                 |                 11 |           0 |
| 28 | aten.stack.default                                |                  9 |           0 |
| 29 | aten.sub.Tensor                                   |                  7 |           5 |
| 30 | aten.unbind.int                                   |                  1 |           0 |
| 31 | aten.unsqueeze.default                            |                  5 |           2 |
| 32 | aten.view.default                                 |                 35 |           0 |
| 33 | aten.zeros_like.default                           |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
|  1 | Tensor<[1, 120, 40, 40]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
|  2 | Tensor<[1, 128, 1, 1]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
|  3 | Tensor<[1, 128, 2, 2]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
|  4 | Tensor<[1, 128, 3, 3]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
|  5 | Tensor<[1, 128, 5, 5]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
|  6 | Tensor<[1, 16, 160, 160]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Unknown  |
|  7 | Tensor<[1, 184, 20, 20]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
|  8 | Tensor<[1, 200, 20, 20]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
|  9 | Tensor<[1, 24, 80, 80]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
| 10 | Tensor<[1, 240, 20, 20]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 11 | Tensor<[1, 240, 40, 40]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 12 | Tensor<[1, 256, 10, 10]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 13 | Tensor<[1, 256, 2, 2]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
| 14 | Tensor<[1, 256, 3, 3]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
| 15 | Tensor<[1, 256, 5, 5]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
| 16 | Tensor<[1, 40, 40, 40]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
| 17 | Tensor<[1, 480, 10, 10]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 18 | Tensor<[1, 480, 20, 20]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 19 | Tensor<[1, 512, 5, 5]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001   | Unknown  |
| 20 | Tensor<[1, 64, 1, 1]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Unknown  |
| 21 | Tensor<[1, 64, 160, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001    | Unknown  |
| 22 | Tensor<[1, 64, 2, 2]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001        | Unknown  |
| 23 | Tensor<[1, 64, 80, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
| 24 | Tensor<[1, 672, 10, 10]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 25 | Tensor<[1, 672, 20, 20]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
| 26 | Tensor<[1, 72, 40, 40]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
| 27 | Tensor<[1, 72, 80, 80]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
| 28 | Tensor<[1, 80, 10, 10]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
| 29 | Tensor<[1, 80, 20, 20]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001      | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[320]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, 'torch.Size([320, 1])', 'torch.Size([320])'] | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]    | Unknown  |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]  | Unknown  |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]       | Unknown  |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]     | Unknown  |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]   | Unknown  |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91] | Unknown  |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]       | Unknown  |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]     | Unknown  |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]      | Unknown  |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]    | Unknown  |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                   | Unknown  |
| 11 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                       | Unknown  |
| 12 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                   | Unknown  |
| 13 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                       | Unknown  |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?   | Done     |
|  1 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ? | Done     |
|  2 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?     | Done     |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?   | Done     |
|  4 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?     | Done     |
|  5 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?     | Done     |
|  6 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?     | Done     |
|  7 | Tensor<[10]> self = ?,<br>Tensor other = 0.5                               | Done     |
|  8 | Tensor<[1]> self = ?,<br>Tensor other = 0.5                                | Done     |
|  9 | Tensor<[20]> self = ?,<br>Tensor other = 0.5                               | Done     |
| 10 | Tensor<[2]> self = ?,<br>Tensor other = 0.5                                | Done     |
| 11 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                              | Done     |
| 12 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                 | Unknown  |
| 13 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                 | Done     |
| 14 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                       | Unknown  |
| 15 | Tensor<[3]> self = ?,<br>Tensor other = 0.5                                | Done     |
| 16 | Tensor<[5]> self = ?,<br>Tensor other = 0.5                                | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 320,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
|  1 | number start = 0,<br>number end = 10,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  2 | number start = 0,<br>number end = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
|  3 | number start = 0,<br>number end = 20,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  4 | number start = 0,<br>number end = 3,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
|  5 | number start = 0,<br>number end = 5,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = ['torch.Size([1, 2400, 4])', 'torch.Size([1, 600, 4])', 'torch.Size([1, 150, 4])', 'torch.Size([1, 54, 4])', 'torch.Size([1, 24, 4])', 'torch.Size([1, 6, 4])'],<br>int dim = 1       | Unknown  |
|  1 | List[Tensor] tensors = ['torch.Size([1, 2400, 91])', 'torch.Size([1, 600, 91])', 'torch.Size([1, 150, 91])', 'torch.Size([1, 54, 91])', 'torch.Size([1, 24, 91])', 'torch.Size([1, 6, 91])'],<br>int dim = 1 | Unknown  |
|  2 | List[Tensor] tensors = ['torch.Size([150, 2])', 'torch.Size([150, 2])'],<br>int dim = 1                                                                                                                      | Unknown  |
|  3 | List[Tensor] tensors = ['torch.Size([24, 2])', 'torch.Size([24, 2])'],<br>int dim = 1                                                                                                                        | Unknown  |
|  4 | List[Tensor] tensors = ['torch.Size([2400, 2])', 'torch.Size([2400, 2])'],<br>int dim = 1                                                                                                                    | Unknown  |
|  5 | List[Tensor] tensors = ['torch.Size([2400, 4])', 'torch.Size([600, 4])', 'torch.Size([150, 4])', 'torch.Size([54, 4])', 'torch.Size([24, 4])', 'torch.Size([6, 4])']                                         | Unknown  |
|  6 | List[Tensor] tensors = ['torch.Size([3234, 2])', 'torch.Size([3234, 2])'],<br>int dim = -1                                                                                                                   | Unknown  |
|  7 | List[Tensor] tensors = ['torch.Size([54, 2])', 'torch.Size([54, 2])'],<br>int dim = 1                                                                                                                        | Unknown  |
|  8 | List[Tensor] tensors = ['torch.Size([6, 2])', 'torch.Size([6, 2])'],<br>int dim = 1                                                                                                                          | Unknown  |
|  9 | List[Tensor] tensors = ['torch.Size([600, 2])', 'torch.Size([600, 2])'],<br>int dim = 1                                                                                                                      | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[320]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[320]> self = ?,<br>Optional[number] min = 0.0                                                | Done     |
|  1 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 479                   | Done     |
|  2 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 639                   | Done     |
|  3 | Tensor<[3234, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356 | Unknown  |
|  4 | Tensor<[3234, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 320               | Unknown  |
|  5 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                    | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 10 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 11 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Done     |
| 12 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 13 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Done     |
| 14 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 20, 20]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
|  1 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  2 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  3 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120        | Unknown  |
|  4 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[40, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  5 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Unknown  |
|  6 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[24, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  7 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[546, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  8 | Tensor<[1, 128, 2, 2]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
|  9 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Unknown  |
| 10 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 11 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128          | Unknown  |
| 12 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16         | Unknown  |
| 13 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 14 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[64, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 15 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 16 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184        | Unknown  |
| 17 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[80, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 18 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200        | Unknown  |
| 19 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[80, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 20 | Tensor<[1, 24, 1, 1]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 21 | Tensor<[1, 24, 80, 80]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 22 | Tensor<[1, 240, 20, 20]> input = ?,<br>Tensor<[80, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 23 | Tensor<[1, 240, 40, 40]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240        | Unknown  |
| 24 | Tensor<[1, 256, 10, 10]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256        | Unknown  |
| 25 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 26 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Unknown  |
| 27 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 28 | Tensor<[1, 256, 2, 2]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 29 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 30 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[24, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 31 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256          | Unknown  |
| 32 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[546, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 33 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 34 | Tensor<[1, 3, 320, 320]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 35 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 36 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 37 | Tensor<[1, 40, 40, 40]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 38 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 39 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[24, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 40 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[256, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
| 41 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Unknown  |
| 42 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Unknown  |
| 43 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[546, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 44 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[80, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 45 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[112, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
| 46 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480        | Unknown  |
| 47 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 48 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[24, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 49 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512          | Unknown  |
| 50 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[546, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 51 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 52 | Tensor<[1, 64, 160, 160]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64         | Unknown  |
| 53 | Tensor<[1, 64, 2, 2]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64             | Unknown  |
| 54 | Tensor<[1, 64, 80, 80]> input = ?,<br>Tensor<[24, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 55 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 56 | Tensor<[1, 672, 10, 10]> input = ?,<br>Tensor<[80, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 57 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[112, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
| 58 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[24, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 59 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[546, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 60 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Unknown  |
| 61 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672        | Unknown  |
| 62 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 63 | Tensor<[1, 72, 40, 40]> input = ?,<br>Tensor<[40, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 64 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 65 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Unknown  |
| 66 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72           | Unknown  |
| 67 | Tensor<[1, 80, 10, 10]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 68 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 69 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 70 | Tensor<[1, 80, 20, 20]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[10]> self = ?,<br>Tensor other = 10                    | Unknown  |
|  1 | Tensor<[1]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  2 | Tensor<[20]> self = ?,<br>Tensor other = 20                    | Unknown  |
|  3 | Tensor<[2]> self = ?,<br>Tensor other = 2                      | Unknown  |
|  4 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     |
|  5 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0             | Unknown  |
|  6 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0              | Unknown  |
|  7 | Tensor<[3]> self = ?,<br>Tensor other = 3                      | Unknown  |
|  8 | Tensor<[5]> self = ?,<br>Tensor other = 5                      | Unknown  |
|  9 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                   | Unknown  |
### aten.exp.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[3234, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10, 10] | Unknown  |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]    | Unknown  |
|  2 | Tensor<[1, 20]> self = ?,<br>List[int] size = [20, 20] | Unknown  |
|  3 | Tensor<[1, 2]> self = ?,<br>List[int] size = [2, 2]    | Unknown  |
|  4 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3, 3]    | Unknown  |
|  5 | Tensor<[1, 5]> self = ?,<br>List[int] size = [5, 5]    | Unknown  |
|  6 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10] | Unknown  |
|  7 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]    | Unknown  |
|  8 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20] | Unknown  |
|  9 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]    | Unknown  |
| 10 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]    | Unknown  |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Unknown  |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | Unknown  |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | Unknown  |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | Unknown  |
### aten.hardswish.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 160, 160]> self = ? | Unknown  |
|  1 | Tensor<[1, 184, 20, 20]> self = ?  | Unknown  |
|  2 | Tensor<[1, 200, 20, 20]> self = ?  | Unknown  |
|  3 | Tensor<[1, 240, 20, 20]> self = ?  | Unknown  |
|  4 | Tensor<[1, 240, 40, 40]> self = ?  | Unknown  |
|  5 | Tensor<[1, 480, 10, 10]> self = ?  | Unknown  |
|  6 | Tensor<[1, 480, 20, 20]> self = ?  | Unknown  |
|  7 | Tensor<[1, 672, 10, 10]> self = ?  | Unknown  |
|  8 | Tensor<[1, 672, 20, 20]> self = ?  | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  1 | Tensor<[1, 128, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  2 | Tensor<[1, 128, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  3 | Tensor<[1, 128, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  4 | Tensor<[1, 256, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
|  5 | Tensor<[1, 256, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  6 | Tensor<[1, 256, 3, 3]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  7 | Tensor<[1, 256, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
|  8 | Tensor<[1, 480, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
|  9 | Tensor<[1, 512, 5, 5]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | Unknown  |
| 10 | Tensor<[1, 64, 1, 1]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Unknown  |
| 11 | Tensor<[1, 64, 2, 2]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0    | Unknown  |
| 12 | Tensor<[1, 672, 20, 20]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  1 | Tensor<[1, 480, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  2 | Tensor<[1, 480, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  3 | Tensor<[1, 672, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  4 | Tensor<[1, 672, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  5 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ? | Done     |
|  1 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?       | Done     |
|  2 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?          | Done     |
|  3 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ? | Done     |
|  4 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ? | Done     |
|  5 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ? | Done     |
|  6 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ? | Done     |
|  7 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?   | Done     |
|  8 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                        | Unknown  |
|  9 | Tensor<[320]> self = ?,<br>Tensor other = 1.5                          | Done     |
| 10 | Tensor<[320]> self = ?,<br>Tensor other = 2.0                          | Done     |
| 11 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  |
| 12 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                      | Done     |
| 13 | Tensor<[3234, 2]> self = ?,<br>Tensor<[2]> other = ?                   | Done     |
| 14 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                         | Unknown  |
| 15 | Tensor<[]> self = ?,<br>Tensor<[3234, 1]> other = ?                    | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     |
|  1 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     |
|  2 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     |
|  3 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     |
|  4 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     |
|  5 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     |
|  6 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     |
|  7 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     |
|  8 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     |
|  9 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     |
| 10 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     |
| 11 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 120, 1, 1]> self = ?    | Done     |
|  1 | Tensor<[1, 120, 40, 40]> self = ?  | Done     |
|  2 | Tensor<[1, 16, 160, 160]> self = ? | Done     |
|  3 | Tensor<[1, 168, 1, 1]> self = ?    | Done     |
|  4 | Tensor<[1, 24, 1, 1]> self = ?     | Done     |
|  5 | Tensor<[1, 32, 1, 1]> self = ?     | Done     |
|  6 | Tensor<[1, 64, 160, 160]> self = ? | Done     |
|  7 | Tensor<[1, 64, 80, 80]> self = ?   | Done     |
|  8 | Tensor<[1, 72, 40, 40]> self = ?   | Done     |
|  9 | Tensor<[1, 72, 80, 80]> self = ?   | Done     |
### aten.repeat.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]   | Unknown  |
|  1 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1] | Unknown  |
|  2 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]  | Unknown  |
|  3 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]   | Unknown  |
|  4 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1] | Unknown  |
|  5 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]   | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[320, 1]> self = ?,<br>number other = 1.0 | Unknown  |
|  1 | Tensor<[320]> self = ?,<br>number other = 1.0    | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
|  1 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 1        | Unknown  |
|  4 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2        | Unknown  |
|  5 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 3        | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3234, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  2 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  3 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                   | Unknown  |
|  4 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  5 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  6 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = -1                  | Unknown  |
|  7 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  8 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  9 | Tensor<[3234]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 10 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = ['torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])'],<br>int dim = -1 | Unknown  |
|  1 | List[Tensor] tensors = ['torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])'],<br>int dim = -1                         | Unknown  |
|  2 | List[Tensor] tensors = ['torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])'],<br>int dim = -1             | Unknown  |
|  3 | List[Tensor] tensors = ['torch.Size([300])', 'torch.Size([300])', 'torch.Size([300])', 'torch.Size([300])'],<br>int dim = 1                                                                                                                                                                          | Unknown  |
|  4 | List[Tensor] tensors = ['torch.Size([3234, 1])', 'torch.Size([3234, 1])', 'torch.Size([3234, 1])', 'torch.Size([3234, 1])'],<br>int dim = 2                                                                                                                                                          | Unknown  |
|  5 | List[Tensor] tensors = ['torch.Size([3234, 2])', 'torch.Size([3234, 2])'],<br>int dim = 2                                                                                                                                                                                                            | Unknown  |
|  6 | List[Tensor] tensors = ['torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])', 'torch.Size([400])'],<br>int dim = -1 | Unknown  |
|  7 | List[Tensor] tensors = ['torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])', 'torch.Size([4])'],<br>int dim = -1                         | Unknown  |
|  8 | List[Tensor] tensors = ['torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])'],<br>int dim = -1                         | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     |
|  1 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?       | Done     |
|  2 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                  | Done     |
|  3 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?             | Done     |
|  4 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?     | Unknown  |
|  5 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?     | Done     |
|  6 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?           | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[300, 4]> self = ?,<br>int dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Done     |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Done     |
|  2 | Tensor<[320]> self = ?,<br>int dim = 1         | Unknown  |
|  3 | Tensor<[3234]> self = ?,<br>int dim = 1        | Unknown  |
|  4 | Tensor<[3]> self = ?,<br>int dim = 1           | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]           | Unknown  |
|  1 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]         | Unknown  |
|  2 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Unknown  |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                          | Unknown  |
|  4 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]       | Unknown  |
|  5 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]   | Unknown  |
|  6 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]       | Unknown  |
|  7 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]   | Unknown  |
|  8 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]       | Unknown  |
|  9 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]       | Unknown  |
| 10 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]     | Unknown  |
| 11 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10] | Unknown  |
| 12 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]     | Unknown  |
| 13 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20] | Unknown  |
| 14 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]     | Unknown  |
| 15 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]     | Unknown  |
| 16 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Unknown  |
| 17 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  |
| 18 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                         | Unknown  |
| 19 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  |
| 20 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  |
| 21 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  |
| 22 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                         | Unknown  |
| 23 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                     | Unknown  |
| 24 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  |
| 25 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  |
| 26 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]               | Unknown  |
| 27 | Tensor<[3234, 2, 2]> self = ?,<br>List[int] size = [3234, 4]               | Unknown  |
| 28 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  |
| 29 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  |
| 30 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Unknown  |
| 31 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Unknown  |
| 32 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  |
| 33 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                          | Unknown  |
| 34 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                      | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[13685]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  |

