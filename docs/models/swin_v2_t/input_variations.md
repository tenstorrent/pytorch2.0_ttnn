# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default           |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  1 | aten._unsafe_view.default       |                 19 |          19 |         0 |          0 | ✅          |    1    |
|  2 | aten.add.Tensor                 |                 11 |           8 |         0 |          0 | 🚧          |    0.73 |
|  3 | aten.addmm.default              |                 18 |           6 |        12 |          0 | ✅          |    1    |
|  4 | aten.as_strided.default         |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.bmm.default                |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default                |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  7 | aten.clamp.default              |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  8 | aten.clamp_min.default          |                  4 |           0 |         4 |          0 | ✅          |    1    |
|  9 | aten.clone.default              |                 38 |           0 |        38 |          0 | ✅          |    1    |
| 10 | aten.constant_pad_nd.default    |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 11 | aten.convolution.default        |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.div.Tensor                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 13 | aten.embedding.default          |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 14 | aten.eq.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 15 | aten.exp.default                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 16 | aten.expand.default             |                 16 |           4 |        12 |          0 | ✅          |    1    |
| 17 | aten.fill.Tensor                |                 10 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.gelu.default               |                  4 |           2 |         2 |          0 | ✅          |    1    |
| 19 | aten.index.Tensor               |                  4 |           0 |         4 |          0 | ✅          |    1    |
| 20 | aten.linalg_vector_norm.default |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.masked_fill.Scalar         |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 22 | aten.mean.dim                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 23 | aten.mm.default                 |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 24 | aten.mul.Tensor                 |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 25 | aten.native_layer_norm.default  |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 26 | aten.ne.Scalar                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 27 | aten.new_zeros.default          |                  3 |           0 |         3 |          0 | ✅          |    1    |
| 28 | aten.permute.default            |                 20 |          20 |         0 |          0 | ✅          |    1    |
| 29 | aten.relu.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 30 | aten.roll.default               |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 31 | aten.select.int                 |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 32 | aten.sigmoid.default            |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 33 | aten.slice.Tensor               |                 54 |          31 |        11 |          0 | 🚧          |    0.78 |
| 34 | aten.slice_scatter.default      |                 31 |          31 |         0 |          0 | ✅          |    1    |
| 35 | aten.sub.Tensor                 |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 36 | aten.t.default                  |                 25 |          13 |        12 |          0 | ✅          |    1    |
| 37 | aten.transpose.int              |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 38 | aten.unsqueeze.default          |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 39 | aten.view.default               |                 84 |          82 |         2 |          0 | ✅          |    1    |
| 40 | aten.zero.default               |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 41 | aten.zeros.default              |                  3 |           3 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999615 |     -1 |
|  1 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999607 |     -1 |
|  2 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999607 |     -1 |
|  3 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999612 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] size = [4, 64, 384]     | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] size = [16, 64, 192]    | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192] | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int] size = [1, 64, 768]          | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]   | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [64, 64, 96]      | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [96, 32, 64]          | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [96, 64, 32]          | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[16, 64, 6, 32]> self = ?,<br>List[int] size = [16, 64, 192]         | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                  | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [48, 32, 64]          | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [48, 64, 32]          | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                 | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[4, 64, 12, 32]> self = ?,<br>List[int] size = [4, 64, 384]          | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [192, 32, 64]         | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [192, 64, 32]         | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[64, 64, 3, 32]> self = ?,<br>List[int] size = [64, 64, 96]          | Done     | Done       |     1 |     -1 |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                 | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?     | Done     | Done       | 0.999998 |     -1 |
|  1 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | None     | Fallback   | 1        |     -1 |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?       | Done     | Done       | 0.999998 |     -1 |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?     | Done     | Done       | 0.999998 |     -1 |
|  4 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | None     | Fallback   | 1        |     -1 |
|  5 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | None     | Fallback   | 1        |     -1 |
|  6 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?       | Done     | Done       | 0.999998 |     -1 |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?         | Done     | Done       | 0.999998 |     -1 |
|  8 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?        | Done     | Done       | 0.999998 |     -1 |
|  9 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?       | Done     | Done       | 0.999998 |     -1 |
| 10 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?        | Done     | Done       | 0.999998 |     -1 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     | Done       | 0.999968 |     -1 |
|  1 | Tensor<[1152]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1152]> mat2 = ? | Removed  | Done       | 0.999972 |     -1 |
|  2 | Tensor<[1536]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 1536]> mat2 = ? | Done     | Done       | 0.999972 |     -1 |
|  3 | Tensor<[192]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?  | Removed  | Done       | 0.999976 |     -1 |
|  4 | Tensor<[192]> self = ?,<br>Tensor<[1024, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ?  | Removed  | Done       | 0.999967 |     -1 |
|  5 | Tensor<[2304]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?  | Removed  | Done       | 0.999967 |     -1 |
|  6 | Tensor<[288]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 288]> mat2 = ?    | Removed  | Done       | 0.999983 |     -1 |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | 0.999967 |     -1 |
|  8 | Tensor<[384]> self = ?,<br>Tensor<[256, 1536]> mat1 = ?,<br>Tensor<[1536, 384]> mat2 = ? | Done     | Done       | 0.999937 |     -1 |
|  9 | Tensor<[384]> self = ?,<br>Tensor<[256, 384]> mat1 = ?,<br>Tensor<[384, 384]> mat2 = ?   | Removed  | Done       | 0.999975 |     -1 |
| 10 | Tensor<[384]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 384]> mat2 = ?    | Removed  | Done       | 0.999983 |     -1 |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?       | Done     | Done       | 0.999992 |     -1 |
| 12 | Tensor<[576]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 576]> mat2 = ?  | Removed  | Done       | 0.99998  |     -1 |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[1024, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ?  | Removed  | Done       | 0.99998  |     -1 |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[64, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Done     | Done       | 0.999943 |     -1 |
| 15 | Tensor<[768]> self = ?,<br>Tensor<[64, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Removed  | Done       | 0.999967 |     -1 |
| 16 | Tensor<[96]> self = ?,<br>Tensor<[4096, 384]> mat1 = ?,<br>Tensor<[384, 96]> mat2 = ?    | Removed  | Done       | 0.999972 |     -1 |
| 17 | Tensor<[96]> self = ?,<br>Tensor<[4096, 96]> mat1 = ?,<br>Tensor<[96, 96]> mat2 = ?      | Removed  | Done       | 0.999983 |     -1 |
### aten.as_strided.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768] | Done     | Done       |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ? | Done     | Done       | 0.99999  |     -1 |
|  1 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ? | Done     | Done       | 0.999986 |     -1 |
|  2 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?   | Done     | Done       | 0.999989 |     -1 |
|  3 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?   | Done     | Done       | 0.999986 |     -1 |
|  4 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?   | Done     | Done       | 0.999989 |     -1 |
|  5 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?   | Done     | Done       | 0.999986 |     -1 |
|  6 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?   | Done     | Done       | 0.99999  |     -1 |
|  7 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?   | Done     | Done       | 0.999986 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 16, 16, 192]>, <[1, 16, 16, 192]>, <[1, 16, 16, 192]>, <[1, 16, 16, 192]>],<br>int dim = -1 | Done     | Done       |     1 |     -1 |
|  1 | List[Tensor] tensors = [<[1, 32, 32, 96]>, <[1, 32, 32, 96]>, <[1, 32, 32, 96]>, <[1, 32, 32, 96]>],<br>int dim = -1     | Done     | Done       |     1 |     -1 |
|  2 | List[Tensor] tensors = [<[1, 8, 8, 384]>, <[1, 8, 8, 384]>, <[1, 8, 8, 384]>, <[1, 8, 8, 384]>],<br>int dim = -1         | Done     | Done       |     1 |     -1 |
### aten.clamp.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 24, 64, 1]> self = ?,<br>Optional[number] min = 1e-12,<br>Optional[number] max = ?         | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | Done     | Done       | 1.0   | -1     |
|  2 | Tensor<[16, 6, 64, 1]> self = ?,<br>Optional[number] min = 1e-12,<br>Optional[number] max = ?         | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[24, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | Done     | Done       | 1.0   | -1     |
|  4 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | Done     | Done       | 1.0   | -1     |
|  5 | Tensor<[4, 12, 64, 1]> self = ?,<br>Optional[number] min = 1e-12,<br>Optional[number] max = ?         | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[6, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | Done     | Done       | 1.0   | -1     |
|  7 | Tensor<[64, 3, 64, 1]> self = ?,<br>Optional[number] min = 1e-12,<br>Optional[number] max = ?         | Done     | Unknown    | N/A   | N/A    |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 24, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[16, 6, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[4, 12, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       |     1 |     -1 |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 16, 1536]> self = ?                                                              | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 16, 384]> self = ?                                                               | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 24, 64, 64]> self = ?                                                                | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 32, 32, 192]> self = ?                                                               | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 32, 32, 768]> self = ?                                                               | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 64, 64, 384]> self = ?                                                               | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 64, 64, 96]> self = ?                                                                | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 64, 768]> self = ?                                                                   | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 8, 8, 3072]> self = ?                                                                | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[1, 8, 8, 768]> self = ?                                                                 | Removed  | Done       |     1 |     -1 |
| 15 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Removed  | Done       |     1 |     -1 |
| 16 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |     -1 |
| 17 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 18 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 19 | Tensor<[16, 6, 64, 64]> self = ?                                                                | Removed  | Done       |     1 |     -1 |
| 20 | Tensor<[16, 64, 192]> self = ?                                                                  | Removed  | Done       |     1 |     -1 |
| 21 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |     -1 |
| 23 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |     -1 |
| 24 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Done       |     1 |     -1 |
| 25 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 26 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 27 | Tensor<[4, 12, 64, 64]> self = ?                                                                | Removed  | Done       |     1 |     -1 |
| 28 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |     -1 |
| 29 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 30 | Tensor<[4, 64, 384]> self = ?                                                                   | Removed  | Done       |     1 |     -1 |
| 31 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Done       |     1 |     -1 |
| 32 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 33 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 34 | Tensor<[64, 3, 64, 64]> self = ?                                                                | Removed  | Done       |     1 |     -1 |
| 35 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       |     1 |     -1 |
| 36 | Tensor<[64, 64, 96]> self = ?                                                                   | Removed  | Done       |     1 |     -1 |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |     -1 |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       |     1 |     -1 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[96, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999968 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ? | Done     | Done       | 0.999997 |     -1 |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ? | Done     | Done       | 0.999997 |     -1 |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ? | Done     | Done       | 0.999999 |     -1 |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ? | Done     | Done       | 0.999999 |     -1 |
### aten.embedding.default
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[225, 12]> weight = ?,<br>Tensor<[4096]> indices = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[225, 24]> weight = ?,<br>Tensor<[4096]> indices = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[225, 3]> weight = ?,<br>Tensor<[4096]> indices = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[225, 6]> weight = ?,<br>Tensor<[4096]> indices = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       |     1 |     -1 |
### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.999979 |     -1 |
|  1 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.999998 |     -1 |
|  2 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 1        |     -1 |
|  3 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.99999  |     -1 |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32] | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64] | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64] | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]  | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32] | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64] | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64] | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]  | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32] | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64] | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64] | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]  | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32] | Removed  | Done       |     1 |     -1 |
| 15 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64] | Removed  | Done       |     1 |     -1 |
### aten.fill.Tensor
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[24, 24]> self = ?,<br>Tensor value = ? | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[24, 4]> self = ?,<br>Tensor value = ?  | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[4, 24]> self = ?,<br>Tensor value = ?  | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[4, 4]> self = ?,<br>Tensor value = ?   | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[4, 56]> self = ?,<br>Tensor value = ?  | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[4, 8]> self = ?,<br>Tensor value = ?   | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[56, 4]> self = ?,<br>Tensor value = ?  | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[56, 56]> self = ?,<br>Tensor value = ? | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[8, 4]> self = ?,<br>Tensor value = ?   | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[8, 8]> self = ?,<br>Tensor value = ?   | None     | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 16, 1536]> self = ? | Done     | Done       | 0.999991 |     -1 |
|  1 | Tensor<[1, 32, 32, 768]> self = ?  | Removed  | Done       | 0.999991 |     -1 |
|  2 | Tensor<[1, 64, 64, 384]> self = ?  | Removed  | Done       | 0.999991 |     -1 |
|  3 | Tensor<[1, 8, 8, 3072]> self = ?   | Done     | Done       | 0.999991 |     -1 |
### aten.index.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[225, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[225, 24]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[225, 3]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[225, 6]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | Removed  | Done       |     1 |     -1 |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[16, 6, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[4, 12, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[64, 3, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = -100.0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0    | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = -100.0   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = 0.0      | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0 | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = 0.0    | Done     | Done       |     1 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |     -1 |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ? | Done     | Done       | 0.999973 |     -1 |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?   | Done     | Done       | 0.999971 |     -1 |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?   | Done     | Done       | 0.999973 |     -1 |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?    | Done     | Done       | 0.999967 |     -1 |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?    | Done     | Done       | 0.999971 |     -1 |
|  5 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?  | Done     | Done       | 0.999963 |     -1 |
|  6 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ? | Done     | Done       | 0.99996  |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   |        PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|-----------:|-------:|
|  0 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16            | Done     | Done       |  1         |     -1 |
|  1 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16            | Done     | Done       |  1         |     -1 |
|  2 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ? | Done     | Done       |  0.999996  |     -1 |
|  3 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16             | Done     | Done       |  1         |     -1 |
|  4 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16             | Done     | Done       |  1         |     -1 |
|  5 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?  | Done     | Done       | -0.0141615 |     -1 |
|  6 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ? | Done     | Done       |  0.295344  |     -1 |
|  7 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?  | Done     | Done       | -0.0820427 |     -1 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 16, 16, 384]> input = ?,<br>List[int] normalized_shape = [384],<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      0 |
|  1 | Tensor<[1, 32, 32, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      0 |
|  2 | Tensor<[1, 64, 64, 96]> input = ?,<br>List[int] normalized_shape = [96],<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |      0 |
|  3 | Tensor<[1, 8, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |      0 |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       |     1 |     -1 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False  | Removed  | Done       |     1 |     -1 |
### aten.permute.default
|    | ATen Input Variations                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[64, 64, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[64, 64, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]      | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       |     1 |     -1 |
| 18 | Tensor<[64, 64, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       |     1 |     -1 |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       |     1 |     -1 |
### aten.relu.default
|    | ATen Input Variations             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Done     | Done       |     1 |     -1 |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2]  | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]    | Done     | Done       |     1 |     -1 |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |     -1 |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 64, 64]> self = ? | Done     | Done       | 0.999756 |     -1 |
|  1 | Tensor<[1, 24, 64, 64]> self = ? | Done     | Done       | 0.999758 |     -1 |
|  2 | Tensor<[1, 3, 64, 64]> self = ?  | Done     | Done       | 0.999757 |     -1 |
|  3 | Tensor<[1, 6, 64, 64]> self = ?  | Done     | Done       | 0.999756 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 16, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | 1.0   | -1     |
| 16 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | 1.0   | -1     |
| 17 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | 1.0   | -1     |
| 19 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | 1.0   | -1     |
| 20 | Tensor<[1, 8, 8, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Done       | 1.0   | -1     |
| 23 | Tensor<[1152]> self = ?,<br>int dim = 0,<br>Optional[int] start = 384,<br>Optional[int] end = 768                                          | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[16, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                         | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[16, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                          | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[16, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                           | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[2304]> self = ?,<br>int dim = 0,<br>Optional[int] start = 768,<br>Optional[int] end = 1536                                         | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[24, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                         | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[24, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                          | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[24, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                           | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[288]> self = ?,<br>int dim = 0,<br>Optional[int] start = 96,<br>Optional[int] end = 192                                            | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[32, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                         | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[32, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                          | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[32, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                           | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[4, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                          | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[4, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                           | Done     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[4, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                            | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[4, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                          | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[4, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                           | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[4, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                            | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[4, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                          | Done     | Unknown    | N/A   | N/A    |
| 42 | Tensor<[4, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                           | Done     | Unknown    | N/A   | N/A    |
| 43 | Tensor<[4, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                            | Done     | Unknown    | N/A   | N/A    |
| 44 | Tensor<[56, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                         | Done     | Unknown    | N/A   | N/A    |
| 45 | Tensor<[56, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                          | Done     | Unknown    | N/A   | N/A    |
| 46 | Tensor<[56, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                           | Done     | Unknown    | N/A   | N/A    |
| 47 | Tensor<[576]> self = ?,<br>int dim = 0,<br>Optional[int] start = 192,<br>Optional[int] end = 384                                           | Done     | Unknown    | N/A   | N/A    |
| 48 | Tensor<[64, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                         | Done     | Unknown    | N/A   | N/A    |
| 49 | Tensor<[64, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                          | Done     | Unknown    | N/A   | N/A    |
| 50 | Tensor<[64, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                           | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[8, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807                          | Done     | Unknown    | N/A   | N/A    |
| 52 | Tensor<[8, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                                           | Done     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[8, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                                            | Done     | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1152]> self = ?,<br>Tensor<[384]> src = ?,<br>int dim = 0,<br>Optional[int] start = 384,<br>Optional[int] end = 768                    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16, 16]> self = ?,<br>Tensor<[4, 16]> src = ?,<br>int dim = 0,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16, 16]> self = ?,<br>Tensor<[4, 16]> src = ?,<br>int dim = 0,<br>Optional[int] start = -8,<br>Optional[int] end = -4                  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16, 16]> self = ?,<br>Tensor<[8, 16]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -8                   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2304]> self = ?,<br>Tensor<[768]> src = ?,<br>int dim = 0,<br>Optional[int] start = 768,<br>Optional[int] end = 1536                   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[24, 32]> self = ?,<br>Tensor<[24, 24]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[24, 32]> self = ?,<br>Tensor<[24, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[24, 32]> self = ?,<br>Tensor<[24, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                  | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[288]> self = ?,<br>Tensor<[96]> src = ?,<br>int dim = 0,<br>Optional[int] start = 96,<br>Optional[int] end = 192                       | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 32]> self = ?,<br>Tensor<[24, 32]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -8                  | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, 32]> self = ?,<br>Tensor<[4, 32]> src = ?,<br>int dim = 0,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807 | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 32]> self = ?,<br>Tensor<[4, 32]> src = ?,<br>int dim = 0,<br>Optional[int] start = -8,<br>Optional[int] end = -4                  | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[4, 16]> self = ?,<br>Tensor<[4, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807   | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[4, 16]> self = ?,<br>Tensor<[4, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                    | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[4, 16]> self = ?,<br>Tensor<[4, 8]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                     | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[4, 32]> self = ?,<br>Tensor<[4, 24]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                    | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[4, 32]> self = ?,<br>Tensor<[4, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807   | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[4, 32]> self = ?,<br>Tensor<[4, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                    | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[4, 64]> self = ?,<br>Tensor<[4, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807   | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[4, 64]> self = ?,<br>Tensor<[4, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                    | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[4, 64]> self = ?,<br>Tensor<[4, 56]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                    | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[56, 64]> self = ?,<br>Tensor<[56, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807 | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[56, 64]> self = ?,<br>Tensor<[56, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                  | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[56, 64]> self = ?,<br>Tensor<[56, 56]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                  | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[576]> self = ?,<br>Tensor<[192]> src = ?,<br>int dim = 0,<br>Optional[int] start = 192,<br>Optional[int] end = 384                     | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[64, 64]> self = ?,<br>Tensor<[4, 64]> src = ?,<br>int dim = 0,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807 | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[64, 64]> self = ?,<br>Tensor<[4, 64]> src = ?,<br>int dim = 0,<br>Optional[int] start = -8,<br>Optional[int] end = -4                  | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[64, 64]> self = ?,<br>Tensor<[56, 64]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -8                  | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[8, 16]> self = ?,<br>Tensor<[8, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -4,<br>Optional[int] end = 9223372036854775807   | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[8, 16]> self = ?,<br>Tensor<[8, 4]> src = ?,<br>int dim = 1,<br>Optional[int] start = -8,<br>Optional[int] end = -4                    | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[8, 16]> self = ?,<br>Tensor<[8, 8]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -8                     | Done     | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | Done     | Done       | 0.479355 |     -1 |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | Done     | Done       | 0.489892 |     -1 |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Done     | Done       | 0.352657 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 768]> self = ? | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1152, 384]> self = ? | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[12, 512]> self = ?   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1536, 384]> self = ? | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[192, 192]> self = ?  | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[192, 384]> self = ?  | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[192, 768]> self = ?  | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[2304, 768]> self = ? | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[24, 512]> self = ?   | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[288, 96]> self = ?   | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[3, 512]> self = ?    | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[3072, 768]> self = ? | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[384, 1536]> self = ? | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[384, 384]> self = ?  | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[384, 768]> self = ?  | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[384, 96]> self = ?   | Removed  | Done       |     1 |     -1 |
| 16 | Tensor<[512, 2]> self = ?    | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[576, 192]> self = ?  | Removed  | Done       |     1 |     -1 |
| 18 | Tensor<[6, 512]> self = ?    | Done     | Done       |     1 |     -1 |
| 19 | Tensor<[768, 1536]> self = ? | Done     | Done       |     1 |     -1 |
| 20 | Tensor<[768, 192]> self = ?  | Removed  | Done       |     1 |     -1 |
| 21 | Tensor<[768, 3072]> self = ? | Done     | Done       |     1 |     -1 |
| 22 | Tensor<[768, 768]> self = ?  | Removed  | Done       |     1 |     -1 |
| 23 | Tensor<[96, 384]> self = ?   | Removed  | Done       |     1 |     -1 |
| 24 | Tensor<[96, 96]> self = ?    | Removed  | Done       |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |     -1 |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[12, 64, 64]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[16, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[16, 64]> self = ?,<br>int dim = 1        | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[16, 64]> self = ?,<br>int dim = 2        | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[24, 64, 64]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0     | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[4, 1, 64, 64]> self = ?,<br>int dim = 0  | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 1     | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[4, 64]> self = ?,<br>int dim = 1         | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[4, 64]> self = ?,<br>int dim = 2         | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[6, 64, 64]> self = ?,<br>int dim = 0     | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[64, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[64, 64, 64]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[64, 64]> self = ?,<br>int dim = 1        | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[64, 64]> self = ?,<br>int dim = 2        | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]              | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]              | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]               | Done     | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                | Done     | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]           | Done     | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]         | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384] | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [256, 384]           | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]           | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]    | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]          | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]          | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]          | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192] | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1024, 192]          | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]          | Done     | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]          | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]   | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]      | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]    | Done     | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]          | Done     | Done       | 1.0   | -1     |
| 24 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]   | Done     | Done       | 1.0   | -1     |
| 25 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]            | Done     | Done       | 1.0   | -1     |
| 26 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 768]     | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]               | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]            | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]            | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]   | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [64, 768]              | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]          | Done     | Done       | 1.0   | -1     |
| 34 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [16, 64, 192]             | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]             | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]          | Removed  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                 | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64, 64]    | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]          | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 192]    | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]             | Done     | Unknown    | N/A   | N/A    |
| 42 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]      | Done     | Unknown    | N/A   | N/A    |
| 43 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]         | Done     | Done       | 1.0   | -1     |
| 44 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]         | Done     | Done       | 1.0   | -1     |
| 45 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]             | Done     | Unknown    | N/A   | N/A    |
| 46 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]             | Done     | Unknown    | N/A   | N/A    |
| 47 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]               | Done     | Done       | 1.0   | -1     |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]           | Done     | Done       | 1.0   | -1     |
| 49 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]               | Done     | Done       | 1.0   | -1     |
| 50 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]          | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]          | Done     | Unknown    | N/A   | N/A    |
| 52 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]             | Done     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]         | Done     | Unknown    | N/A   | N/A    |
| 54 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]           | Done     | Unknown    | N/A   | N/A    |
| 55 | Tensor<[256, 384]> self = ?,<br>List[int] size = [4, 64, 384]               | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                 | Done     | Unknown    | N/A   | N/A    |
| 57 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [1, 4, 12, 64, 64]    | Done     | Unknown    | N/A   | N/A    |
| 58 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]          | Done     | Unknown    | N/A   | N/A    |
| 59 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]      | Done     | Unknown    | N/A   | N/A    |
| 60 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 384]     | Done     | Unknown    | N/A   | N/A    |
| 61 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]               | Done     | Unknown    | N/A   | N/A    |
| 62 | Tensor<[4096, 12]> self = ?,<br>List[int] size = [64, 64, -1]               | Done     | Unknown    | N/A   | N/A    |
| 63 | Tensor<[4096, 24]> self = ?,<br>List[int] size = [64, 64, -1]               | Done     | Unknown    | N/A   | N/A    |
| 64 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]             | Done     | Done       | 1.0   | -1     |
| 65 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]          | Removed  | Done       | 1.0   | -1     |
| 66 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                | Done     | Done       | 1.0   | -1     |
| 67 | Tensor<[4096, 6]> self = ?,<br>List[int] size = [64, 64, -1]                | Done     | Unknown    | N/A   | N/A    |
| 68 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]            | Done     | Done       | 1.0   | -1     |
| 69 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]               | Done     | Done       | 1.0   | -1     |
| 70 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]          | Done     | Unknown    | N/A   | N/A    |
| 71 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]          | Done     | Unknown    | N/A   | N/A    |
| 72 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]              | Done     | Unknown    | N/A   | N/A    |
| 73 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [1, 64, 3, 64, 64]    | Done     | Done       | 1.0   | -1     |
| 74 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]         | Done     | Done       | 1.0   | -1     |
| 75 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]            | Done     | Unknown    | N/A   | N/A    |
| 76 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]      | Done     | Done       | 1.0   | -1     |
| 77 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]      | Done     | Done       | 1.0   | -1     |
| 78 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Done     | Done       | 1.0   | -1     |
| 79 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                 | Done     | Done       | 1.0   | -1     |
| 80 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 64, 768]                | Done     | Unknown    | N/A   | N/A    |
| 81 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]              | Done     | Unknown    | N/A   | N/A    |
| 82 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]          | Done     | Unknown    | N/A   | N/A    |
| 83 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]          | Done     | Unknown    | N/A   | N/A    |
### aten.zero.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[192]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[384]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[96]> self = ?   | None     | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [16, 16],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [32, 32],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [64, 64],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |

