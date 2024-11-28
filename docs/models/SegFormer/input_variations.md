# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax.default                             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten._to_copy.default                             |                  6 |           5 |         0 |          0 | 🚧          |    0.83 |
|  3 | aten._unsafe_index.Tensor                         |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.add.Tensor                                   |                 10 |          10 |         0 |          0 | ✅          |    1    |
|  5 | aten.addmm.default                                |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  6 | aten.arange.default                               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.bmm.default                                  |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  8 | aten.cat.default                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.ceil.default                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.clamp.default                                |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.clone.default                                |                 21 |          21 |         0 |          0 | ✅          |    1    |
| 12 | aten.convolution.default                          |                 13 |          11 |         0 |          0 | 🚧          |    0.85 |
| 13 | aten.div.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 14 | aten.expand.default                               |                 15 |           0 |        15 |          0 | ✅          |    1    |
| 15 | aten.gelu.default                                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 16 | aten.mm.default                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 17 | aten.mul.Tensor                                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 18 | aten.native_layer_norm.default                    |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 19 | aten.permute.default                              |                 25 |          25 |         0 |          0 | ✅          |    1    |
| 20 | aten.relu.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 21 | aten.rsub.Scalar                                  |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.sub.Tensor                                   |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 23 | aten.t.default                                    |                 14 |          14 |         0 |          0 | ✅          |    1    |
| 24 | aten.transpose.int                                |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 25 | aten.unsqueeze.default                            |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 26 | aten.view.default                                 |                 83 |          83 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | True  |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   | True  |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   | True  |
|  2 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | True  |
|  3 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | True  |
|  4 | Tensor<[1, 256, 64, 64]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | True  |
|  5 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Fallback   | True  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]   | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?         | Done     | Done       | True  |
|  1 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | True  |
|  2 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                 | Done     | Done       | True  |
|  3 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?         | Done     | Done       | True  |
|  4 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     | Done       | True  |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?           | Done     | Done       | True  |
|  6 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | True  |
|  7 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | True  |
|  8 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?           | Done     | Done       | True  |
|  9 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 128]> mat2 = ?   | Done     | Done       | True  |
|  2 | Tensor<[160]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?  | Done     | Done       | True  |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 160]> mat2 = ?  | Done     | Done       | True  |
|  4 | Tensor<[160]> self = ?,<br>Tensor<[256, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?   | Done     | Done       | True  |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Done     | Done       | True  |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | Done       | True  |
|  7 | Tensor<[256]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     | Done       | True  |
|  8 | Tensor<[32]> self = ?,<br>Tensor<[16384, 128]> mat1 = ?,<br>Tensor<[128, 32]> mat2 = ?   | Done     | Done       | True  |
|  9 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?     | Done     | Done       | True  |
| 10 | Tensor<[32]> self = ?,<br>Tensor<[256, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     | Done       | True  |
| 11 | Tensor<[640]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 640]> mat2 = ?  | Done     | Done       | True  |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[256, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?       | Done     | Done       | True  |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[4096, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | Done       | True  |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | Done       | True  |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 128,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?  | Done     | Done       | True  |
|  2 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?  | Done     | Done       | True  |
|  3 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?  | Done     | Done       | True  |
|  5 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?   | Done     | Done       | True  |
|  6 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?   | Done     | Done       | True  |
|  7 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?    | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 256, 128, 128]>, <[1, 256, 128, 128]>, <[1, 256, 128, 128]>, <[1, 256, 128, 128]>],<br>int dim = 1 | Done     | Done       | True  |
### aten.ceil.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[128]> self = ?  | None     | Fallback   | True  |
### aten.clamp.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[128]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
|  1 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 127 | None     | Fallback   | True  |
|  2 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 15  | None     | Fallback   | True  |
|  3 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 31  | None     | Fallback   | True  |
|  4 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 63  | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                          | Done     | Done       | True  |
|  1 | Tensor<[1, 1024, 160]> self = ?                                                              | Done     | Done       | True  |
|  2 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
|  3 | Tensor<[1, 1024, 640]> self = ?                                                              | Done     | Done       | True  |
|  4 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
|  5 | Tensor<[1, 16384, 128]> self = ?                                                             | Done     | Done       | True  |
|  6 | Tensor<[1, 16384, 32]> self = ?                                                              | Done     | Done       | True  |
|  7 | Tensor<[1, 2, 4096, 256]> self = ?                                                           | Done     | Done       | True  |
|  8 | Tensor<[1, 256, 1024]> self = ?                                                              | Done     | Done       | True  |
|  9 | Tensor<[1, 256, 128, 128]> self = ?                                                          | Done     | Done       | True  |
| 10 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last    | Done     | Done       | True  |
| 11 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 12 | Tensor<[1, 256, 256]> self = ?                                                               | Done     | Done       | True  |
| 13 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 14 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
| 15 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 16 | Tensor<[1, 4096, 256]> self = ?                                                              | Done     | Done       | True  |
| 17 | Tensor<[1, 4096, 64]> self = ?                                                               | Done     | Done       | True  |
| 18 | Tensor<[1, 5, 1024, 256]> self = ?                                                           | Done     | Done       | True  |
| 19 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 20 | Tensor<[1, 8, 256, 256]> self = ?                                                            | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Fallback   | True  |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Done     | Done       | True  |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Done     | Done       | True  |
|  3 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  4 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  5 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | Done     | Done       | True  |
|  7 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Fallback   | True  |
|  8 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  9 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 10 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 11 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 12 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | True  |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]       | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]       | Removed  | Fallback   | True  |
|  4 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]       | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]       | Removed  | Fallback   | True  |
|  6 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Removed  | Fallback   | True  |
|  7 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Removed  | Fallback   | True  |
|  8 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Removed  | Fallback   | True  |
|  9 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Removed  | Fallback   | True  |
| 10 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]       | Removed  | Fallback   | True  |
| 11 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]       | Removed  | Fallback   | True  |
| 12 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Removed  | Fallback   | True  |
| 13 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Removed  | Fallback   | True  |
| 14 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]       | Removed  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 640]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 16384, 128]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 256, 1024]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 4096, 256]> self = ?  | Done     | Done       | True  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?  | Done     | Done       | True  |
|  2 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?  | Done     | Done       | True  |
|  3 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?   | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?    | Done     | Done       | True  |
|  2 | Tensor<[128]> self = ?,<br>Tensor other = 0.125                    | Done     | Done       | True  |
|  3 | Tensor<[128]> self = ?,<br>Tensor other = 0.25                     | Done     | Done       | True  |
|  4 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                      | Done     | Done       | True  |
|  5 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                      | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  1 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | N/A   |
|  2 | Tensor<[1, 256, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
|  3 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
|  4 | Tensor<[1, 256, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | N/A   |
|  5 | Tensor<[1, 256, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | N/A   |
|  6 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  1 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       | True  |
|  2 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       | True  |
|  3 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
|  4 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Done       | True  |
|  5 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       | True  |
|  6 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       | True  |
|  7 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  8 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | Done       | True  |
|  9 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       | True  |
| 10 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
| 11 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
| 12 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
| 13 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Unknown    | N/A   |
| 14 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
| 15 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
| 16 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       | True  |
| 17 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       | True  |
| 18 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
| 19 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       | True  |
| 20 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       | True  |
| 21 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
| 22 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       | True  |
| 23 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]   | Done     | Done       | True  |
| 24 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   | PCC   |
|---:|:------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 256, 128, 128]> self = ? | Done     | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[128, 1]> self = ?,<br>number other = 1.0 | None     | Fallback   | True  |
|  1 | Tensor<[128]> self = ?,<br>number other = 1.0    | None     | Fallback   | True  |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[128]> self = ?,<br>Tensor other = 0.5            | Done     | Done       | True  |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?       | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024, 256]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[128, 32]> self = ?   | Done     | Done       | True  |
|  2 | Tensor<[160, 160]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[160, 640]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[256, 1024]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[256, 160]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[256, 256]> self = ?  | Done     | Done       | True  |
|  7 | Tensor<[256, 32]> self = ?   | Done     | Done       | True  |
|  8 | Tensor<[256, 64]> self = ?   | Done     | Done       | True  |
|  9 | Tensor<[32, 128]> self = ?   | Done     | Done       | True  |
| 10 | Tensor<[32, 32]> self = ?    | Done     | Done       | True  |
| 11 | Tensor<[64, 256]> self = ?   | Done     | Done       | True  |
| 12 | Tensor<[64, 64]> self = ?    | Done     | Done       | True  |
| 13 | Tensor<[640, 160]> self = ?  | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  1 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  2 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  3 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  4 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  5 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  6 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  7 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  8 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
|  9 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 10 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 11 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 12 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
| 13 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
| 14 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 15 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[128]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256] | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       | True  |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]       | Done     | Done       | True  |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | Done       | True  |
|  4 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]   | Done     | Done       | True  |
|  5 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]    | Done     | Done       | True  |
|  6 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]     | Done     | Done       | True  |
|  7 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]         | Done     | Done       | True  |
|  8 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]   | Done     | Done       | True  |
|  9 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]    | Done     | Done       | True  |
| 10 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]         | Done     | Done       | True  |
| 11 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384] | Done     | Done       | True  |
| 12 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128] | Done     | Done       | True  |
| 13 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]    | Done     | Done       | True  |
| 14 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]     | Done     | Done       | True  |
| 15 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]    | Done     | Done       | True  |
| 16 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | Done       | True  |
| 17 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]       | Done     | Done       | True  |
| 18 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Done     | Done       | True  |
| 19 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Done     | Done       | True  |
| 20 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]   | Done     | Done       | True  |
| 21 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]   | Done     | Done       | True  |
| 22 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]         | Done     | Done       | True  |
| 23 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]       | Done     | Done       | True  |
| 24 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]       | Done     | Done       | True  |
| 25 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]   | Done     | Done       | True  |
| 26 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]     | Done     | Done       | True  |
| 27 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]    | Done     | Done       | True  |
| 28 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]         | Done     | Done       | True  |
| 29 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]     | Done     | Done       | True  |
| 30 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]      | Done     | Done       | True  |
| 31 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]           | Done     | Done       | True  |
| 32 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128] | Done     | Done       | True  |
| 33 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]      | Done     | Done       | True  |
| 34 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]     | Done     | Done       | True  |
| 35 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]      | Done     | Done       | True  |
| 36 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]           | Done     | Done       | True  |
| 37 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]       | Done     | Done       | True  |
| 38 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]             | Done     | Done       | True  |
| 39 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]    | Done     | Done       | True  |
| 40 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]    | Done     | Done       | True  |
| 41 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]       | Done     | Done       | True  |
| 42 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]             | Done     | Done       | True  |
| 43 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]      | Done     | Done       | True  |
| 44 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]   | Done     | Done       | True  |
| 45 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | Done       | True  |
| 46 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]   | Done     | Done       | True  |
| 47 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]     | Done     | Done       | True  |
| 48 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]         | Done     | Done       | True  |
| 49 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]     | Done     | Done       | True  |
| 50 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]      | Done     | Done       | True  |
| 51 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]           | Done     | Done       | True  |
| 52 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]   | Done     | Done       | True  |
| 53 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]     | Done     | Done       | True  |
| 54 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]       | Done     | Done       | True  |
| 55 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]       | Done     | Done       | True  |
| 56 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]       | Done     | Done       | True  |
| 57 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]      | Done     | Done       | True  |
| 58 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]      | Done     | Done       | True  |
| 59 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]    | Done     | Done       | True  |
| 60 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]    | Done     | Done       | True  |
| 61 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]     | Done     | Done       | True  |
| 62 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]       | Done     | Done       | True  |
| 63 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]       | Done     | Done       | True  |
| 64 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]         | Done     | Done       | True  |
| 65 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]         | Done     | Done       | True  |
| 66 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]         | Done     | Done       | True  |
| 67 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]       | Done     | Done       | True  |
| 68 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | Done       | True  |
| 69 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | True  |
| 70 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Done     | Done       | True  |
| 71 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Done     | Done       | True  |
| 72 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]         | Done     | Done       | True  |
| 73 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]           | Done     | Done       | True  |
| 74 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Done       | True  |
| 75 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | True  |
| 76 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]             | Done     | Done       | True  |
| 77 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]         | Done     | Done       | True  |
| 78 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | Done       | True  |
| 79 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Done     | Done       | True  |
| 80 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Done     | Done       | True  |
| 81 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Done     | Done       | True  |
| 82 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Done     | Done       | True  |

