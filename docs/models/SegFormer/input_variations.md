# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |           0 |
|  1 | aten._softmax.default                             |                  4 |           4 |
|  2 | aten._to_copy.default                             |                  1 |           0 |
|  3 | aten._unsafe_index.Tensor                         |                  4 |           0 |
|  4 | aten.add.Tensor                                   |                 10 |          10 |
|  5 | aten.addmm.default                                |                 15 |          15 |
|  6 | aten.arange.default                               |                  1 |           0 |
|  7 | aten.bmm.default                                  |                  8 |           8 |
|  8 | aten.cat.default                                  |                  1 |           0 |
|  9 | aten.ceil.default                                 |                  1 |           0 |
| 10 | aten.clamp.default                                |                  5 |           5 |
| 11 | aten.clone.default                                |                 21 |          17 |
| 12 | aten.convolution.default                          |                 13 |           0 |
| 13 | aten.div.Tensor                                   |                  4 |           4 |
| 14 | aten.expand.default                               |                 15 |           0 |
| 15 | aten.gelu.default                                 |                  4 |           4 |
| 16 | aten.mm.default                                   |                  4 |           4 |
| 17 | aten.mul.Tensor                                   |                  6 |           6 |
| 18 | aten.native_layer_norm.default                    |                  7 |           7 |
| 19 | aten.permute.default                              |                 25 |          25 |
| 20 | aten.relu.default                                 |                  1 |           1 |
| 21 | aten.rsub.Scalar                                  |                  2 |           0 |
| 22 | aten.sub.Tensor                                   |                  3 |           3 |
| 23 | aten.t.default                                    |                 14 |          14 |
| 24 | aten.transpose.int                                |                 16 |          16 |
| 25 | aten.unsqueeze.default                            |                  1 |           0 |
| 26 | aten.view.default                                 |                 83 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Done     |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False  | Done     |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False   | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([128, 1])', 'torch.Size([128])'] | Unknown  |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([128, 1])', 'torch.Size([128])']   | Unknown  |
|  2 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([128, 1])', 'torch.Size([128])']   | Unknown  |
|  3 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([128, 1])', 'torch.Size([128])']   | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?         | Done     |
|  1 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     |
|  2 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                 | Done     |
|  3 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?         | Done     |
|  4 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?           | Done     |
|  6 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     |
|  7 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     |
|  8 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?           | Done     |
|  9 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.5                              | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Done     |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 128]> mat2 = ?   | Done     |
|  2 | Tensor<[160]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?  | Done     |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 160]> mat2 = ?  | Done     |
|  4 | Tensor<[160]> self = ?,<br>Tensor<[256, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?   | Done     |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Done     |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     |
|  7 | Tensor<[256]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     |
|  8 | Tensor<[32]> self = ?,<br>Tensor<[16384, 128]> mat1 = ?,<br>Tensor<[128, 32]> mat2 = ?   | Done     |
|  9 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?     | Done     |
| 10 | Tensor<[32]> self = ?,<br>Tensor<[256, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     |
| 11 | Tensor<[640]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 640]> mat2 = ?  | Done     |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[256, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?       | Done     |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[4096, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 128,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ? | Done     |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?  | Done     |
|  2 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?  | Done     |
|  3 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?   | Done     |
|  4 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?  | Done     |
|  5 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?   | Done     |
|  6 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?   | Done     |
|  7 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?    | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 256, 128, 128])', 'torch.Size([1, 256, 128, 128])', 'torch.Size([1, 256, 128, 128])', 'torch.Size([1, 256, 128, 128])'],<br>int<> dim = 1 | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[128]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Optional[number]<> min = 0.0                                | Done     |
|  1 | Tensor<[128]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 127 | Done     |
|  2 | Tensor<[128]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 15  | Done     |
|  3 | Tensor<[128]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 31  | Done     |
|  4 | Tensor<[128]> self = ?,<br>Optional[number]<> min = ?,<br>Optional[number]<> max = 63  | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                            | Done     |
|  1 | Tensor<[1, 1024, 160]> self = ?                                                                | Unknown  |
|  2 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  3 | Tensor<[1, 1024, 640]> self = ?                                                                | Done     |
|  4 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
|  5 | Tensor<[1, 16384, 128]> self = ?                                                               | Done     |
|  6 | Tensor<[1, 16384, 32]> self = ?                                                                | Unknown  |
|  7 | Tensor<[1, 2, 4096, 256]> self = ?                                                             | Done     |
|  8 | Tensor<[1, 256, 1024]> self = ?                                                                | Done     |
|  9 | Tensor<[1, 256, 128, 128]> self = ?                                                            | Done     |
| 10 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int]<> memory_format = torch.channels_last    | Done     |
| 11 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 12 | Tensor<[1, 256, 256]> self = ?                                                                 | Unknown  |
| 13 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
| 14 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
| 15 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 16 | Tensor<[1, 4096, 256]> self = ?                                                                | Done     |
| 17 | Tensor<[1, 4096, 64]> self = ?                                                                 | Unknown  |
| 18 | Tensor<[1, 5, 1024, 256]> self = ?                                                             | Done     |
| 19 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
| 20 | Tensor<[1, 8, 256, 256]> self = ?                                                              | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1024 | Unknown  |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 128   | Unknown  |
|  3 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  4 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  5 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 256     | Unknown  |
|  7 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [3, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
|  8 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [8, 8],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  9 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 10 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 11 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [4, 4],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 12 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 640     | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor<> other = 5.656854249492381 | Done     |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor<> other = 5.656854249492381  | Done     |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor<> other = 5.656854249492381  | Done     |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor<> other = 5.656854249492381   | Done     |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int]<> size = [1, 1, 16384, 256] | Unknown  |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int]<> size = [1, 1, 16384, 32]   | Unknown  |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int]<> size = [1, 1, 256, 32]       | Unknown  |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int]<> size = [1, 1, 32, 256]       | Unknown  |
|  4 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int]<> size = [1, 2, 256, 32]       | Unknown  |
|  5 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int]<> size = [1, 2, 32, 256]       | Unknown  |
|  6 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int]<> size = [1, 2, 4096, 256]   | Unknown  |
|  7 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int]<> size = [1, 2, 4096, 32]     | Unknown  |
|  8 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int]<> size = [1, 5, 1024, 256]   | Unknown  |
|  9 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int]<> size = [1, 5, 1024, 32]     | Unknown  |
| 10 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int]<> size = [1, 5, 256, 32]       | Unknown  |
| 11 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int]<> size = [1, 5, 32, 256]       | Unknown  |
| 12 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int]<> size = [1, 8, 256, 256]     | Unknown  |
| 13 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int]<> size = [1, 8, 256, 32]       | Unknown  |
| 14 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int]<> size = [1, 8, 32, 256]       | Unknown  |
### aten.gelu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1024, 640]> self = ?  | Done     |
|  1 | Tensor<[1, 16384, 128]> self = ? | Done     |
|  2 | Tensor<[1, 256, 1024]> self = ?  | Done     |
|  3 | Tensor<[1, 4096, 256]> self = ?  | Done     |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ? | Done     |
|  1 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?  | Done     |
|  2 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?  | Done     |
|  3 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?   | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?    | Done     |
|  2 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.125                  | Done     |
|  3 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.25                   | Done     |
|  4 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.5                    | Done     |
|  5 | Tensor<[128]> self = ?,<br>Tensor<> other = 1.0                    | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 160]> input = ?,<br>List[int]<> normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 16384, 32]> input = ?,<br>List[int]<> normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float<> eps = 1e-05    | Done     |
|  2 | Tensor<[1, 256, 160]> input = ?,<br>List[int]<> normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float<> eps = 1e-05  | Done     |
|  3 | Tensor<[1, 256, 256]> input = ?,<br>List[int]<> normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float<> eps = 1e-05  | Done     |
|  4 | Tensor<[1, 256, 32]> input = ?,<br>List[int]<> normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float<> eps = 1e-05      | Done     |
|  5 | Tensor<[1, 256, 64]> input = ?,<br>List[int]<> normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float<> eps = 1e-05      | Done     |
|  6 | Tensor<[1, 4096, 64]> input = ?,<br>List[int]<> normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float<> eps = 1e-05     | Done     |
### aten.permute.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 1024, 160]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
|  2 | Tensor<[1, 1024, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
|  3 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
|  4 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2] | Done     |
|  5 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
|  6 | Tensor<[1, 160, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]        | Done     |
|  7 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  8 | Tensor<[1, 16384, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]      | Done     |
|  9 | Tensor<[1, 16384, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
| 10 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
| 11 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 12 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 13 | Tensor<[1, 256, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]        | Done     |
| 14 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 15 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
| 16 | Tensor<[1, 32, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]         | Done     |
| 17 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]  | Done     |
| 18 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
| 19 | Tensor<[1, 4096, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Done     |
| 20 | Tensor<[1, 4096, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1]        | Done     |
| 21 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
| 22 | Tensor<[1, 64, 256]> self = ?,<br>List[int]<> dims = [0, 2, 1]         | Done     |
| 23 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int]<> dims = [0, 3, 1, 2]   | Done     |
| 24 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]   | Done     |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> self = ? | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[128, 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>number<> other = 1.0    | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     |
|  1 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.5          | Done     |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?       | Done     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1024, 256]> self = ? | Done     |
|  1 | Tensor<[128, 32]> self = ?   | Done     |
|  2 | Tensor<[160, 160]> self = ?  | Done     |
|  3 | Tensor<[160, 640]> self = ?  | Done     |
|  4 | Tensor<[256, 1024]> self = ? | Done     |
|  5 | Tensor<[256, 160]> self = ?  | Done     |
|  6 | Tensor<[256, 256]> self = ?  | Done     |
|  7 | Tensor<[256, 32]> self = ?   | Done     |
|  8 | Tensor<[256, 64]> self = ?   | Done     |
|  9 | Tensor<[32, 128]> self = ?   | Done     |
| 10 | Tensor<[32, 32]> self = ?    | Done     |
| 11 | Tensor<[64, 256]> self = ?   | Done     |
| 12 | Tensor<[64, 64]> self = ?    | Done     |
| 13 | Tensor<[640, 160]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  1 | Tensor<[1, 1024, 256]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  2 | Tensor<[1, 1024, 640]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  3 | Tensor<[1, 128, 16384]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[1, 160, 1024]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  5 | Tensor<[1, 16384, 128]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  6 | Tensor<[1, 2, 256, 32]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  7 | Tensor<[1, 256, 1024]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  8 | Tensor<[1, 256, 256]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
|  9 | Tensor<[1, 256, 4096]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 10 | Tensor<[1, 32, 16384]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 11 | Tensor<[1, 4096, 256]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 12 | Tensor<[1, 5, 256, 32]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
| 13 | Tensor<[1, 64, 4096]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
| 14 | Tensor<[1, 640, 1024]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
| 15 | Tensor<[1, 8, 256, 32]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>int<> dim = 1 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int]<> size = [1, 16384, 256] | Unknown  |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int]<> size = [1, 16384, 32]   | Unknown  |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int]<> size = [1, 256, 32]       | Unknown  |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int]<> size = [1, 32, 256]       | Unknown  |
|  4 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int]<> size = [1, 1024, 256]   | Unknown  |
|  5 | Tensor<[1, 1024, 160]> self = ?,<br>List[int]<> size = [1, 1024, 5, 32]    | Unknown  |
|  6 | Tensor<[1, 1024, 160]> self = ?,<br>List[int]<> size = [1, 32, 32, -1]     | Unknown  |
|  7 | Tensor<[1, 1024, 160]> self = ?,<br>List[int]<> size = [1024, 160]         | Unknown  |
|  8 | Tensor<[1, 1024, 256]> self = ?,<br>List[int]<> size = [1, 1024, 16, 16]   | Unknown  |
|  9 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int]<> size = [1, 1024, 160]    | Unknown  |
| 10 | Tensor<[1, 1024, 640]> self = ?,<br>List[int]<> size = [1024, 640]         | Unknown  |
| 11 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int]<> size = [1, 128, 16384] | Unknown  |
| 12 | Tensor<[1, 128, 16384]> self = ?,<br>List[int]<> size = [1, 128, 128, 128] | Unknown  |
| 13 | Tensor<[1, 160, 1024]> self = ?,<br>List[int]<> size = [1, 160, 32, 32]    | Unknown  |
| 14 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int]<> size = [1, 160, 256]     | Unknown  |
| 15 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int]<> size = [1, 160, 1024]    | Unknown  |
| 16 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int]<> size = [1, 16384, 32]   | Unknown  |
| 17 | Tensor<[1, 16384, 128]> self = ?,<br>List[int]<> size = [16384, 128]       | Unknown  |
| 18 | Tensor<[1, 16384, 256]> self = ?,<br>List[int]<> size = [1, 1, 16384, 256] | Unknown  |
| 19 | Tensor<[1, 16384, 32]> self = ?,<br>List[int]<> size = [1, 1, 16384, 32]   | Unknown  |
| 20 | Tensor<[1, 16384, 32]> self = ?,<br>List[int]<> size = [1, 128, 128, -1]   | Unknown  |
| 21 | Tensor<[1, 16384, 32]> self = ?,<br>List[int]<> size = [1, 16384, 1, 32]   | Unknown  |
| 22 | Tensor<[1, 16384, 32]> self = ?,<br>List[int]<> size = [16384, 32]         | Unknown  |
| 23 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int]<> size = [2, 256, 32]       | Unknown  |
| 24 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int]<> size = [2, 32, 256]       | Unknown  |
| 25 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int]<> size = [2, 4096, 256]   | Unknown  |
| 26 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int]<> size = [2, 4096, 32]     | Unknown  |
| 27 | Tensor<[1, 256, 1024]> self = ?,<br>List[int]<> size = [1, 256, 32, 32]    | Unknown  |
| 28 | Tensor<[1, 256, 1024]> self = ?,<br>List[int]<> size = [256, 1024]         | Unknown  |
| 29 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int]<> size = [1, 256, 256]     | Unknown  |
| 30 | Tensor<[1, 256, 160]> self = ?,<br>List[int]<> size = [1, 256, 5, 32]      | Unknown  |
| 31 | Tensor<[1, 256, 160]> self = ?,<br>List[int]<> size = [256, 160]           | Unknown  |
| 32 | Tensor<[1, 256, 16384]> self = ?,<br>List[int]<> size = [1, 256, 128, 128] | Unknown  |
| 33 | Tensor<[1, 256, 256]> self = ?,<br>List[int]<> size = [1, 16, 16, -1]      | Unknown  |
| 34 | Tensor<[1, 256, 256]> self = ?,<br>List[int]<> size = [1, 256, 16, 16]     | Unknown  |
| 35 | Tensor<[1, 256, 256]> self = ?,<br>List[int]<> size = [1, 256, 8, 32]      | Unknown  |
| 36 | Tensor<[1, 256, 256]> self = ?,<br>List[int]<> size = [256, 256]           | Unknown  |
| 37 | Tensor<[1, 256, 32]> self = ?,<br>List[int]<> size = [1, 256, 1, 32]       | Unknown  |
| 38 | Tensor<[1, 256, 32]> self = ?,<br>List[int]<> size = [256, 32]             | Unknown  |
| 39 | Tensor<[1, 256, 4096]> self = ?,<br>List[int]<> size = [1, 256, 64, 64]    | Unknown  |
| 40 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int]<> size = [1, 256, 4096]    | Unknown  |
| 41 | Tensor<[1, 256, 64]> self = ?,<br>List[int]<> size = [1, 256, 2, 32]       | Unknown  |
| 42 | Tensor<[1, 256, 64]> self = ?,<br>List[int]<> size = [256, 64]             | Unknown  |
| 43 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int]<> size = [1, 256, 256]      | Unknown  |
| 44 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int]<> size = [1, 32, 16384]   | Unknown  |
| 45 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int]<> size = [1, 32, 256]       | Unknown  |
| 46 | Tensor<[1, 32, 16384]> self = ?,<br>List[int]<> size = [1, 32, 128, 128]   | Unknown  |
| 47 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int]<> size = [1, 4096, 64]     | Unknown  |
| 48 | Tensor<[1, 4096, 256]> self = ?,<br>List[int]<> size = [4096, 256]         | Unknown  |
| 49 | Tensor<[1, 4096, 64]> self = ?,<br>List[int]<> size = [1, 4096, 2, 32]     | Unknown  |
| 50 | Tensor<[1, 4096, 64]> self = ?,<br>List[int]<> size = [1, 64, 64, -1]      | Unknown  |
| 51 | Tensor<[1, 4096, 64]> self = ?,<br>List[int]<> size = [4096, 64]           | Unknown  |
| 52 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int]<> size = [5, 1024, 256]   | Unknown  |
| 53 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int]<> size = [5, 1024, 32]     | Unknown  |
| 54 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int]<> size = [5, 256, 32]       | Unknown  |
| 55 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int]<> size = [5, 32, 256]       | Unknown  |
| 56 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int]<> size = [1, 64, 256]       | Unknown  |
| 57 | Tensor<[1, 64, 4096]> self = ?,<br>List[int]<> size = [1, 64, 64, 64]      | Unknown  |
| 58 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int]<> size = [1, 64, 4096]      | Unknown  |
| 59 | Tensor<[1, 640, 1024]> self = ?,<br>List[int]<> size = [1, 640, 32, 32]    | Unknown  |
| 60 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int]<> size = [1, 640, 1024]    | Unknown  |
| 61 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int]<> size = [8, 256, 256]     | Unknown  |
| 62 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int]<> size = [8, 256, 32]       | Unknown  |
| 63 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int]<> size = [8, 32, 256]       | Unknown  |
| 64 | Tensor<[1024, 160]> self = ?,<br>List[int]<> size = [1, 1024, 160]         | Unknown  |
| 65 | Tensor<[1024, 256]> self = ?,<br>List[int]<> size = [1, 1024, 256]         | Unknown  |
| 66 | Tensor<[1024, 640]> self = ?,<br>List[int]<> size = [1, 1024, 640]         | Unknown  |
| 67 | Tensor<[16384, 128]> self = ?,<br>List[int]<> size = [1, 16384, 128]       | Unknown  |
| 68 | Tensor<[16384, 256]> self = ?,<br>List[int]<> size = [1, 16384, 256]       | Unknown  |
| 69 | Tensor<[16384, 32]> self = ?,<br>List[int]<> size = [1, 16384, 32]         | Unknown  |
| 70 | Tensor<[2, 4096, 256]> self = ?,<br>List[int]<> size = [1, 2, 4096, 256]   | Unknown  |
| 71 | Tensor<[2, 4096, 32]> self = ?,<br>List[int]<> size = [1, 2, 4096, 32]     | Unknown  |
| 72 | Tensor<[256, 1024]> self = ?,<br>List[int]<> size = [1, 256, 1024]         | Unknown  |
| 73 | Tensor<[256, 160]> self = ?,<br>List[int]<> size = [1, 256, 160]           | Unknown  |
| 74 | Tensor<[256, 256]> self = ?,<br>List[int]<> size = [1, 256, 256]           | Unknown  |
| 75 | Tensor<[256, 32]> self = ?,<br>List[int]<> size = [1, 256, 32]             | Unknown  |
| 76 | Tensor<[256, 64]> self = ?,<br>List[int]<> size = [1, 256, 64]             | Unknown  |
| 77 | Tensor<[4096, 256]> self = ?,<br>List[int]<> size = [1, 4096, 256]         | Unknown  |
| 78 | Tensor<[4096, 64]> self = ?,<br>List[int]<> size = [1, 4096, 64]           | Unknown  |
| 79 | Tensor<[5, 1024, 256]> self = ?,<br>List[int]<> size = [1, 5, 1024, 256]   | Unknown  |
| 80 | Tensor<[5, 1024, 32]> self = ?,<br>List[int]<> size = [1, 5, 1024, 32]     | Unknown  |
| 81 | Tensor<[8, 256, 256]> self = ?,<br>List[int]<> size = [1, 8, 256, 256]     | Unknown  |
| 82 | Tensor<[8, 256, 32]> self = ?,<br>List[int]<> size = [1, 8, 256, 32]       | Unknown  |

