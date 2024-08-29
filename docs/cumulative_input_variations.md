# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._log_softmax.default                         |                  1 |
|  1 | aten._native_batch_norm_legit_no_training.default |                  4 |
|  2 | aten._scaled_dot_product_flash_attention.default  |                  2 |
|  3 | aten._softmax.default                             |                 23 |
|  4 | aten._to_copy.default                             |                 26 |
|  5 | aten._unsafe_index.Tensor                         |                 10 |
|  6 | aten._unsafe_view.default                         |                 13 |
|  7 | aten.abs.default                                  |                  2 |
|  8 | aten.add.Tensor                                   |                 47 |
|  9 | aten.addmm.default                                |                 26 |
| 10 | aten.all.default                                  |                  1 |
| 11 | aten.arange.default                               |                  8 |
| 12 | aten.arange.start                                 |                  3 |
| 13 | aten.argmax.default                               |                  3 |
| 14 | aten.baddbmm.default                              |                  2 |
| 15 | aten.bitwise_not.default                          |                  1 |
| 16 | aten.bmm.default                                  |                 24 |
| 17 | aten.cat.default                                  |                  8 |
| 18 | aten.ceil.default                                 |                  2 |
| 19 | aten.clamp.default                                |                 13 |
| 20 | aten.clone.default                                |                 52 |
| 21 | aten.convolution.default                          |                 53 |
| 22 | aten.cos.default                                  |                  1 |
| 23 | aten.cumsum.default                               |                  4 |
| 24 | aten.div.Tensor                                   |                 25 |
| 25 | aten.embedding.default                            |                 27 |
| 26 | aten.eq.Scalar                                    |                  4 |
| 27 | aten.exp.default                                  |                  1 |
| 28 | aten.expand.default                               |                145 |
| 29 | aten.floor_divide.default                         |                  1 |
| 30 | aten.full.default                                 |                  3 |
| 31 | aten.full_like.default                            |                  3 |
| 32 | aten.gelu.default                                 |                 12 |
| 33 | aten.gt.Scalar                                    |                  3 |
| 34 | aten.hardtanh.default                             |                  1 |
| 35 | aten.index.Tensor                                 |                  7 |
| 36 | aten.le.Tensor                                    |                  1 |
| 37 | aten.lift_fresh_copy.default                      |                  1 |
| 38 | aten.linalg_vector_norm.default                   |                  1 |
| 39 | aten.log.default                                  |                  2 |
| 40 | aten.logical_not.default                          |                  1 |
| 41 | aten.lt.Scalar                                    |                  3 |
| 42 | aten.masked_fill.Scalar                           |                  4 |
| 43 | aten.masked_fill.Tensor                           |                  1 |
| 44 | aten.max_pool2d_with_indices.default              |                  3 |
| 45 | aten.mean.dim                                     |                 10 |
| 46 | aten.minimum.default                              |                  2 |
| 47 | aten.mm.default                                   |                 14 |
| 48 | aten.mul.Scalar                                   |                  1 |
| 49 | aten.mul.Tensor                                   |                 60 |
| 50 | aten.native_dropout.default                       |                  3 |
| 51 | aten.native_layer_norm.default                    |                 33 |
| 52 | aten.ne.Scalar                                    |                  1 |
| 53 | aten.neg.default                                  |                  3 |
| 54 | aten.new_ones.default                             |                  1 |
| 55 | aten.ones.default                                 |                  4 |
| 56 | aten.permute.default                              |                 36 |
| 57 | aten.pow.Scalar                                   |                  1 |
| 58 | aten.pow.Tensor_Scalar                            |                 13 |
| 59 | aten.pow.Tensor_Tensor                            |                  1 |
| 60 | aten.relu.default                                 |                  8 |
| 61 | aten.remainder.Scalar                             |                  1 |
| 62 | aten.repeat.default                               |                  3 |
| 63 | aten.rsqrt.default                                |                  3 |
| 64 | aten.rsub.Scalar                                  |                 14 |
| 65 | aten.select.int                                   |                 13 |
| 66 | aten.sigmoid.default                              |                  3 |
| 67 | aten.sin.default                                  |                  1 |
| 68 | aten.slice.Tensor                                 |                 67 |
| 69 | aten.split.Tensor                                 |                  7 |
| 70 | aten.squeeze.dim                                  |                  4 |
| 71 | aten.stack.default                                |                  3 |
| 72 | aten.sub.Tensor                                   |                 10 |
| 73 | aten.sum.default                                  |                  1 |
| 74 | aten.sym_size.int                                 |                  6 |
| 75 | aten.t.default                                    |                 20 |
| 76 | aten.tanh.default                                 |                 11 |
| 77 | aten.transpose.int                                |                 37 |
| 78 | aten.tril.default                                 |                  1 |
| 79 | aten.unsqueeze.default                            |                 42 |
| 80 | aten.view.default                                 |                483 |
| 81 | aten.where.self                                   |                  4 |
| 82 | aten.zeros.default                                |                  5 |
| 83 | aten.zeros_like.default                           |                  4 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Unknown  |
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
|  2 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  |
|  3 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05        | Unknown  |
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                            | Unknown  |
|  1 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>float dropout_p = 0.0,<br>bool is_causal = True | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
|  2 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  3 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  4 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  5 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  6 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
|  7 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  8 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
|  9 | Tensor<[1, 12, 8, 8]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 10 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 11 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 12 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
| 13 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
| 14 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 15 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 16 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 17 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  |
| 18 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 19 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 20 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  |
| 21 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  |
| 22 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  4 | Tensor<[1, 1, 1, 256]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  |
|  5 | Tensor<[1, 1, 1, 25]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  6 | Tensor<[1, 1, 1, 5]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
|  7 | Tensor<[1, 1, 1, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                              | Unknown  |
|  8 | Tensor<[1, 1, 1, 8]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
|  9 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
| 10 | Tensor<[1, 1, 23, 40]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  |
| 11 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  |
| 12 | Tensor<[1, 1, 720, 1280]> self = ?,<br>Optional[int] dtype = torch.float32                                                                          | Unknown  |
| 13 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32                                                                                      | Unknown  |
| 14 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu           | Unknown  |
| 15 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
| 16 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                          | Unknown  |
| 17 | Tensor<[1, 7]> self = ?,<br>Optional[int] dtype = torch.int32                                                                                       | Unknown  |
| 18 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                     | Unknown  |
| 19 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  |
| 20 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                     | Unknown  |
| 21 | Tensor<[16, 1, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                               | Unknown  |
| 22 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                  | Unknown  |
| 23 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu                                                     | Unknown  |
| 24 | Tensor<[23]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | Unknown  |
| 25 | Tensor<[30]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 720, 1280]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]   | Unknown  |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]  | Unknown  |
|  2 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_10, _to_copy_14]  | Unknown  |
|  3 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_7, _to_copy_10]   | Unknown  |
|  4 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_4, _to_copy_6]    | Unknown  |
|  5 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_16, _to_copy_14] | Unknown  |
|  6 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]     | Unknown  |
|  7 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_19, _to_copy_18] | Unknown  |
|  8 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_6]     | Unknown  |
|  9 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_11, _to_copy_10]   | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>List[int] size = [1, 1, 16, 64]      | Unknown  |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 768]         | Unknown  |
|  2 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] size = [1, 14, 768]         | Unknown  |
|  3 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] size = [1, 256, 768] | Unknown  |
|  4 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536]        | Unknown  |
|  5 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>List[int] size = [1, 5, 16, 64]      | Unknown  |
|  6 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768]         | Unknown  |
|  7 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544]          | Unknown  |
|  8 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] size = [1, 9, 768]           | Unknown  |
|  9 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] size = [1, 9, 2048]         | Unknown  |
| 10 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] size = [1, 9, 1024]          | Unknown  |
| 11 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] size = [1, 9, 4096]          | Unknown  |
| 12 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]            | Unknown  |
### aten.abs.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ? | Unknown  |
|  1 | Tensor<[15, 15]> self = ? | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
|  1 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?           | Unknown  |
|  3 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                              | Unknown  |
|  4 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?           | Unknown  |
|  5 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ? | Unknown  |
|  6 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
|  7 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?           | Unknown  |
|  8 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
|  9 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 10 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
| 11 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?          | Unknown  |
| 12 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Unknown  |
| 13 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?           | Unknown  |
| 14 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?       | Unknown  |
| 15 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Unknown  |
| 16 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?         | Unknown  |
| 17 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                              | Unknown  |
| 18 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Unknown  |
| 19 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?           | Unknown  |
| 20 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?       | Unknown  |
| 21 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?         | Unknown  |
| 22 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?   | Unknown  |
| 23 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?         | Unknown  |
| 24 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                        | Unknown  |
| 25 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?       | Unknown  |
| 26 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 27 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?           | Unknown  |
| 28 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | Unknown  |
| 29 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  |
| 30 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?     | Unknown  |
| 31 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 32 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?             | Unknown  |
| 33 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ?       | Unknown  |
| 34 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?             | Unknown  |
| 35 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?             | Unknown  |
| 36 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 37 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 38 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 39 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 40 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                             | Unknown  |
| 41 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                   | Unknown  |
| 42 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
| 43 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                             | Unknown  |
| 44 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                   | Unknown  |
| 45 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                               | Unknown  |
| 46 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                               | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ?   | Unknown  |
|  1 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ?   | Unknown  |
|  2 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ?     | Unknown  |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
|  4 | Tensor<[1024]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
|  5 | Tensor<[1024]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 1024]> mat2 = ?     | Unknown  |
|  6 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ?     | Unknown  |
|  7 | Tensor<[2048]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 2048]> mat2 = ?     | Unknown  |
|  8 | Tensor<[2304]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?     | Unknown  |
|  9 | Tensor<[256]> self = ?,<br>Tensor<[920, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?     | Unknown  |
| 10 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?       | Unknown  |
| 11 | Tensor<[4096]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Unknown  |
| 12 | Tensor<[4096]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 4096]> mat2 = ?     | Unknown  |
| 13 | Tensor<[4608]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 4608]> mat2 = ?  | Unknown  |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[256, 768]> mat1 = ?,<br>Tensor<[768, 512]> mat2 = ?     | Unknown  |
| 15 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?       | Unknown  |
| 16 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  |
| 17 | Tensor<[768]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 18 | Tensor<[768]> self = ?,<br>Tensor<[12, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?      | Unknown  |
| 19 | Tensor<[768]> self = ?,<br>Tensor<[14, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?      | Unknown  |
| 20 | Tensor<[768]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
| 21 | Tensor<[768]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 22 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
| 23 | Tensor<[768]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 24 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
| 25 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?       | Unknown  |
### aten.all.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  |
|  1 | number end = 10,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  2 | number end = 128,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
|  3 | number end = 15,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  4 | number end = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  |
|  5 | number end = 23,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  |
|  6 | number end = 30,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False      | Unknown  |
|  7 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                       | Unknown  |
|  1 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
|  2 | number start = 1,<br>number end = 17,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.argmax.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1 | Unknown  |
|  1 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = -1     | Unknown  |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1     | Unknown  |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 32]> self = ?,<br>Tensor<[16, 32, 96]> batch1 = ?,<br>Tensor<[16, 96, 32]> batch2 = ?,<br>number beta = 1.0,<br>number alpha = 0.10206207261596577 | Unknown  |
|  1 | Tensor<[8, 1, 920]> self = ?,<br>Tensor<[8, 920, 32]> batch1 = ?,<br>Tensor<[8, 32, 920]> batch2 = ?                                                              | Unknown  |
### aten.bitwise_not.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 23, 40]> self = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ? | Unknown  |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ? | Unknown  |
|  2 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?   | Unknown  |
|  3 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?   | Unknown  |
|  4 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?   | Unknown  |
|  5 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?   | Unknown  |
|  6 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ? | Unknown  |
|  7 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?   | Unknown  |
|  8 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?   | Unknown  |
|  9 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?     | Unknown  |
| 10 | Tensor<[12, 8, 64]> self = ?,<br>Tensor<[12, 64, 8]> mat2 = ?     | Unknown  |
| 11 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?     | Unknown  |
| 12 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?   | Unknown  |
| 13 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ? | Unknown  |
| 14 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ? | Unknown  |
| 15 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?   | Unknown  |
| 16 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?     | Unknown  |
| 17 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?   | Unknown  |
| 18 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?     | Unknown  |
| 19 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?     | Unknown  |
| 20 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?     | Unknown  |
| 21 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ?     | Unknown  |
| 22 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?     | Unknown  |
| 23 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [add, slice_10],<br>int dim = -1                         | Unknown  |
|  1 | List[Tensor] tensors = [clone_46, clone_45, clone_44, clone_43],<br>int dim = 1 | Unknown  |
|  2 | List[Tensor] tensors = [convolution_84, add_86],<br>int dim = 1                 | Unknown  |
|  3 | List[Tensor] tensors = [expand, transpose],<br>int dim = 1                      | Unknown  |
|  4 | List[Tensor] tensors = [mul, mul_1, mul_2, mul_3],<br>int dim = -1              | Unknown  |
|  5 | List[Tensor] tensors = [neg, slice_7],<br>int dim = -1                          | Unknown  |
|  6 | List[Tensor] tensors = [ones_1, _to_copy],<br>int dim = -1                      | Unknown  |
|  7 | List[Tensor] tensors = [view_213, view_212],<br>int dim = 3                     | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[128]> self = ?  | Unknown  |
|  1 | Tensor<[30]> self = ?   | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[120]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 59  | Unknown  |
|  1 | Tensor<[128]> self = ?,<br>Optional[number] min = 0.0                                 | Unknown  |
|  2 | Tensor<[128]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 127 | Unknown  |
|  3 | Tensor<[160]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 79  | Unknown  |
|  4 | Tensor<[240]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 119 | Unknown  |
|  5 | Tensor<[30]> self = ?,<br>Optional[number] min = 0.0                                  | Unknown  |
|  6 | Tensor<[30]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 14   | Unknown  |
|  7 | Tensor<[320]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 159 | Unknown  |
|  8 | Tensor<[40]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 19   | Unknown  |
|  9 | Tensor<[480]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 239 | Unknown  |
| 10 | Tensor<[60]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 29   | Unknown  |
| 11 | Tensor<[640]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 319 | Unknown  |
| 12 | Tensor<[80]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 39   | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Unknown  |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Unknown  |
|  2 | Tensor<[1, 10, 1024]> self = ?                                                                    | Unknown  |
|  3 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
|  4 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
|  5 | Tensor<[1, 10, 512]> self = ?                                                                     | Unknown  |
|  6 | Tensor<[1, 10, 768]> self = ?                                                                     | Unknown  |
|  7 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
|  8 | Tensor<[1, 1024, 512]> self = ?                                                                   | Unknown  |
|  9 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 10 | Tensor<[1, 12, 128]> self = ?                                                                     | Unknown  |
| 11 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 12 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 13 | Tensor<[1, 12, 64, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 14 | Tensor<[1, 1280]> self = ?                                                                        | Unknown  |
| 15 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 16 | Tensor<[1, 14, 128]> self = ?                                                                     | Unknown  |
| 17 | Tensor<[1, 15, 512]> self = ?                                                                     | Unknown  |
| 18 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 19 | Tensor<[1, 1500, 768]> self = ?                                                                   | Unknown  |
| 20 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 21 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
| 22 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Unknown  |
| 23 | Tensor<[1, 16, 768]> self = ?                                                                     | Unknown  |
| 24 | Tensor<[1, 197, 1024]> self = ?                                                                   | Unknown  |
| 25 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 26 | Tensor<[1, 197, 768]> self = ?                                                                    | Unknown  |
| 27 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 28 | Tensor<[1, 25, 768]> self = ?                                                                     | Unknown  |
| 29 | Tensor<[1, 256, 1024]> self = ?                                                                   | Unknown  |
| 30 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Unknown  |
| 31 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 32 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 33 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 34 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  |
| 35 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 36 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Unknown  |
| 37 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 38 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 39 | Tensor<[1, 7, 4544]> self = ?                                                                     | Unknown  |
| 40 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 41 | Tensor<[1, 7, 768]> self = ?                                                                      | Unknown  |
| 42 | Tensor<[1, 8, 768]> self = ?                                                                      | Unknown  |
| 43 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 44 | Tensor<[1, 9, 128]> self = ?                                                                      | Unknown  |
| 45 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 46 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 47 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 48 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 49 | Tensor<[12, 50, 50]> self = ?                                                                     | Unknown  |
| 50 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 51 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
|  1 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  2 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Unknown  |
|  3 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Unknown  |
|  4 | Tensor<[1, 128, 180, 320]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  5 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  6 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  7 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  8 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | Unknown  |
|  9 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
| 10 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 11 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
| 12 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | Unknown  |
| 13 | Tensor<[1, 2048, 23, 40]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 14 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | Unknown  |
| 15 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 16 | Tensor<[1, 256, 180, 320]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 17 | Tensor<[1, 256, 512]> input = ?,<br>Tensor<[1024, 256, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                     | Unknown  |
| 18 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 19 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | Unknown  |
| 20 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
| 21 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 22 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 23 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 24 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 25 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 26 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 27 | Tensor<[1, 3, 720, 1280]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 28 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 29 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
| 30 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 31 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 32 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 33 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[384, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 384         | Unknown  |
| 34 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 35 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | Unknown  |
| 36 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576         | Unknown  |
| 37 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 38 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
| 39 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 40 | Tensor<[1, 64, 180, 320]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 41 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 42 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 43 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 44 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 45 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
| 46 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | Unknown  |
| 47 | Tensor<[1, 768, 3000]> input = ?,<br>Tensor<[768, 768, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [2],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                      | Unknown  |
| 48 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[768, 192, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 4                         | Unknown  |
| 49 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[768, 768, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                         | Unknown  |
| 50 | Tensor<[1, 80, 3000]> input = ?,<br>Tensor<[768, 80, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1                        | Unknown  |
| 51 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96          | Unknown  |
| 52 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960           | Unknown  |
### aten.cos.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Unknown  |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | Unknown  |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = -1                                            | Unknown  |
|  3 | Tensor<[1, 5]> self = ?,<br>int dim = -1                                             | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Unknown  |
|  2 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  3 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  4 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  5 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  6 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Unknown  |
|  7 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Unknown  |
|  8 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  |
|  9 | Tensor<[1, 12, 8, 8]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 10 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 11 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0                | Unknown  |
| 12 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Unknown  |
| 13 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  |
| 14 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Unknown  |
| 15 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 16 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  |
| 17 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Unknown  |
| 18 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  |
| 19 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Unknown  |
| 20 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  |
| 21 | Tensor<[128]> self = ?,<br>Tensor other = 128                            | Unknown  |
| 22 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  |
| 23 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  |
| 24 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Unknown  |
|  1 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Unknown  |
|  2 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Unknown  |
|  3 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Unknown  |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Unknown  |
|  5 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Unknown  |
|  6 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | Unknown  |
|  7 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Unknown  |
|  8 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Unknown  |
|  9 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 10 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Unknown  |
| 11 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Unknown  |
| 12 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 13 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Unknown  |
| 14 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | Unknown  |
| 15 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Unknown  |
| 16 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Unknown  |
| 17 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  |
| 18 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Unknown  |
| 19 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  |
| 20 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Unknown  |
| 21 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Unknown  |
| 22 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Unknown  |
| 23 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Unknown  |
| 24 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  |
| 25 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  |
| 26 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 16]> self = ?,<br>number other = 0    | Unknown  |
|  1 | Tensor<[1, 7]> self = ?,<br>number other = 1     | Unknown  |
|  2 | Tensor<[1, 7]> self = ?,<br>number other = 50256 | Unknown  |
|  3 | Tensor<[1]> self = ?,<br>number other = 50256    | Unknown  |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[]> self = ?     | Unknown  |
### aten.expand.default
|     | ATen Input Variations                                                                  | Status   |
|----:|:---------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]                | Unknown  |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]                    | Unknown  |
|   2 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1]                   | Unknown  |
|   3 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]                         | Unknown  |
|   4 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]            | Unknown  |
|   5 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]              | Unknown  |
|   6 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]            | Unknown  |
|   7 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]              | Unknown  |
|   8 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]                  | Unknown  |
|   9 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]                  | Unknown  |
|  10 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]                  | Unknown  |
|  11 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]                    | Unknown  |
|  12 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]                  | Unknown  |
|  13 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]                     | Unknown  |
|  14 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7]                        | Unknown  |
|  15 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]                          | Unknown  |
|  16 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]                                  | Unknown  |
|  17 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]                    | Unknown  |
|  18 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                      | Unknown  |
|  19 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                      | Unknown  |
|  20 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                    | Unknown  |
|  21 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int]      | Unknown  |
|  22 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]                  | Unknown  |
|  23 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]                  | Unknown  |
|  24 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]                  | Unknown  |
|  25 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]                  | Unknown  |
|  26 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]                  | Unknown  |
|  27 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]                  | Unknown  |
|  28 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]                  | Unknown  |
|  29 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]              | Unknown  |
|  30 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]                | Unknown  |
|  31 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [1, 12, 2, 64]                    | Unknown  |
|  32 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]                  | Unknown  |
|  33 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]                  | Unknown  |
|  34 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10]                  | Unknown  |
|  35 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12]                  | Unknown  |
|  36 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [1, 12, 64, 14]                  | Unknown  |
|  37 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [1, 12, 64, 16]                  | Unknown  |
|  38 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]                | Unknown  |
|  39 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [1, 12, 64, 1]                    | Unknown  |
|  40 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [1, 12, 64, 25]                  | Unknown  |
|  41 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [1, 12, 64, 2]                    | Unknown  |
|  42 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7]                    | Unknown  |
|  43 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int] size = [1, 12, 64, 8]                    | Unknown  |
|  44 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [1, 12, 64, 9]                    | Unknown  |
|  45 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 64, sym_size_int]    | Unknown  |
|  46 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]                    | Unknown  |
|  47 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                      | Unknown  |
|  48 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int] size = [1, 12, 8, 64]                    | Unknown  |
|  49 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int] size = [1, 12, 8, 8]                      | Unknown  |
|  50 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]                    | Unknown  |
|  51 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                      | Unknown  |
|  52 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 12, sym_size_int_1, 64]  | Unknown  |
|  53 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]                    | Unknown  |
|  54 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                      | Unknown  |
|  55 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                      | Unknown  |
|  56 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]                    | Unknown  |
|  57 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                      | Unknown  |
|  58 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]      | Unknown  |
|  59 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int_1]   | Unknown  |
|  60 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]                  | Unknown  |
|  61 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]                  | Unknown  |
|  62 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [1, 16, 128, 9]                  | Unknown  |
|  63 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]              | Unknown  |
|  64 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]                | Unknown  |
|  65 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [1, 16, 2, 64]                    | Unknown  |
|  66 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]              | Unknown  |
|  67 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]                | Unknown  |
|  68 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                      | Unknown  |
|  69 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]                    | Unknown  |
|  70 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]                    | Unknown  |
|  71 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [1, 16, 64, 10]                  | Unknown  |
|  72 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]                | Unknown  |
|  73 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [1, 16, 64, 1]                    | Unknown  |
|  74 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]                | Unknown  |
|  75 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [1, 16, 64, 2]                    | Unknown  |
|  76 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]                    | Unknown  |
|  77 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]                    | Unknown  |
|  78 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [1, 16, 64, 9]                    | Unknown  |
|  79 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 64, sym_size_int]    | Unknown  |
|  80 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 64, sym_size_int]   | Unknown  |
|  81 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]                  | Unknown  |
|  82 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]                    | Unknown  |
|  83 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                      | Unknown  |
|  84 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 16, sym_size_int_1, 64]  | Unknown  |
|  85 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 16, sym_size_int_2, 64] | Unknown  |
|  86 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]                  | Unknown  |
|  87 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]                  | Unknown  |
|  88 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]                  | Unknown  |
|  89 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]              | Unknown  |
|  90 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]                | Unknown  |
|  91 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]              | Unknown  |
|  92 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]                | Unknown  |
|  93 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]                  | Unknown  |
|  94 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                                  | Unknown  |
|  95 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]                | Unknown  |
|  96 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]              | Unknown  |
|  97 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]                | Unknown  |
|  98 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]              | Unknown  |
|  99 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]                | Unknown  |
| 100 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]                  | Unknown  |
| 101 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]                  | Unknown  |
| 102 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]                  | Unknown  |
| 103 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]                  | Unknown  |
| 104 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                      | Unknown  |
| 105 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                      | Unknown  |
| 106 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                        | Unknown  |
| 107 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                        | Unknown  |
| 108 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                      | Unknown  |
| 109 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, sym_size_int]        | Unknown  |
| 110 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]                    | Unknown  |
| 111 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]                    | Unknown  |
| 112 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [1, 6, 17, 64]                    | Unknown  |
| 113 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]                      | Unknown  |
| 114 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]                    | Unknown  |
| 115 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [1, 6, 64, 17]                    | Unknown  |
| 116 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]                      | Unknown  |
| 117 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]                      | Unknown  |
| 118 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, sym_size_int]      | Unknown  |
| 119 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, sym_size_int_1, 64]    | Unknown  |
| 120 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [1, 64, 64, 9]                    | Unknown  |
| 121 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]                    | Unknown  |
| 122 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                      | Unknown  |
| 123 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]                    | Unknown  |
| 124 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]                      | Unknown  |
| 125 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                      | Unknown  |
| 126 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                        | Unknown  |
| 127 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                        | Unknown  |
| 128 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                      | Unknown  |
| 129 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, sym_size_int]        | Unknown  |
| 130 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]                    | Unknown  |
| 131 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]                    | Unknown  |
| 132 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [1, 8, 2, 64]                      | Unknown  |
| 133 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]                | Unknown  |
| 134 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]                  | Unknown  |
| 135 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]                | Unknown  |
| 136 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]                  | Unknown  |
| 137 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]                  | Unknown  |
| 138 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [1, 8, 64, 10]                    | Unknown  |
| 139 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [1, 8, 64, 1]                      | Unknown  |
| 140 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [1, 8, 64, 2]                      | Unknown  |
| 141 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]                  | Unknown  |
| 142 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 64, sym_size_int]      | Unknown  |
| 143 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 8, sym_size_int_1, 64]    | Unknown  |
| 144 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]                                 | Unknown  |
### aten.floor_divide.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Tensor other = 2 | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                | Unknown  |
|  1 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                  | Unknown  |
|  2 | List[int] size = [],<br>number fill_value = 8.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.full_like.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False   | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False | Unknown  |
|  2 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.gelu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 10, 3072]> self = ?   | Unknown  |
|  1 | Tensor<[1, 1024, 512]> self = ?  | Unknown  |
|  2 | Tensor<[1, 16, 3072]> self = ?   | Unknown  |
|  3 | Tensor<[1, 16384, 128]> self = ? | Unknown  |
|  4 | Tensor<[1, 19200, 256]> self = ? | Unknown  |
|  5 | Tensor<[1, 197, 3072]> self = ?  | Unknown  |
|  6 | Tensor<[1, 197, 4096]> self = ?  | Unknown  |
|  7 | Tensor<[1, 25, 3072]> self = ?   | Unknown  |
|  8 | Tensor<[1, 256, 4096]> self = ?  | Unknown  |
|  9 | Tensor<[1, 3072, 8]> self = ?    | Unknown  |
| 10 | Tensor<[1, 7, 18176]> self = ?   | Unknown  |
| 11 | Tensor<[1, 768, 3000]> self = ?  | Unknown  |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Unknown  |
|  1 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Unknown  |
|  2 | Tensor<[]> self = ?,<br>number other = 0       | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 112, 112]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 2]> self = ?,<br>List[Optional[Tensor]] indices = [arange_1, remainder]              | Unknown  |
|  1 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, lift_fresh_copy] | Unknown  |
|  2 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [arange, argmax]                 | Unknown  |
|  3 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [arg226_1]                        | Unknown  |
|  4 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [primals_260]                        | Unknown  |
|  5 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [view_13]                          | Unknown  |
|  6 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [view_13]                          | Unknown  |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
### aten.log.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ? | Unknown  |
|  1 | Tensor<[15, 15]> self = ? | Unknown  |
### aten.logical_not.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.lt.Scalar
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16  | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8 | Unknown  |
|  2 | Tensor<[15, 15]> self = ?,<br>number other = 8 | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  |
|  1 | Tensor<[1, 920]> self = ?,<br>Tensor<[1, 920]> mask = ?,<br>number value = -inf                                | Unknown  |
|  2 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38     | Unknown  |
|  3 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf                                    | Unknown  |
### aten.masked_fill.Tensor
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?,<br>Tensor<[1, 12, 16, 16]> mask = ?,<br>Tensor<[]> value = ? | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  |
|  1 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2]                                                                | Unknown  |
|  2 | Tensor<[1, 64, 360, 640]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True       | Unknown  |
|  1 | Tensor<[1, 10, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True        | Unknown  |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True        | Unknown  |
|  3 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
|  4 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True        | Unknown  |
|  5 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1]                               | Unknown  |
|  6 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1]                                | Unknown  |
|  7 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
|  8 | Tensor<[1, 256, 512]> self = ?,<br>Optional[List[int]] dim = [1]                                | Unknown  |
|  9 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Unknown  |
### aten.minimum.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ? | Unknown  |
|  1 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?       | Unknown  |
|  1 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Unknown  |
|  2 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?      | Unknown  |
|  3 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
|  4 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?      | Unknown  |
|  5 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
|  6 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?     | Unknown  |
|  7 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  |
|  8 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
|  9 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Unknown  |
| 10 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?    | Unknown  |
| 11 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ?    | Unknown  |
| 12 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ?         | Unknown  |
| 13 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Unknown  |
### aten.mul.Scalar
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.4028234663852886e+38  | Unknown  |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.4028234663852886e+38  | Unknown  |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.4028234663852886e+38  | Unknown  |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.4028234663852886e+38  | Unknown  |
|  4 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  |
|  5 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.4028234663852886e+38  | Unknown  |
|  6 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.4028234663852886e+38   | Unknown  |
|  7 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38   | Unknown  |
|  8 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.4028234663852886e+38   | Unknown  |
|  9 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.4028234663852886e+38   | Unknown  |
| 10 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                   | Unknown  |
| 11 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                  | Unknown  |
| 12 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                  | Unknown  |
| 13 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                    | Unknown  |
| 14 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922        | Unknown  |
| 15 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161        | Unknown  |
| 16 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?            | Unknown  |
| 17 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?             | Unknown  |
| 18 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?             | Unknown  |
| 19 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                     | Unknown  |
| 20 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 21 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?         | Unknown  |
| 22 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 23 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?         | Unknown  |
| 24 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 25 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?             | Unknown  |
| 26 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                               | Unknown  |
| 27 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258                           | Unknown  |
| 28 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586          | Unknown  |
| 29 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?         | Unknown  |
| 30 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 31 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                     | Unknown  |
| 32 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?        | Unknown  |
| 33 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
| 34 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                    | Unknown  |
| 35 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?         | Unknown  |
| 36 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                     | Unknown  |
| 37 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  |
| 38 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?             | Unknown  |
| 39 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
| 40 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?           | Unknown  |
| 41 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?        | Unknown  |
| 42 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                   | Unknown  |
| 43 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
| 44 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?         | Unknown  |
| 45 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
| 46 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?           | Unknown  |
| 47 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
| 48 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?           | Unknown  |
| 49 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
| 50 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?           | Unknown  |
| 51 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                            | Unknown  |
| 52 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?               | Unknown  |
| 53 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                              | Unknown  |
| 54 | Tensor<[128]> self = ?,<br>Tensor other = 2                                | Unknown  |
| 55 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                            | Unknown  |
| 56 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957                | Unknown  |
| 57 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                               | Unknown  |
| 58 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                              | Unknown  |
| 59 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                 | Unknown  |
### aten.native_dropout.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128]> input = ?,<br>float p = 0.5,<br>Optional[bool] train = True         | Unknown  |
|  1 | Tensor<[1, 64, 12, 12]> input = ?,<br>float p = 0.25,<br>Optional[bool] train = True | Unknown  |
|  2 | Tensor<[8, 920, 920]> input = ?,<br>float p = 0.1,<br>Optional[bool] train = True    | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05      | Unknown  |
|  1 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05    | Unknown  |
|  2 | Tensor<[1, 12, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12      | Unknown  |
|  3 | Tensor<[1, 12, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Unknown  |
|  4 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05    | Unknown  |
|  5 | Tensor<[1, 14, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12      | Unknown  |
|  6 | Tensor<[1, 14, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Unknown  |
|  7 | Tensor<[1, 1500, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  |
|  8 | Tensor<[1, 16, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Unknown  |
|  9 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 10 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 11 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Unknown  |
| 12 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12     | Unknown  |
| 13 | Tensor<[1, 25, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Unknown  |
| 14 | Tensor<[1, 256, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Unknown  |
| 15 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 16 | Tensor<[1, 256, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 17 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05     | Unknown  |
| 18 | Tensor<[1, 32, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05  | Unknown  |
| 19 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05        | Unknown  |
| 20 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05    | Unknown  |
| 21 | Tensor<[1, 5, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05   | Unknown  |
| 22 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05      | Unknown  |
| 23 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05   | Unknown  |
| 24 | Tensor<[1, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 25 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12       | Unknown  |
| 26 | Tensor<[1, 9, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12   | Unknown  |
| 27 | Tensor<[1, 9, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12       | Unknown  |
| 28 | Tensor<[1, 9, 2048]> input = ?,<br>List[int] normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float eps = 1e-12   | Unknown  |
| 29 | Tensor<[1, 9, 4096]> input = ?,<br>List[int] normalized_shape = [4096],<br>Optional[Tensor]<[4096]> weight = ?,<br>Optional[Tensor]<[4096]> bias = ?,<br>float eps = 1e-12   | Unknown  |
| 30 | Tensor<[1, 9, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12       | Unknown  |
| 31 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 32 | Tensor<[920, 1, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05     | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>number other = 1 | Unknown  |
### aten.neg.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?         | Unknown  |
|  1 | Tensor<[1, 5, 16, 16]> self = ? | Unknown  |
|  2 | Tensor<[1, 71, 7, 32]> self = ? | Unknown  |
### aten.new_ones.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                              | Unknown  |
|  1 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  2 | List[int] size = [1, 720, 1280],<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  3 | List[int] size = [7, 7],<br>Optional[int] dtype = torch.bool,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
|  2 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int] dims = [0, 1, 3, 2]               | Unknown  |
|  3 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  4 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  |
|  5 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
|  6 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
|  7 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Unknown  |
|  8 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
|  9 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Unknown  |
| 10 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
| 11 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 12 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 13 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  |
| 14 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 15 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  |
| 16 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Unknown  |
| 17 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | Unknown  |
| 18 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Unknown  |
| 19 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 20 | Tensor<[1, 512]> self = ?,<br>List[int] dims = [0, 1]                           | Unknown  |
| 21 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 22 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 23 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  |
| 24 | Tensor<[1, 8, 768]> self = ?,<br>List[int] dims = [0, 2, 1]                     | Unknown  |
| 25 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 26 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  |
| 27 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 28 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  |
| 29 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Unknown  |
| 30 | Tensor<[10, 10, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Unknown  |
| 31 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 32 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  |
| 33 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Unknown  |
| 34 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Unknown  |
| 35 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]                       | Unknown  |
### aten.pow.Scalar
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | number self = 10000,<br>Tensor<[128]> exponent = ? | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 1024]> self = ?,<br>number exponent = 2   | Unknown  |
|  1 | Tensor<[1, 10, 512]> self = ?,<br>number exponent = 2    | Unknown  |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>number exponent = 2    | Unknown  |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  4 | Tensor<[1, 14, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  5 | Tensor<[1, 15, 1024]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  6 | Tensor<[1, 15, 512]> self = ?,<br>number exponent = 2    | Unknown  |
|  7 | Tensor<[1, 5, 4096]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  8 | Tensor<[1, 7, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  9 | Tensor<[1, 9, 16384]> self = ?,<br>number exponent = 3.0 | Unknown  |
| 10 | Tensor<[1, 9, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
| 11 | Tensor<[1, 9, 4096]> self = ?,<br>number exponent = 3.0  | Unknown  |
| 12 | Tensor<[1, 9, 8192]> self = ?,<br>number exponent = 3.0  | Unknown  |
### aten.pow.Tensor_Tensor
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>Tensor<[16]> exponent = ? | Unknown  |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 10, 2048]> self = ?      | Unknown  |
|  1 | Tensor<[1, 10, 3072]> self = ?      | Unknown  |
|  2 | Tensor<[1, 10, 4096]> self = ?      | Unknown  |
|  3 | Tensor<[1, 256, 128, 128]> self = ? | Unknown  |
|  4 | Tensor<[1, 32, 26, 26]> self = ?    | Unknown  |
|  5 | Tensor<[1, 64, 112, 112]> self = ?  | Unknown  |
|  6 | Tensor<[1, 64, 30, 40]> self = ?    | Unknown  |
|  7 | Tensor<[1, 64, 360, 640]> self = ?  | Unknown  |
### aten.remainder.Scalar
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number other = 7 | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1]             | Unknown  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Unknown  |
|  2 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]         | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 10, 1]> self = ?    | Unknown  |
|  1 | Tensor<[1, 15, 1]> self = ?    | Unknown  |
|  2 | Tensor<[1, 64, 1, 1]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0  | Unknown  |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0  | Unknown  |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0  | Unknown  |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0  | Unknown  |
|  4 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0 | Unknown  |
|  5 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0  | Unknown  |
|  6 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0   | Unknown  |
|  7 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0   | Unknown  |
|  8 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0   | Unknown  |
|  9 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0   | Unknown  |
| 10 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0 | Unknown  |
| 11 | Tensor<[128, 1]> self = ?,<br>number other = 1.0       | Unknown  |
| 12 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0   | Unknown  |
| 13 | Tensor<[30, 1]> self = ?,<br>number other = 1.0        | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0     | Unknown  |
|  1 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1     | Unknown  |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Unknown  |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1     | Unknown  |
|  5 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Unknown  |
|  6 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Unknown  |
|  7 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Unknown  |
|  8 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1            | Unknown  |
|  9 | Tensor<[1, 8, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  |
| 10 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  |
| 11 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0                | Unknown  |
| 12 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1   | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 2, 30, 40]> self = ? | Unknown  |
|  1 | Tensor<[1, 50, 3072]> self = ?  | Unknown  |
|  2 | Tensor<[6, 1, 100, 4]> self = ? | Unknown  |
### aten.sin.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 23, 40, 64]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  1 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  2 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 6                    | Unknown  |
|  3 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?           | Unknown  |
|  4 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  5 | Tensor<[1, 1, 1, 25]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
|  6 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  7 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  8 | Tensor<[1, 1, 1, 8]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
|  9 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                | Unknown  |
| 10 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2   | Unknown  |
| 11 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Unknown  |
| 12 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
| 13 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                | Unknown  |
| 14 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 5                 | Unknown  |
| 15 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?   | Unknown  |
| 16 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 17 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
| 18 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
| 19 | Tensor<[1, 1, 5, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 5                    | Unknown  |
| 20 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7                    | Unknown  |
| 21 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = -1                    | Unknown  |
| 22 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
| 23 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
| 24 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                    | Unknown  |
| 25 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
| 26 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                    | Unknown  |
| 27 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 28 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 29 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 30 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 31 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 32 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 33 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
| 34 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
| 35 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
| 36 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
| 37 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
| 38 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
| 39 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 40 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2   | Unknown  |
| 41 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 42 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
| 43 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
| 44 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                         | Unknown  |
| 45 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                           | Unknown  |
| 46 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
| 47 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 48 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                     | Unknown  |
| 49 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                       | Unknown  |
| 50 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                           | Unknown  |
| 51 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 5,<br>Optional[int] end = -1                            | Unknown  |
| 52 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
| 53 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                    | Unknown  |
| 54 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Unknown  |
| 55 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
| 56 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                            | Unknown  |
| 57 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 58 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1                     | Unknown  |
| 59 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 60 | Tensor<[1, 8]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                            | Unknown  |
| 61 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = -1                          | Unknown  |
| 62 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = -1                   | Unknown  |
| 63 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                      | Unknown  |
| 64 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                         | Unknown  |
| 65 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1                         | Unknown  |
| 66 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ?             | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Unknown  |
|  1 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Unknown  |
|  2 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1      | Unknown  |
|  3 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  |
|  4 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  |
|  5 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2    | Unknown  |
|  6 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                      | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Unknown  |
|  1 | Tensor<[1, 14, 1]> self = ?,<br>int dim = -1      | Unknown  |
|  2 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1      | Unknown  |
|  3 | Tensor<[1, 256, 1]> self = ?,<br>int dim = -1     | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [getitem_155, getitem_191, getitem_227, getitem_263, getitem_299, getitem_335] | Unknown  |
|  1 | List[Tensor] tensors = [neg, slice_28],<br>int dim = -1                                               | Unknown  |
|  2 | List[Tensor] tensors = [sin, cos],<br>int dim = 4                                                     | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?             | Unknown  |
|  1 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?             | Unknown  |
|  2 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  3 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                       | Unknown  |
|  4 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ? | Unknown  |
|  5 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?           | Unknown  |
|  6 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
|  7 | Tensor<[1]> self = ?,<br>Tensor other = 1                          | Unknown  |
|  8 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?             | Unknown  |
|  9 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                       | Unknown  |
### aten.sum.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1]> self = ?    | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  |
|  1 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim = 2  | Unknown  |
|  2 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim = 2  | Unknown  |
|  3 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  |
|  4 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim = 2   | Unknown  |
|  5 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim = 2   | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ?  | Unknown  |
|  1 | Tensor<[1000, 2048]> self = ?  | Unknown  |
|  2 | Tensor<[1000, 512]> self = ?   | Unknown  |
|  3 | Tensor<[1024, 1024]> self = ?  | Unknown  |
|  4 | Tensor<[1024, 128]> self = ?   | Unknown  |
|  5 | Tensor<[128, 9216]> self = ?   | Unknown  |
|  6 | Tensor<[2, 768]> self = ?      | Unknown  |
|  7 | Tensor<[2048, 128]> self = ?   | Unknown  |
|  8 | Tensor<[256, 256]> self = ?    | Unknown  |
|  9 | Tensor<[3072, 1024]> self = ?  | Unknown  |
| 10 | Tensor<[32, 32]> self = ?      | Unknown  |
| 11 | Tensor<[384, 512]> self = ?    | Unknown  |
| 12 | Tensor<[4096, 128]> self = ?   | Unknown  |
| 13 | Tensor<[4608, 1536]> self = ?  | Unknown  |
| 14 | Tensor<[512, 512]> self = ?    | Unknown  |
| 15 | Tensor<[512, 768]> self = ?    | Unknown  |
| 16 | Tensor<[64, 64]> self = ?      | Unknown  |
| 17 | Tensor<[65024, 4544]> self = ? | Unknown  |
| 18 | Tensor<[768, 128]> self = ?    | Unknown  |
| 19 | Tensor<[768, 768]> self = ?    | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 12, 3072]> self = ? | Unknown  |
|  1 | Tensor<[1, 14, 3072]> self = ? | Unknown  |
|  2 | Tensor<[1, 15, 1024]> self = ? | Unknown  |
|  3 | Tensor<[1, 32, 6144]> self = ? | Unknown  |
|  4 | Tensor<[1, 5, 4096]> self = ?  | Unknown  |
|  5 | Tensor<[1, 7, 3072]> self = ?  | Unknown  |
|  6 | Tensor<[1, 768]> self = ?      | Unknown  |
|  7 | Tensor<[1, 9, 16384]> self = ? | Unknown  |
|  8 | Tensor<[1, 9, 3072]> self = ?  | Unknown  |
|  9 | Tensor<[1, 9, 4096]> self = ?  | Unknown  |
| 10 | Tensor<[1, 9, 8192]> self = ?  | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
|  1 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
|  2 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1    | Unknown  |
|  3 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
|  4 | Tensor<[1, 10, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
|  5 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
|  6 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
|  7 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
|  8 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  |
|  9 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
| 10 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
| 11 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3    | Unknown  |
| 12 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
| 13 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
| 14 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 15 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 16 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
| 17 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  |
| 18 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  |
| 19 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
| 20 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
| 21 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
| 22 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 23 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
| 24 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 25 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
| 26 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
| 27 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  |
| 28 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
| 29 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 30 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
| 31 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  |
| 32 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  |
| 33 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  |
| 34 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  |
| 35 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1     | Unknown  |
| 36 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1       | Unknown  |
### aten.tril.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2      | Unknown  |
|  1 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2      | Unknown  |
|  2 | Tensor<[1, 1, 14]> self = ?,<br>int dim = 2      | Unknown  |
|  3 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2      | Unknown  |
|  4 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2     | Unknown  |
|  5 | Tensor<[1, 1, 25]> self = ?,<br>int dim = 2      | Unknown  |
|  6 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2      | Unknown  |
|  7 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2       | Unknown  |
|  8 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2       | Unknown  |
|  9 | Tensor<[1, 1, 8]> self = ?,<br>int dim = 2       | Unknown  |
| 10 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2       | Unknown  |
| 11 | Tensor<[1, 10]> self = ?,<br>int dim = 1         | Unknown  |
| 12 | Tensor<[1, 12]> self = ?,<br>int dim = 1         | Unknown  |
| 13 | Tensor<[1, 14]> self = ?,<br>int dim = 1         | Unknown  |
| 14 | Tensor<[1, 15]> self = ?,<br>int dim = 1         | Unknown  |
| 15 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Unknown  |
| 16 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3     | Unknown  |
| 17 | Tensor<[1, 256]> self = ?,<br>int dim = 1        | Unknown  |
| 18 | Tensor<[1, 25]> self = ?,<br>int dim = 1         | Unknown  |
| 19 | Tensor<[1, 32]> self = ?,<br>int dim = 1         | Unknown  |
| 20 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4   | Unknown  |
| 21 | Tensor<[1, 5]> self = ?,<br>int dim = 1          | Unknown  |
| 22 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | Unknown  |
| 23 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1      | Unknown  |
| 24 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1       | Unknown  |
| 25 | Tensor<[1, 720, 1280]> self = ?,<br>int dim = 0  | Unknown  |
| 26 | Tensor<[1, 7]> self = ?,<br>int dim = 1          | Unknown  |
| 27 | Tensor<[1, 8]> self = ?,<br>int dim = 1          | Unknown  |
| 28 | Tensor<[1, 9]> self = ?,<br>int dim = 1          | Unknown  |
| 29 | Tensor<[100, 256]> self = ?,<br>int dim = 1      | Unknown  |
| 30 | Tensor<[10]> self = ?,<br>int dim = 0            | Unknown  |
| 31 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0  | Unknown  |
| 32 | Tensor<[128]> self = ?,<br>int dim = 1           | Unknown  |
| 33 | Tensor<[15]> self = ?,<br>int dim = 0            | Unknown  |
| 34 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0  | Unknown  |
| 35 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2       | Unknown  |
| 36 | Tensor<[23]> self = ?,<br>int dim = -1           | Unknown  |
| 37 | Tensor<[30]> self = ?,<br>int dim = 1            | Unknown  |
| 38 | Tensor<[32, 32]> self = ?,<br>int dim = 0        | Unknown  |
| 39 | Tensor<[32]> self = ?,<br>int dim = 0            | Unknown  |
| 40 | Tensor<[7, 7]> self = ?,<br>int dim = 0          | Unknown  |
| 41 | Tensor<[7]> self = ?,<br>int dim = 0             | Unknown  |
### aten.view.default
|     | ATen Input Variations                                                               | Status   |
|----:|:------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]                | Unknown  |
|   1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                        | Unknown  |
|   2 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]              | Unknown  |
|   3 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  |
|   4 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]            | Unknown  |
|   5 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300]            | Unknown  |
|   6 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]                        | Unknown  |
|   7 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]                    | Unknown  |
|   8 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                        | Unknown  |
|   9 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                          | Unknown  |
|  10 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]               | Unknown  |
|  11 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                        | Unknown  |
|  12 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                          | Unknown  |
|  13 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]                   | Unknown  |
|  14 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                          | Unknown  |
|  15 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [10, 1024]                      | Unknown  |
|  16 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]                  | Unknown  |
|  17 | Tensor<[1, 10, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]                 | Unknown  |
|  18 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]                      | Unknown  |
|  19 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]                      | Unknown  |
|  20 | Tensor<[1, 10, 4096]> self = ?,<br>List[int] size = [10, 4096]                      | Unknown  |
|  21 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]                        | Unknown  |
|  22 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                        | Unknown  |
|  23 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]                   | Unknown  |
|  24 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196]              | Unknown  |
|  25 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]              | Unknown  |
|  26 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]                    | Unknown  |
|  27 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]              | Unknown  |
|  28 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]                    | Unknown  |
|  29 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                        | Unknown  |
|  30 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                              | Unknown  |
|  31 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]                    | Unknown  |
|  32 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]                      | Unknown  |
|  33 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]                      | Unknown  |
|  34 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]                    | Unknown  |
|  35 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, sym_size_int]      | Unknown  |
|  36 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]                  | Unknown  |
|  37 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]                  | Unknown  |
|  38 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12]                  | Unknown  |
|  39 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64]                  | Unknown  |
|  40 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]                        | Unknown  |
|  41 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [12, 14, 14]                  | Unknown  |
|  42 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [12, 14, 64]                  | Unknown  |
|  43 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16]                  | Unknown  |
|  44 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64]                  | Unknown  |
|  45 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197]              | Unknown  |
|  46 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]                | Unknown  |
|  47 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]                    | Unknown  |
|  48 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25]                  | Unknown  |
|  49 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64]                  | Unknown  |
|  50 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]                      | Unknown  |
|  51 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64]                  | Unknown  |
|  52 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]                  | Unknown  |
|  53 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12]                  | Unknown  |
|  54 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [12, 64, 14]                  | Unknown  |
|  55 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16]                  | Unknown  |
|  56 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]                | Unknown  |
|  57 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]                    | Unknown  |
|  58 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25]                  | Unknown  |
|  59 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]                    | Unknown  |
|  60 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7]                    | Unknown  |
|  61 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int] size = [12, 64, 8]                    | Unknown  |
|  62 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9]                    | Unknown  |
|  63 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, sym_size_int]    | Unknown  |
|  64 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64]                    | Unknown  |
|  65 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]                      | Unknown  |
|  66 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]                        | Unknown  |
|  67 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int] size = [12, 8, 64]                    | Unknown  |
|  68 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int] size = [12, 8, 8]                      | Unknown  |
|  69 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64]                    | Unknown  |
|  70 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]                      | Unknown  |
|  71 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, sym_size_int_1, 64]  | Unknown  |
|  72 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]                  | Unknown  |
|  73 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]                    | Unknown  |
|  74 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384]            | Unknown  |
|  75 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]                | Unknown  |
|  76 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128]            | Unknown  |
|  77 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]               | Unknown  |
|  78 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]               | Unknown  |
|  79 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280]                     | Unknown  |
|  80 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]             | Unknown  |
|  81 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]             | Unknown  |
|  82 | Tensor<[1, 14, 128]> self = ?,<br>List[int] size = [14, 128]                        | Unknown  |
|  83 | Tensor<[1, 14, 3072]> self = ?,<br>List[int] size = [14, 3072]                      | Unknown  |
|  84 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [14, 768]                        | Unknown  |
|  85 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]                      | Unknown  |
|  86 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]                   | Unknown  |
|  87 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]                        | Unknown  |
|  88 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]                   | Unknown  |
|  89 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]                  | Unknown  |
|  90 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]                    | Unknown  |
|  91 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                              | Unknown  |
|  92 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [16, 1, 10]                    | Unknown  |
|  93 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [16, 1, 1]                      | Unknown  |
|  94 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [16, 1, 2]                      | Unknown  |
|  95 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]                    | Unknown  |
|  96 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                      | Unknown  |
|  97 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, sym_size_int]      | Unknown  |
|  98 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, sym_size_int_1]   | Unknown  |
|  99 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [16, 10, 10]                  | Unknown  |
| 100 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [16, 10, 64]                  | Unknown  |
| 101 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]                  | Unknown  |
| 102 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [16, 128, 9]                  | Unknown  |
| 103 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197]              | Unknown  |
| 104 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]                | Unknown  |
| 105 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [16, 2, 64]                    | Unknown  |
| 106 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256]              | Unknown  |
| 107 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]                | Unknown  |
| 108 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]                      | Unknown  |
| 109 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]                  | Unknown  |
| 110 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]                  | Unknown  |
| 111 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]                       | Unknown  |
| 112 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                      | Unknown  |
| 113 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]                    | Unknown  |
| 114 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]                    | Unknown  |
| 115 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [16, 64, 10]                  | Unknown  |
| 116 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]                | Unknown  |
| 117 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [16, 64, 1]                    | Unknown  |
| 118 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]                | Unknown  |
| 119 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [16, 64, 2]                    | Unknown  |
| 120 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]                    | Unknown  |
| 121 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]                    | Unknown  |
| 122 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]                    | Unknown  |
| 123 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, sym_size_int]    | Unknown  |
| 124 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, sym_size_int]   | Unknown  |
| 125 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]                        | Unknown  |
| 126 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [16, 9, 128]                  | Unknown  |
| 127 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]                    | Unknown  |
| 128 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]                      | Unknown  |
| 129 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]                  | Unknown  |
| 130 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, sym_size_int_1, 64]  | Unknown  |
| 131 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, sym_size_int_2, 64] | Unknown  |
| 132 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]               | Unknown  |
| 133 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]                | Unknown  |
| 134 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]               | Unknown  |
| 135 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]                  | Unknown  |
| 136 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]            | Unknown  |
| 137 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]                    | Unknown  |
| 138 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]                         | Unknown  |
| 139 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]                  | Unknown  |
| 140 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]            | Unknown  |
| 141 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]                    | Unknown  |
| 142 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]                    | Unknown  |
| 143 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]                    | Unknown  |
| 144 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]                    | Unknown  |
| 145 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]                      | Unknown  |
| 146 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                                | Unknown  |
| 147 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                                    | Unknown  |
| 148 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]                  | Unknown  |
| 149 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]                  | Unknown  |
| 150 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]                  | Unknown  |
| 151 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]              | Unknown  |
| 152 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]                | Unknown  |
| 153 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]              | Unknown  |
| 154 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]                | Unknown  |
| 155 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]                  | Unknown  |
| 156 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048]                     | Unknown  |
| 157 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]              | Unknown  |
| 158 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]              | Unknown  |
| 159 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]                        | Unknown  |
| 160 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128]           | Unknown  |
| 161 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                          | Unknown  |
| 162 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]                      | Unknown  |
| 163 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]                        | Unknown  |
| 164 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]                    | Unknown  |
| 165 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200]            | Unknown  |
| 166 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]                | Unknown  |
| 167 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]                      | Unknown  |
| 168 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128]            | Unknown  |
| 169 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160]            | Unknown  |
| 170 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]                | Unknown  |
| 171 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                      | Unknown  |
| 172 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]                        | Unknown  |
| 173 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]               | Unknown  |
| 174 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]                    | Unknown  |
| 175 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                      | Unknown  |
| 176 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]               | Unknown  |
| 177 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]                        | Unknown  |
| 178 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                      | Unknown  |
| 179 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                               | Unknown  |
| 180 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16]       | Unknown  |
| 181 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]                      | Unknown  |
| 182 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]                    | Unknown  |
| 183 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]                      | Unknown  |
| 184 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]                      | Unknown  |
| 185 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]                        | Unknown  |
| 186 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                        | Unknown  |
| 187 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]              | Unknown  |
| 188 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]                      | Unknown  |
| 189 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]                  | Unknown  |
| 190 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]              | Unknown  |
| 191 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96]              | Unknown  |
| 192 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]                      | Unknown  |
| 193 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]               | Unknown  |
| 194 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]                | Unknown  |
| 195 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]               | Unknown  |
| 196 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]                      | Unknown  |
| 197 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                          | Unknown  |
| 198 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]                        | Unknown  |
| 199 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]                          | Unknown  |
| 200 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]                    | Unknown  |
| 201 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]                      | Unknown  |
| 202 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                        | Unknown  |
| 203 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]                    | Unknown  |
| 204 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]                    | Unknown  |
| 205 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                                | Unknown  |
| 206 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]                | Unknown  |
| 207 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]              | Unknown  |
| 208 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]                | Unknown  |
| 209 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                        | Unknown  |
| 210 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]              | Unknown  |
| 211 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]                | Unknown  |
| 212 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]              | Unknown  |
| 213 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  |
| 214 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]                  | Unknown  |
| 215 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]                  | Unknown  |
| 216 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]                    | Unknown  |
| 217 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]                  | Unknown  |
| 218 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]               | Unknown  |
| 219 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                        | Unknown  |
| 220 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]                  | Unknown  |
| 221 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]                      | Unknown  |
| 222 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]                        | Unknown  |
| 223 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512]                       | Unknown  |
| 224 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]                | Unknown  |
| 225 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]               | Unknown  |
| 226 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]               | Unknown  |
| 227 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                      | Unknown  |
| 228 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                          | Unknown  |
| 229 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512]                             | Unknown  |
| 230 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]                      | Unknown  |
| 231 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                                | Unknown  |
| 232 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]                      | Unknown  |
| 233 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]                      | Unknown  |
| 234 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]                        | Unknown  |
| 235 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]                        | Unknown  |
| 236 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]                      | Unknown  |
| 237 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, sym_size_int]        | Unknown  |
| 238 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]                    | Unknown  |
| 239 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]                    | Unknown  |
| 240 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]                    | Unknown  |
| 241 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]                      | Unknown  |
| 242 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]                    | Unknown  |
| 243 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]                    | Unknown  |
| 244 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]                      | Unknown  |
| 245 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]                      | Unknown  |
| 246 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, sym_size_int]      | Unknown  |
| 247 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, sym_size_int_1, 64]    | Unknown  |
| 248 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]                     | Unknown  |
| 249 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]              | Unknown  |
| 250 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]                  | Unknown  |
| 251 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]                  | Unknown  |
| 252 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]              | Unknown  |
| 253 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]                 | Unknown  |
| 254 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]                 | Unknown  |
| 255 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [64, 64, 9]                    | Unknown  |
| 256 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [64, 9, 64]                    | Unknown  |
| 257 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [64, 9, 9]                      | Unknown  |
| 258 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]               | Unknown  |
| 259 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]               | Unknown  |
| 260 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                                | Unknown  |
| 261 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768]                    | Unknown  |
| 262 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]                      | Unknown  |
| 263 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]                       | Unknown  |
| 264 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]                        | Unknown  |
| 265 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]                   | Unknown  |
| 266 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]                         | Unknown  |
| 267 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]                    | Unknown  |
| 268 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]                 | Unknown  |
| 269 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]                      | Unknown  |
| 270 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]                | Unknown  |
| 271 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]                   | Unknown  |
| 272 | Tensor<[1, 768, 8]> self = ?,<br>List[int] size = [1, 12, 64, 8]                    | Unknown  |
| 273 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                          | Unknown  |
| 274 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]                                | Unknown  |
| 275 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]                      | Unknown  |
| 276 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]                        | Unknown  |
| 277 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]                        | Unknown  |
| 278 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]                      | Unknown  |
| 279 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]                    | Unknown  |
| 280 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, sym_size_int]        | Unknown  |
| 281 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]                    | Unknown  |
| 282 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]                    | Unknown  |
| 283 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]                      | Unknown  |
| 284 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]                | Unknown  |
| 285 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]                  | Unknown  |
| 286 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]                | Unknown  |
| 287 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]                  | Unknown  |
| 288 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]                  | Unknown  |
| 289 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]                    | Unknown  |
| 290 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]                      | Unknown  |
| 291 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]                      | Unknown  |
| 292 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]                  | Unknown  |
| 293 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, sym_size_int]      | Unknown  |
| 294 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, sym_size_int_1, 64]    | Unknown  |
| 295 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]                        | Unknown  |
| 296 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]                          | Unknown  |
| 297 | Tensor<[1, 9, 16384]> self = ?,<br>List[int] size = [9, 16384]                      | Unknown  |
| 298 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [9, 2048]                        | Unknown  |
| 299 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]                        | Unknown  |
| 300 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]                        | Unknown  |
| 301 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                          | Unknown  |
| 302 | Tensor<[1, 9, 8192]> self = ?,<br>List[int] size = [9, 8192]                        | Unknown  |
| 303 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]                       | Unknown  |
| 304 | Tensor<[10, 1024]> self = ?,<br>List[int] size = [1, 10, 1024]                      | Unknown  |
| 305 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]                      | Unknown  |
| 306 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002]                  | Unknown  |
| 307 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]                      | Unknown  |
| 308 | Tensor<[10, 4096]> self = ?,<br>List[int] size = [1, 10, 4096]                      | Unknown  |
| 309 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]                        | Unknown  |
| 310 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                        | Unknown  |
| 311 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]                    | Unknown  |
| 312 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]                      | Unknown  |
| 313 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]                    | Unknown  |
| 314 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]                      | Unknown  |
| 315 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]                    | Unknown  |
| 316 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]                    | Unknown  |
| 317 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]                    | Unknown  |
| 318 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                      | Unknown  |
| 319 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                      | Unknown  |
| 320 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                    | Unknown  |
| 321 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int]      | Unknown  |
| 322 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]                  | Unknown  |
| 323 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]                  | Unknown  |
| 324 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]                  | Unknown  |
| 325 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]                  | Unknown  |
| 326 | Tensor<[12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]                  | Unknown  |
| 327 | Tensor<[12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]                  | Unknown  |
| 328 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]                  | Unknown  |
| 329 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]                  | Unknown  |
| 330 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]              | Unknown  |
| 331 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]                | Unknown  |
| 332 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]                  | Unknown  |
| 333 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]                  | Unknown  |
| 334 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]                            | Unknown  |
| 335 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]                      | Unknown  |
| 336 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]                  | Unknown  |
| 337 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]                    | Unknown  |
| 338 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                      | Unknown  |
| 339 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]                        | Unknown  |
| 340 | Tensor<[12, 8, 64]> self = ?,<br>List[int] size = [1, 12, 8, 64]                    | Unknown  |
| 341 | Tensor<[12, 8, 8]> self = ?,<br>List[int] size = [1, 12, 8, 8]                      | Unknown  |
| 342 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]                    | Unknown  |
| 343 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                      | Unknown  |
| 344 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]                  | Unknown  |
| 345 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]                    | Unknown  |
| 346 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]                       | Unknown  |
| 347 | Tensor<[14, 2]> self = ?,<br>List[int] size = [1, 14, 2]                            | Unknown  |
| 348 | Tensor<[14, 3072]> self = ?,<br>List[int] size = [1, 14, 3072]                      | Unknown  |
| 349 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]                         | Unknown  |
| 350 | Tensor<[14, 768]> self = ?,<br>List[int] size = [1, 14, 768]                        | Unknown  |
| 351 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]                      | Unknown  |
| 352 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]                        | Unknown  |
| 353 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]                        | Unknown  |
| 354 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]                  | Unknown  |
| 355 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]                    | Unknown  |
| 356 | Tensor<[16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]                    | Unknown  |
| 357 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                      | Unknown  |
| 358 | Tensor<[16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                      | Unknown  |
| 359 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]                    | Unknown  |
| 360 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                      | Unknown  |
| 361 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]      | Unknown  |
| 362 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]     | Unknown  |
| 363 | Tensor<[16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]                  | Unknown  |
| 364 | Tensor<[16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]                  | Unknown  |
| 365 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]              | Unknown  |
| 366 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]                | Unknown  |
| 367 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]              | Unknown  |
| 368 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]                | Unknown  |
| 369 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]                      | Unknown  |
| 370 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]                  | Unknown  |
| 371 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]                  | Unknown  |
| 372 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                      | Unknown  |
| 373 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]                    | Unknown  |
| 374 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]                     | Unknown  |
| 375 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]                       | Unknown  |
| 376 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]                        | Unknown  |
| 377 | Tensor<[16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]                  | Unknown  |
| 378 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]                    | Unknown  |
| 379 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                      | Unknown  |
| 380 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]                  | Unknown  |
| 381 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]                    | Unknown  |
| 382 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]                  | Unknown  |
| 383 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]                    | Unknown  |
| 384 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]                    | Unknown  |
| 385 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                               | Unknown  |
| 386 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]                    | Unknown  |
| 387 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]                    | Unknown  |
| 388 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]                      | Unknown  |
| 389 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]              | Unknown  |
| 390 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]                | Unknown  |
| 391 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]              | Unknown  |
| 392 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]                | Unknown  |
| 393 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]                       | Unknown  |
| 394 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]                         | Unknown  |
| 395 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]                                | Unknown  |
| 396 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]                    | Unknown  |
| 397 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]                       | Unknown  |
| 398 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]                            | Unknown  |
| 399 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]                      | Unknown  |
| 400 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]                        | Unknown  |
| 401 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]                    | Unknown  |
| 402 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]                      | Unknown  |
| 403 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                      | Unknown  |
| 404 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]                          | Unknown  |
| 405 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]                        | Unknown  |
| 406 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]                    | Unknown  |
| 407 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                      | Unknown  |
| 408 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]                        | Unknown  |
| 409 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]                      | Unknown  |
| 410 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]                    | Unknown  |
| 411 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]                      | Unknown  |
| 412 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]                      | Unknown  |
| 413 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]                        | Unknown  |
| 414 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]                      | Unknown  |
| 415 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]                  | Unknown  |
| 416 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]                      | Unknown  |
| 417 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]                      | Unknown  |
| 418 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]                    | Unknown  |
| 419 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]                    | Unknown  |
| 420 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]                        | Unknown  |
| 421 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]                      | Unknown  |
| 422 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]                          | Unknown  |
| 423 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]                    | Unknown  |
| 424 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]                      | Unknown  |
| 425 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]                    | Unknown  |
| 426 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]                    | Unknown  |
| 427 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]              | Unknown  |
| 428 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]                | Unknown  |
| 429 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]              | Unknown  |
| 430 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]                | Unknown  |
| 431 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                        | Unknown  |
| 432 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                        | Unknown  |
| 433 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                      | Unknown  |
| 434 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]                      | Unknown  |
| 435 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]                        | Unknown  |
| 436 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]                   | Unknown  |
| 437 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                      | Unknown  |
| 438 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                      | Unknown  |
| 439 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                        | Unknown  |
| 440 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                        | Unknown  |
| 441 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                      | Unknown  |
| 442 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, sym_size_int]        | Unknown  |
| 443 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]                    | Unknown  |
| 444 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]                    | Unknown  |
| 445 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]                   | Unknown  |
| 446 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]                       | Unknown  |
| 447 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]                     | Unknown  |
| 448 | Tensor<[64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]                    | Unknown  |
| 449 | Tensor<[64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                      | Unknown  |
| 450 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                            | Unknown  |
| 451 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]                      | Unknown  |
| 452 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]                        | Unknown  |
| 453 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]                              | Unknown  |
| 454 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]                        | Unknown  |
| 455 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]                        | Unknown  |
| 456 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]                        | Unknown  |
| 457 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]                      | Unknown  |
| 458 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]                      | Unknown  |
| 459 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                      | Unknown  |
| 460 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                        | Unknown  |
| 461 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                        | Unknown  |
| 462 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                      | Unknown  |
| 463 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, sym_size_int]        | Unknown  |
| 464 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]                    | Unknown  |
| 465 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]                    | Unknown  |
| 466 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]                | Unknown  |
| 467 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]                  | Unknown  |
| 468 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]                | Unknown  |
| 469 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]                  | Unknown  |
| 470 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]                        | Unknown  |
| 471 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]                          | Unknown  |
| 472 | Tensor<[9, 16384]> self = ?,<br>List[int] size = [1, 9, 16384]                      | Unknown  |
| 473 | Tensor<[9, 2048]> self = ?,<br>List[int] size = [1, 9, 2048]                        | Unknown  |
| 474 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]                      | Unknown  |
| 475 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]                        | Unknown  |
| 476 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]                        | Unknown  |
| 477 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]                          | Unknown  |
| 478 | Tensor<[9, 8192]> self = ?,<br>List[int] size = [1, 9, 8192]                        | Unknown  |
| 479 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]                    | Unknown  |
| 480 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]                      | Unknown  |
| 481 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]                    | Unknown  |
| 482 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]                      | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 5, 5]> condition = ?,<br>Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
|  1 | Tensor<[1, 1, 7, 7]> condition = ?,<br>Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
|  2 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?    | Unknown  |
|  3 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?    | Unknown  |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  |
|  1 | List[int] size = [1, 16, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  |
|  2 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  3 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
|  4 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False                                           | Unknown  |
|  1 | Tensor<[1, 920]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[bool] pin_memory = False | Unknown  |
|  2 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                                    | Unknown  |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                        | Unknown  |

