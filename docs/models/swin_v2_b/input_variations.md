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
| 26 | aten.permute.default            |                 20 |           9 |         0 |          0 | 🚧          |    0.45 |
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
|    | ATen Input Variations                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] size = [4, 64, 512]     | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] size = [16, 64, 256]    | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256] | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 64, 32, 32]> self = ?,<br>List[int] size = [1, 64, 1024]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] size = [1, 64, 64, 128] | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] size = [64, 64, 128]    | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[16, 64, 8, 32]> self = ?,<br>List[int] size = [16, 64, 256]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [128, 32, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int] size = [128, 64, 32]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [64, 32, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int] size = [64, 64, 32]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[4, 64, 16, 32]> self = ?,<br>List[int] size = [4, 64, 512]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [256, 32, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int] size = [256, 64, 32]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[64, 64, 4, 32]> self = ?,<br>List[int] size = [64, 64, 128]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[64, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[4096, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1536]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 1536]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[2048]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[256]> self = ?,<br>Tensor<[1024, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[256]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[3072]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[384]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 384]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[4096]> self = ?,<br>Tensor<[64, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[512]> self = ?,<br>Tensor<[225, 2]> mat1 = ?,<br>Tensor<[2, 512]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[256, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[512]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[512]> self = ?,<br>Tensor<[4096, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[768]> self = ?,<br>Tensor<[1024, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.as_strided.default
|    | ATen Input Variations                                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 1, 1],<br>List[int] stride = [1024, 1, 1024, 1024] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 16, 16, 256]>, <[1, 16, 16, 256]>, <[1, 16, 16, 256]>, <[1, 16, 16, 256]>],<br>int dim = -1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[1, 32, 32, 128]>, <[1, 32, 32, 128]>, <[1, 32, 32, 128]>, <[1, 32, 32, 128]>],<br>int dim = -1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[Tensor] tensors = [<[1, 8, 8, 512]>, <[1, 8, 8, 512]>, <[1, 8, 8, 512]>, <[1, 8, 8, 512]>],<br>int dim = -1         | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clamp.default
|    | ATen Input Variations                                                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[32, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[8, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 32, 64, 1]> self = ?,<br>number min = 1e-12 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 8, 64, 1]> self = ?,<br>number min = 1e-12 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 16, 64, 1]> self = ?,<br>number min = 1e-12 | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[64, 4, 64, 1]> self = ?,<br>number min = 1e-12 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 2048]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 16, 512]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 32, 32, 1024]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 32, 32, 256]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 32, 64, 64]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 64, 1024]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 64, 64, 128]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 64, 64, 512]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 8, 8, 1024]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 8, 8, 4096]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[16, 64, 256]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[16, 8, 64, 64]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[4, 16, 64, 64]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[4, 64, 512]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[64, 4, 64, 64]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[64, 64, 128]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[128, 3, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.exp.default
|    | ATen Input Variations       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 1, 1]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[32, 1, 1]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 1, 1]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[8, 1, 1]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [1, 32, 32, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int] size = [1, 32, 64, 32]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [16, 8, 32, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int] size = [16, 8, 64, 32]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [4, 16, 32, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int] size = [4, 16, 64, 32]  | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [64, 4, 32, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int] size = [64, 4, 64, 32]  | None     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 2048]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 32, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 64, 64, 512]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 8, 4096]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.index.Tensor
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[225, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[225, 32]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>] | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[225, 4]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[225, 8]> self = ?,<br>List[Optional[Tensor]] indices = [<[4096]>]  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 8, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 16, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[64, 4, 64, 32]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = -100.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = -100.0   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = 0.0      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = 0.0    | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 16]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 32]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 8]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[64, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?  | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 32, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 64, 64, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 8, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.ne.Scalar
|    | ATen Input Variations                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.new_zeros.default
|    | ATen Input Variations                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [32, 32],<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [16, 16],<br>Optional[bool] pin_memory = False  | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [64, 64],<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5] | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 64, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[16, 64, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[4, 64, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[64, 64, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]       | None     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[64, 64, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[64, 64, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[64, 64, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.relu.default
|    | ATen Input Variations             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 15, 15, 512]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.roll.default
|    | ATen Input Variations                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] shifts = [-4, -4],<br>List[int] dims = [1, 2] | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] shifts = [4, 4],<br>List[int] dims = [1, 2]   | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 64, 64]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 64, 64]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 4, 64, 64]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 64, 64]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 8, 16, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 8, 16, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 8, 8, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1024, 2048]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1024, 256]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1024, 4096]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[128, 128]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[128, 512]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1536, 512]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[16, 512]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[2048, 512]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[256, 1024]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[256, 256]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[256, 512]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[3072, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[32, 512]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[384, 128]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[4, 512]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[4096, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[512, 1024]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[512, 128]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[512, 2048]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[512, 2]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[512, 512]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[768, 256]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[8, 512]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 0    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 1    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[16, 64]> self = ?,<br>int dim = 1        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[16, 64]> self = ?,<br>int dim = 2        | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[32, 64, 64]> self = ?,<br>int dim = 0    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[4, 1, 64, 64]> self = ?,<br>int dim = 0  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 0     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[4, 64]> self = ?,<br>int dim = 1         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[4, 64]> self = ?,<br>int dim = 2         | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[64, 1, 64, 64]> self = ?,<br>int dim = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[64, 64, 64]> self = ?,<br>int dim = 1    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[64, 64]> self = ?,<br>int dim = 1        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[64, 64]> self = ?,<br>int dim = 2        | None     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[8, 64, 64]> self = ?,<br>int dim = 0     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int] size = [-1, 16]              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]               | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int] size = [-1, 32]              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int] size = [-1, 4]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int] size = [-1, 8]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int] size = [256, 1024]         | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int] size = [256, 2048]         | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 512] | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [256, 512]           | None     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int] size = [-1, 8, 64, 64]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int] size = [1024, 1024]        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 256] | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1024, 256]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int] size = [1024, 512]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [32, 32, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [32, 64, 32]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [32, 64, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int] size = [-1, 16, 64, 64]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 1024]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [64, 1024]              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 64, 3072]> self = ?,<br>List[int] size = [1, 64, 3, 32, 32]      | None     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int] size = [-1, 4, 64, 64]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128] | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int] size = [4096, 512]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 1024] | Done     | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [64, 1024]            | None     | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int] size = [64, 2048]            | None     | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int] size = [64, 4096]            | None     | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[1024, 1024]> self = ?,<br>List[int] size = [1, 32, 32, 1024]        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [16, 64, 256]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [16, 64, 768]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[128, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[128, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 256]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1024, 256]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[16, 64, 768]> self = ?,<br>List[int] size = [16, 64, 3, 8, 32]      | None     | N/A                 | N/A          | N/A               | N/A                |
| 43 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [1, 16, 8, 64, 64]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 44 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [128, 64, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 45 | Tensor<[225, 16]> self = ?,<br>List[int] size = [1, 15, 15, 16]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 46 | Tensor<[225, 32]> self = ?,<br>List[int] size = [1, 15, 15, 32]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 47 | Tensor<[225, 4]> self = ?,<br>List[int] size = [1, 15, 15, 4]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 48 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 49 | Tensor<[225, 8]> self = ?,<br>List[int] size = [1, 15, 15, 8]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 50 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [4, 64, 1536]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 51 | Tensor<[256, 2048]> self = ?,<br>List[int] size = [1, 16, 16, 2048]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 52 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 53 | Tensor<[256, 512]> self = ?,<br>List[int] size = [4, 64, 512]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 54 | Tensor<[256, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 55 | Tensor<[256, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 56 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 57 | Tensor<[32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 58 | Tensor<[32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 59 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [1, 4, 16, 64, 64]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 60 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [64, 64, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 61 | Tensor<[4, 64, 1536]> self = ?,<br>List[int] size = [4, 64, 3, 16, 32]      | None     | N/A                 | N/A          | N/A               | N/A                |
| 62 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 512]     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 63 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [256, 512]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 64 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [1, 64, 64, 128]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 65 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [64, 64, 128]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 66 | Tensor<[4096, 16]> self = ?,<br>List[int] size = [64, 64, -1]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 67 | Tensor<[4096, 32]> self = ?,<br>List[int] size = [64, 64, -1]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 68 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [64, 64, 384]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 69 | Tensor<[4096, 4]> self = ?,<br>List[int] size = [64, 64, -1]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 70 | Tensor<[4096, 512]> self = ?,<br>List[int] size = [1, 64, 64, 512]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 71 | Tensor<[4096, 8]> self = ?,<br>List[int] size = [64, 64, -1]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 72 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 73 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 74 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 64, 3072]              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 75 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4, 64, 64]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 76 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [256, 64, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 77 | Tensor<[64, 4096]> self = ?,<br>List[int] size = [1, 8, 8, 4096]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 78 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 79 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 80 | Tensor<[64, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 81 | Tensor<[64, 64, 384]> self = ?,<br>List[int] size = [64, 64, 3, 4, 32]      | None     | N/A                 | N/A          | N/A               | N/A                |
| 82 | Tensor<[64, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 83 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                 | Done     | N/A                 | N/A          | N/A               | N/A                |

