# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  2 |           0 |
|  1 | aten._softmax.default                             |                 10 |           1 |
|  2 | aten._to_copy.default                             |                  4 |           0 |
|  3 | aten._unsafe_view.default                         |                  1 |           0 |
|  4 | aten.add.Tensor                                   |                 12 |           4 |
|  5 | aten.addmm.default                                |                 14 |           3 |
|  6 | aten.arange.start                                 |                  1 |           0 |
|  7 | aten.bernoulli.p                                  |                  2 |           0 |
|  8 | aten.bmm.default                                  |                 21 |           3 |
|  9 | aten.cat.default                                  |                  9 |           0 |
| 10 | aten.clamp_min.default                            |                  1 |           0 |
| 11 | aten.clone.default                                |                 19 |           4 |
| 12 | aten.convolution.default                          |                 45 |           0 |
| 13 | aten.div.Tensor                                   |                  8 |           0 |
| 14 | aten.embedding.default                            |                  2 |           2 |
| 15 | aten.eq.Scalar                                    |                  2 |           0 |
| 16 | aten.expand.default                               |                  7 |           1 |
| 17 | aten.gelu.default                                 |                  2 |           1 |
| 18 | aten.leaky_relu.default                           |                  6 |           0 |
| 19 | aten.linalg_vector_norm.default                   |                  1 |           0 |
| 20 | aten.masked_fill.Scalar                           |                  2 |           0 |
| 21 | aten.mul.Tensor                                   |                  7 |           2 |
| 22 | aten.native_layer_norm.default                    |                  2 |           1 |
| 23 | aten.relu.default                                 |                  4 |           0 |
| 24 | aten.repeat.default                               |                  2 |           0 |
| 25 | aten.rsub.Scalar                                  |                  2 |           1 |
| 26 | aten.scalar_tensor.default                        |                  1 |           0 |
| 27 | aten.select.int                                   |                  2 |           0 |
| 28 | aten.slice.Tensor                                 |                  9 |           0 |
| 29 | aten.squeeze.dim                                  |                  1 |           0 |
| 30 | aten.sub.Tensor                                   |                  2 |           1 |
| 31 | aten.sym_size.int                                 |                  2 |           0 |
| 32 | aten.t.default                                    |                  7 |           3 |
| 33 | aten.tanh.default                                 |                  2 |           0 |
| 34 | aten.transpose.int                                |                 20 |           6 |
| 35 | aten.unsqueeze.default                            |                  8 |           3 |
| 36 | aten.view.default                                 |                 43 |           0 |
| 37 | aten.where.self                                   |                  2 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 96]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 80, 96]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False       | Unknown  |
|  1 | Tensor<[12, 1, 24]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False      | Unknown  |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False       | Unknown  |
|  3 | Tensor<[12, 1, s0 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Unknown  |
|  4 | Tensor<[12, 1, s10 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  5 | Tensor<[12, 1, s2 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Unknown  |
|  6 | Tensor<[12, 1, s4 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Unknown  |
|  7 | Tensor<[12, 1, s6 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Unknown  |
|  8 | Tensor<[12, 1, s8 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Unknown  |
|  9 | Tensor<[12, 24, 24]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False     | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int]<> dtype = torch.bool     | Unknown  |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int]<> dtype = torch.float32  | Unknown  |
|  2 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int]<> dtype = torch.bool    | Unknown  |
|  3 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int]<> size = [1, 24, 768] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?        | Unknown  |
|  1 | Tensor<[1, 12, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?   | Unknown  |
|  2 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ? | Done     |
|  3 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor<[1, 128, 1536]> other = ?  | Unknown  |
|  4 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?      | Done     |
|  5 | Tensor<[1, 256, 384]> self = ?,<br>Tensor<[1, 256, 384]> other = ?    | Unknown  |
|  6 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor<[1, 32, 24576]> other = ?  | Unknown  |
|  7 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor<[1, 64, 6144]> other = ?    | Unknown  |
|  8 | Tensor<[1, 96, 80]> self = ?,<br>Tensor<[1, 96, 80]> other = ?        | Unknown  |
|  9 | Tensor<[1, s0, 768]> self = ?,<br>Tensor<[1, s0, 768]> other = ?      | Unknown  |
| 10 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?      | Done     |
| 11 | Tensor<[24, 24]> self = ?,<br>Tensor<> other = 160                    | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[256]> self = ?,<br>Tensor<[1, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?    | Unknown  |
|  1 | Tensor<[256]> self = ?,<br>Tensor<[1, 80]> mat1 = ?,<br>Tensor<[80, 256]> mat2 = ?      | Unknown  |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[s0, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[s0, 80]> mat1 = ?,<br>Tensor<[80, 256]> mat2 = ?     | Unknown  |
|  4 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  |
|  5 | Tensor<[3072]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  6 | Tensor<[768]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ?  | Unknown  |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[1, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?    | Unknown  |
|  8 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  |
|  9 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
| 10 | Tensor<[768]> self = ?,<br>Tensor<[24, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
| 11 | Tensor<[768]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     |
| 12 | Tensor<[768]> self = ?,<br>Tensor<[s0, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ? | Unknown  |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[s0, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?   | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> start = 0,<br>number<> end = 24,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.bernoulli.p
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 256]> self = ?,<br>float<> p = 0.5  | Unknown  |
|  1 | Tensor<[s0, 256]> self = ?,<br>float<> p = 0.5 | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  |
|  1 | Tensor<[12, 1, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?           | Unknown  |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  |
|  3 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  |
|  4 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?           | Unknown  |
|  5 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  |
|  6 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  |
|  7 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  |
|  8 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s2 + 1]> mat2 = ?       | Unknown  |
|  9 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s4 + 1]> mat2 = ?       | Unknown  |
| 10 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s6 + 1]> mat2 = ?       | Unknown  |
| 11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s8 + 1]> mat2 = ?       | Unknown  |
| 12 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  |
| 13 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  |
| 14 | Tensor<[12, 1, s2 + 1]> self = ?,<br>Tensor<[12, s2 + 1, 64]> mat2 = ?   | Unknown  |
| 15 | Tensor<[12, 1, s4 + 1]> self = ?,<br>Tensor<[12, s4 + 1, 64]> mat2 = ?   | Unknown  |
| 16 | Tensor<[12, 1, s6 + 1]> self = ?,<br>Tensor<[12, s6 + 1, 64]> mat2 = ?   | Unknown  |
| 17 | Tensor<[12, 1, s8 + 1]> self = ?,<br>Tensor<[12, s8 + 1, 64]> mat2 = ?   | Unknown  |
| 18 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     |
| 19 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     |
| 20 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 1, 768])', 'torch.Size([1, 1, 512])'],<br>int<> dim = -1        | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 12, 1, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2   | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 12, s0, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2  | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, 12, s10, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2 | Unknown  |
|  4 | List[Tensor]<> tensors = ['torch.Size([1, 12, s2, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2  | Unknown  |
|  5 | List[Tensor]<> tensors = ['torch.Size([1, 12, s4, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2  | Unknown  |
|  6 | List[Tensor]<> tensors = ['torch.Size([1, 12, s6, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2  | Unknown  |
|  7 | List[Tensor]<> tensors = ['torch.Size([1, 12, s8, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int<> dim = 2  | Unknown  |
|  8 | List[Tensor]<> tensors = ['torch.Size([1, s0, 768])', 'torch.Size([1, s0, 512])'],<br>int<> dim = -1      | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number<> min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                                | Unknown  |
|  1 | Tensor<[1, 1, 768]> self = ?                                                                 | Unknown  |
|  2 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 24, 3072]> self = ?                                                               | Done     |
|  5 | Tensor<[1, 24, 768]> self = ?                                                                | Done     |
|  6 | Tensor<[1, 256, 96]> self = ?                                                                | Unknown  |
|  7 | Tensor<[1, 80, 96]> self = ?                                                                 | Unknown  |
|  8 | Tensor<[1, s0, 768]> self = ?                                                                | Unknown  |
|  9 | Tensor<[12, 1, 1]> self = ?                                                                  | Unknown  |
| 10 | Tensor<[12, 1, 24]> self = ?                                                                 | Unknown  |
| 11 | Tensor<[12, 1, 2]> self = ?                                                                  | Unknown  |
| 12 | Tensor<[12, 1, s0 + 1]> self = ?                                                             | Unknown  |
| 13 | Tensor<[12, 1, s10 + 1]> self = ?                                                            | Unknown  |
| 14 | Tensor<[12, 1, s2 + 1]> self = ?                                                             | Unknown  |
| 15 | Tensor<[12, 1, s4 + 1]> self = ?                                                             | Unknown  |
| 16 | Tensor<[12, 1, s6 + 1]> self = ?                                                             | Unknown  |
| 17 | Tensor<[12, 1, s8 + 1]> self = ?                                                             | Unknown  |
| 18 | Tensor<[12, 24, 24]> self = ?                                                                | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1 | Unknown  |
|  1 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [25],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1 | Unknown  |
|  2 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1  | Unknown  |
|  3 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [1],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
|  4 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
|  5 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
|  6 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1  | Unknown  |
|  7 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
|  8 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [9],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
|  9 | Tensor<[1, 128, 1536]> input = ?,<br>Tensor<[128, 64, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [4],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 10 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 128, 8]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [4],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0],<br>int<> groups = 1     | Unknown  |
| 11 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1  | Unknown  |
| 12 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [25],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1  | Unknown  |
| 13 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
| 14 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [1],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 15 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 16 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 17 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
| 18 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 19 | Tensor<[1, 256, 384]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [9],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 20 | Tensor<[1, 256, 96]> input = ?,<br>Tensor<[256, 256, 5]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1          | Unknown  |
| 21 | Tensor<[1, 256, 96]> input = ?,<br>Tensor<[80, 256, 5]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1           | Unknown  |
| 22 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[1, 32, 7]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1        | Unknown  |
| 23 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 24 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [25],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1    | Unknown  |
| 25 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1     | Unknown  |
| 26 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [1],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 27 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 28 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 29 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1     | Unknown  |
| 30 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 31 | Tensor<[1, 32, 24576]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [9],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 32 | Tensor<[1, 512, 96]> input = ?,<br>Tensor<[512, 256, 8]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [4],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 33 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 32, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [4],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0],<br>int<> groups = 1        | Unknown  |
| 34 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1     | Unknown  |
| 35 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [25],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1     | Unknown  |
| 36 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 37 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [1],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1       | Unknown  |
| 38 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1       | Unknown  |
| 39 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [5],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1       | Unknown  |
| 40 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [15],<br>List[int]<> dilation = [5],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1      | Unknown  |
| 41 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1       | Unknown  |
| 42 | Tensor<[1, 64, 6144]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [9],<br>List[int]<> dilation = [3],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1       | Unknown  |
| 43 | Tensor<[1, 80, 96]> input = ?,<br>Tensor<[256, 80, 5]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [2],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1            | Unknown  |
| 44 | Tensor<[1, 80, 96]> input = ?,<br>Tensor<[512, 80, 7]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [3],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1       | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor<> other = 0.5    | Unknown  |
|  1 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor<> other = 3   | Unknown  |
|  2 | Tensor<[1, 256, 384]> self = ?,<br>Tensor<> other = 3    | Unknown  |
|  3 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor<> other = 3   | Unknown  |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ? | Unknown  |
|  5 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor<> other = 3    | Unknown  |
|  6 | Tensor<[1, s0, 256]> self = ?,<br>Tensor<> other = 0.5   | Unknown  |
|  7 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?     | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                          | Done     |
|  1 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int<> padding_idx = 1 | Done     |
### aten.eq.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>number<> other = 1  | Unknown  |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>number<> other = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int]<> size = [1, 1, 1, 24]            | Unknown  |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int]<> size = [1, 1, 24, 24]           | Done     |
|  2 | Tensor<[1, 1, 512]> self = ?,<br>List[int]<> size = [-1, 'torch.Size(s0)', -1] | Unknown  |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>List[int]<> size = [-1, 1, -1]                | Unknown  |
|  4 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [1, 512]                        | Unknown  |
|  5 | Tensor<[24, 12, 64]> self = ?,<br>List[int]<> size = [24, 12, 64]              | Unknown  |
|  6 | Tensor<[24, 64, 24]> self = ?,<br>List[int]<> size = [24, 64, 24]              | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  |
|  1 | Tensor<[1, 24, 3072]> self = ? | Done     |
### aten.leaky_relu.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 1536]> self = ?,<br>number<> negative_slope = 0.1 | Unknown  |
|  1 | Tensor<[1, 256, 384]> self = ?,<br>number<> negative_slope = 0.1  | Unknown  |
|  2 | Tensor<[1, 32, 24576]> self = ?                                   | Unknown  |
|  3 | Tensor<[1, 32, 24576]> self = ?,<br>number<> negative_slope = 0.1 | Unknown  |
|  4 | Tensor<[1, 512, 96]> self = ?,<br>number<> negative_slope = 0.1   | Unknown  |
|  5 | Tensor<[1, 64, 6144]> self = ?,<br>number<> negative_slope = 0.1  | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>number<> ord = 2.0,<br>Optional[List[int]]<> dim = [1],<br>bool<> keepdim = True | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> mask = ?,<br>number<> value = -3.4028234663852886e+38   | Unknown  |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number<> value = -3.4028234663852886e+38 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor<> other = 1      | Unknown  |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<> other = 0.125  | Unknown  |
|  2 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<> other = 0.125 | Done     |
|  3 | Tensor<[1, s0, 256]> self = ?,<br>Tensor<> other = 1     | Unknown  |
|  4 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?    | Unknown  |
|  5 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?   | Done     |
|  6 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?   | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05  | Unknown  |
|  1 | Tensor<[1, 24, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05 | Done     |
### aten.relu.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?  | Unknown  |
|  1 | Tensor<[1, 1, 768]> self = ?  | Unknown  |
|  2 | Tensor<[1, s0, 256]> self = ? | Unknown  |
|  3 | Tensor<[1, s0, 768]> self = ? | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>List[int]<> repeats = [1, 1, 1]  | Unknown  |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>List[int]<> repeats = [1, 1, 1] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>number<> other = 1.0  | Unknown  |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> s = 0,<br>Optional[int]<> dtype = torch.float32,<br>Optional[int]<> layout = torch.strided,<br>Optional[Device]<> device = cpu | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int<> dim = 0,<br>int<> index = 0  | Unknown  |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>int<> dim = 0,<br>int<> index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Unknown  |
|  1 | Tensor<[1, 1876, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1  | Unknown  |
|  2 | Tensor<[1, 1876, 768]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 1   | Unknown  |
|  3 | Tensor<[1, 1876, 768]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<s0> end = ? | Unknown  |
|  4 | Tensor<[1, 24]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1         | Unknown  |
|  5 | Tensor<[1, 24]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1         | Unknown  |
|  6 | Tensor<[1, 600, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1   | Unknown  |
|  7 | Tensor<[1, 600, 768]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 24   | Unknown  |
|  8 | Tensor<[24]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 24576]> self = ?,<br>int<> dim = 0 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ? | Done     |
|  1 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?   | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1, s0, 256]> self = ?,<br>int<> dim = 1 | Unknown  |
|  1 | Tensor<[1, s0, 768]> self = ?,<br>int<> dim = 1 | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[256, 256]> self = ?  | Unknown  |
|  1 | Tensor<[256, 80]> self = ?   | Unknown  |
|  2 | Tensor<[3072, 768]> self = ? | Done     |
|  3 | Tensor<[768, 1280]> self = ? | Unknown  |
|  4 | Tensor<[768, 256]> self = ?  | Unknown  |
|  5 | Tensor<[768, 3072]> self = ? | Done     |
|  6 | Tensor<[768, 768]> self = ?  | Done     |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 24576]> self = ? | Unknown  |
|  1 | Tensor<[1, 256, 96]> self = ?  | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Unknown  |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Unknown  |
|  2 | Tensor<[1, 12, 24, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  3 | Tensor<[1, 24, 12, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[1, 24576]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 0        | Unknown  |
|  5 | Tensor<[1, 80, 96]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2       | Unknown  |
|  6 | Tensor<[1, 96, 80]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2       | Unknown  |
|  7 | Tensor<[1, 96, 80]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1       | Unknown  |
|  8 | Tensor<[12, 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2       | Unknown  |
|  9 | Tensor<[12, 2, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2       | Unknown  |
| 10 | Tensor<[12, 24, 64]> self = ?,<br>int<> dim0 = 0,<br>int<> dim1 = 1      | Done     |
| 11 | Tensor<[12, 24, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2      | Done     |
| 12 | Tensor<[12, s0 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Unknown  |
| 13 | Tensor<[12, s10 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Unknown  |
| 14 | Tensor<[12, s2 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Unknown  |
| 15 | Tensor<[12, s4 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Unknown  |
| 16 | Tensor<[12, s6 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Unknown  |
| 17 | Tensor<[12, s8 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2  | Unknown  |
| 18 | Tensor<[24, 12, 24]> self = ?,<br>int<> dim0 = 0,<br>int<> dim1 = 1      | Done     |
| 19 | Tensor<[24, 24, 64]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1    | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 24]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 24]> self = ?,<br>int<> dim = 1    | Done     |
|  2 | Tensor<[1, 256]> self = ?,<br>int<> dim = 0   | Unknown  |
|  3 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1   | Unknown  |
|  4 | Tensor<[24]> self = ?,<br>int<> dim = 0       | Done     |
|  5 | Tensor<[24]> self = ?,<br>int<> dim = 1       | Unknown  |
|  6 | Tensor<[96, 80]> self = ?,<br>int<> dim = 0   | Unknown  |
|  7 | Tensor<[s0, 256]> self = ?,<br>int<> dim = 0  | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int]<> size = [1, 1, 768]             | Unknown  |
|  1 | Tensor<[1, 1, 1280]> self = ?,<br>List[int]<> size = [1, 1280]                 | Unknown  |
|  2 | Tensor<[1, 1, 256]> self = ?,<br>List[int]<> size = [1, 256]                   | Unknown  |
|  3 | Tensor<[1, 1, 3072]> self = ?,<br>List[int]<> size = [1, 3072]                 | Unknown  |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int]<> size = [1, -1, 12, 64]            | Unknown  |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int]<> size = [1, 1, 12, 64]             | Unknown  |
|  6 | Tensor<[1, 1, 768]> self = ?,<br>List[int]<> size = [1, 768]                   | Unknown  |
|  7 | Tensor<[1, 1, 80]> self = ?,<br>List[int]<> size = [1, 80]                     | Unknown  |
|  8 | Tensor<[1, 12, 1, 24]> self = ?,<br>List[int]<> size = [12, 1, 24]             | Unknown  |
|  9 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]            | Unknown  |
| 10 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]            | Unknown  |
| 11 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int]<> size = [12, 24, 24]           | Unknown  |
| 12 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]           | Unknown  |
| 13 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]       | Unknown  |
| 14 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]      | Unknown  |
| 15 | Tensor<[1, 12, s2 + 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]       | Unknown  |
| 16 | Tensor<[1, 12, s4 + 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]       | Unknown  |
| 17 | Tensor<[1, 12, s6 + 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]       | Unknown  |
| 18 | Tensor<[1, 12, s8 + 1, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]       | Unknown  |
| 19 | Tensor<[1, 24, 3072]> self = ?,<br>List[int]<> size = [24, 3072]               | Unknown  |
| 20 | Tensor<[1, 24, 768]> self = ?,<br>List[int]<> size = [1, -1, 12, 64]           | Unknown  |
| 21 | Tensor<[1, 24, 768]> self = ?,<br>List[int]<> size = [1, 24, 12, 64]           | Unknown  |
| 22 | Tensor<[1, 24, 768]> self = ?,<br>List[int]<> size = [24, 768]                 | Unknown  |
| 23 | Tensor<[1, 256]> self = ?,<br>List[int]<> size = [1, 1, 256]                   | Unknown  |
| 24 | Tensor<[1, 3072]> self = ?,<br>List[int]<> size = [1, 1, 3072]                 | Unknown  |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int]<> size = [1, 1, 768]                   | Unknown  |
| 26 | Tensor<[1, s0, 1280]> self = ?,<br>List[int]<> size = ['torch.Size(s0)', 1280] | Unknown  |
| 27 | Tensor<[1, s0, 256]> self = ?,<br>List[int]<> size = ['torch.Size(s0)', 256]   | Unknown  |
| 28 | Tensor<[1, s0, 80]> self = ?,<br>List[int]<> size = ['torch.Size(s0)', 80]     | Unknown  |
| 29 | Tensor<[12, 1, 24]> self = ?,<br>List[int]<> size = [1, 12, 1, 24]             | Unknown  |
| 30 | Tensor<[12, 1, 64]> self = ?,<br>List[int]<> size = [1, 12, 1, 64]             | Unknown  |
| 31 | Tensor<[12, 24, 24]> self = ?,<br>List[int]<> size = [1, 12, 24, 24]           | Unknown  |
| 32 | Tensor<[12, 24, 24]> self = ?,<br>List[int]<> size = [12, 24, 24]              | Unknown  |
| 33 | Tensor<[12, 24, 64]> self = ?,<br>List[int]<> size = [1, 12, 24, 64]           | Unknown  |
| 34 | Tensor<[12, 24, 64]> self = ?,<br>List[int]<> size = [12, -1, 64]              | Unknown  |
| 35 | Tensor<[24, 12, 24]> self = ?,<br>List[int]<> size = [24, 12, 24]              | Unknown  |
| 36 | Tensor<[24, 12, 64]> self = ?,<br>List[int]<> size = [24, 12, 64]              | Unknown  |
| 37 | Tensor<[24, 3072]> self = ?,<br>List[int]<> size = [1, 24, 3072]               | Unknown  |
| 38 | Tensor<[24, 64, 24]> self = ?,<br>List[int]<> size = [24, 64, 24]              | Unknown  |
| 39 | Tensor<[24, 768]> self = ?,<br>List[int]<> size = [1, 24, 768]                 | Unknown  |
| 40 | Tensor<[24576, 1]> self = ?,<br>List[int]<> size = [-1]                        | Unknown  |
| 41 | Tensor<[s0, 256]> self = ?,<br>List[int]<> size = [1, 'torch.Size(s0)', 256]   | Unknown  |
| 42 | Tensor<[s0, 768]> self = ?,<br>List[int]<> size = [1, 'torch.Size(s0)', 768]   | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> condition = ?,<br>Tensor<[1, 1, 256]> self = ?,<br>Tensor<[]> other = ?   | Unknown  |
|  1 | Tensor<[1, s0, 256]> condition = ?,<br>Tensor<[1, s0, 256]> self = ?,<br>Tensor<[]> other = ? | Unknown  |

