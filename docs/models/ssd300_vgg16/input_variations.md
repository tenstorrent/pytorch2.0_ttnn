# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._to_copy.default                |                  3 |           0 |         0 |          0 | ✘           |               0    |
|  1 | aten._unsafe_index.Tensor            |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  2 | aten._unsafe_view.default            |                 15 |           0 |         0 |          0 | ✘           |               0    |
|  3 | aten.add.Tensor                      |                 13 |           9 |         0 |          0 | 🚧          |               0.69 |
|  4 | aten.arange.default                  |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  5 | aten.arange.start                    |                  6 |           0 |         0 |          0 | ✘           |               0    |
|  6 | aten.cat.default                     |                 10 |           0 |         0 |          0 | ✘           |               0    |
|  7 | aten.ceil.default                    |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  8 | aten.clamp.default                   |                  7 |           5 |         0 |          0 | 🚧          |               0.71 |
|  9 | aten.clamp_min.default               |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 10 | aten.clone.default                   |                 15 |          15 |         0 |          0 | ✅          |               1    |
| 11 | aten.convolution.default             |                 31 |           0 |         0 |          0 | ✘           |               0    |
| 12 | aten.div.Tensor                      |                 11 |           1 |         0 |          0 | 🚧          |               0.09 |
| 13 | aten.exp.default                     |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 14 | aten.expand.default                  |                 12 |           6 |         0 |          0 | 🚧          |               0.5  |
| 15 | aten.lift_fresh_copy.default         |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 16 | aten.linalg_vector_norm.default      |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 17 | aten.max.default                     |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 18 | aten.max_pool2d_with_indices.default |                  5 |           0 |         0 |          0 | ✘           |               0    |
| 19 | aten.mul.Tensor                      |                 12 |           7 |         0 |          0 | 🚧          |               0.58 |
| 20 | aten.new_full.default                |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 21 | aten.permute.default                 |                 12 |          12 |         0 |          0 | ✅          |               1    |
| 22 | aten.relu.default                    |                 14 |          14 |         0 |          0 | ✅          |               1    |
| 23 | aten.repeat.default                  |                  6 |           5 |         0 |          0 | 🚧          |               0.83 |
| 24 | aten.rsub.Scalar                     |                  2 |           0 |         0 |          0 | ✘           |               0    |
| 25 | aten.select.int                      |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 26 | aten.slice.Tensor                    |                 12 |           2 |         0 |          0 | 🚧          |               0.17 |
| 27 | aten.stack.default                   |                  9 |           0 |         0 |          0 | ✘           |               0    |
| 28 | aten.sub.Tensor                      |                  7 |           5 |         0 |          0 | 🚧          |               0.71 |
| 29 | aten.unbind.int                      |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 30 | aten.unsqueeze.default               |                  6 |           2 |         0 |          0 | 🚧          |               0.33 |
| 31 | aten.view.default                    |                 36 |           0 |         0 |         34 | ✘           |               0    |
***
### aten._to_copy.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[25]> self = ?,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu | Unknown  |
|  1 | Tensor<[300]> self = ?,<br>Optional[int]<> dtype = torch.int64                                      | None     |
|  2 | Tensor<[]> self = ?,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu   | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([300, 1])', 'torch.Size([300])'] | None     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int]<> size = [1, 600, 4]    | None     |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int]<> size = [1, 600, 91]  | None     |
|  2 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>List[int]<> size = [1, 2166, 4]   | None     |
|  3 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>List[int]<> size = [1, 2166, 91] | None     |
|  4 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>List[int]<> size = [1, 36, 4]       | None     |
|  5 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>List[int]<> size = [1, 36, 91]     | None     |
|  6 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>List[int]<> size = [1, 5776, 4]   | None     |
|  7 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>List[int]<> size = [1, 5776, 91] | None     |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int]<> size = [1, 150, 4]      | None     |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int]<> size = [1, 150, 91]    | None     |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int]<> size = [100]                   | None     |
| 11 | Tensor<[19, 19]> self = ?,<br>List[int]<> size = [361]                   | None     |
| 12 | Tensor<[3, 3]> self = ?,<br>List[int]<> size = [9]                       | None     |
| 13 | Tensor<[38, 38]> self = ?,<br>List[int]<> size = [1444]                  | None     |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int]<> size = [25]                      | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ? | Done     |
|  1 | Tensor<[10]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
|  2 | Tensor<[19]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
|  3 | Tensor<[1]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
|  4 | Tensor<[25, 4]> self = ?,<br>Tensor<[25, 1]> other = ?                   | Unknown  |
|  5 | Tensor<[300]> self = ?,<br>Tensor<> other = 0.5                          | Done     |
|  6 | Tensor<[38]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
|  7 | Tensor<[3]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
|  8 | Tensor<[5]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
|  9 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?               | Unknown  |
| 10 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?               | Done     |
| 11 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                     | Unknown  |
| 12 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                             | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 300,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
### aten.arange.start
|    | ATen Input Variations                                                                                                | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> start = 0,<br>number<> end = 1,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | None     |
|  1 | number<> start = 0,<br>number<> end = 10,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
|  2 | number<> start = 0,<br>number<> end = 19,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
|  3 | number<> start = 0,<br>number<> end = 3,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | None     |
|  4 | number<> start = 0,<br>number<> end = 38,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
|  5 | number<> start = 0,<br>number<> end = 5,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | None     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 5776, 4])', 'torch.Size([1, 2166, 4])', 'torch.Size([1, 600, 4])', 'torch.Size([1, 150, 4])', 'torch.Size([1, 36, 4])', 'torch.Size([1, 4, 4])'],<br>int<> dim = 1       | None     |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 5776, 91])', 'torch.Size([1, 2166, 91])', 'torch.Size([1, 600, 91])', 'torch.Size([1, 150, 91])', 'torch.Size([1, 36, 91])', 'torch.Size([1, 4, 91])'],<br>int<> dim = 1 | None     |
|  2 | List[Tensor]<> tensors = ['torch.Size([150, 2])', 'torch.Size([150, 2])'],<br>int<> dim = 1                                                                                                                        | None     |
|  3 | List[Tensor]<> tensors = ['torch.Size([2166, 2])', 'torch.Size([2166, 2])'],<br>int<> dim = 1                                                                                                                      | None     |
|  4 | List[Tensor]<> tensors = ['torch.Size([36, 2])', 'torch.Size([36, 2])'],<br>int<> dim = 1                                                                                                                          | None     |
|  5 | List[Tensor]<> tensors = ['torch.Size([4, 2])', 'torch.Size([4, 2])'],<br>int<> dim = 1                                                                                                                            | None     |
|  6 | List[Tensor]<> tensors = ['torch.Size([5776, 2])', 'torch.Size([5776, 2])'],<br>int<> dim = 1                                                                                                                      | None     |
|  7 | List[Tensor]<> tensors = ['torch.Size([5776, 4])', 'torch.Size([2166, 4])', 'torch.Size([600, 4])', 'torch.Size([150, 4])', 'torch.Size([36, 4])', 'torch.Size([4, 4])']                                           | None     |
|  8 | List[Tensor]<> tensors = ['torch.Size([600, 2])', 'torch.Size([600, 2])'],<br>int<> dim = 1                                                                                                                        | None     |
|  9 | List[Tensor]<> tensors = ['torch.Size([8732, 2])', 'torch.Size([8732, 2])'],<br>int<> dim = -1                                                                                                                     | None     |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[300]> self = ?  | None     |
### aten.clamp.default
|    | ATen Input Variations                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[300]> self = ?,<br>Optional[number]<> min = 0.0                                                  | Done     |
|  1 | Tensor<[300]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 479                   | Done     |
|  2 | Tensor<[300]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 639                   | Done     |
|  3 | Tensor<[4, 2]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 1                    | Done     |
|  4 | Tensor<[6, 2]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 1                    | Done     |
|  5 | Tensor<[8732, 1]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 4.135166556742356 | Unknown  |
|  6 | Tensor<[8732, 2]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 300               | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>number<> min = 1e-12 | None     |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  3 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format    | Done     |
|  5 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
|  6 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  7 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format    | Done     |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
| 10 | Tensor<[10, 10]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format           | Done     |
| 11 | Tensor<[19, 19]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format           | Done     |
| 12 | Tensor<[3, 3]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format             | Done     |
| 13 | Tensor<[38, 38]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format           | Done     |
| 14 | Tensor<[5, 5]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format             | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | None     |
|  1 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[24, 1024, 3, 3]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
|  2 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
|  3 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[546, 1024, 3, 3]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
|  4 | Tensor<[1, 128, 10, 10]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
|  5 | Tensor<[1, 128, 150, 150]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
|  6 | Tensor<[1, 128, 3, 3]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
|  7 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
|  8 | Tensor<[1, 128, 75, 75]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
|  9 | Tensor<[1, 256, 1, 1]> input = ?,<br>Tensor<[16, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 10 | Tensor<[1, 256, 1, 1]> input = ?,<br>Tensor<[364, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[364]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 11 | Tensor<[1, 256, 19, 19]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 12 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 13 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[16, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 14 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[364, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[364]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 15 | Tensor<[1, 256, 38, 38]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 16 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 17 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[24, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 18 | Tensor<[1, 256, 5, 5]> input = ?,<br>Tensor<[546, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 19 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 20 | Tensor<[1, 3, 300, 300]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 21 | Tensor<[1, 512, 10, 10]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 22 | Tensor<[1, 512, 10, 10]> input = ?,<br>Tensor<[24, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 23 | Tensor<[1, 512, 10, 10]> input = ?,<br>Tensor<[546, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[546]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 24 | Tensor<[1, 512, 19, 19]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [6, 6],<br>List[int]<> dilation = [6, 6],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 25 | Tensor<[1, 512, 19, 19]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 26 | Tensor<[1, 512, 38, 38]> input = ?,<br>Tensor<[16, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 27 | Tensor<[1, 512, 38, 38]> input = ?,<br>Tensor<[364, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[364]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 28 | Tensor<[1, 512, 38, 38]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 29 | Tensor<[1, 64, 150, 150]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 30 | Tensor<[1, 64, 300, 300]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | None     |
|  1 | Tensor<[10]> self = ?,<br>Tensor<> other = 9.375                         | None     |
|  2 | Tensor<[19]> self = ?,<br>Tensor<> other = 18.75                         | None     |
|  3 | Tensor<[1]> self = ?,<br>Tensor<> other = 1.0                            | None     |
|  4 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     |
|  5 | Tensor<[38]> self = ?,<br>Tensor<> other = 37.5                          | None     |
|  6 | Tensor<[3]> self = ?,<br>Tensor<> other = 3.0                            | None     |
|  7 | Tensor<[5]> self = ?,<br>Tensor<> other = 4.6875                         | None     |
|  8 | Tensor<[8732, 1]> self = ?,<br>Tensor<> other = 10.0                     | Unknown  |
|  9 | Tensor<[8732, 1]> self = ?,<br>Tensor<> other = 5.0                      | Unknown  |
| 10 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                             | Unknown  |
### aten.exp.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[8732, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>List[int]<> size = [1, 512, 38, 38] | Done     |
|  1 | Tensor<[1, 10]> self = ?,<br>List[int]<> size = [10, 10]                | Done     |
|  2 | Tensor<[1, 19]> self = ?,<br>List[int]<> size = [19, 19]                | Done     |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [1, 1]                   | None     |
|  4 | Tensor<[1, 38]> self = ?,<br>List[int]<> size = [38, 38]                | Done     |
|  5 | Tensor<[1, 3]> self = ?,<br>List[int]<> size = [3, 3]                   | Done     |
|  6 | Tensor<[1, 5]> self = ?,<br>List[int]<> size = [5, 5]                   | Done     |
|  7 | Tensor<[10, 1]> self = ?,<br>List[int]<> size = [10, 10]                | None     |
|  8 | Tensor<[19, 1]> self = ?,<br>List[int]<> size = [19, 19]                | None     |
|  9 | Tensor<[3, 1]> self = ?,<br>List[int]<> size = [3, 3]                   | None     |
| 10 | Tensor<[38, 1]> self = ?,<br>List[int]<> size = [38, 38]                | None     |
| 11 | Tensor<[5, 1]> self = ?,<br>List[int]<> size = [5, 5]                   | None     |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<> self = ?       | None     |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 38, 38]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [1],<br>bool<> keepdim = True | None     |
### aten.max.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[25, 4]> self = ? | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 150, 150]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]                                                                                              | None     |
|  1 | Tensor<[1, 256, 75, 75]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> ceil_mode = True | None     |
|  2 | Tensor<[1, 512, 19, 19]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1]                                                               | None     |
|  3 | Tensor<[1, 512, 38, 38]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]                                                                                                | None     |
|  4 | Tensor<[1, 64, 300, 300]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]                                                                                               | None     |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?       | Done     |
|  1 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?          | Done     |
|  2 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Done     |
|  3 | Tensor<[12]> self = ?,<br>Tensor<[]> other = ?                         | Unknown  |
|  4 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                         | Unknown  |
|  5 | Tensor<[300]> self = ?,<br>Tensor<> other = 1.6                        | Done     |
|  6 | Tensor<[300]> self = ?,<br>Tensor<> other = 2.1333333333333333         | Done     |
|  7 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  |
|  8 | Tensor<[8732, 2]> self = ?,<br>Tensor<> other = 0.5                    | Done     |
|  9 | Tensor<[8732, 2]> self = ?,<br>Tensor<[2]> other = ?                   | Done     |
| 10 | Tensor<[8732]> self = ?,<br>Tensor<> other = 0.5                       | Unknown  |
| 11 | Tensor<[]> self = ?,<br>Tensor<[8732, 1]> other = ?                    | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 300, 300]> self = ?,<br>List[int]<> size = [1, 3, 300, 300],<br>number<> fill_value = 0,<br>Optional[bool]<> pin_memory = False | None     |
### aten.permute.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 4, 4, 1, 1]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]    | Done     |
|  1 | Tensor<[1, 4, 4, 3, 3]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]    | Done     |
|  2 | Tensor<[1, 4, 4, 38, 38]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]  | Done     |
|  3 | Tensor<[1, 4, 91, 1, 1]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]   | Done     |
|  4 | Tensor<[1, 4, 91, 3, 3]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]   | Done     |
|  5 | Tensor<[1, 4, 91, 38, 38]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2] | Done     |
|  6 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]  | Done     |
|  7 | Tensor<[1, 6, 4, 19, 19]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]  | Done     |
|  8 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]    | Done     |
|  9 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2] | Done     |
| 10 | Tensor<[1, 6, 91, 19, 19]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2] | Done     |
| 11 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int]<> dims = [0, 3, 4, 1, 2]   | Done     |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 19, 19]> self = ?  | Done     |
|  1 | Tensor<[1, 128, 10, 10]> self = ?   | Done     |
|  2 | Tensor<[1, 128, 150, 150]> self = ? | Done     |
|  3 | Tensor<[1, 128, 3, 3]> self = ?     | Done     |
|  4 | Tensor<[1, 128, 5, 5]> self = ?     | Done     |
|  5 | Tensor<[1, 256, 1, 1]> self = ?     | Done     |
|  6 | Tensor<[1, 256, 19, 19]> self = ?   | Done     |
|  7 | Tensor<[1, 256, 3, 3]> self = ?     | Done     |
|  8 | Tensor<[1, 256, 5, 5]> self = ?     | Done     |
|  9 | Tensor<[1, 256, 75, 75]> self = ?   | Done     |
| 10 | Tensor<[1, 512, 10, 10]> self = ?   | Done     |
| 11 | Tensor<[1, 512, 19, 19]> self = ?   | Done     |
| 12 | Tensor<[1, 512, 38, 38]> self = ?   | Done     |
| 13 | Tensor<[1, 64, 300, 300]> self = ?  | Done     |
### aten.repeat.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[4, 2]> self = ?,<br>List[int]<> repeats = [1, 1]    | Unknown  |
|  1 | Tensor<[4, 2]> self = ?,<br>List[int]<> repeats = [1444, 1] | Done     |
|  2 | Tensor<[4, 2]> self = ?,<br>List[int]<> repeats = [9, 1]    | Done     |
|  3 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [100, 1]  | Done     |
|  4 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [25, 1]   | Done     |
|  5 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [361, 1]  | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[300, 1]> self = ?,<br>number<> other = 1.0 | None     |
|  1 | Tensor<[300]> self = ?,<br>number<> other = 1.0    | None     |
### aten.select.int
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 300, 300]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | None     |
|  1 | Tensor<[1, 3, 480, 640]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | None     |
|  2 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 0        | Unknown  |
|  3 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 1        | Unknown  |
|  4 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 2        | Unknown  |
|  5 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>int<> index = 3        | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[25]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                         | Unknown  |
|  1 | Tensor<[3]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                          | Unknown  |
|  2 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                    | Unknown  |
|  3 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 2                                      | Done     |
|  4 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | Unknown  |
|  5 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 4 | Unknown  |
|  6 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 2 | Unknown  |
|  7 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 4 | Unknown  |
|  8 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 2,<br>Optional[int]<> end = 9223372036854775807                    | Done     |
|  9 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 2,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 4 | Unknown  |
| 10 | Tensor<[8732, 4]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 3,<br>Optional[int]<> end = 9223372036854775807,<br>int<> step = 4 | Unknown  |
| 11 | Tensor<[8732]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9223372036854775807                       | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])', 'torch.Size([100])'],<br>int<> dim = -1 | None     |
|  1 | List[Tensor]<> tensors = ['torch.Size([12])', 'torch.Size([12])', 'torch.Size([12])', 'torch.Size([12])'],<br>int<> dim = 1                                                                                                                                                                              | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1444])', 'torch.Size([1444])', 'torch.Size([1444])', 'torch.Size([1444])', 'torch.Size([1444])', 'torch.Size([1444])', 'torch.Size([1444])', 'torch.Size([1444])'],<br>int<> dim = -1                                                                             | None     |
|  3 | List[Tensor]<> tensors = ['torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])', 'torch.Size([1])'],<br>int<> dim = -1                                                                                                     | None     |
|  4 | List[Tensor]<> tensors = ['torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])', 'torch.Size([25])'],<br>int<> dim = -1             | None     |
|  5 | List[Tensor]<> tensors = ['torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])', 'torch.Size([361])'],<br>int<> dim = -1 | None     |
|  6 | List[Tensor]<> tensors = ['torch.Size([8732, 1])', 'torch.Size([8732, 1])', 'torch.Size([8732, 1])', 'torch.Size([8732, 1])'],<br>int<> dim = 2                                                                                                                                                          | Unknown  |
|  7 | List[Tensor]<> tensors = ['torch.Size([8732, 2])', 'torch.Size([8732, 2])'],<br>int<> dim = 2                                                                                                                                                                                                            | Unknown  |
|  8 | List[Tensor]<> tensors = ['torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])', 'torch.Size([9])'],<br>int<> dim = -1                                                                                                     | None     |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     |
|  1 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?       | Done     |
|  2 | Tensor<[300]> self = ?,<br>Tensor<> other = 0.5                | Done     |
|  3 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?             | Done     |
|  4 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?     | Unknown  |
|  5 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?     | Done     |
|  6 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?           | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[12, 4]> self = ?,<br>int<> dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[25]> self = ?,<br>int<> dim = 1          | Unknown  |
|  1 | Tensor<[3, 1]> self = ?,<br>int<> dim = 2        | Done     |
|  2 | Tensor<[3, 480, 640]> self = ?,<br>int<> dim = 0 | Done     |
|  3 | Tensor<[300]> self = ?,<br>int<> dim = 1         | None     |
|  4 | Tensor<[3]> self = ?,<br>int<> dim = 1           | None     |
|  5 | Tensor<[8732]> self = ?,<br>int<> dim = 1        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 4, 4]> self = ?,<br>List[int]<> size = [1, -1, 4]           | Fallback |
|  1 | Tensor<[1, 1, 1, 4, 91]> self = ?,<br>List[int]<> size = [1, -1, 91]         | Fallback |
|  2 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int]<> size = [1, -1, 4, 1, 1]       | Fallback |
|  3 | Tensor<[1, 16, 3, 3]> self = ?,<br>List[int]<> size = [1, -1, 4, 3, 3]       | Fallback |
|  4 | Tensor<[1, 16, 38, 38]> self = ?,<br>List[int]<> size = [1, -1, 4, 38, 38]   | Fallback |
|  5 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [-1]                          | Fallback |
|  6 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int]<> size = [1, -1, 4, 10, 10]   | Fallback |
|  7 | Tensor<[1, 24, 19, 19]> self = ?,<br>List[int]<> size = [1, -1, 4, 19, 19]   | Fallback |
|  8 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int]<> size = [1, -1, 4, 5, 5]       | Fallback |
|  9 | Tensor<[1, 364, 1, 1]> self = ?,<br>List[int]<> size = [1, -1, 91, 1, 1]     | Fallback |
| 10 | Tensor<[1, 364, 3, 3]> self = ?,<br>List[int]<> size = [1, -1, 91, 3, 3]     | Fallback |
| 11 | Tensor<[1, 364, 38, 38]> self = ?,<br>List[int]<> size = [1, -1, 91, 38, 38] | Fallback |
| 12 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int]<> size = [1, -1, 91, 10, 10] | Fallback |
| 13 | Tensor<[1, 546, 19, 19]> self = ?,<br>List[int]<> size = [1, -1, 91, 19, 19] | Fallback |
| 14 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int]<> size = [1, -1, 91, 5, 5]     | Fallback |
| 15 | Tensor<[1, 8]> self = ?,<br>List[int]<> size = [-1, 2]                       | Fallback |
| 16 | Tensor<[100, 12]> self = ?,<br>List[int]<> size = [-1, 2]                    | Fallback |
| 17 | Tensor<[10]> self = ?,<br>List[int]<> size = [-1, 1]                         | Fallback |
| 18 | Tensor<[10]> self = ?,<br>List[int]<> size = [1, -1]                         | Fallback |
| 19 | Tensor<[1444, 8]> self = ?,<br>List[int]<> size = [-1, 2]                    | Fallback |
| 20 | Tensor<[19]> self = ?,<br>List[int]<> size = [-1, 1]                         | Fallback |
| 21 | Tensor<[19]> self = ?,<br>List[int]<> size = [1, -1]                         | Fallback |
| 22 | Tensor<[1]> self = ?,<br>List[int]<> size = [-1, 1]                          | Fallback |
| 23 | Tensor<[1]> self = ?,<br>List[int]<> size = [1, -1]                          | Fallback |
| 24 | Tensor<[25, 12]> self = ?,<br>List[int]<> size = [-1, 2]                     | Fallback |
| 25 | Tensor<[361, 12]> self = ?,<br>List[int]<> size = [-1, 2]                    | Fallback |
| 26 | Tensor<[38]> self = ?,<br>List[int]<> size = [-1, 1]                         | Fallback |
| 27 | Tensor<[38]> self = ?,<br>List[int]<> size = [1, -1]                         | Fallback |
| 28 | Tensor<[3]> self = ?,<br>List[int]<> size = [-1, 1]                          | Fallback |
| 29 | Tensor<[3]> self = ?,<br>List[int]<> size = [1, -1]                          | Fallback |
| 30 | Tensor<[512]> self = ?,<br>List[int]<> size = [1, -1, 1, 1]                  | Fallback |
| 31 | Tensor<[5]> self = ?,<br>List[int]<> size = [-1, 1]                          | Fallback |
| 32 | Tensor<[5]> self = ?,<br>List[int]<> size = [1, -1]                          | Fallback |
| 33 | Tensor<[8732, 1, 4]> self = ?,<br>List[int]<> size = [8732, 4]               | Unknown  |
| 34 | Tensor<[8732, 2, 2]> self = ?,<br>List[int]<> size = [8732, 4]               | Unknown  |
| 35 | Tensor<[9, 8]> self = ?,<br>List[int]<> size = [-1, 2]                       | Fallback |

