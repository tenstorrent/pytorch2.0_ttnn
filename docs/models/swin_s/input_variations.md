# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  1 | aten._unsafe_view.default      |                 19 |          19 |         0 |          0 | ✅          |    1    |
|  2 | aten.add.Tensor                |                 11 |          11 |         0 |          0 | ✅          |    1    |
|  3 | aten.addmm.default             |                 17 |          16 |         1 |          0 | ✅          |    1    |
|  4 | aten.as_strided.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default               |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default               |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default             |                 39 |          39 |         0 |          0 | ✅          |    1    |
|  8 | aten.constant_pad_nd.default   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  9 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.eq.Scalar                 |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.expand.default            |                 12 |           0 |        12 |          0 | ✅          |    1    |
| 12 | aten.gelu.default              |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 13 | aten.index.Tensor              |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.masked_fill.Scalar        |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.mean.dim                  |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 16 | aten.mm.default                |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 17 | aten.mul.Tensor                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 18 | aten.native_layer_norm.default |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 19 | aten.ne.Scalar                 |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.new_zeros.default         |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.permute.default           |                 21 |           9 |         0 |          0 | 🚧          |    0.43 |
| 22 | aten.roll.default              |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.select.int                |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 24 | aten.slice.Tensor              |                 23 |           0 |        11 |          0 | 🚧          |    0.48 |
| 25 | aten.sub.Tensor                |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.t.default                 |                 20 |          20 |         0 |          0 | ✅          |    1    |
| 27 | aten.transpose.int             |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 28 | aten.unsqueeze.default         |                 16 |          10 |         6 |          0 | ✅          |    1    |
| 29 | aten.view.default              |                 73 |          61 |        12 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  2 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  3 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] size = [4, 49, 384]     | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384] | Done     | Done       | True  |
|  2 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] size = [16, 49, 192]    | Done     | Done       | True  |
|  3 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192] | Done     | Done       | True  |
|  4 | Tensor<[1, 49, 24, 32]> self = ?,<br>List[int] size = [1, 49, 768]          | Done     | Done       | True  |
|  5 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]   | Done     | Done       | True  |
|  6 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] size = [64, 49, 96]      | Done     | Done       | True  |
|  7 | Tensor<[16, 49, 6, 32]> self = ?,<br>List[int] size = [16, 49, 192]         | Done     | Done       | True  |
|  8 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [96, 32, 49]          | Done     | Done       | True  |
|  9 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [96, 49, 32]          | Done     | Done       | True  |
| 10 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int] size = [4, 49]                  | Done     | Done       | True  |
| 11 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [48, 32, 49]          | Done     | Done       | True  |
| 12 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [48, 49, 32]          | Done     | Done       | True  |
| 13 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int] size = [16, 49]                 | Done     | Done       | True  |
| 14 | Tensor<[4, 49, 12, 32]> self = ?,<br>List[int] size = [4, 49, 384]          | Done     | Done       | True  |
| 15 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [192, 32, 49]         | Done     | Done       | True  |
| 16 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [192, 49, 32]         | Done     | Done       | True  |
| 17 | Tensor<[64, 49, 3, 32]> self = ?,<br>List[int] size = [64, 49, 96]          | Done     | Done       | True  |
| 18 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int] size = [64, 49]                 | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?     | Done     | Done       | True  |
|  1 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?       | Done     | Done       | True  |
|  3 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?     | Done     | Done       | True  |
|  4 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?  | Done     | Done       | True  |
|  5 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?       | Done     | Done       | True  |
|  6 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ? | Done     | Done       | True  |
|  7 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?         | Done     | Done       | True  |
|  8 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?        | Done     | Done       | True  |
|  9 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?       | Done     | Done       | True  |
| 10 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?        | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Removed  | Done       | True  |
|  1 | Tensor<[1152]> self = ?,<br>Tensor<[196, 384]> mat1 = ?,<br>Tensor<[384, 1152]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[1536]> self = ?,<br>Tensor<[196, 384]> mat1 = ?,<br>Tensor<[384, 1536]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[192]> self = ?,<br>Tensor<[784, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[192]> self = ?,<br>Tensor<[784, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ?   | Done     | Done       | True  |
|  5 | Tensor<[2304]> self = ?,<br>Tensor<[49, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?  | Done     | Done       | True  |
|  6 | Tensor<[288]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?    | Done     | Done       | True  |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[49, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | True  |
|  8 | Tensor<[384]> self = ?,<br>Tensor<[196, 1536]> mat1 = ?,<br>Tensor<[1536, 384]> mat2 = ? | Done     | Done       | True  |
|  9 | Tensor<[384]> self = ?,<br>Tensor<[196, 384]> mat1 = ?,<br>Tensor<[384, 384]> mat2 = ?   | Done     | Done       | True  |
| 10 | Tensor<[384]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 384]> mat2 = ?    | Done     | Done       | True  |
| 11 | Tensor<[576]> self = ?,<br>Tensor<[784, 192]> mat1 = ?,<br>Tensor<[192, 576]> mat2 = ?   | Done     | Done       | True  |
| 12 | Tensor<[768]> self = ?,<br>Tensor<[49, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Done     | Done       | True  |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[49, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     | Done       | True  |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[784, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ?   | Done     | Done       | True  |
| 15 | Tensor<[96]> self = ?,<br>Tensor<[3136, 384]> mat1 = ?,<br>Tensor<[384, 96]> mat2 = ?    | Done     | Done       | True  |
| 16 | Tensor<[96]> self = ?,<br>Tensor<[3136, 96]> mat1 = ?,<br>Tensor<[96, 96]> mat2 = ?      | Done     | Done       | True  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768] | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?   | Done     | Done       | True  |
|  3 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?   | Done     | Done       | True  |
|  5 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?   | Done     | Done       | True  |
|  6 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?   | Done     | Done       | True  |
|  7 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?   | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 14, 14, 192]>, <[1, 14, 14, 192]>, <[1, 14, 14, 192]>, <[1, 14, 14, 192]>],<br>int dim = -1 | None     | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[1, 28, 28, 96]>, <[1, 28, 28, 96]>, <[1, 28, 28, 96]>, <[1, 28, 28, 96]>],<br>int dim = -1     | None     | Fallback   | True  |
|  2 | List[Tensor] tensors = [<[1, 7, 7, 384]>, <[1, 7, 7, 384]>, <[1, 7, 7, 384]>, <[1, 7, 7, 384]>],<br>int dim = -1         | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 1536]> self = ?                                                              | Done     | Done       | True  |
|  1 | Tensor<[1, 14, 14, 384]> self = ?                                                               | Done     | Done       | True  |
|  2 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  3 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  4 | Tensor<[1, 24, 49, 49]> self = ?                                                                | Done     | Done       | True  |
|  5 | Tensor<[1, 28, 28, 192]> self = ?                                                               | Done     | Done       | True  |
|  6 | Tensor<[1, 28, 28, 768]> self = ?                                                               | Done     | Done       | True  |
|  7 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  8 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  9 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 10 | Tensor<[1, 49, 768]> self = ?                                                                   | Done     | Done       | True  |
| 11 | Tensor<[1, 56, 56, 384]> self = ?                                                               | Done     | Done       | True  |
| 12 | Tensor<[1, 56, 56, 96]> self = ?                                                                | Done     | Done       | True  |
| 13 | Tensor<[1, 7, 7, 3072]> self = ?                                                                | Done     | Done       | True  |
| 14 | Tensor<[1, 7, 7, 768]> self = ?                                                                 | Done     | Done       | True  |
| 15 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 16 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 17 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 18 | Tensor<[16, 49, 192]> self = ?                                                                  | Done     | Done       | True  |
| 19 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 20 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 21 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 22 | Tensor<[16, 6, 49, 49]> self = ?                                                                | Done     | Done       | True  |
| 23 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 24 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 25 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       | True  |
| 26 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 27 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 28 | Tensor<[4, 12, 49, 49]> self = ?                                                                | Done     | Done       | True  |
| 29 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 30 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 31 | Tensor<[4, 49, 384]> self = ?                                                                   | Done     | Done       | True  |
| 32 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       | True  |
| 33 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 34 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 35 | Tensor<[64, 3, 49, 49]> self = ?                                                                | Done     | Done       | True  |
| 36 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 37 | Tensor<[64, 49, 96]> self = ?                                                                   | Done     | Done       | True  |
| 38 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | True  |
|  1 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | True  |
|  2 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | True  |
|  3 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | None     | Fallback   | True  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [1, 24, 32, 49] | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32] | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49] | Removed  | Fallback   | True  |
|  3 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [16, 6, 32, 49] | Removed  | Fallback   | True  |
|  4 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32] | Removed  | Fallback   | True  |
|  5 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49] | Removed  | Fallback   | True  |
|  6 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [4, 12, 32, 49] | Removed  | Fallback   | True  |
|  7 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32] | Removed  | Fallback   | True  |
|  8 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49] | Removed  | Fallback   | True  |
|  9 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [64, 3, 32, 49] | Removed  | Fallback   | True  |
| 10 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32] | Removed  | Fallback   | True  |
| 11 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49] | Removed  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 1536]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 28, 28, 768]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 56, 56, 384]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 7, 7, 3072]> self = ?   | Done     | Done       | True  |
### aten.index.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[169, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>] | None     | Fallback   | True  |
|  1 | Tensor<[169, 24]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>] | None     | Fallback   | True  |
|  2 | Tensor<[169, 3]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>]  | None     | Fallback   | True  |
|  3 | Tensor<[169, 6]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>]  | None     | Fallback   | True  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = -100.0 | None     | Fallback   | True  |
|  1 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0    | None     | Fallback   | True  |
|  2 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = -100.0   | None     | Fallback   | True  |
|  3 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = 0.0      | None     | Fallback   | True  |
|  4 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0 | None     | Fallback   | True  |
|  5 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = 0.0    | None     | Fallback   | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Removed  | Done       | True  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?  | Done     | Done       | True  |
|  1 | Tensor<[49, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?  | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | True  |
|  1 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | True  |
|  2 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | True  |
|  3 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |
|  1 | Tensor<[1, 14, 14, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |
|  2 | Tensor<[1, 28, 28, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |
|  3 | Tensor<[1, 28, 28, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |
|  4 | Tensor<[1, 56, 56, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05       | Done     | Done       | N/A   |
|  5 | Tensor<[1, 7, 7, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  6 | Tensor<[1, 7, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | None     | Fallback   | True  |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [28, 28],<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  1 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [14, 14],<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
|  2 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [56, 56],<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
### aten.permute.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  1 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  2 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  3 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  4 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  5 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  6 | Tensor<[1, 49, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
|  7 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | True  |
|  8 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
|  9 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
| 10 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | Done       | True  |
| 11 | Tensor<[16, 49, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
| 12 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 13 | Tensor<[4, 49, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
| 14 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 15 | Tensor<[49, 49, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       | True  |
| 16 | Tensor<[49, 49, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       | True  |
| 17 | Tensor<[49, 49, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       | True  |
| 18 | Tensor<[49, 49, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       | True  |
| 19 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
| 20 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | None     | Fallback   | True  |
|  1 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | None     | Fallback   | True  |
|  2 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | None     | Fallback   | True  |
|  3 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | None     | Fallback   | True  |
|  4 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2]  | None     | Fallback   | True  |
|  5 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]    | None     | Fallback   | True  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | True  |
|  1 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | True  |
|  2 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | True  |
|  3 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | True  |
|  4 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | True  |
|  5 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | True  |
|  6 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | True  |
|  7 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | True  |
|  8 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | True  |
|  9 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | True  |
| 10 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | True  |
| 11 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  3 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  4 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  6 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  7 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
|  8 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  9 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 10 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 11 | Tensor<[1, 28, 28, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 12 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 13 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 14 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 15 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 16 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 17 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 18 | Tensor<[1, 7, 14, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 19 | Tensor<[1, 7, 14, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 20 | Tensor<[1, 7, 7, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 21 | Tensor<[1, 7, 7, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 22 | Tensor<[1, 7, 7, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ? | None     | Fallback   | True  |
|  1 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?   | None     | Fallback   | True  |
|  2 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | None     | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 768]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1152, 384]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1536, 384]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[192, 192]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[192, 384]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[192, 768]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[2304, 768]> self = ? | Done     | Done       | True  |
|  7 | Tensor<[288, 96]> self = ?   | Done     | Done       | True  |
|  8 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
|  9 | Tensor<[384, 1536]> self = ? | Done     | Done       | True  |
| 10 | Tensor<[384, 384]> self = ?  | Done     | Done       | True  |
| 11 | Tensor<[384, 768]> self = ?  | Done     | Done       | True  |
| 12 | Tensor<[384, 96]> self = ?   | Done     | Done       | True  |
| 13 | Tensor<[576, 192]> self = ?  | Done     | Done       | True  |
| 14 | Tensor<[768, 1536]> self = ? | Done     | Done       | True  |
| 15 | Tensor<[768, 192]> self = ?  | Done     | Done       | True  |
| 16 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
| 17 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
| 18 | Tensor<[96, 384]> self = ?   | Done     | Done       | True  |
| 19 | Tensor<[96, 96]> self = ?    | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  1 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  2 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  3 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  4 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  5 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  6 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  7 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 49, 49]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
|  1 | Tensor<[16, 1, 49, 49]> self = ?,<br>int dim = 0 | Done     | Done       | True  |
|  2 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
|  3 | Tensor<[16, 49]> self = ?,<br>int dim = 1        | Removed  | Done       | True  |
|  4 | Tensor<[16, 49]> self = ?,<br>int dim = 2        | Removed  | Done       | True  |
|  5 | Tensor<[24, 49, 49]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
|  6 | Tensor<[3, 49, 49]> self = ?,<br>int dim = 0     | Done     | Done       | True  |
|  7 | Tensor<[4, 1, 49, 49]> self = ?,<br>int dim = 0  | Done     | Done       | True  |
|  8 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 1     | Done     | Done       | True  |
|  9 | Tensor<[4, 49]> self = ?,<br>int dim = 1         | Removed  | Done       | True  |
| 10 | Tensor<[4, 49]> self = ?,<br>int dim = 2         | Removed  | Done       | True  |
| 11 | Tensor<[6, 49, 49]> self = ?,<br>int dim = 0     | Done     | Done       | True  |
| 12 | Tensor<[64, 1, 49, 49]> self = ?,<br>int dim = 0 | Done     | Done       | True  |
| 13 | Tensor<[64, 49, 49]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
| 14 | Tensor<[64, 49]> self = ?,<br>int dim = 1        | Removed  | Done       | True  |
| 15 | Tensor<[64, 49]> self = ?,<br>int dim = 2        | Removed  | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 49, 768]     | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]   | Done     | Done       | True  |
|  2 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int] size = [196, 1536]         | Done     | Done       | True  |
|  3 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 384] | Removed  | Done       | True  |
|  4 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [196, 384]           | Done     | Done       | True  |
|  5 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int] size = [196, 768]           | Done     | Done       | True  |
|  6 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int] size = [-1, 6, 49, 49]    | Done     | Done       | True  |
|  7 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [24, 32, 49]          | Done     | Done       | True  |
|  8 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [24, 49, 32]          | Done     | Done       | True  |
|  9 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [24, 49, 49]          | Done     | Done       | True  |
| 10 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 192] | Removed  | Done       | True  |
| 11 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [784, 192]           | Done     | Done       | True  |
| 12 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int] size = [784, 384]           | Done     | Done       | True  |
| 13 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int] size = [784, 768]           | Done     | Done       | True  |
| 14 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int] size = [-1, 12, 49, 49]   | Done     | Done       | True  |
| 15 | Tensor<[1, 49, 2304]> self = ?,<br>List[int] size = [1, 49, 3, 24, 32]      | Removed  | Done       | True  |
| 16 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 768]     | Removed  | Done       | True  |
| 17 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [49, 768]                | Done     | Done       | True  |
| 18 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int] size = [3136, 384]          | Done     | Done       | True  |
| 19 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 96]   | Removed  | Done       | True  |
| 20 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [3136, 96]            | Done     | Done       | True  |
| 21 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int] size = [-1, 3, 49, 49]    | Done     | Done       | True  |
| 22 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int] size = [49, 1536]            | Done     | Done       | True  |
| 23 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int] size = [49, 3072]            | Done     | Done       | True  |
| 24 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 768]   | Removed  | Done       | True  |
| 25 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [49, 768]              | Done     | Done       | True  |
| 26 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]               | Done     | Done       | True  |
| 27 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                 | Done     | Done       | True  |
| 28 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 192]    | Removed  | Done       | True  |
| 29 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [784, 192]              | Done     | Done       | True  |
| 30 | Tensor<[16, 49, 576]> self = ?,<br>List[int] size = [16, 49, 3, 6, 32]      | Removed  | Done       | True  |
| 31 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [1, 16, 6, 49, 49]    | Done     | Done       | True  |
| 32 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [96, 49, 49]          | Done     | Done       | True  |
| 33 | Tensor<[192, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]         | Done     | Done       | True  |
| 34 | Tensor<[192, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]         | Done     | Done       | True  |
| 35 | Tensor<[196, 1152]> self = ?,<br>List[int] size = [4, 49, 1152]             | Done     | Done       | True  |
| 36 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [1, 14, 14, 1536]         | Done     | Done       | True  |
| 37 | Tensor<[196, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]           | Done     | Done       | True  |
| 38 | Tensor<[196, 384]> self = ?,<br>List[int] size = [4, 49, 384]               | Done     | Done       | True  |
| 39 | Tensor<[24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]          | Done     | Done       | True  |
| 40 | Tensor<[24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]          | Done     | Done       | True  |
| 41 | Tensor<[2401, 12]> self = ?,<br>List[int] size = [49, 49, -1]               | Done     | Done       | True  |
| 42 | Tensor<[2401, 24]> self = ?,<br>List[int] size = [49, 49, -1]               | Done     | Done       | True  |
| 43 | Tensor<[2401, 3]> self = ?,<br>List[int] size = [49, 49, -1]                | Done     | Done       | True  |
| 44 | Tensor<[2401, 6]> self = ?,<br>List[int] size = [49, 49, -1]                | Done     | Done       | True  |
| 45 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                 | Done     | Done       | True  |
| 46 | Tensor<[3136, 288]> self = ?,<br>List[int] size = [64, 49, 288]             | Done     | Done       | True  |
| 47 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [1, 56, 56, 384]          | Done     | Done       | True  |
| 48 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]            | Done     | Done       | True  |
| 49 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [64, 49, 96]               | Done     | Done       | True  |
| 50 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [1, 4, 12, 49, 49]    | Done     | Done       | True  |
| 51 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [48, 49, 49]          | Done     | Done       | True  |
| 52 | Tensor<[4, 49, 1152]> self = ?,<br>List[int] size = [4, 49, 3, 12, 32]      | Removed  | Done       | True  |
| 53 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 384]     | Removed  | Done       | True  |
| 54 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [196, 384]               | Done     | Done       | True  |
| 55 | Tensor<[48, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]          | Done     | Done       | True  |
| 56 | Tensor<[48, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]          | Done     | Done       | True  |
| 57 | Tensor<[49, 2304]> self = ?,<br>List[int] size = [1, 49, 2304]              | Done     | Done       | True  |
| 58 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 7, 7, 3072]            | Done     | Done       | True  |
| 59 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 49, 768]                | Done     | Done       | True  |
| 60 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]              | Done     | Done       | True  |
| 61 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                 | Done     | Done       | True  |
| 62 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [1, 64, 3, 49, 49]    | Done     | Done       | True  |
| 63 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [192, 49, 49]         | Done     | Done       | True  |
| 64 | Tensor<[64, 49, 288]> self = ?,<br>List[int] size = [64, 49, 3, 3, 32]      | Removed  | Done       | True  |
| 65 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 96]      | Removed  | Done       | True  |
| 66 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [3136, 96]               | Done     | Done       | True  |
| 67 | Tensor<[784, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]           | Done     | Done       | True  |
| 68 | Tensor<[784, 192]> self = ?,<br>List[int] size = [16, 49, 192]              | Done     | Done       | True  |
| 69 | Tensor<[784, 576]> self = ?,<br>List[int] size = [16, 49, 576]              | Done     | Done       | True  |
| 70 | Tensor<[784, 768]> self = ?,<br>List[int] size = [1, 28, 28, 768]           | Done     | Done       | True  |
| 71 | Tensor<[96, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]          | Done     | Done       | True  |
| 72 | Tensor<[96, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]          | Done     | Done       | True  |

