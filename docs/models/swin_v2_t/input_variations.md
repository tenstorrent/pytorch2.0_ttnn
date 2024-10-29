# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default           |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  1 | aten._unsafe_view.default       |                 19 |          13 |         0 |          0 | 🚧          |    0.68 |
|  2 | aten.add.Tensor                 |                 11 |           8 |         0 |          0 | 🚧          |    0.73 |
|  3 | aten.addmm.default              |                 18 |          18 |         0 |          0 | ✅          |    1    |
|  4 | aten.as_strided.default         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default                |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default                |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clamp.default              |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.clamp_min.default          |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.clone.default              |                 38 |          38 |         0 |          0 | ✅          |    1    |
| 10 | aten.constant_pad_nd.default    |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 11 | aten.convolution.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.div.Tensor                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 13 | aten.eq.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 14 | aten.exp.default                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 15 | aten.expand.default             |                 16 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.gelu.default               |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 17 | aten.index.Tensor               |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.linalg_vector_norm.default |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.masked_fill.Scalar         |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 20 | aten.mean.dim                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 21 | aten.mm.default                 |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 22 | aten.mul.Tensor                 |                  8 |           5 |         0 |          0 | 🚧          |    0.62 |
| 23 | aten.native_layer_norm.default  |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 24 | aten.ne.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 25 | aten.new_zeros.default          |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.permute.default            |                 20 |           8 |         0 |          0 | 🚧          |    0.4  |
| 27 | aten.relu.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 28 | aten.roll.default               |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.select.int                 |                 12 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.sigmoid.default            |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 31 | aten.slice.Tensor               |                 23 |           0 |         0 |          0 | ✘           |    0    |
| 32 | aten.sub.Tensor                 |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 33 | aten.t.default                  |                 25 |          25 |         0 |          0 | ✅          |    1    |
| 34 | aten.transpose.int              |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 35 | aten.unsqueeze.default          |                 16 |          13 |         0 |          0 | 🚧          |    0.81 |
| 36 | aten.view.default               |                 84 |          73 |         0 |          0 | 🚧          |    0.87 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  2 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  3 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] size = [4, 64, 384]     | None     | Fallback   | True  |
|  1 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384] | Done     | Done       | True  |
|  2 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] size = [16, 64, 192]    | None     | Fallback   | True  |
|  3 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192] | None     | Fallback   | True  |
|  4 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int] size = [1, 64, 768]          | Done     | Done       | True  |
|  5 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]   | None     | Fallback   | True  |
|  6 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [64, 64, 96]      | None     | Fallback   | True  |
|  7 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [96, 32, 64]          | Done     | Done       | True  |
|  8 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [96, 64, 32]          | Done     | Done       | True  |
|  9 | Tensor<[16, 64, 6, 32]> self = ?,<br>List[int] size = [16, 64, 192]         | Done     | Done       | True  |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                  | Done     | Done       | True  |
| 11 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [48, 32, 64]          | Done     | Done       | True  |
| 12 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [48, 64, 32]          | Done     | Done       | True  |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                 | Done     | Done       | True  |
| 14 | Tensor<[4, 64, 12, 32]> self = ?,<br>List[int] size = [4, 64, 384]          | Done     | Done       | True  |
| 15 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [192, 32, 64]         | Done     | Done       | True  |
| 16 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [192, 64, 32]         | Done     | Done       | True  |
| 17 | Tensor<[64, 64, 3, 32]> self = ?,<br>List[int] size = [64, 64, 96]          | Done     | Done       | True  |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                 | None     | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?     | Done     | Done       | True  |
|  1 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | None     | Fallback   | True  |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?       | Done     | Done       | True  |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?     | Done     | Done       | True  |
|  4 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | None     | Fallback   | True  |
|  5 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | None     | Fallback   | True  |
|  6 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?       | Done     | Done       | True  |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?         | Done     | Done       | True  |
|  8 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?        | Done     | Done       | True  |
|  9 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?       | Done     | Done       | True  |
| 10 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?        | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     | Done       | True  |
|  1 | Tensor<[1152]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1152]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[1536]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1536]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[192]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?  | Done     | Done       | True  |
|  4 | Tensor<[192]> self = ?,<br>Tensor<[1024, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ?  | Done     | Done       | True  |
|  5 | Tensor<[2304]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?  | Done     | Done       | True  |
|  6 | Tensor<[288]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?    | Done     | Done       | True  |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | True  |
|  8 | Tensor<[384]> self = ?,<br>Tensor<[256, 1536]> mat1 = ?,<br>Tensor<[1536, 384]> mat2 = ? | Done     | Done       | True  |
|  9 | Tensor<[384]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 384]> mat2 = ?   | Done     | Done       | True  |
| 10 | Tensor<[384]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 384]> mat2 = ?    | Done     | Done       | True  |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?       | Done     | Done       | True  |
| 12 | Tensor<[576]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 576]> mat2 = ?  | Done     | Done       | True  |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ?  | Done     | Done       | True  |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[64, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Done     | Done       | True  |
| 15 | Tensor<[768]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     | Done       | True  |
| 16 | Tensor<[96]> self = ?,<br>Tensor<[4096, 384]> mat1 = ?,<br>Tensor<[384, 96]> mat2 = ?    | Done     | Done       | True  |
| 17 | Tensor<[96]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 96]> mat2 = ?      | Done     | Done       | True  |
### aten.as_strided.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768] | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?   | Done     | Done       | True  |
|  3 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?   | Done     | Done       | True  |
|  5 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?   | Done     | Done       | True  |
|  6 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?   | Done     | Done       | True  |
|  7 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?   | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 16, 16, 192]>, <[1, 16, 16, 192]>, <[1, 16, 16, 192]>, <[1, 16, 16, 192]>],<br>int dim = -1 | None     | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[1, 32, 32, 96]>, <[1, 32, 32, 96]>, <[1, 32, 32, 96]>, <[1, 32, 32, 96]>],<br>int dim = -1     | None     | Fallback   | True  |
|  2 | List[Tensor] tensors = [<[1, 8, 8, 384]>, <[1, 8, 8, 384]>, <[1, 8, 8, 384]>, <[1, 8, 8, 384]>],<br>int dim = -1         | None     | Fallback   | True  |
### aten.clamp.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | Fallback   | True  |
|  1 | Tensor<[24, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | Fallback   | True  |
|  2 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | Fallback   | True  |
|  3 | Tensor<[6, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | Fallback   | True  |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  1 | Tensor<[16, 6, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  2 | Tensor<[4, 12, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  3 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 1536]> self = ?                                                              | Done     | Done       | True  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?                                                               | Done     | Done       | True  |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  4 | Tensor<[1, 24, 64, 64]> self = ?                                                                | Done     | Done       | True  |
|  5 | Tensor<[1, 32, 32, 192]> self = ?                                                               | Done     | Done       | True  |
|  6 | Tensor<[1, 32, 32, 768]> self = ?                                                               | Done     | Done       | True  |
|  7 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  8 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  9 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 10 | Tensor<[1, 64, 64, 384]> self = ?                                                               | Done     | Done       | True  |
| 11 | Tensor<[1, 64, 64, 96]> self = ?                                                                | Done     | Done       | True  |
| 12 | Tensor<[1, 64, 768]> self = ?                                                                   | Done     | Done       | True  |
| 13 | Tensor<[1, 8, 8, 3072]> self = ?                                                                | Done     | Done       | True  |
| 14 | Tensor<[1, 8, 8, 768]> self = ?                                                                 | Done     | Done       | True  |
| 15 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 16 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 17 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 18 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 19 | Tensor<[16, 6, 64, 64]> self = ?                                                                | Done     | Done       | True  |
| 20 | Tensor<[16, 64, 192]> self = ?                                                                  | Done     | Done       | True  |
| 21 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 23 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 24 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       | True  |
| 25 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 26 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 27 | Tensor<[4, 12, 64, 64]> self = ?                                                                | Done     | Done       | True  |
| 28 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 29 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 30 | Tensor<[4, 64, 384]> self = ?                                                                   | Done     | Done       | True  |
| 31 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       | True  |
| 32 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 33 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 34 | Tensor<[64, 3, 64, 64]> self = ?                                                                | Done     | Done       | True  |
| 35 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 36 | Tensor<[64, 64, 96]> self = ?                                                                   | Done     | Done       | True  |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | True  |
|  1 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | True  |
|  2 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ? | Done     | Done       | True  |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       | True  |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |
### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   |
|---:|:----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | True  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64] | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]  | None     | Fallback   | True  |
|  2 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32] | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64] | Unknown  | Fallback   | True  |
|  4 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64] | Unknown  | Fallback   | True  |
|  5 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]  | None     | Fallback   | True  |
|  6 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32] | Unknown  | Fallback   | True  |
|  7 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64] | Unknown  | Fallback   | True  |
|  8 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64] | Unknown  | Fallback   | True  |
|  9 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]  | None     | Fallback   | True  |
| 10 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32] | Unknown  | Fallback   | True  |
| 11 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64] | Unknown  | Fallback   | True  |
| 12 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64] | Unknown  | Fallback   | True  |
| 13 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]  | None     | Fallback   | True  |
| 14 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32] | Unknown  | Fallback   | True  |
| 15 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64] | Unknown  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 1536]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 32, 32, 768]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 64, 64, 384]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 8, 3072]> self = ?   | Done     | Done       | True  |
### aten.index.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | None     | Fallback   | True  |
|  1 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | None     | Fallback   | True  |
|  2 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | None     | Fallback   | True  |
|  3 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | None     | Fallback   | True  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = -100.0 | Done     | Done       | True  |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0    | Done     | Done       | True  |
|  2 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = -100.0   | Done     | Done       | True  |
|  3 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = 0.0      | Done     | Done       | True  |
|  4 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0 | Done     | Done       | True  |
|  5 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = 0.0    | Done     | Done       | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | True  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?   | Done     | Done       | True  |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?   | Done     | Done       | True  |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?    | Done     | Done       | True  |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?    | Done     | Done       | True  |
|  5 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?  | Done     | Done       | True  |
|  6 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ? | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16            | Done     | Done       | True  |
|  1 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16            | Done     | Done       | True  |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16             | Done     | Done       | True  |
|  4 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16             | Done     | Done       | True  |
|  5 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?  | None     | Fallback   | True  |
|  6 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ? | None     | Fallback   | True  |
|  7 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?  | None     | Fallback   | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  1 | Tensor<[1, 32, 32, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  2 | Tensor<[1, 64, 64, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |
|  3 | Tensor<[1, 8, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       | True  |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  1 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
|  2 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
### aten.permute.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  4 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  5 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   | True  |
|  6 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | True  |
|  8 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
|  9 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | Done       | True  |
| 10 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 12 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 14 | Tensor<[64, 64, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       | True  |
| 15 | Tensor<[64, 64, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       | True  |
| 16 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | None     | Fallback   | True  |
| 17 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                   | None     | Fallback   | True  |
| 18 | Tensor<[64, 64, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       | True  |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Done     | Done       | True  |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     | Fallback   | True  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     | Fallback   | True  |
|  2 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     | Fallback   | True  |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     | Fallback   | True  |
|  4 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2]  | None     | Fallback   | True  |
|  5 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]    | None     | Fallback   | True  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  1 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  2 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  3 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  4 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  5 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  6 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  7 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  8 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  9 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
| 10 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
| 11 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 64, 64]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 24, 64, 64]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 3, 64, 64]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 6, 64, 64]> self = ?  | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 16, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  3 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  4 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  6 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  7 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
|  9 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 10 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 11 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 13 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 14 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 15 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 16 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 17 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 18 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 19 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 20 | Tensor<[1, 8, 8, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 21 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 22 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | None     | Fallback   | True  |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | None     | Fallback   | True  |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | None     | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 768]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1152, 384]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[12, 512]> self = ?   | Done     | Done       | True  |
|  3 | Tensor<[1536, 384]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[192, 192]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[192, 384]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[192, 768]> self = ?  | Done     | Done       | True  |
|  7 | Tensor<[2304, 768]> self = ? | Done     | Done       | True  |
|  8 | Tensor<[24, 512]> self = ?   | Done     | Done       | True  |
|  9 | Tensor<[288, 96]> self = ?   | Done     | Done       | True  |
| 10 | Tensor<[3, 512]> self = ?    | Done     | Done       | True  |
| 11 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
| 12 | Tensor<[384, 1536]> self = ? | Done     | Done       | True  |
| 13 | Tensor<[384, 384]> self = ?  | Done     | Done       | True  |
| 14 | Tensor<[384, 768]> self = ?  | Done     | Done       | True  |
| 15 | Tensor<[384, 96]> self = ?   | Done     | Done       | True  |
| 16 | Tensor<[512, 2]> self = ?    | Done     | Done       | True  |
| 17 | Tensor<[576, 192]> self = ?  | Done     | Done       | True  |
| 18 | Tensor<[6, 512]> self = ?    | Done     | Done       | True  |
| 19 | Tensor<[768, 1536]> self = ? | Done     | Done       | True  |
| 20 | Tensor<[768, 192]> self = ?  | Done     | Done       | True  |
| 21 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
| 22 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
| 23 | Tensor<[96, 384]> self = ?   | Done     | Done       | True  |
| 24 | Tensor<[96, 96]> self = ?    | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  1 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  2 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  3 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  4 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  5 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  6 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  7 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 64, 64]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
|  1 | Tensor<[16, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     | Done       | True  |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
|  3 | Tensor<[16, 64]> self = ?,<br>int dim = 1        | Done     | Done       | True  |
|  4 | Tensor<[16, 64]> self = ?,<br>int dim = 2        | None     | Fallback   | True  |
|  5 | Tensor<[24, 64, 64]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
|  6 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0     | Done     | Done       | True  |
|  7 | Tensor<[4, 1, 64, 64]> self = ?,<br>int dim = 0  | Done     | Done       | True  |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 1     | Done     | Done       | True  |
|  9 | Tensor<[4, 64]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
| 10 | Tensor<[4, 64]> self = ?,<br>int dim = 2         | None     | Fallback   | True  |
| 11 | Tensor<[6, 64, 64]> self = ?,<br>int dim = 0     | Done     | Done       | True  |
| 12 | Tensor<[64, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     | Done       | True  |
| 13 | Tensor<[64, 64, 64]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
| 14 | Tensor<[64, 64]> self = ?,<br>int dim = 1        | Done     | Done       | True  |
| 15 | Tensor<[64, 64]> self = ?,<br>int dim = 2        | None     | Fallback   | True  |
### aten.view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]     | None     | Fallback   | True  |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]   | Done     | Done       | True  |
|  2 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]              | Done     | Done       | True  |
|  3 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]              | Done     | Done       | True  |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]               | Done     | Done       | True  |
|  5 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                | Done     | Done       | True  |
|  6 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]           | Done     | Done       | True  |
|  7 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                | Done     | Done       | True  |
|  8 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]         | None     | Fallback   | True  |
|  9 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384] | Done     | Done       | True  |
| 10 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [256, 384]           | None     | Fallback   | True  |
| 11 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]           | None     | Fallback   | True  |
| 12 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]    | Done     | Done       | True  |
| 13 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]          | Done     | Done       | True  |
| 14 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]          | Done     | Done       | True  |
| 15 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]          | Done     | Done       | True  |
| 16 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192] | Done     | Done       | True  |
| 17 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1024, 192]          | Done     | Done       | True  |
| 18 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]          | Done     | Done       | True  |
| 19 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]          | Done     | Done       | True  |
| 20 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]   | Done     | Done       | True  |
| 21 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]      | None     | Fallback   | True  |
| 22 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]    | Done     | Done       | True  |
| 23 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]          | Done     | Done       | True  |
| 24 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]   | Done     | Done       | True  |
| 25 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]            | Done     | Done       | True  |
| 26 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 768]     | Done     | Done       | True  |
| 27 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                | Done     | Done       | True  |
| 28 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]               | Done     | Done       | True  |
| 29 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]            | None     | Fallback   | True  |
| 30 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]            | None     | Fallback   | True  |
| 31 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]   | Done     | Done       | True  |
| 32 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [64, 768]              | None     | Fallback   | True  |
| 33 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]          | Done     | Done       | True  |
| 34 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [16, 64, 192]             | Done     | Done       | True  |
| 35 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]             | Done     | Done       | True  |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]          | Done     | Done       | True  |
| 37 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                 | Done     | Done       | True  |
| 38 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64, 64]    | Done     | Done       | True  |
| 39 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]          | Done     | Done       | True  |
| 40 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 192]    | Done     | Done       | True  |
| 41 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]             | Done     | Done       | True  |
| 42 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]      | None     | Fallback   | True  |
| 43 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]         | Done     | Done       | True  |
| 44 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]         | Done     | Done       | True  |
| 45 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]             | Done     | Done       | True  |
| 46 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]             | Done     | Done       | True  |
| 47 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]               | Done     | Done       | True  |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]           | Done     | Done       | True  |
| 49 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]               | Done     | Done       | True  |
| 50 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]          | Done     | Done       | True  |
| 51 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]          | Done     | Done       | True  |
| 52 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]             | Done     | Done       | True  |
| 53 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]         | Done     | Done       | True  |
| 54 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]           | Done     | Done       | True  |
| 55 | Tensor<[256, 384]> self = ?,<br>List[int] size = [4, 64, 384]               | Done     | Done       | True  |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                 | Done     | Done       | True  |
| 57 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [1, 4, 12, 64, 64]    | Done     | Done       | True  |
| 58 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]          | Done     | Done       | True  |
| 59 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]      | None     | Fallback   | True  |
| 60 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 384]     | Done     | Done       | True  |
| 61 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]               | Done     | Done       | True  |
| 62 | Tensor<[4096, 12]> self = ?,<br>List[int] size = [64, 64, -1]               | Done     | Done       | True  |
| 63 | Tensor<[4096, 24]> self = ?,<br>List[int] size = [64, 64, -1]               | Done     | Done       | True  |
| 64 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]             | Done     | Done       | True  |
| 65 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]          | Done     | Done       | True  |
| 66 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                | Done     | Done       | True  |
| 67 | Tensor<[4096, 6]> self = ?,<br>List[int] size = [64, 64, -1]                | Done     | Done       | True  |
| 68 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]            | Done     | Done       | True  |
| 69 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]               | Done     | Done       | True  |
| 70 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]          | Done     | Done       | True  |
| 71 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]          | Done     | Done       | True  |
| 72 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]              | Done     | Done       | True  |
| 73 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [1, 64, 3, 64, 64]    | Done     | Done       | True  |
| 74 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]         | Done     | Done       | True  |
| 75 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]            | Done     | Done       | True  |
| 76 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]      | None     | Fallback   | True  |
| 77 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]      | Done     | Done       | True  |
| 78 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Done     | Done       | True  |
| 79 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                 | Done     | Done       | True  |
| 80 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 64, 768]                | Done     | Done       | True  |
| 81 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]              | Done     | Done       | True  |
| 82 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]          | Done     | Done       | True  |
| 83 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]          | Done     | Done       | True  |

