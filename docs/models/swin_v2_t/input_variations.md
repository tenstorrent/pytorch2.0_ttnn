# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._softmax.default           |                  4 |           4 |         0 |          0 | ✅          |               1    |
|  1 | aten._unsafe_view.default       |                 19 |           0 |         0 |          0 | ✘           |               0    |
|  2 | aten.add.Tensor                 |                 11 |          11 |         0 |          0 | ✅          |               1    |
|  3 | aten.addmm.default              |                 18 |          18 |         0 |          0 | ✅          |               1    |
|  4 | aten.as_strided.default         |                  1 |           0 |         0 |          0 | ✘           |               0    |
|  5 | aten.bmm.default                |                  8 |           8 |         0 |          0 | ✅          |               1    |
|  6 | aten.cat.default                |                  3 |           0 |         0 |          0 | ✘           |               0    |
|  7 | aten.clamp.default              |                  4 |           4 |         0 |          0 | ✅          |               1    |
|  8 | aten.clamp_min.default          |                  4 |           0 |         0 |          0 | ✘           |               0    |
|  9 | aten.clone.default              |                 38 |          38 |         0 |          0 | ✅          |               1    |
| 10 | aten.constant_pad_nd.default    |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 11 | aten.convolution.default        |                  1 |           0 |         0 |          0 | ✘           |               0    |
| 12 | aten.div.Tensor                 |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 13 | aten.eq.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |               1    |
| 14 | aten.exp.default                |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 15 | aten.expand.default             |                 16 |           0 |         0 |          0 | ✘           |               0    |
| 16 | aten.gelu.default               |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 17 | aten.index.Tensor               |                  4 |           0 |         0 |          0 | ✘           |               0    |
| 18 | aten.linalg_vector_norm.default |                  4 |           0 |         0 |          0 | ✘           |               0    |
| 19 | aten.masked_fill.Scalar         |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 20 | aten.mean.dim                   |                  1 |           1 |         0 |          0 | ✅          |               1    |
| 21 | aten.mm.default                 |                  7 |           7 |         0 |          0 | ✅          |               1    |
| 22 | aten.mul.Tensor                 |                  8 |           8 |         0 |          0 | ✅          |               1    |
| 23 | aten.native_layer_norm.default  |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 24 | aten.ne.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |               1    |
| 25 | aten.new_zeros.default          |                  3 |           0 |         0 |          0 | ✘           |               0    |
| 26 | aten.permute.default            |                 20 |          20 |         0 |          0 | ✅          |               1    |
| 27 | aten.relu.default               |                  1 |           1 |         0 |          0 | ✅          |               1    |
| 28 | aten.roll.default               |                  6 |           0 |         0 |          0 | ✘           |               0    |
| 29 | aten.select.int                 |                 12 |           0 |         0 |          0 | ✘           |               0    |
| 30 | aten.sigmoid.default            |                  4 |           4 |         0 |          0 | ✅          |               1    |
| 31 | aten.slice.Tensor               |                 23 |           0 |         0 |          0 | ✘           |               0    |
| 32 | aten.sub.Tensor                 |                  3 |           3 |         0 |          0 | ✅          |               1    |
| 33 | aten.t.default                  |                 25 |          25 |         0 |          0 | ✅          |               1    |
| 34 | aten.transpose.int              |                  8 |           8 |         0 |          0 | ✅          |               1    |
| 35 | aten.unsqueeze.default          |                 16 |          13 |         0 |          0 | 🚧          |               0.81 |
| 36 | aten.view.default               |                 84 |           8 |         0 |         76 | 🚧          |               0.1  |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
|  1 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
|  2 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
|  3 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] size = [4, 64, 384]     | None     |
|  1 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384] | None     |
|  2 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] size = [16, 64, 192]    | None     |
|  3 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192] | None     |
|  4 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int] size = [1, 64, 768]          | None     |
|  5 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]   | None     |
|  6 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [64, 64, 96]      | None     |
|  7 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [96, 32, 64]          | None     |
|  8 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [96, 64, 32]          | None     |
|  9 | Tensor<[16, 64, 6, 32]> self = ?,<br>List[int] size = [16, 64, 192]         | None     |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                  | None     |
| 11 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [48, 32, 64]          | None     |
| 12 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [48, 64, 32]          | None     |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                 | None     |
| 14 | Tensor<[4, 64, 12, 32]> self = ?,<br>List[int] size = [4, 64, 384]          | None     |
| 15 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [192, 32, 64]         | None     |
| 16 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [192, 64, 32]         | None     |
| 17 | Tensor<[64, 64, 3, 32]> self = ?,<br>List[int] size = [64, 64, 96]          | None     |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                 | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?     | Done     |
|  1 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | Done     |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?       | Done     |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?     | Done     |
|  4 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | Done     |
|  5 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | Done     |
|  6 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?       | Done     |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?         | Done     |
|  8 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?        | Done     |
|  9 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?       | Done     |
| 10 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?        | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     |
|  1 | Tensor<[1152]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1152]> mat2 = ? | Done     |
|  2 | Tensor<[1536]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1536]> mat2 = ? | Done     |
|  3 | Tensor<[192]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?  | Done     |
|  4 | Tensor<[192]> self = ?,<br>Tensor<[1024, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ?  | Done     |
|  5 | Tensor<[2304]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?  | Done     |
|  6 | Tensor<[288]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?    | Done     |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     |
|  8 | Tensor<[384]> self = ?,<br>Tensor<[256, 1536]> mat1 = ?,<br>Tensor<[1536, 384]> mat2 = ? | Done     |
|  9 | Tensor<[384]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 384]> mat2 = ?   | Done     |
| 10 | Tensor<[384]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 384]> mat2 = ?    | Done     |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?       | Done     |
| 12 | Tensor<[576]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 576]> mat2 = ?  | Done     |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ?  | Done     |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[64, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Done     |
| 15 | Tensor<[768]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     |
| 16 | Tensor<[96]> self = ?,<br>Tensor<[4096, 384]> mat1 = ?,<br>Tensor<[384, 96]> mat2 = ?    | Done     |
| 17 | Tensor<[96]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 96]> mat2 = ?      | Done     |
### aten.as_strided.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768] | None     |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ? | Done     |
|  1 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ? | Done     |
|  2 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?   | Done     |
|  3 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?   | Done     |
|  4 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?   | Done     |
|  5 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?   | Done     |
|  6 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?   | Done     |
|  7 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [<[1, 16, 16, 192]>, <[1, 16, 16, 192]>, <[1, 16, 16, 192]>, <[1, 16, 16, 192]>],<br>int dim = -1 | None     |
|  1 | List[Tensor] tensors = [<[1, 32, 32, 96]>, <[1, 32, 32, 96]>, <[1, 32, 32, 96]>, <[1, 32, 32, 96]>],<br>int dim = -1     | None     |
|  2 | List[Tensor] tensors = [<[1, 8, 8, 384]>, <[1, 8, 8, 384]>, <[1, 8, 8, 384]>, <[1, 8, 8, 384]>],<br>int dim = -1         | None     |
### aten.clamp.default
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | Done     |
|  1 | Tensor<[24, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | Done     |
|  2 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | Done     |
|  3 | Tensor<[6, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | Done     |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 1]> self = ?,<br>number min = 1e-12 | None     |
|  1 | Tensor<[16, 6, 64, 1]> self = ?,<br>number min = 1e-12 | None     |
|  2 | Tensor<[4, 12, 64, 1]> self = ?,<br>number min = 1e-12 | None     |
|  3 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | None     |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 1536]> self = ?                                                              | Done     |
|  1 | Tensor<[1, 16, 16, 384]> self = ?                                                               | Done     |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 24, 64, 64]> self = ?                                                                | Done     |
|  5 | Tensor<[1, 32, 32, 192]> self = ?                                                               | Done     |
|  6 | Tensor<[1, 32, 32, 768]> self = ?                                                               | Done     |
|  7 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  8 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  9 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 10 | Tensor<[1, 64, 64, 384]> self = ?                                                               | Done     |
| 11 | Tensor<[1, 64, 64, 96]> self = ?                                                                | Done     |
| 12 | Tensor<[1, 64, 768]> self = ?                                                                   | Done     |
| 13 | Tensor<[1, 8, 8, 3072]> self = ?                                                                | Done     |
| 14 | Tensor<[1, 8, 8, 768]> self = ?                                                                 | Done     |
| 15 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     |
| 16 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 17 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 18 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 19 | Tensor<[16, 6, 64, 64]> self = ?                                                                | Done     |
| 20 | Tensor<[16, 64, 192]> self = ?                                                                  | Done     |
| 21 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 23 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 24 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     |
| 25 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 26 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 27 | Tensor<[4, 12, 64, 64]> self = ?                                                                | Done     |
| 28 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 29 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 30 | Tensor<[4, 64, 384]> self = ?                                                                   | Done     |
| 31 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     |
| 32 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 33 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 34 | Tensor<[64, 3, 64, 64]> self = ?                                                                | Done     |
| 35 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 36 | Tensor<[64, 64, 96]> self = ?                                                                   | Done     |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     |
|  1 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     |
|  2 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     |
|  3 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ? | Done     |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ? | Done     |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ? | Done     |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ? | Done     |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     |
### aten.exp.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     |
|  1 | Tensor<[24, 1, 1]> self = ? | Done     |
|  2 | Tensor<[3, 1, 1]> self = ?  | Done     |
|  3 | Tensor<[6, 1, 1]> self = ?  | Done     |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64] | Unknown  |
|  1 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]  | None     |
|  2 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32] | Unknown  |
|  3 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64] | Unknown  |
|  4 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64] | Unknown  |
|  5 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]  | None     |
|  6 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32] | Unknown  |
|  7 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64] | Unknown  |
|  8 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64] | Unknown  |
|  9 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]  | None     |
| 10 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32] | Unknown  |
| 11 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64] | Unknown  |
| 12 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64] | Unknown  |
| 13 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]  | None     |
| 14 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32] | Unknown  |
| 15 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 1536]> self = ? | Done     |
|  1 | Tensor<[1, 32, 32, 768]> self = ?  | Done     |
|  2 | Tensor<[1, 64, 64, 384]> self = ?  | Done     |
|  3 | Tensor<[1, 8, 8, 3072]> self = ?   | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | None     |
|  1 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | None     |
|  2 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | None     |
|  3 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | None     |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = -100.0 | None     |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0    | None     |
|  2 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = -100.0   | None     |
|  3 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = 0.0      | None     |
|  4 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0 | None     |
|  5 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = 0.0    | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ? | Done     |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?   | Done     |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?   | Done     |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?    | Done     |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?    | Done     |
|  5 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?  | Done     |
|  6 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16            | Done     |
|  1 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16            | Done     |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ? | Done     |
|  3 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16             | Done     |
|  4 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16             | Done     |
|  5 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?  | Done     |
|  6 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ? | Done     |
|  7 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?  | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05 | Done     |
|  1 | Tensor<[1, 32, 32, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05 | Done     |
|  2 | Tensor<[1, 64, 64, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05     | Done     |
|  3 | Tensor<[1, 8, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05   | Done     |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | None     |
|  1 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | None     |
|  2 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False  | None     |
### aten.permute.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     |
|  4 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     |
|  5 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     |
|  6 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     |
|  8 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | Done     |
|  9 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     |
| 10 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     |
| 12 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     |
| 14 | Tensor<[64, 64, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     |
| 15 | Tensor<[64, 64, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     |
| 16 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     |
| 17 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     |
| 18 | Tensor<[64, 64, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     |
### aten.relu.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Done     |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     |
|  2 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     |
|  4 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2]  | None     |
|  5 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]    | None     |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     |
|  1 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     |
|  2 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     |
|  3 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     |
|  4 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     |
|  5 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     |
|  6 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     |
|  7 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     |
|  8 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     |
|  9 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     |
| 10 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     |
| 11 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 64]> self = ? | Done     |
|  1 | Tensor<[1, 24, 64, 64]> self = ? | Done     |
|  2 | Tensor<[1, 3, 64, 64]> self = ?  | Done     |
|  3 | Tensor<[1, 6, 64, 64]> self = ?  | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  |
|  2 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     |
|  3 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     |
|  4 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  |
|  5 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     |
|  6 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     |
|  7 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  |
|  8 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     |
|  9 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     |
| 10 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  |
| 11 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  |
| 12 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     |
| 13 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     |
| 14 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  |
| 15 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     |
| 16 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     |
| 17 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  |
| 18 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     |
| 19 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     |
| 20 | Tensor<[1, 8, 8, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  |
| 21 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  |
| 22 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | Done     |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | Done     |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Done     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1000, 768]> self = ? | Done     |
|  1 | Tensor<[1152, 384]> self = ? | Done     |
|  2 | Tensor<[12, 512]> self = ?   | Done     |
|  3 | Tensor<[1536, 384]> self = ? | Done     |
|  4 | Tensor<[192, 192]> self = ?  | Done     |
|  5 | Tensor<[192, 384]> self = ?  | Done     |
|  6 | Tensor<[192, 768]> self = ?  | Done     |
|  7 | Tensor<[2304, 768]> self = ? | Done     |
|  8 | Tensor<[24, 512]> self = ?   | Done     |
|  9 | Tensor<[288, 96]> self = ?   | Done     |
| 10 | Tensor<[3, 512]> self = ?    | Done     |
| 11 | Tensor<[3072, 768]> self = ? | Done     |
| 12 | Tensor<[384, 1536]> self = ? | Done     |
| 13 | Tensor<[384, 384]> self = ?  | Done     |
| 14 | Tensor<[384, 768]> self = ?  | Done     |
| 15 | Tensor<[384, 96]> self = ?   | Done     |
| 16 | Tensor<[512, 2]> self = ?    | Done     |
| 17 | Tensor<[576, 192]> self = ?  | Done     |
| 18 | Tensor<[6, 512]> self = ?    | Done     |
| 19 | Tensor<[768, 1536]> self = ? | Done     |
| 20 | Tensor<[768, 192]> self = ?  | Done     |
| 21 | Tensor<[768, 3072]> self = ? | Done     |
| 22 | Tensor<[768, 768]> self = ?  | Done     |
| 23 | Tensor<[96, 384]> self = ?   | Done     |
| 24 | Tensor<[96, 96]> self = ?    | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     |
|  1 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     |
|  2 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     |
|  3 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     |
|  4 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     |
|  5 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     |
|  6 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     |
|  7 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[12, 64, 64]> self = ?,<br>int dim = 0    | Done     |
|  1 | Tensor<[16, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 1    | Done     |
|  3 | Tensor<[16, 64]> self = ?,<br>int dim = 1        | Done     |
|  4 | Tensor<[16, 64]> self = ?,<br>int dim = 2        | None     |
|  5 | Tensor<[24, 64, 64]> self = ?,<br>int dim = 0    | Done     |
|  6 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0     | Done     |
|  7 | Tensor<[4, 1, 64, 64]> self = ?,<br>int dim = 0  | Done     |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 1     | Done     |
|  9 | Tensor<[4, 64]> self = ?,<br>int dim = 1         | Done     |
| 10 | Tensor<[4, 64]> self = ?,<br>int dim = 2         | None     |
| 11 | Tensor<[6, 64, 64]> self = ?,<br>int dim = 0     | Done     |
| 12 | Tensor<[64, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     |
| 13 | Tensor<[64, 64, 64]> self = ?,<br>int dim = 1    | Done     |
| 14 | Tensor<[64, 64]> self = ?,<br>int dim = 1        | Done     |
| 15 | Tensor<[64, 64]> self = ?,<br>int dim = 2        | None     |
### aten.view.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]     | Fallback |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]   | Fallback |
|  2 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]              | Fallback |
|  3 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]              | Fallback |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]               | Fallback |
|  5 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                | Fallback |
|  6 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]           | Fallback |
|  7 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                | Fallback |
|  8 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]         | Fallback |
|  9 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384] | Fallback |
| 10 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [256, 384]           | Fallback |
| 11 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]           | Fallback |
| 12 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]    | Fallback |
| 13 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]          | Done     |
| 14 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]          | Done     |
| 15 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]          | Done     |
| 16 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192] | Fallback |
| 17 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1024, 192]          | Fallback |
| 18 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]          | Fallback |
| 19 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]          | Fallback |
| 20 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]   | Fallback |
| 21 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]      | Fallback |
| 22 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]    | Fallback |
| 23 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]          | Fallback |
| 24 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]   | Fallback |
| 25 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]            | Fallback |
| 26 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 768]     | Fallback |
| 27 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                | Done     |
| 28 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]               | Fallback |
| 29 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]            | Fallback |
| 30 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]            | Fallback |
| 31 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]   | Fallback |
| 32 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [64, 768]              | Fallback |
| 33 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]          | Fallback |
| 34 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [16, 64, 192]             | Fallback |
| 35 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]             | Fallback |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]          | Fallback |
| 37 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                 | Fallback |
| 38 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64, 64]    | Fallback |
| 39 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]          | Fallback |
| 40 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 192]    | Fallback |
| 41 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]             | Fallback |
| 42 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]      | Fallback |
| 43 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]         | Fallback |
| 44 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]         | Fallback |
| 45 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]             | Fallback |
| 46 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]             | Fallback |
| 47 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]               | Fallback |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]           | Fallback |
| 49 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]               | Fallback |
| 50 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]          | Done     |
| 51 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]          | Done     |
| 52 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]             | Fallback |
| 53 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]         | Fallback |
| 54 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]           | Fallback |
| 55 | Tensor<[256, 384]> self = ?,<br>List[int] size = [4, 64, 384]               | Fallback |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                 | Fallback |
| 57 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [1, 4, 12, 64, 64]    | Fallback |
| 58 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]          | Fallback |
| 59 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]      | Fallback |
| 60 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 384]     | Fallback |
| 61 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]               | Fallback |
| 62 | Tensor<[4096, 12]> self = ?,<br>List[int] size = [64, 64, -1]               | Fallback |
| 63 | Tensor<[4096, 24]> self = ?,<br>List[int] size = [64, 64, -1]               | Fallback |
| 64 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]             | Fallback |
| 65 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]          | Fallback |
| 66 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                | Fallback |
| 67 | Tensor<[4096, 6]> self = ?,<br>List[int] size = [64, 64, -1]                | Fallback |
| 68 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]            | Fallback |
| 69 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]               | Fallback |
| 70 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]          | Fallback |
| 71 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]          | Fallback |
| 72 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]              | Done     |
| 73 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [1, 64, 3, 64, 64]    | Fallback |
| 74 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]         | Fallback |
| 75 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]            | Fallback |
| 76 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]      | Fallback |
| 77 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]      | Fallback |
| 78 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Fallback |
| 79 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                 | Fallback |
| 80 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 64, 768]                | Done     |
| 81 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]              | Fallback |
| 82 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]          | Fallback |
| 83 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]          | Fallback |

