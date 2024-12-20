# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  1 | aten._unsafe_view.default      |                 19 |          19 |         0 |          0 | ✅          |    1    |
|  2 | aten.add.Tensor                |                 11 |           8 |         0 |          0 | 🚧          |    0.73 |
|  3 | aten.addmm.default             |                 17 |          17 |         0 |          0 | ✅          |    1    |
|  4 | aten.as_strided.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default               |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default               |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  7 | aten.clone.default             |                 39 |          39 |         0 |          0 | ✅          |    1    |
|  8 | aten.constant_pad_nd.default   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  9 | aten.convolution.default       |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.eq.Scalar                 |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 11 | aten.expand.default            |                 12 |           0 |        12 |          0 | ✅          |    1    |
| 12 | aten.gelu.default              |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 13 | aten.index.Tensor              |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.masked_fill.Scalar        |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 15 | aten.mean.dim                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.mm.default                |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 17 | aten.mul.Tensor                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 18 | aten.native_layer_norm.default |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 19 | aten.ne.Scalar                 |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 20 | aten.new_zeros.default         |                  3 |           0 |         3 |          0 | ✅          |    1    |
| 21 | aten.permute.default           |                 21 |           9 |         0 |          0 | 🚧          |    0.43 |
| 22 | aten.roll.default              |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 23 | aten.select.int                |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 24 | aten.slice.Tensor              |                 23 |           0 |        11 |          0 | 🚧          |    0.48 |
| 25 | aten.sub.Tensor                |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 26 | aten.t.default                 |                 20 |          20 |         0 |          0 | ✅          |    1    |
| 27 | aten.transpose.int             |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 28 | aten.unsqueeze.default         |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 29 | aten.view.default              |                 73 |          73 |         0 |          0 | ✅          |    1    |
| 30 | aten.zeros.default             |                  3 |           3 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999612 |      0 |
|  1 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999611 |      0 |
|  2 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999605 |      0 |
|  3 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999607 |      0 |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] size = [4, 49, 512]     | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] size = [16, 49, 256]    | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256] | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 49, 32, 32]> self = ?,<br>List[int] size = [1, 49, 1024]         | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128] | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] size = [64, 49, 128]    | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[16, 49, 8, 32]> self = ?,<br>List[int] size = [16, 49, 256]         | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [128, 32, 49]         | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [128, 49, 32]         | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int] size = [4, 49]                  | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [64, 32, 49]          | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [64, 49, 32]          | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int] size = [16, 49]                 | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[4, 49, 16, 32]> self = ?,<br>List[int] size = [4, 49, 512]          | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [256, 32, 49]         | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [256, 49, 32]         | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[64, 49, 4, 32]> self = ?,<br>List[int] size = [64, 49, 128]         | Done     | Done       |     1 |     -1 |
| 18 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int] size = [64, 49]                 | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ? | None     | Fallback   | 1        |     -1 |
|  2 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?       | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?  | None     | Fallback   | 1        |     -1 |
|  5 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ? | None     | Fallback   | 1        |     -1 |
|  7 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?       | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?        | Done     | Done       | 0.999998 |      0 |
|  9 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 10 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?        | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Done     | Done       | 0.999967 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[49, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999965 |      0 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[49, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999934 |      0 |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[784, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ?  | Done     | Done       | 0.999978 |      0 |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     | Done       | 0.999979 |      0 |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[3136, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     | Done       | 0.99997  |      0 |
|  6 | Tensor<[1536]> self = ?,<br>Tensor<[196, 512]> mat1 = ?,<br>Tensor<[512, 1536]> mat2 = ?  | Done     | Done       | 0.99997  |      0 |
|  7 | Tensor<[2048]> self = ?,<br>Tensor<[196, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     | Done       | 0.99997  |      0 |
|  8 | Tensor<[256]> self = ?,<br>Tensor<[784, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ?  | Done     | Done       | 0.999964 |      0 |
|  9 | Tensor<[256]> self = ?,<br>Tensor<[784, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?    | Done     | Done       | 0.999974 |      0 |
| 10 | Tensor<[3072]> self = ?,<br>Tensor<[49, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
| 11 | Tensor<[384]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ?   | Done     | Done       | 0.999979 |      0 |
| 12 | Tensor<[4096]> self = ?,<br>Tensor<[49, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
| 13 | Tensor<[512]> self = ?,<br>Tensor<[196, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     | Done       | 0.999605 |      0 |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[196, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | Done       | 0.999928 |      0 |
| 15 | Tensor<[512]> self = ?,<br>Tensor<[3136, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     | Done       | 0.999979 |      0 |
| 16 | Tensor<[768]> self = ?,<br>Tensor<[784, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?    | Done     | Done       | 0.999978 |      0 |
### aten.as_strided.default
|    | ATen Input Variations                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 1, 1],<br>List[int] stride = [1024, 1, 1024, 1024] | None     | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ? | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ? | Done     | Done       | 0.999988 |      0 |
|  2 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ? | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ? | Done     | Done       | 0.999988 |      0 |
|  4 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?   | Done     | Done       | 0.999991 |      0 |
|  5 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?   | Done     | Done       | 0.999988 |      0 |
|  6 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?   | Done     | Done       | 0.999991 |      0 |
|  7 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?   | Done     | Done       | 0.999988 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 14, 14, 256]>, <[1, 14, 14, 256]>, <[1, 14, 14, 256]>, <[1, 14, 14, 256]>],<br>int dim = -1 | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 28, 28, 128]>, <[1, 28, 28, 128]>, <[1, 28, 28, 128]>, <[1, 28, 28, 128]>],<br>int dim = -1 | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[1, 7, 7, 512]>, <[1, 7, 7, 512]>, <[1, 7, 7, 512]>, <[1, 7, 7, 512]>],<br>int dim = -1         | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 14, 14, 2048]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 14, 14, 512]> self = ?                                                               | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 28, 28, 1024]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 28, 28, 256]> self = ?                                                               | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 32, 49, 49]> self = ?                                                                | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 49, 1024]> self = ?                                                                  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 56, 56, 128]> self = ?                                                               | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 56, 56, 512]> self = ?                                                               | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 7, 7, 1024]> self = ?                                                                | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 7, 7, 4096]> self = ?                                                                | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
| 17 | Tensor<[16, 49, 256]> self = ?                                                                  | Done     | Done       |     1 |      0 |
| 18 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       |     1 |      0 |
| 19 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 20 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 21 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 22 | Tensor<[16, 8, 49, 49]> self = ?                                                                | Done     | Done       |     1 |      0 |
| 23 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       |     1 |      0 |
| 24 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       |     1 |      0 |
| 25 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 26 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 27 | Tensor<[4, 16, 49, 49]> self = ?                                                                | Done     | Done       |     1 |      0 |
| 28 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       |     1 |      0 |
| 29 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 30 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       |     1 |      0 |
| 31 | Tensor<[4, 49, 512]> self = ?                                                                   | Done     | Done       |     1 |      0 |
| 32 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 33 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 34 | Tensor<[64, 4, 49, 49]> self = ?                                                                | Done     | Done       |     1 |      0 |
| 35 | Tensor<[64, 49, 128]> self = ?                                                                  | Done     | Done       |     1 |      0 |
| 36 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
| 37 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       |     1 |      0 |
| 38 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       |     1 |      0 |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999967 |      6 |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [1, 32, 32, 49] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49] | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [16, 8, 32, 49] | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32] | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49] | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [4, 16, 32, 49] | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32] | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49] | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [64, 4, 32, 49] | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32] | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49] | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 14, 14, 2048]> self = ? | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 28, 28, 1024]> self = ? | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 56, 56, 512]> self = ?  | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 7, 7, 4096]> self = ?   | Done     | Done       | 0.999991 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[169, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>] | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[169, 32]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>] | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[169, 4]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>]  | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[169, 8]> self = ?,<br>List[Optional[Tensor]] indices = [<[2401]>]  | None     | Fallback   |     1 |     -1 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = -100.0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = -100.0   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = 0.0      | Done     | Done       |     1 |      0 |
|  4 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0 | Done     | Done       |     1 |      0 |
|  5 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = 0.0    | Done     | Done       |     1 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |      0 |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[196, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     | Done       | 0.99984  |      0 |
|  1 | Tensor<[49, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ? | Done     | Done       | 0.999956 |      0 |
|  2 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?   | Done     | Done       | 0.999971 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369 | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                           | Status   | Isolated   | PCC   |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 14, 14, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
|  1 | Tensor<[1, 14, 14, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |      1 |
|  2 | Tensor<[1, 28, 28, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |      1 |
|  3 | Tensor<[1, 28, 28, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |      1 |
|  4 | Tensor<[1, 56, 56, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |      1 |
|  5 | Tensor<[1, 7, 7, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |      1 |
|  6 | Tensor<[1, 7, 7, 2048]> input = ?,<br>List[int] normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float eps = 1e-05   | Done     | Done       | N/A   |      1 |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [28, 28],<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [14, 14],<br>Optional[bool] pin_memory = False  | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [56, 56],<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 49, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   |     1 |     -1 |
| 10 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   |     1 |     -1 |
| 11 | Tensor<[16, 49, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | Fallback   |     1 |     -1 |
| 12 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                | Done     | Done       |     1 |      0 |
| 13 | Tensor<[4, 49, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | Fallback   |     1 |     -1 |
| 14 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                | Done     | Done       |     1 |      0 |
| 15 | Tensor<[49, 49, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       |     1 |      0 |
| 16 | Tensor<[49, 49, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       |     1 |      0 |
| 17 | Tensor<[49, 49, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       |     1 |      0 |
| 18 | Tensor<[49, 49, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       |     1 |      0 |
| 19 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | Fallback   |     1 |     -1 |
| 20 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                | Done     | Done       |     1 |      0 |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] shifts = [-3, -3],<br>List[int] dims = [1, 2] | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] shifts = [3, 3],<br>List[int] dims = [1, 2]   | Done     | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |      0 |
|  3 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |      0 |
|  4 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |      0 |
|  5 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |      0 |
|  6 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |      0 |
|  7 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |      0 |
|  8 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |      0 |
|  9 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |      0 |
| 10 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |      0 |
| 11 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 14, 14, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 28, 28, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
| 10 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
| 11 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
| 13 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
| 14 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
| 15 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
| 16 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   |     1 |     -1 |
| 17 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Done       |     1 |     -1 |
| 18 | Tensor<[1, 7, 14, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   |     1 |     -1 |
| 19 | Tensor<[1, 7, 14, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   |     1 |     -1 |
| 20 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Done       |     1 |     -1 |
| 21 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Done       |     1 |     -1 |
| 22 | Tensor<[1, 7, 7, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Done       |     1 |     -1 |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ? | Done     | Done       | 0.474555 |      0 |
|  1 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?   | Done     | Done       | 0.496205 |      0 |
|  2 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | Done     | Done       | 0.355771 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1024, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1024, 2048]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1024, 256]> self = ?  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1024, 4096]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[128, 128]> self = ?   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[128, 512]> self = ?   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1536, 512]> self = ?  | Done     | Done       |     1 |      0 |
|  8 | Tensor<[2048, 512]> self = ?  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[256, 1024]> self = ?  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[256, 256]> self = ?   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[256, 512]> self = ?   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[3072, 1024]> self = ? | Done     | Done       |     1 |      0 |
| 13 | Tensor<[384, 128]> self = ?   | Done     | Done       |     1 |      0 |
| 14 | Tensor<[4096, 1024]> self = ? | Done     | Done       |     1 |      0 |
| 15 | Tensor<[512, 1024]> self = ?  | Done     | Done       |     1 |      0 |
| 16 | Tensor<[512, 128]> self = ?   | Done     | Done       |     1 |      0 |
| 17 | Tensor<[512, 2048]> self = ?  | Done     | Done       |     1 |      0 |
| 18 | Tensor<[512, 512]> self = ?   | Done     | Done       |     1 |      0 |
| 19 | Tensor<[768, 256]> self = ?   | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |      0 |
|  3 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |      0 |
|  5 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       |     1 |      0 |
|  7 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 1, 49, 49]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[16, 49]> self = ?,<br>int dim = 1        | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[16, 49]> self = ?,<br>int dim = 2        | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[32, 49, 49]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[4, 1, 49, 49]> self = ?,<br>int dim = 0  | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 0     | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 1     | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[4, 49]> self = ?,<br>int dim = 1         | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[4, 49]> self = ?,<br>int dim = 2         | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[64, 1, 49, 49]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[64, 49, 49]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[64, 49]> self = ?,<br>int dim = 1        | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[64, 49]> self = ?,<br>int dim = 2        | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[8, 49, 49]> self = ?,<br>int dim = 0     | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]             | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int] size = [196, 1024]         | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int] size = [196, 2048]         | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 512] | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [196, 512]           | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int] size = [-1, 8, 49, 49]    | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int] size = [784, 1024]         | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 256] | Done     | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [784, 256]           | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int] size = [784, 512]           | Done     | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [32, 32, 49]          | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [32, 49, 32]          | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [32, 49, 49]          | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int] size = [-1, 16, 49, 49]   | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 1024]   | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [49, 1024]              | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 49, 3072]> self = ?,<br>List[int] size = [1, 49, 3, 32, 32]      | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 128] | Done     | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [3136, 128]          | Done     | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int] size = [3136, 512]          | Done     | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int] size = [-1, 4, 49, 49]    | Done     | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 1024] | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [49, 1024]            | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int] size = [49, 2048]            | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int] size = [49, 4096]            | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[128, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]         | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[128, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]         | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                 | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 256]    | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [784, 256]              | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[16, 49, 768]> self = ?,<br>List[int] size = [16, 49, 3, 8, 32]      | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [1, 16, 8, 49, 49]    | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [128, 49, 49]         | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [4, 49, 1536]             | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[196, 2048]> self = ?,<br>List[int] size = [1, 14, 14, 2048]         | Done     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[196, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]           | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[196, 512]> self = ?,<br>List[int] size = [4, 49, 512]               | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[2401, 16]> self = ?,<br>List[int] size = [49, 49, -1]               | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[2401, 32]> self = ?,<br>List[int] size = [49, 49, -1]               | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[2401, 4]> self = ?,<br>List[int] size = [49, 49, -1]                | Done     | Done       | 1.0   | -1     |
| 42 | Tensor<[2401, 8]> self = ?,<br>List[int] size = [49, 49, -1]                | Done     | Done       | 1.0   | -1     |
| 43 | Tensor<[256, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]         | Done     | Done       | 1.0   | -1     |
| 44 | Tensor<[256, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]         | Done     | Done       | 1.0   | -1     |
| 45 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                 | Done     | Unknown    | N/A   | N/A    |
| 46 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128]          | Done     | Done       | 1.0   | -1     |
| 47 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [64, 49, 128]             | Done     | Done       | 1.0   | -1     |
| 48 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [64, 49, 384]             | Done     | Done       | 1.0   | -1     |
| 49 | Tensor<[3136, 512]> self = ?,<br>List[int] size = [1, 56, 56, 512]          | Done     | Done       | 1.0   | -1     |
| 50 | Tensor<[32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]          | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]          | Done     | Unknown    | N/A   | N/A    |
| 52 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [1, 4, 16, 49, 49]    | Done     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [64, 49, 49]          | Done     | Unknown    | N/A   | N/A    |
| 54 | Tensor<[4, 49, 1536]> self = ?,<br>List[int] size = [4, 49, 3, 16, 32]      | Done     | Unknown    | N/A   | N/A    |
| 55 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 512]     | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [196, 512]               | Done     | Unknown    | N/A   | N/A    |
| 57 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]              | Done     | Unknown    | N/A   | N/A    |
| 58 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]            | Done     | Unknown    | N/A   | N/A    |
| 59 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 49, 3072]              | Done     | Unknown    | N/A   | N/A    |
| 60 | Tensor<[49, 4096]> self = ?,<br>List[int] size = [1, 7, 7, 4096]            | Done     | Unknown    | N/A   | N/A    |
| 61 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                 | Done     | Done       | 1.0   | -1     |
| 62 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [1, 64, 4, 49, 49]    | Done     | Done       | 1.0   | -1     |
| 63 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [256, 49, 49]         | Done     | Done       | 1.0   | -1     |
| 64 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 128]    | Done     | Done       | 1.0   | -1     |
| 65 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [3136, 128]             | Done     | Done       | 1.0   | -1     |
| 66 | Tensor<[64, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]          | Done     | Unknown    | N/A   | N/A    |
| 67 | Tensor<[64, 49, 384]> self = ?,<br>List[int] size = [64, 49, 3, 4, 32]      | Done     | Done       | 1.0   | -1     |
| 68 | Tensor<[64, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]          | Done     | Unknown    | N/A   | N/A    |
| 69 | Tensor<[784, 1024]> self = ?,<br>List[int] size = [1, 28, 28, 1024]         | Done     | Unknown    | N/A   | N/A    |
| 70 | Tensor<[784, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]           | Done     | Done       | 1.0   | -1     |
| 71 | Tensor<[784, 256]> self = ?,<br>List[int] size = [16, 49, 256]              | Done     | Unknown    | N/A   | N/A    |
| 72 | Tensor<[784, 768]> self = ?,<br>List[int] size = [16, 49, 768]              | Done     | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [14, 14],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [28, 28],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [56, 56],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |

