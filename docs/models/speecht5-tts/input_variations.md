# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._softmax.default                             |                 10 |           1 |         0 |          0 | 🚧          |    0.1  |
|  2 | aten._to_copy.default                             |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten._unsafe_view.default                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  4 | aten.add.Tensor                                   |                 12 |           4 |         0 |          0 | 🚧          |    0.33 |
|  5 | aten.addmm.default                                |                 14 |           3 |         0 |          0 | 🚧          |    0.21 |
|  6 | aten.arange.start                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.bernoulli.p                                  |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.bmm.default                                  |                 21 |           3 |         0 |          0 | 🚧          |    0.14 |
|  9 | aten.cat.default                                  |                  9 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.clamp_min.default                            |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.clone.default                                |                 19 |           5 |         0 |          0 | 🚧          |    0.26 |
| 12 | aten.convolution.default                          |                 45 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.div.Tensor                                   |                  8 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.embedding.default                            |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.eq.Scalar                                    |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.expand.default                               |                  7 |           1 |         0 |          0 | 🚧          |    0.14 |
| 17 | aten.gelu.default                                 |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 18 | aten.leaky_relu.default                           |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.linalg_vector_norm.default                   |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.masked_fill.Scalar                           |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 21 | aten.mul.Tensor                                   |                  7 |           2 |         0 |          0 | 🚧          |    0.29 |
| 22 | aten.native_layer_norm.default                    |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 23 | aten.relu.default                                 |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.repeat.default                               |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.rsub.Scalar                                  |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 26 | aten.scalar_tensor.default                        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.select.int                                   |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.slice.Tensor                                 |                  9 |           1 |         0 |          0 | 🚧          |    0.11 |
| 29 | aten.squeeze.dim                                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.sub.Tensor                                   |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 31 | aten.sym_size.int                                 |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 32 | aten.t.default                                    |                  7 |           3 |         0 |          0 | 🚧          |    0.43 |
| 33 | aten.tanh.default                                 |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 34 | aten.transpose.int                                |                 20 |           6 |         0 |          0 | 🚧          |    0.3  |
| 35 | aten.unsqueeze.default                            |                  8 |           3 |         0 |          0 | 🚧          |    0.38 |
| 36 | aten.view.default                                 |                 43 |          15 |         0 |          0 | 🚧          |    0.35 |
| 37 | aten.where.self                                   |                  2 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 100]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 80, 100]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._softmax.default
|    | ATen Input Variations                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[12, 1, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[12, 1, s2 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[12, 1, s4 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[12, 1, s6 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[12, 1, s8 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bool      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.bool     | None     | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int] size = [1, 24, 768] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 100, 80]> self = ?,<br>Tensor<[1, 100, 80]> other = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 128, 1600]> self = ?,<br>Tensor<[1, 128, 1600]> other = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 400]> self = ?,<br>Tensor<[1, 256, 400]> other = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 32, 25600]> self = ?,<br>Tensor<[1, 32, 25600]> other = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 64, 6400]> self = ?,<br>Tensor<[1, 64, 6400]> other = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, s0, 768]> self = ?,<br>Tensor<[1, s0, 768]> other = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                      | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[256]> self = ?,<br>Tensor<[1, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[256]> self = ?,<br>Tensor<[1, 80]> mat1 = ?,<br>Tensor<[80, 256]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[s0, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[s0, 80]> mat1 = ?,<br>Tensor<[80, 256]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[3072]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[768]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[1, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[768]> self = ?,<br>Tensor<[24, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[768]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[768]> self = ?,<br>Tensor<[s0, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[768]> self = ?,<br>Tensor<[s0, 256]> mat1 = ?,<br>Tensor<[256, 768]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number start = 0,<br>number end = 24,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.bernoulli.p
|    | ATen Input Variations                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256]> self = ?,<br>float p = 0.5  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[s0, 256]> self = ?,<br>float p = 0.5 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[12, 1, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s2 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s4 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s6 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s8 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[12, 1, s2 + 1]> self = ?,<br>Tensor<[12, s2 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[12, 1, s4 + 1]> self = ?,<br>Tensor<[12, s4 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[12, 1, s6 + 1]> self = ?,<br>Tensor<[12, s6 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[12, 1, s8 + 1]> self = ?,<br>Tensor<[12, s8 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 1, 512]>],<br>int dim = -1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[1, 12, 1, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[Tensor] tensors = [<[1, 12, s0, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | List[Tensor] tensors = [<[1, 12, s2, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | List[Tensor] tensors = [<[1, 12, s4, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | List[Tensor] tensors = [<[1, 12, s6, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | List[Tensor] tensors = [<[1, 12, s8, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | List[Tensor] tensors = [<[1, s0, 768]>, <[1, s0, 512]>],<br>int dim = -1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.clamp_min.default
|    | ATen Input Variations                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?,<br>number min = 1e-12 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 24, 3072]> self = ?                                                             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 24, 768]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 100]> self = ?                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 80, 100]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, s0, 768]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[12, 1, 1]> self = ?                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[12, 1, 24]> self = ?                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[12, 1, 2]> self = ?                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[12, 1, s0 + 1]> self = ?                                                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[12, 1, s10 + 1]> self = ?                                                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[12, 1, s2 + 1]> self = ?                                                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[12, 1, s4 + 1]> self = ?                                                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[12, 1, s6 + 1]> self = ?                                                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[12, 1, s8 + 1]> self = ?                                                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[12, 24, 24]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 11]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 128, 7]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 128, 1600]> input = ?,<br>Tensor<[128, 64, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 256, 100]> input = ?,<br>Tensor<[256, 256, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 256, 100]> input = ?,<br>Tensor<[80, 256, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 128, 8]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 11]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 256, 400]> input = ?,<br>Tensor<[256, 256, 7]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[1, 32, 7]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 11]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[1, 32, 25600]> input = ?,<br>Tensor<[32, 32, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[1, 512, 100]> input = ?,<br>Tensor<[512, 256, 8]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 32, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = True,<br>List[int] output_padding = [0],<br>int groups = 1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [25],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 11]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [5],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [15],<br>List[int] dilation = [5],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[1, 64, 6400]> input = ?,<br>Tensor<[64, 64, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [9],<br>List[int] dilation = [3],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 43 | Tensor<[1, 80, 100]> input = ?,<br>Tensor<[256, 80, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [2],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 44 | Tensor<[1, 80, 100]> input = ?,<br>Tensor<[512, 80, 7]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 0.5      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 1600]> self = ?,<br>Tensor other = 3     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 400]> self = ?,<br>Tensor other = 3      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 32, 25600]> self = ?,<br>Tensor other = 3     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 6400]> self = ?,<br>Tensor other = 3      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 0.5     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[100, 80]> self = ?,<br>Tensor<[80]> other = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                        | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>number other = 1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>number other = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 1, 24]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [-1, 1, -1]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [-1, <s0>, -1]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 512]              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 24, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.leaky_relu.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 128, 1600]> self = ?,<br>number negative_slope = 0.1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 400]> self = ?,<br>number negative_slope = 0.1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 32, 25600]> self = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 32, 25600]> self = ?,<br>number negative_slope = 0.1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 512, 100]> self = ?,<br>number negative_slope = 0.1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 64, 6400]> self = ?,<br>number negative_slope = 0.1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> mask = ?,<br>number value = -3.3895313892515355e+38   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 24, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.relu.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 768]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, s0, 256]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, s0, 768]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.repeat.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.scalar_tensor.default
|    | ATen Input Variations                                                                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number s = 0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 0,<br>int index = 0  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int]<s0> end = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 24]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.squeeze.dim
|    | ATen Input Variations                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 25600]> self = ?,<br>int dim = 0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[100, 80]> self = ?,<br>Tensor<[80]> other = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.sym_size.int
|    | ATen Input Variations                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s0, 768]> self = ?,<br>int dim = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[256, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[256, 80]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[3072, 768]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768, 1280]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[768, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[768, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 25600]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 100]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 100, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 100, 80]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 25600]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 80, 100]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[12, 2, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[12, s0 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[12, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[12, s2 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[12, s4 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[12, s6 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[12, s8 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[24, 12, 24]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1    | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 24]> self = ?,<br>int dim = 1    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256]> self = ?,<br>int dim = 0   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[100, 80]> self = ?,<br>int dim = 0  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[24]> self = ?,<br>int dim = 0       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[24]> self = ?,<br>int dim = 1       | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[s0, 256]> self = ?,<br>int dim = 0  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, 1280]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [1, 256]              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1, 80]> self = ?,<br>List[int] size = [1, 80]                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 12, 1, 24]> self = ?,<br>List[int] size = [12, 1, 24]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, -1, 64]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 12, s2 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 12, s4 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 12, s6 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 12, s8 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, 24, 12, 64]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 256]> self = ?,<br>List[int] size = [1, 1, 256]              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, s0, 1280]> self = ?,<br>List[int] size = [<s0>, 1280]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, s0, 256]> self = ?,<br>List[int] size = [<s0>, 256]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, s0, 80]> self = ?,<br>List[int] size = [<s0>, 80]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[12, 1, 24]> self = ?,<br>List[int] size = [1, 12, 1, 24]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [1, 12, 24, 24]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[25600, 1]> self = ?,<br>List[int] size = [-1]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[s0, 256]> self = ?,<br>List[int] size = [1, <s0>, 256]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[s0, 768]> self = ?,<br>List[int] size = [1, <s0>, 768]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.where.self
|    | ATen Input Variations                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256]> condition = ?,<br>Tensor<[1, 1, 256]> self = ?,<br>Tensor<[]> other = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s0, 256]> condition = ?,<br>Tensor<[1, s0, 256]> self = ?,<br>Tensor<[]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |

