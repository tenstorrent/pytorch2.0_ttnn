# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |           0 |
|  1 | aten._softmax.default                             |                  4 |           4 |
|  2 | aten._to_copy.default                             |                  2 |           0 |
|  3 | aten._unsafe_view.default                         |                  5 |           0 |
|  4 | aten.add.Tensor                                   |                 26 |          26 |
|  5 | aten.addmm.default                                |                 29 |          29 |
|  6 | aten.bmm.default                                  |                 10 |          10 |
|  7 | aten.clone.default                                |                 19 |          14 |
|  8 | aten.convolution.default                          |                 30 |           0 |
|  9 | aten.div.Tensor                                   |                  5 |           5 |
| 10 | aten.embedding.default                            |                  6 |           6 |
| 11 | aten.expand.default                               |                 14 |           0 |
| 12 | aten.hardtanh.default                             |                 12 |           0 |
| 13 | aten.mean.dim                                     |                  1 |           1 |
| 14 | aten.mul.Tensor                                   |                 26 |          26 |
| 15 | aten.native_layer_norm.default                    |                  7 |           7 |
| 16 | aten.permute.default                              |                  5 |           5 |
| 17 | aten.pow.Tensor_Scalar                            |                  6 |           6 |
| 18 | aten.rsub.Scalar                                  |                  2 |           2 |
| 19 | aten.select.int                                   |                  1 |           0 |
| 20 | aten.slice.Tensor                                 |                  4 |           0 |
| 21 | aten.split.Tensor                                 |                  1 |           0 |
| 22 | aten.squeeze.dim                                  |                  1 |           0 |
| 23 | aten.t.default                                    |                 23 |          23 |
| 24 | aten.tanh.default                                 |                  7 |           7 |
| 25 | aten.transpose.int                                |                 10 |          10 |
| 26 | aten.unsqueeze.default                            |                  4 |           4 |
| 27 | aten.view.default                                 |                 52 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>Tensor<[1280]> running_mean = ?,<br>Tensor<[1280]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 144, 28, 28]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  2 | Tensor<[1, 144, 56, 56]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  3 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | Unknown  |
|  4 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  5 | Tensor<[1, 192, 14, 14]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  6 | Tensor<[1, 192, 28, 28]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  7 | Tensor<[1, 24, 56, 56]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
|  8 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | Unknown  |
|  9 | Tensor<[1, 32, 28, 28]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
| 10 | Tensor<[1, 320, 7, 7]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
| 11 | Tensor<[1, 384, 14, 14]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
| 12 | Tensor<[1, 576, 14, 14]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
| 13 | Tensor<[1, 576, 7, 7]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
| 14 | Tensor<[1, 64, 14, 14]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
| 15 | Tensor<[1, 96, 112, 112]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | Unknown  |
| 16 | Tensor<[1, 96, 14, 14]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
| 17 | Tensor<[1, 96, 56, 56]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
| 18 | Tensor<[1, 960, 7, 7]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 14]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[1, 12, 9, 9]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False   | Done     |
|  2 | Tensor<[1, 16, 9, 9]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False   | Done     |
|  3 | Tensor<[1, 64, 9, 9]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False   | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 14]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
|  1 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int]<> dtype = torch.float32  | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int]<> size = [1, 14, 768] | Unknown  |
|  1 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int]<> size = [1, 9, 768]   | Unknown  |
|  2 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int]<> size = [1, 9, 2048] | Unknown  |
|  3 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int]<> size = [1, 9, 1024]  | Unknown  |
|  4 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int]<> size = [1, 9, 4096]  | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?   | Done     |
|  1 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Done     |
|  2 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?       | Done     |
|  3 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 1.0                | Done     |
|  4 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?     | Done     |
|  5 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?       | Done     |
|  6 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Done     |
|  7 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?   | Done     |
|  8 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ? | Done     |
|  9 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ? | Done     |
| 10 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ? | Done     |
| 11 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Done     |
| 12 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?       | Done     |
| 13 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 1.0                  | Done     |
| 14 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?         | Done     |
| 15 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 1.0                | Done     |
| 16 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?     | Done     |
| 17 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?       | Done     |
| 18 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 1.0                 | Done     |
| 19 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?       | Done     |
| 20 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 1.0                 | Done     |
| 21 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?       | Done     |
| 22 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?         | Done     |
| 23 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 1.0                 | Done     |
| 24 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?       | Done     |
| 25 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ?   | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Done     |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 1024]> mat2 = ?     | Done     |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Done     |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 128]> mat2 = ?     | Done     |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[9, 2048]> mat1 = ?,<br>Tensor<[2048, 128]> mat2 = ?     | Done     |
|  6 | Tensor<[128]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 128]> mat2 = ?     | Done     |
|  7 | Tensor<[128]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 128]> mat2 = ?       | Done     |
|  8 | Tensor<[16384]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 16384]> mat2 = ? | Done     |
|  9 | Tensor<[2048]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 2048]> mat2 = ?     | Done     |
| 10 | Tensor<[2048]> self = ?,<br>Tensor<[9, 2048]> mat1 = ?,<br>Tensor<[2048, 2048]> mat2 = ?   | Done     |
| 11 | Tensor<[2048]> self = ?,<br>Tensor<[9, 8192]> mat1 = ?,<br>Tensor<[8192, 2048]> mat2 = ?   | Done     |
| 12 | Tensor<[2]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?           | Done     |
| 13 | Tensor<[2]> self = ?,<br>Tensor<[14, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?          | Done     |
| 14 | Tensor<[30000]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 30000]> mat2 = ?   | Done     |
| 15 | Tensor<[3072]> self = ?,<br>Tensor<[14, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Done     |
| 16 | Tensor<[3072]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     |
| 17 | Tensor<[4096]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Done     |
| 18 | Tensor<[4096]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 4096]> mat2 = ?     | Done     |
| 19 | Tensor<[4096]> self = ?,<br>Tensor<[9, 16384]> mat1 = ?,<br>Tensor<[16384, 4096]> mat2 = ? | Done     |
| 20 | Tensor<[4096]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Done     |
| 21 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Done     |
| 22 | Tensor<[768]> self = ?,<br>Tensor<[14, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?      | Done     |
| 23 | Tensor<[768]> self = ?,<br>Tensor<[14, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     |
| 24 | Tensor<[768]> self = ?,<br>Tensor<[14, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Done     |
| 25 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?       | Done     |
| 26 | Tensor<[768]> self = ?,<br>Tensor<[9, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Done     |
| 27 | Tensor<[768]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Done     |
| 28 | Tensor<[8192]> self = ?,<br>Tensor<[9, 2048]> mat1 = ?,<br>Tensor<[2048, 8192]> mat2 = ?   | Done     |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ? | Done     |
|  1 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ? | Done     |
|  2 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?   | Done     |
|  3 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?    | Done     |
|  4 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ? | Done     |
|  5 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?   | Done     |
|  6 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?   | Done     |
|  7 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?    | Done     |
|  8 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?   | Done     |
|  9 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?    | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 14]> self = ?                                                             | Done     |
|  1 | Tensor<[1, 12, 9, 9]> self = ?                                                               | Done     |
|  2 | Tensor<[1, 1280]> self = ?                                                                   | Done     |
|  3 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  4 | Tensor<[1, 14, 128]> self = ?                                                                | Done     |
|  5 | Tensor<[1, 14, 768]> self = ?                                                                | Unknown  |
|  6 | Tensor<[1, 14]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
|  7 | Tensor<[1, 16, 9, 9]> self = ?                                                               | Done     |
|  8 | Tensor<[1, 64, 9, 9]> self = ?                                                               | Done     |
|  9 | Tensor<[1, 768]> self = ?                                                                    | Done     |
| 10 | Tensor<[1, 9, 1024]> self = ?                                                                | Unknown  |
| 11 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 12 | Tensor<[1, 9, 128]> self = ?                                                                 | Done     |
| 13 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
| 14 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 15 | Tensor<[1, 9, 2048]> self = ?                                                                | Unknown  |
| 16 | Tensor<[1, 9, 4096]> self = ?                                                                | Unknown  |
| 17 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format  | Done     |
| 18 | Tensor<[1, 9, 768]> self = ?                                                                 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[32, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
|  1 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 144 | Unknown  |
|  2 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 144 | Unknown  |
|  3 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[24, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
|  4 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[96, 16, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
|  5 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  6 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[64, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
|  7 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 192 | Unknown  |
|  8 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 192 | Unknown  |
|  9 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[32, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 10 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[144, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 11 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Unknown  |
| 12 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 13 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 32  | Unknown  |
| 14 | Tensor<[1, 32, 28, 28]> input = ?,<br>Tensor<[192, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 15 | Tensor<[1, 320, 7, 7]> input = ?,<br>Tensor<[1280, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 16 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[384, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 384 | Unknown  |
| 17 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[64, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 18 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[96, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 19 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 576 | Unknown  |
| 20 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 576 | Unknown  |
| 21 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[96, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 22 | Tensor<[1, 576, 7, 7]> input = ?,<br>Tensor<[160, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 23 | Tensor<[1, 64, 14, 14]> input = ?,<br>Tensor<[384, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 24 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 96  | Unknown  |
| 25 | Tensor<[1, 96, 14, 14]> input = ?,<br>Tensor<[576, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 26 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[24, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Unknown  |
| 27 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[160, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 28 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 29 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 960   | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<> other = 8.0              | Done     |
|  1 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<> other = 8.0                | Done     |
|  2 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<> other = 11.313708498984761 | Done     |
|  3 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<> other = 8.0                | Done     |
|  4 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<> other = 8.0                | Done     |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                               | Done     |
|  1 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                | Done     |
|  2 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int<> padding_idx = 0 | Done     |
|  3 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int<> padding_idx = 0  | Done     |
|  4 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                             | Done     |
|  5 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                              | Done     |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int]<> size = [1, 12, 14, 14] | Unknown  |
|  1 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int]<> size = [1, 12, 14, 64] | Unknown  |
|  2 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int]<> size = [1, 12, 64, 14] | Unknown  |
|  3 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int]<> size = [1, 12, 64, 9]   | Unknown  |
|  4 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int]<> size = [1, 12, 9, 64]   | Unknown  |
|  5 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int]<> size = [1, 12, 9, 9]     | Unknown  |
|  6 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int]<> size = [1, 16, 128, 9] | Unknown  |
|  7 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int]<> size = [1, 16, 64, 9]   | Unknown  |
|  8 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int]<> size = [1, 16, 9, 128] | Unknown  |
|  9 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int]<> size = [1, 16, 9, 64]   | Unknown  |
| 10 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int]<> size = [1, 16, 9, 9]     | Unknown  |
| 11 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int]<> size = [1, 64, 64, 9]   | Unknown  |
| 12 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int]<> size = [1, 64, 9, 64]   | Unknown  |
| 13 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int]<> size = [1, 64, 9, 9]     | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0   | Unknown  |
|  1 | Tensor<[1, 144, 28, 28]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | Unknown  |
|  2 | Tensor<[1, 144, 56, 56]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | Unknown  |
|  3 | Tensor<[1, 192, 14, 14]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | Unknown  |
|  4 | Tensor<[1, 192, 28, 28]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | Unknown  |
|  5 | Tensor<[1, 32, 112, 112]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0 | Unknown  |
|  6 | Tensor<[1, 384, 14, 14]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | Unknown  |
|  7 | Tensor<[1, 576, 14, 14]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | Unknown  |
|  8 | Tensor<[1, 576, 7, 7]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0    | Unknown  |
|  9 | Tensor<[1, 96, 112, 112]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0 | Unknown  |
| 10 | Tensor<[1, 96, 56, 56]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0   | Unknown  |
| 11 | Tensor<[1, 960, 7, 7]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0    | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Done     |
|  1 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38  | Done     |
|  2 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 0.044715                | Done     |
|  3 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 0.5                     | Done     |
|  4 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654      | Done     |
|  5 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?          | Done     |
|  6 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.044715                  | Done     |
|  7 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.5                       | Done     |
|  8 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.7978845608028654        | Done     |
|  9 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?              | Done     |
| 10 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.044715                | Done     |
| 11 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.5                     | Done     |
| 12 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.7978845608028654      | Done     |
| 13 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?          | Done     |
| 14 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 0.044715                 | Done     |
| 15 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 0.5                      | Done     |
| 16 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654       | Done     |
| 17 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?            | Done     |
| 18 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 0.044715                 | Done     |
| 19 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 0.5                      | Done     |
| 20 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 0.7978845608028654       | Done     |
| 21 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?            | Done     |
| 22 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 0.044715                 | Done     |
| 23 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 0.5                      | Done     |
| 24 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 0.7978845608028654       | Done     |
| 25 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?            | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                          | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-12    | Done     |
|  1 | Tensor<[1, 14, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12    | Done     |
|  2 | Tensor<[1, 9, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-12 | Done     |
|  3 | Tensor<[1, 9, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-12     | Done     |
|  4 | Tensor<[1, 9, 2048]> input = ?,<br>List[int]<> normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float<> eps = 1e-12 | Done     |
|  5 | Tensor<[1, 9, 4096]> input = ?,<br>List[int]<> normalized_shape = [4096],<br>Optional[Tensor]<[4096]> weight = ?,<br>Optional[Tensor]<[4096]> bias = ?,<br>float<> eps = 1e-12 | Done     |
|  6 | Tensor<[1, 9, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12     | Done     |
### aten.permute.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
|  2 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  3 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
|  4 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3]  | Done     |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 3072]> self = ?,<br>number<> exponent = 3.0 | Done     |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>number<> exponent = 3.0   | Done     |
|  2 | Tensor<[1, 9, 16384]> self = ?,<br>number<> exponent = 3.0 | Done     |
|  3 | Tensor<[1, 9, 3072]> self = ?,<br>number<> exponent = 3.0  | Done     |
|  4 | Tensor<[1, 9, 4096]> self = ?,<br>number<> exponent = 3.0  | Done     |
|  5 | Tensor<[1, 9, 8192]> self = ?,<br>number<> exponent = 3.0  | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 14]> self = ?,<br>number<> other = 1.0 | Done     |
|  1 | Tensor<[1, 1, 1, 9]> self = ?,<br>number<> other = 1.0  | Done     |
### aten.select.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 768]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1    | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 14    | Unknown  |
|  2 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9     | Unknown  |
|  3 | Tensor<[1, 9, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 2]> self = ?,<br>int<> split_size = 1,<br>int<> dim = -1 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 1]> self = ?,<br>int<> dim = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ?  | Done     |
|  1 | Tensor<[1024, 1024]> self = ?  | Done     |
|  2 | Tensor<[1024, 128]> self = ?   | Done     |
|  3 | Tensor<[1024, 4096]> self = ?  | Done     |
|  4 | Tensor<[128, 1024]> self = ?   | Done     |
|  5 | Tensor<[128, 2048]> self = ?   | Done     |
|  6 | Tensor<[128, 4096]> self = ?   | Done     |
|  7 | Tensor<[128, 768]> self = ?    | Done     |
|  8 | Tensor<[16384, 4096]> self = ? | Done     |
|  9 | Tensor<[2, 768]> self = ?      | Done     |
| 10 | Tensor<[2048, 128]> self = ?   | Done     |
| 11 | Tensor<[2048, 2048]> self = ?  | Done     |
| 12 | Tensor<[2048, 8192]> self = ?  | Done     |
| 13 | Tensor<[30000, 128]> self = ?  | Done     |
| 14 | Tensor<[3072, 768]> self = ?   | Done     |
| 15 | Tensor<[4096, 1024]> self = ?  | Done     |
| 16 | Tensor<[4096, 128]> self = ?   | Done     |
| 17 | Tensor<[4096, 16384]> self = ? | Done     |
| 18 | Tensor<[4096, 4096]> self = ?  | Done     |
| 19 | Tensor<[768, 128]> self = ?    | Done     |
| 20 | Tensor<[768, 3072]> self = ?   | Done     |
| 21 | Tensor<[768, 768]> self = ?    | Done     |
| 22 | Tensor<[8192, 2048]> self = ?  | Done     |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 14, 3072]> self = ? | Done     |
|  1 | Tensor<[1, 768]> self = ?      | Done     |
|  2 | Tensor<[1, 9, 128]> self = ?   | Done     |
|  3 | Tensor<[1, 9, 16384]> self = ? | Done     |
|  4 | Tensor<[1, 9, 3072]> self = ?  | Done     |
|  5 | Tensor<[1, 9, 4096]> self = ?  | Done     |
|  6 | Tensor<[1, 9, 8192]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  1 | Tensor<[1, 12, 14, 64]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1   | Done     |
|  2 | Tensor<[1, 12, 9, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2  | Done     |
|  3 | Tensor<[1, 12, 9, 64]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1    | Done     |
|  4 | Tensor<[1, 16, 9, 128]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  5 | Tensor<[1, 16, 9, 128]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1   | Done     |
|  6 | Tensor<[1, 16, 9, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2  | Done     |
|  7 | Tensor<[1, 16, 9, 64]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1    | Done     |
|  8 | Tensor<[1, 64, 9, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2  | Done     |
|  9 | Tensor<[1, 64, 9, 64]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1    | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 14]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 1, 9]> self = ?,<br>int<> dim = 2  | Done     |
|  2 | Tensor<[1, 14]> self = ?,<br>int<> dim = 1    | Done     |
|  3 | Tensor<[1, 9]> self = ?,<br>int<> dim = 1     | Done     |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int]<> size = [12, 14, 14] | Unknown  |
|  1 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int]<> size = [12, 14, 64] | Unknown  |
|  2 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int]<> size = [12, 64, 14] | Unknown  |
|  3 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int]<> size = [12, 64, 9]   | Unknown  |
|  4 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int]<> size = [12, 9, 64]   | Unknown  |
|  5 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int]<> size = [12, 9, 9]     | Unknown  |
|  6 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int]<> size = [1, 1280]    | Unknown  |
|  7 | Tensor<[1, 14, 128]> self = ?,<br>List[int]<> size = [14, 128]       | Unknown  |
|  8 | Tensor<[1, 14, 3072]> self = ?,<br>List[int]<> size = [14, 3072]     | Unknown  |
|  9 | Tensor<[1, 14, 768]> self = ?,<br>List[int]<> size = [1, 14, 12, 64] | Unknown  |
| 10 | Tensor<[1, 14, 768]> self = ?,<br>List[int]<> size = [14, 768]       | Unknown  |
| 11 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int]<> size = [16, 128, 9] | Unknown  |
| 12 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int]<> size = [16, 64, 9]   | Unknown  |
| 13 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int]<> size = [16, 9, 128] | Unknown  |
| 14 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int]<> size = [16, 9, 64]   | Unknown  |
| 15 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int]<> size = [16, 9, 9]     | Unknown  |
| 16 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int]<> size = [64, 64, 9]   | Unknown  |
| 17 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int]<> size = [64, 9, 64]   | Unknown  |
| 18 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int]<> size = [64, 9, 9]     | Unknown  |
| 19 | Tensor<[1, 9, 1024]> self = ?,<br>List[int]<> size = [1, 9, 16, 64]  | Unknown  |
| 20 | Tensor<[1, 9, 1024]> self = ?,<br>List[int]<> size = [9, 1024]       | Unknown  |
| 21 | Tensor<[1, 9, 128]> self = ?,<br>List[int]<> size = [9, 128]         | Unknown  |
| 22 | Tensor<[1, 9, 16384]> self = ?,<br>List[int]<> size = [9, 16384]     | Unknown  |
| 23 | Tensor<[1, 9, 2048]> self = ?,<br>List[int]<> size = [1, 9, 16, 128] | Unknown  |
| 24 | Tensor<[1, 9, 2048]> self = ?,<br>List[int]<> size = [9, 2048]       | Unknown  |
| 25 | Tensor<[1, 9, 3072]> self = ?,<br>List[int]<> size = [9, 3072]       | Unknown  |
| 26 | Tensor<[1, 9, 4096]> self = ?,<br>List[int]<> size = [1, 9, 64, 64]  | Unknown  |
| 27 | Tensor<[1, 9, 4096]> self = ?,<br>List[int]<> size = [9, 4096]       | Unknown  |
| 28 | Tensor<[1, 9, 768]> self = ?,<br>List[int]<> size = [1, 9, 12, 64]   | Unknown  |
| 29 | Tensor<[1, 9, 768]> self = ?,<br>List[int]<> size = [9, 768]         | Unknown  |
| 30 | Tensor<[1, 9, 8192]> self = ?,<br>List[int]<> size = [9, 8192]       | Unknown  |
| 31 | Tensor<[12, 14, 14]> self = ?,<br>List[int]<> size = [1, 12, 14, 14] | Unknown  |
| 32 | Tensor<[12, 14, 64]> self = ?,<br>List[int]<> size = [1, 12, 14, 64] | Unknown  |
| 33 | Tensor<[12, 9, 64]> self = ?,<br>List[int]<> size = [1, 12, 9, 64]   | Unknown  |
| 34 | Tensor<[12, 9, 9]> self = ?,<br>List[int]<> size = [1, 12, 9, 9]     | Unknown  |
| 35 | Tensor<[14, 2]> self = ?,<br>List[int]<> size = [1, 14, 2]           | Unknown  |
| 36 | Tensor<[14, 3072]> self = ?,<br>List[int]<> size = [1, 14, 3072]     | Unknown  |
| 37 | Tensor<[14, 768]> self = ?,<br>List[int]<> size = [1, 14, 768]       | Unknown  |
| 38 | Tensor<[16, 9, 128]> self = ?,<br>List[int]<> size = [1, 16, 9, 128] | Unknown  |
| 39 | Tensor<[16, 9, 64]> self = ?,<br>List[int]<> size = [1, 16, 9, 64]   | Unknown  |
| 40 | Tensor<[16, 9, 9]> self = ?,<br>List[int]<> size = [1, 16, 9, 9]     | Unknown  |
| 41 | Tensor<[64, 9, 64]> self = ?,<br>List[int]<> size = [1, 64, 9, 64]   | Unknown  |
| 42 | Tensor<[64, 9, 9]> self = ?,<br>List[int]<> size = [1, 64, 9, 9]     | Unknown  |
| 43 | Tensor<[9, 1024]> self = ?,<br>List[int]<> size = [1, 9, 1024]       | Unknown  |
| 44 | Tensor<[9, 128]> self = ?,<br>List[int]<> size = [1, 9, 128]         | Unknown  |
| 45 | Tensor<[9, 16384]> self = ?,<br>List[int]<> size = [1, 9, 16384]     | Unknown  |
| 46 | Tensor<[9, 2048]> self = ?,<br>List[int]<> size = [1, 9, 2048]       | Unknown  |
| 47 | Tensor<[9, 30000]> self = ?,<br>List[int]<> size = [1, 9, 30000]     | Unknown  |
| 48 | Tensor<[9, 3072]> self = ?,<br>List[int]<> size = [1, 9, 3072]       | Unknown  |
| 49 | Tensor<[9, 4096]> self = ?,<br>List[int]<> size = [1, 9, 4096]       | Unknown  |
| 50 | Tensor<[9, 768]> self = ?,<br>List[int]<> size = [1, 9, 768]         | Unknown  |
| 51 | Tensor<[9, 8192]> self = ?,<br>List[int]<> size = [1, 9, 8192]       | Unknown  |

