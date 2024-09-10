# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 12 |           0 |
|  1 | aten._to_copy.default                             |                  6 |           0 |
|  2 | aten._unsafe_index.Tensor                         |                  3 |           0 |
|  3 | aten._unsafe_view.default                         |                 15 |           0 |
|  4 | aten.add.Tensor                                   |                 20 |           0 |
|  5 | aten.arange.default                               |                  6 |           0 |
|  6 | aten.arange.start                                 |                 10 |           0 |
|  7 | aten.cat.default                                  |                  3 |           0 |
|  8 | aten.ceil.default                                 |                  2 |           0 |
|  9 | aten.clamp.default                                |                  7 |           0 |
| 10 | aten.clone.default                                |                 15 |           0 |
| 11 | aten.convolution.default                          |                 45 |           0 |
| 12 | aten.div.Tensor                                   |                  3 |           0 |
| 13 | aten.empty.memory_format                          |                  2 |           0 |
| 14 | aten.exp.default                                  |                  1 |           0 |
| 15 | aten.expand.default                               |                 10 |           0 |
| 16 | aten.fill.Scalar                                  |                  7 |           0 |
| 17 | aten.lift_fresh_copy.default                      |                  1 |           0 |
| 18 | aten.max_pool2d_with_indices.default              |                  1 |           0 |
| 19 | aten.mul.Tensor                                   |                 22 |           0 |
| 20 | aten.native_group_norm.default                    |                  5 |           0 |
| 21 | aten.new_full.default                             |                  1 |           0 |
| 22 | aten.permute.default                              |                 10 |           0 |
| 23 | aten.relu.default                                 |                 15 |           0 |
| 24 | aten.rsub.Scalar                                  |                  2 |           0 |
| 25 | aten.select.int                                   |                  6 |           0 |
| 26 | aten.slice.Tensor                                 |                  9 |           0 |
| 27 | aten.split_with_sizes.default                     |                  3 |           0 |
| 28 | aten.stack.default                                |                  8 |           0 |
| 29 | aten.sub.Tensor                                   |                  7 |           0 |
| 30 | aten.unbind.int                                   |                  1 |           0 |
| 31 | aten.unsqueeze.default                            |                  7 |           0 |
| 32 | aten.view.default                                 |                 33 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 128, 100, 136]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  2 | Tensor<[1, 128, 200, 272]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  3 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  4 | Tensor<[1, 256, 100, 136]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  5 | Tensor<[1, 256, 200, 272]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  6 | Tensor<[1, 256, 50, 68]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  7 | Tensor<[1, 512, 100, 136]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  8 | Tensor<[1, 512, 25, 34]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  9 | Tensor<[1, 512, 50, 68]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
| 10 | Tensor<[1, 64, 200, 272]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
| 11 | Tensor<[1, 64, 400, 544]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[100]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
|  1 | Tensor<[1066]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  2 | Tensor<[136]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
|  3 | Tensor<[50]> self = ?,<br>Optional[int]<> dtype = torch.int64   | Unknown  |
|  4 | Tensor<[68]> self = ?,<br>Optional[int]<> dtype = torch.int64   | Unknown  |
|  5 | Tensor<[800]> self = ?,<br>Optional[int]<> dtype = torch.int64  | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 25, 34]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([50, 1])', 'torch.Size([68])']    | Unknown  |
|  1 | Tensor<[1, 256, 50, 68]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([100, 1])', 'torch.Size([136])']  | Unknown  |
|  2 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([800, 1])', 'torch.Size([1066])'] | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int]<> size = [1, 122400, 4]   | Unknown  |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int]<> size = [1, 122400, 91] | Unknown  |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int]<> size = [1, 1989, 4]       | Unknown  |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int]<> size = [1, 1989, 91]     | Unknown  |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int]<> size = [1, 7650, 4]       | Unknown  |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int]<> size = [1, 7650, 91]     | Unknown  |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int]<> size = [1, 30600, 4]      | Unknown  |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int]<> size = [1, 30600, 91]    | Unknown  |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int]<> size = [1, 567, 4]          | Unknown  |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int]<> size = [1, 567, 91]        | Unknown  |
| 10 | Tensor<[100, 136]> self = ?,<br>List[int]<> size = [13600]                   | Unknown  |
| 11 | Tensor<[13, 17]> self = ?,<br>List[int]<> size = [221]                       | Unknown  |
| 12 | Tensor<[25, 34]> self = ?,<br>List[int]<> size = [850]                       | Unknown  |
| 13 | Tensor<[50, 68]> self = ?,<br>List[int]<> size = [3400]                      | Unknown  |
| 14 | Tensor<[7, 9]> self = ?,<br>List[int]<> size = [63]                          | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                         | Unknown  |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                               | Unknown  |
|  2 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?   | Unknown  |
|  3 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?   | Unknown  |
|  4 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ? | Unknown  |
|  5 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ? | Unknown  |
|  6 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?     | Unknown  |
|  7 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?   | Unknown  |
|  8 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ? | Unknown  |
|  9 | Tensor<[100]> self = ?,<br>Tensor<> other = 0.0                              | Unknown  |
| 10 | Tensor<[1066]> self = ?,<br>Tensor<> other = 0.5                             | Unknown  |
| 11 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?               | Unknown  |
| 12 | Tensor<[136]> self = ?,<br>Tensor<> other = 0.0                              | Unknown  |
| 13 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  |
| 14 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Unknown  |
| 15 | Tensor<[50]> self = ?,<br>Tensor<> other = 0.0                               | Unknown  |
| 16 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Unknown  |
| 17 | Tensor<[68]> self = ?,<br>Tensor<> other = 0.0                               | Unknown  |
| 18 | Tensor<[800]> self = ?,<br>Tensor<> other = 0.5                              | Unknown  |
| 19 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 100,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  1 | number<> end = 1066,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  2 | number<> end = 136,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  3 | number<> end = 50,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False   | Unknown  |
|  4 | number<> end = 68,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False   | Unknown  |
|  5 | number<> end = 800,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> start = 0,<br>number<> end = 100,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | number<> start = 0,<br>number<> end = 13,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  2 | number<> start = 0,<br>number<> end = 136,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  3 | number<> start = 0,<br>number<> end = 17,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  4 | number<> start = 0,<br>number<> end = 25,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  5 | number<> start = 0,<br>number<> end = 34,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  6 | number<> start = 0,<br>number<> end = 50,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  7 | number<> start = 0,<br>number<> end = 68,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  8 | number<> start = 0,<br>number<> end = 7,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False   | Unknown  |
|  9 | number<> start = 0,<br>number<> end = 9,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False   | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 122400, 4])', 'torch.Size([1, 30600, 4])', 'torch.Size([1, 7650, 4])', 'torch.Size([1, 1989, 4])', 'torch.Size([1, 567, 4])'],<br>int<> dim = 1      | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 122400, 91])', 'torch.Size([1, 30600, 91])', 'torch.Size([1, 7650, 91])', 'torch.Size([1, 1989, 91])', 'torch.Size([1, 567, 91])'],<br>int<> dim = 1 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([122400, 4])', 'torch.Size([30600, 4])', 'torch.Size([7650, 4])', 'torch.Size([1989, 4])', 'torch.Size([567, 4])']                                       | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1066]> self = ? | Unknown  |
|  1 | Tensor<[800]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.135166556742356 | Unknown  |
|  1 | Tensor<[0, 2]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 1066              | Unknown  |
|  2 | Tensor<[0, 2]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 800               | Unknown  |
|  3 | Tensor<[1066]> self = ?,<br>Optional[number]<> min = 0.0                                              | Unknown  |
|  4 | Tensor<[1066]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 639               | Unknown  |
|  5 | Tensor<[800]> self = ?,<br>Optional[number]<> min = 0.0                                               | Unknown  |
|  6 | Tensor<[800]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 479                | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Unknown  |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format    | Unknown  |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Unknown  |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format    | Unknown  |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Unknown  |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format    | Unknown  |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Unknown  |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format      | Unknown  |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format     | Unknown  |
| 10 | Tensor<[100, 136]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format           | Unknown  |
| 11 | Tensor<[13, 17]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format             | Unknown  |
| 12 | Tensor<[25, 34]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format             | Unknown  |
| 13 | Tensor<[50, 68]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format             | Unknown  |
| 14 | Tensor<[7, 9]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format               | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  1 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  2 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  3 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  4 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  5 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  6 | Tensor<[1, 128, 200, 272]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  7 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  8 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  9 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 10 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 11 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 12 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 13 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 14 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 15 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 16 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 17 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 18 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 19 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 20 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 21 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 22 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 23 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 24 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 25 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 26 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 27 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 28 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 29 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 30 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 31 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Unknown  |
| 32 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 33 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 34 | Tensor<[1, 3, 800, 1088]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [3, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Unknown  |
| 35 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 36 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 37 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 38 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 39 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 40 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 41 | Tensor<[1, 512, 50, 68]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 42 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 43 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 44 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<> other = 1.0               | Unknown  |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  2 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                   | Unknown  |
### aten.empty.memory_format
|    | ATen Input Variations                                                                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int]<> size = [0],<br>Optional[int]<> dtype = torch.int64,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  1 | List[int]<> size = [],<br>Optional[int]<> dtype = torch.int64,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 136]> self = ?,<br>List[int]<> size = [100, 136] | Unknown  |
|  1 | Tensor<[1, 17]> self = ?,<br>List[int]<> size = [13, 17]    | Unknown  |
|  2 | Tensor<[1, 34]> self = ?,<br>List[int]<> size = [25, 34]    | Unknown  |
|  3 | Tensor<[1, 68]> self = ?,<br>List[int]<> size = [50, 68]    | Unknown  |
|  4 | Tensor<[1, 9]> self = ?,<br>List[int]<> size = [7, 9]       | Unknown  |
|  5 | Tensor<[100, 1]> self = ?,<br>List[int]<> size = [100, 136] | Unknown  |
|  6 | Tensor<[13, 1]> self = ?,<br>List[int]<> size = [13, 17]    | Unknown  |
|  7 | Tensor<[25, 1]> self = ?,<br>List[int]<> size = [25, 34]    | Unknown  |
|  8 | Tensor<[50, 1]> self = ?,<br>List[int]<> size = [50, 68]    | Unknown  |
|  9 | Tensor<[7, 1]> self = ?,<br>List[int]<> size = [7, 9]       | Unknown  |
### aten.fill.Scalar
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>number<> value = 114 | Unknown  |
|  1 | Tensor<[]> self = ?,<br>number<> value = 120 | Unknown  |
|  2 | Tensor<[]> self = ?,<br>number<> value = 16  | Unknown  |
|  3 | Tensor<[]> self = ?,<br>number<> value = 32  | Unknown  |
|  4 | Tensor<[]> self = ?,<br>number<> value = 61  | Unknown  |
|  5 | Tensor<[]> self = ?,<br>number<> value = 64  | Unknown  |
|  6 | Tensor<[]> self = ?,<br>number<> value = 8   | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<> self = ?       | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 400, 544]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1] | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?              | Unknown  |
|  1 | Tensor<[0]> self = ?,<br>Tensor<> other = 0.5                     | Unknown  |
|  2 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                     | Unknown  |
|  3 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?   | Unknown  |
|  4 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ? | Unknown  |
|  5 | Tensor<[100]> self = ?,<br>Tensor<> other = 0.5                   | Unknown  |
|  6 | Tensor<[100]> self = ?,<br>Tensor<[]> other = ?                   | Unknown  |
|  7 | Tensor<[1066]> self = ?,<br>Tensor<> other = 0.600375234521576    | Unknown  |
|  8 | Tensor<[136]> self = ?,<br>Tensor<> other = 0.5                   | Unknown  |
|  9 | Tensor<[136]> self = ?,<br>Tensor<[]> other = ?                   | Unknown  |
| 10 | Tensor<[13]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  |
| 11 | Tensor<[17]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  |
| 12 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  |
| 13 | Tensor<[34]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  |
| 14 | Tensor<[50]> self = ?,<br>Tensor<> other = 0.5                    | Unknown  |
| 15 | Tensor<[50]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  |
| 16 | Tensor<[68]> self = ?,<br>Tensor<> other = 0.5                    | Unknown  |
| 17 | Tensor<[68]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  |
| 18 | Tensor<[7]> self = ?,<br>Tensor<[]> other = ?                     | Unknown  |
| 19 | Tensor<[800]> self = ?,<br>Tensor<> other = 0.6                   | Unknown  |
| 20 | Tensor<[9]> self = ?,<br>Tensor<[]> other = ?                     | Unknown  |
| 21 | Tensor<[]> self = ?,<br>Tensor<[0, 1]> other = ?                  | Unknown  |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 100, 136]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int<> N = 1,<br>int<> C = 256,<br>int<> HxW = 13600,<br>int<> group = 32,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 256, 13, 17]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int<> N = 1,<br>int<> C = 256,<br>int<> HxW = 221,<br>int<> group = 32,<br>float<> eps = 1e-05     | Unknown  |
|  2 | Tensor<[1, 256, 25, 34]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int<> N = 1,<br>int<> C = 256,<br>int<> HxW = 850,<br>int<> group = 32,<br>float<> eps = 1e-05     | Unknown  |
|  3 | Tensor<[1, 256, 50, 68]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int<> N = 1,<br>int<> C = 256,<br>int<> HxW = 3400,<br>int<> group = 32,<br>float<> eps = 1e-05    | Unknown  |
|  4 | Tensor<[1, 256, 7, 9]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int<> N = 1,<br>int<> C = 256,<br>int<> HxW = 63,<br>int<> group = 32,<br>float<> eps = 1e-05        | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 800, 1066]> self = ?,<br>List[int]<> size = [1, 3, 800, 1088],<br>number<> fill_value = 0,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 4, 100, 136]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]  | Unknown  |
|  1 | Tensor<[1, 9, 4, 13, 17]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]    | Unknown  |
|  2 | Tensor<[1, 9, 4, 25, 34]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]    | Unknown  |
|  3 | Tensor<[1, 9, 4, 50, 68]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]    | Unknown  |
|  4 | Tensor<[1, 9, 4, 7, 9]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]      | Unknown  |
|  5 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2] | Unknown  |
|  6 | Tensor<[1, 9, 91, 13, 17]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]   | Unknown  |
|  7 | Tensor<[1, 9, 91, 25, 34]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]   | Unknown  |
|  8 | Tensor<[1, 9, 91, 50, 68]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]   | Unknown  |
|  9 | Tensor<[1, 9, 91, 7, 9]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]     | Unknown  |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 50, 68]> self = ?  | Unknown  |
|  1 | Tensor<[1, 128, 100, 136]> self = ? | Unknown  |
|  2 | Tensor<[1, 128, 200, 272]> self = ? | Unknown  |
|  3 | Tensor<[1, 2048, 25, 34]> self = ?  | Unknown  |
|  4 | Tensor<[1, 256, 100, 136]> self = ? | Unknown  |
|  5 | Tensor<[1, 256, 13, 17]> self = ?   | Unknown  |
|  6 | Tensor<[1, 256, 200, 272]> self = ? | Unknown  |
|  7 | Tensor<[1, 256, 25, 34]> self = ?   | Unknown  |
|  8 | Tensor<[1, 256, 50, 68]> self = ?   | Unknown  |
|  9 | Tensor<[1, 256, 7, 9]> self = ?     | Unknown  |
| 10 | Tensor<[1, 512, 100, 136]> self = ? | Unknown  |
| 11 | Tensor<[1, 512, 25, 34]> self = ?   | Unknown  |
| 12 | Tensor<[1, 512, 50, 68]> self = ?   | Unknown  |
| 13 | Tensor<[1, 64, 200, 272]> self = ?  | Unknown  |
| 14 | Tensor<[1, 64, 400, 544]> self = ?  | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1066]> self = ?,<br>number<> other = 1.0   | Unknown  |
|  1 | Tensor<[800, 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 0            | Unknown  |
|  1 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 1            | Unknown  |
|  2 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 2            | Unknown  |
|  3 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 3            | Unknown  |
|  4 | Tensor<[1, 3, 480, 640]> self = ?,<br>int<> dim = 0,<br>int<> index = 0  | Unknown  |
|  5 | Tensor<[1, 3, 800, 1066]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                    | Unknown  |
|  1 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  2 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1,<br>int<> step = 4 | Unknown  |
|  3 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 2 | Unknown  |
|  4 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -1,<br>int<> step = 4 | Unknown  |
|  5 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 2,<br>Optional[int]<> end = -1,<br>int<> step = 4 | Unknown  |
|  6 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 3,<br>Optional[int]<> end = -1,<br>int<> step = 4 | Unknown  |
|  7 | Tensor<[0]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                       | Unknown  |
|  8 | Tensor<[3]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1                       | Unknown  |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 163206, 4]> self = ?,<br>List[int]<> split_sizes = [122400, 30600, 7650, 1989, 567],<br>int<> dim = 1  | Unknown  |
|  1 | Tensor<[1, 163206, 91]> self = ?,<br>List[int]<> split_sizes = [122400, 30600, 7650, 1989, 567],<br>int<> dim = 1 | Unknown  |
|  2 | Tensor<[163206, 4]> self = ?,<br>List[int]<> split_sizes = [122400, 30600, 7650, 1989, 567]                       | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([0, 1])', 'torch.Size([0, 1])', 'torch.Size([0, 1])', 'torch.Size([0, 1])'],<br>int<> dim = 2     | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([0, 2])', 'torch.Size([0, 2])'],<br>int<> dim = 2                                                 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([0])', 'torch.Size([0])', 'torch.Size([0])', 'torch.Size([0])'],<br>int<> dim = 1                 | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([13600])', 'torch.Size([13600])', 'torch.Size([13600])', 'torch.Size([13600])'],<br>int<> dim = 1 | Unknown  |
|  4 | List[Tensor]<> tensors = ['torch.Size([221])', 'torch.Size([221])', 'torch.Size([221])', 'torch.Size([221])'],<br>int<> dim = 1         | Unknown  |
|  5 | List[Tensor]<> tensors = ['torch.Size([3400])', 'torch.Size([3400])', 'torch.Size([3400])', 'torch.Size([3400])'],<br>int<> dim = 1     | Unknown  |
|  6 | List[Tensor]<> tensors = ['torch.Size([63])', 'torch.Size([63])', 'torch.Size([63])', 'torch.Size([63])'],<br>int<> dim = 1             | Unknown  |
|  7 | List[Tensor]<> tensors = ['torch.Size([850])', 'torch.Size([850])', 'torch.Size([850])', 'torch.Size([850])'],<br>int<> dim = 1         | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?           | Unknown  |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                 | Unknown  |
|  2 | Tensor<[1066]> self = ?,<br>Tensor<> other = 0.5               | Unknown  |
|  3 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?           | Unknown  |
|  4 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  5 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?       | Unknown  |
|  6 | Tensor<[800]> self = ?,<br>Tensor<> other = 0.5                | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int<> dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[0]> self = ?,<br>int<> dim = 1           | Unknown  |
|  1 | Tensor<[100]> self = ?,<br>int<> dim = -1        | Unknown  |
|  2 | Tensor<[3, 1]> self = ?,<br>int<> dim = 2        | Unknown  |
|  3 | Tensor<[3, 480, 640]> self = ?,<br>int<> dim = 0 | Unknown  |
|  4 | Tensor<[3]> self = ?,<br>int<> dim = 1           | Unknown  |
|  5 | Tensor<[50]> self = ?,<br>int<> dim = -1         | Unknown  |
|  6 | Tensor<[800]> self = ?,<br>int<> dim = 1         | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1, 4]> self = ?,<br>List[int]<> size = [0, 4]                         | Unknown  |
|  1 | Tensor<[0, 2, 2]> self = ?,<br>List[int]<> size = [0, 4]                         | Unknown  |
|  2 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int]<> size = [1, -1, 4, 100, 136]   | Unknown  |
|  3 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int]<> size = [1, -1, 4, 13, 17]       | Unknown  |
|  4 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int]<> size = [1, -1, 4, 25, 34]       | Unknown  |
|  5 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int]<> size = [1, -1, 4, 50, 68]       | Unknown  |
|  6 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int]<> size = [1, -1, 4, 7, 9]           | Unknown  |
|  7 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int]<> size = [1, -1, 91, 100, 136] | Unknown  |
|  8 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int]<> size = [1, -1, 91, 13, 17]     | Unknown  |
|  9 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int]<> size = [1, -1, 91, 25, 34]     | Unknown  |
| 10 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int]<> size = [1, -1, 91, 50, 68]     | Unknown  |
| 11 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int]<> size = [1, -1, 91, 7, 9]         | Unknown  |
| 12 | Tensor<[100]> self = ?,<br>List[int]<> size = [-1, 1]                            | Unknown  |
| 13 | Tensor<[13600, 4]> self = ?,<br>List[int]<> size = [-1, 1, 4]                    | Unknown  |
| 14 | Tensor<[13600, 9, 4]> self = ?,<br>List[int]<> size = [-1, 4]                    | Unknown  |
| 15 | Tensor<[136]> self = ?,<br>List[int]<> size = [1, -1]                            | Unknown  |
| 16 | Tensor<[13]> self = ?,<br>List[int]<> size = [-1, 1]                             | Unknown  |
| 17 | Tensor<[17]> self = ?,<br>List[int]<> size = [1, -1]                             | Unknown  |
| 18 | Tensor<[221, 4]> self = ?,<br>List[int]<> size = [-1, 1, 4]                      | Unknown  |
| 19 | Tensor<[221, 9, 4]> self = ?,<br>List[int]<> size = [-1, 4]                      | Unknown  |
| 20 | Tensor<[25]> self = ?,<br>List[int]<> size = [-1, 1]                             | Unknown  |
| 21 | Tensor<[3400, 4]> self = ?,<br>List[int]<> size = [-1, 1, 4]                     | Unknown  |
| 22 | Tensor<[3400, 9, 4]> self = ?,<br>List[int]<> size = [-1, 4]                     | Unknown  |
| 23 | Tensor<[34]> self = ?,<br>List[int]<> size = [1, -1]                             | Unknown  |
| 24 | Tensor<[50]> self = ?,<br>List[int]<> size = [-1, 1]                             | Unknown  |
| 25 | Tensor<[63, 4]> self = ?,<br>List[int]<> size = [-1, 1, 4]                       | Unknown  |
| 26 | Tensor<[63, 9, 4]> self = ?,<br>List[int]<> size = [-1, 4]                       | Unknown  |
| 27 | Tensor<[68]> self = ?,<br>List[int]<> size = [1, -1]                             | Unknown  |
| 28 | Tensor<[7]> self = ?,<br>List[int]<> size = [-1, 1]                              | Unknown  |
| 29 | Tensor<[850, 4]> self = ?,<br>List[int]<> size = [-1, 1, 4]                      | Unknown  |
| 30 | Tensor<[850, 9, 4]> self = ?,<br>List[int]<> size = [-1, 4]                      | Unknown  |
| 31 | Tensor<[9, 4]> self = ?,<br>List[int]<> size = [1, -1, 4]                        | Unknown  |
| 32 | Tensor<[9]> self = ?,<br>List[int]<> size = [1, -1]                              | Unknown  |

