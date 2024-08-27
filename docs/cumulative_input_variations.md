# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._log_softmax.default                         |                  1 |
|  1 | aten._native_batch_norm_legit_no_training.default |                  2 |
|  2 | aten._softmax.default                             |                 13 |
|  3 | aten._to_copy.default                             |                 11 |
|  4 | aten._unsafe_index.Tensor                         |                  1 |
|  5 | aten._unsafe_view.default                         |                  7 |
|  6 | aten.add.Tensor                                   |                 24 |
|  7 | aten.addmm.default                                |                 15 |
|  8 | aten.all.default                                  |                  1 |
|  9 | aten.all.dim                                      |                  1 |
| 10 | aten.any.default                                  |                  1 |
| 11 | aten.arange.default                               |                  1 |
| 12 | aten.arange.start                                 |                  3 |
| 13 | aten.argmax.default                               |                  1 |
| 14 | aten.baddbmm.default                              |                  1 |
| 15 | aten.bitwise_not.default                          |                  1 |
| 16 | aten.bmm.default                                  |                 14 |
| 17 | aten.cat.default                                  |                  4 |
| 18 | aten.clamp.default                                |                  2 |
| 19 | aten.clone.default                                |                 28 |
| 20 | aten.convolution.default                          |                 17 |
| 21 | aten.cos.default                                  |                  1 |
| 22 | aten.cumsum.default                               |                  1 |
| 23 | aten.div.Tensor                                   |                 11 |
| 24 | aten.embedding.default                            |                 12 |
| 25 | aten.eq.Scalar                                    |                  3 |
| 26 | aten.eq.Tensor                                    |                  1 |
| 27 | aten.expand.default                               |                 44 |
| 28 | aten.floor.default                                |                  1 |
| 29 | aten.full.default                                 |                  2 |
| 30 | aten.gelu.default                                 |                  6 |
| 31 | aten.hardtanh.default                             |                  1 |
| 32 | aten.index.Tensor                                 |                  6 |
| 33 | aten.lift_fresh_copy.default                      |                  1 |
| 34 | aten.logical_not.default                          |                  1 |
| 35 | aten.masked_fill.Scalar                           |                  2 |
| 36 | aten.masked_fill.Tensor                           |                  1 |
| 37 | aten.max_pool2d_with_indices.default              |                  2 |
| 38 | aten.mean.dim                                     |                  5 |
| 39 | aten.min.default                                  |                  1 |
| 40 | aten.mm.default                                   |                  6 |
| 41 | aten.mul.Scalar                                   |                  2 |
| 42 | aten.mul.Tensor                                   |                 27 |
| 43 | aten.native_dropout.default                       |                  2 |
| 44 | aten.native_layer_norm.default                    |                 15 |
| 45 | aten.ne.Scalar                                    |                  1 |
| 46 | aten.neg.default                                  |                  2 |
| 47 | aten.ones.default                                 |                  1 |
| 48 | aten.permute.default                              |                 16 |
| 49 | aten.pow.Tensor_Scalar                            |                  7 |
| 50 | aten.pow.Tensor_Tensor                            |                  1 |
| 51 | aten.relu.default                                 |                  3 |
| 52 | aten.remainder.Scalar                             |                  1 |
| 53 | aten.repeat.default                               |                  1 |
| 54 | aten.rsqrt.default                                |                  1 |
| 55 | aten.rsub.Scalar                                  |                  7 |
| 56 | aten.select.int                                   |                  4 |
| 57 | aten.sigmoid.default                              |                  1 |
| 58 | aten.silu.default                                 |                  1 |
| 59 | aten.sin.default                                  |                  1 |
| 60 | aten.slice.Tensor                                 |                 28 |
| 61 | aten.split.Tensor                                 |                  2 |
| 62 | aten.squeeze.dim                                  |                  1 |
| 63 | aten.sub.Tensor                                   |                  5 |
| 64 | aten.t.default                                    |                 14 |
| 65 | aten.tanh.default                                 |                  7 |
| 66 | aten.transpose.int                                |                 19 |
| 67 | aten.tril.default                                 |                  1 |
| 68 | aten.unsqueeze.default                            |                 20 |
| 69 | aten.view.default                                 |                162 |
| 70 | aten.where.self                                   |                  1 |
| 71 | aten.zeros_like.default                           |                  1 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Unknown  |
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
|  1 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
|  2 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  3 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
|  4 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  5 | Tensor<[1, 32, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
|  6 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
|  7 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
|  8 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
|  9 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 10 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  |
| 11 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
| 12 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                | Unknown  |
|  1 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  |
|  3 | Tensor<[1, 1, 1, 256]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  |
|  4 | Tensor<[1, 7]> self = ?,<br>Optional[int] dtype = torch.int32                                                                                       | Unknown  |
|  5 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  6 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  |
|  7 | Tensor<[1, 1, 1, 12]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  |
|  8 | Tensor<[1, 1, 1, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                              | Unknown  |
|  9 | Tensor<[16, 1, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                               | Unknown  |
| 10 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                        | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 50, 83]> self = ?,<br>List[Optional[Tensor]] indices = [view_2, view_3, clamp, clamp_1] | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] size = [1, 9, 1024]   | Unknown  |
|  1 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536] | Unknown  |
|  2 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 768]  | Unknown  |
|  3 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] size = [1, 9, 4096]   | Unknown  |
|  4 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544]   | Unknown  |
|  5 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] size = [1, 9, 768]    | Unknown  |
|  6 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] size = [1, 9, 2048]  | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                        | Unknown  |
|  1 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                        | Unknown  |
|  2 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
|  3 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
|  4 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?             | Unknown  |
|  5 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?           | Unknown  |
|  6 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?             | Unknown  |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ?   | Unknown  |
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
|  9 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?         | Unknown  |
| 10 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ? | Unknown  |
| 11 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ?       | Unknown  |
| 12 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 13 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 14 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Unknown  |
| 15 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?         | Unknown  |
| 16 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?       | Unknown  |
| 17 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?   | Unknown  |
| 18 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?     | Unknown  |
| 19 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                      | Unknown  |
| 20 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  |
| 21 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                       | Unknown  |
| 22 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?           | Unknown  |
| 23 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ?     | Unknown  |
|  1 | Tensor<[4096]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 4096]> mat2 = ?     | Unknown  |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
|  3 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ?     | Unknown  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[12, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?      | Unknown  |
|  5 | Tensor<[2048]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 2048]> mat2 = ?     | Unknown  |
|  6 | Tensor<[2304]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ?     | Unknown  |
|  7 | Tensor<[768]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  |
|  8 | Tensor<[4608]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 4608]> mat2 = ?  | Unknown  |
|  9 | Tensor<[1024]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
| 10 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ?   | Unknown  |
| 11 | Tensor<[192]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?    | Unknown  |
| 12 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
| 13 | Tensor<[1024]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 1024]> mat2 = ?     | Unknown  |
| 14 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?       | Unknown  |
### aten.all.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ? | Unknown  |
### aten.all.dim
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = -1 | Unknown  |
### aten.any.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 1,<br>number end = 17,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                       | Unknown  |
|  2 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  |
### aten.argmax.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = -1 | Unknown  |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 32]> self = ?,<br>Tensor<[16, 32, 96]> batch1 = ?,<br>Tensor<[16, 96, 32]> batch2 = ?,<br>number beta = 1.0,<br>number alpha = 0.10206207261596577 | Unknown  |
### aten.bitwise_not.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 1]> self = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ? | Unknown  |
|  1 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?     | Unknown  |
|  2 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?     | Unknown  |
|  3 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ? | Unknown  |
|  4 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ? | Unknown  |
|  5 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ?     | Unknown  |
|  6 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?   | Unknown  |
|  7 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ? | Unknown  |
|  8 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?     | Unknown  |
|  9 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?   | Unknown  |
| 10 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?   | Unknown  |
| 11 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?   | Unknown  |
| 12 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?       | Unknown  |
| 13 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?     | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [expand, transpose, expand_1],<br>int dim = 1 | Unknown  |
|  1 | List[Tensor] tensors = [expand, transpose],<br>int dim = 1           | Unknown  |
|  2 | List[Tensor] tensors = [neg, slice_1],<br>int dim = -1               | Unknown  |
|  3 | List[Tensor] tensors = [transpose_3, transpose_3],<br>int dim = -1   | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 49 | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 82 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> self = ?                                                             | Unknown  |
|  1 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Unknown  |
|  3 | Tensor<[1, 16, 32, 32]> self = ?                                                            | Unknown  |
|  4 | Tensor<[1, 9, 128]> self = ?                                                                | Unknown  |
|  5 | Tensor<[1, 32, 32, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  6 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  7 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
|  8 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  |
|  9 | Tensor<[1, 64, 12, 12]> self = ?                                                            | Unknown  |
| 10 | Tensor<[1, 197, 1024]> self = ?                                                             | Unknown  |
| 11 | Tensor<[1, 16, 768]> self = ?                                                               | Unknown  |
| 12 | Tensor<[1, 1280]> self = ?                                                                  | Unknown  |
| 13 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  |
| 14 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  |
| 15 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
| 16 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  |
| 17 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
| 18 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
| 19 | Tensor<[1, 7, 768]> self = ?                                                                | Unknown  |
| 20 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
| 21 | Tensor<[1, 256, 1024]> self = ?                                                             | Unknown  |
| 22 | Tensor<[1, 7, 4544]> self = ?                                                               | Unknown  |
| 23 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last     | Unknown  |
| 24 | Tensor<[1, 12, 128]> self = ?                                                               | Unknown  |
| 25 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
| 26 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
| 27 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32          | Unknown  |
|  1 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[384, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 384         | Unknown  |
|  2 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144         | Unknown  |
|  3 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192         | Unknown  |
|  4 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
|  5 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  6 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
|  7 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
|  8 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576         | Unknown  |
|  9 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
| 10 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 11 | Tensor<[1, 3, 512, 672]> input = ?,<br>Tensor<[192, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 12 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  |
| 13 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  |
| 14 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96          | Unknown  |
| 15 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960           | Unknown  |
| 16 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  |
### aten.cos.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>int dim = -1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0              | Unknown  |
|  1 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0           | Unknown  |
|  2 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                | Unknown  |
|  3 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0              | Unknown  |
|  4 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0            | Unknown  |
|  5 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?              | Unknown  |
|  6 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                | Unknown  |
|  7 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761 | Unknown  |
|  8 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0            | Unknown  |
|  9 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                | Unknown  |
| 10 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0            | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                           | Unknown  |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0    | Unknown  |
|  2 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Unknown  |
|  3 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0 | Unknown  |
|  4 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0  | Unknown  |
|  5 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                             | Unknown  |
|  6 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0   | Unknown  |
|  7 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0   | Unknown  |
|  8 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                             | Unknown  |
|  9 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                               | Unknown  |
| 10 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                | Unknown  |
| 11 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                         | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1     | Unknown  |
|  1 | Tensor<[1, 7]> self = ?,<br>number other = 50256 | Unknown  |
|  2 | Tensor<[1, 16]> self = ?,<br>number other = 0    | Unknown  |
### aten.eq.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]     | Unknown  |
|  1 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [1, 64, 64, 9]         | Unknown  |
|  2 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]       | Unknown  |
|  3 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]         | Unknown  |
|  4 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12]       | Unknown  |
|  5 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]           | Unknown  |
|  6 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]     | Unknown  |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128]     | Unknown  |
|  8 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]           | Unknown  |
|  9 | Tensor<[1, 1, 192]> self = ?,<br>List[int] size = [1, -1, -1]               | Unknown  |
| 10 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [1, 16, 128, 9]       | Unknown  |
| 11 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]         | Unknown  |
| 12 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]               | Unknown  |
| 13 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]              | Unknown  |
| 14 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]     | Unknown  |
| 15 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]           | Unknown  |
| 16 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]         | Unknown  |
| 17 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]         | Unknown  |
| 18 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]   | Unknown  |
| 19 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]   | Unknown  |
| 20 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]           | Unknown  |
| 21 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]       | Unknown  |
| 22 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]     | Unknown  |
| 23 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                 | Unknown  |
| 24 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]     | Unknown  |
| 25 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]     | Unknown  |
| 26 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]                 | Unknown  |
| 27 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445] | Unknown  |
| 28 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [1, 12, 64, 16]       | Unknown  |
| 29 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]         | Unknown  |
| 30 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]     | Unknown  |
| 31 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]   | Unknown  |
| 32 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [1, 12, 64, 9]         | Unknown  |
| 33 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [1, 32, 128, 32]     | Unknown  |
| 34 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]       | Unknown  |
| 35 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [1, 3, 64, 1445]     | Unknown  |
| 36 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7]         | Unknown  |
| 37 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]       | Unknown  |
| 38 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]          | Unknown  |
| 39 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [1, 16, 64, 9]         | Unknown  |
| 40 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]           | Unknown  |
| 41 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]         | Unknown  |
| 42 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]         | Unknown  |
| 43 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]       | Unknown  |
### aten.floor.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ? | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [],<br>number fill_value = 8.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
|  1 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 16, 3072]> self = ?  | Unknown  |
|  1 | Tensor<[1, 197, 4096]> self = ? | Unknown  |
|  2 | Tensor<[1, 1445, 768]> self = ? | Unknown  |
|  3 | Tensor<[1, 197, 3072]> self = ? | Unknown  |
|  4 | Tensor<[1, 256, 4096]> self = ? | Unknown  |
|  5 | Tensor<[1, 7, 18176]> self = ?  | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 112, 112]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [primals_2]                          | Unknown  |
|  1 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, lift_fresh_copy] | Unknown  |
|  2 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [view_13]                          | Unknown  |
|  3 | Tensor<[1, 1, 2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, arg324_1]      | Unknown  |
|  4 | Tensor<[1, 7, 2]> self = ?,<br>List[Optional[Tensor]] indices = [arange_1, remainder]              | Unknown  |
|  5 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [view_13]                          | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.logical_not.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf                                    | Unknown  |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  |
### aten.masked_fill.Tensor
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?,<br>Tensor<[1, 12, 16, 16]> mask = ?,<br>Tensor<[]> value = ? | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2]                                                                | Unknown  |
|  1 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True       | Unknown  |
|  1 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
|  2 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1]                               | Unknown  |
|  3 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Unknown  |
|  4 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1]                                | Unknown  |
### aten.min.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ?         | Unknown  |
|  1 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Unknown  |
|  2 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Unknown  |
|  3 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  |
|  4 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  |
|  5 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ?    | Unknown  |
### aten.mul.Scalar
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738    | Unknown  |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>number other = 0.29730177875068026 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Unknown  |
|  2 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
|  3 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  4 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625                       | Unknown  |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763           | Unknown  |
|  6 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.4028234663852886e+38       | Unknown  |
|  7 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.4028234663852886e+38      | Unknown  |
|  8 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
|  9 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Unknown  |
| 10 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Unknown  |
| 11 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  |
| 12 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
| 13 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Unknown  |
| 14 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
| 15 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Unknown  |
| 16 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Unknown  |
| 17 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Unknown  |
| 18 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Unknown  |
| 19 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  |
| 20 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  |
| 21 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  |
| 22 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Unknown  |
| 23 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  |
| 24 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Unknown  |
| 25 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Unknown  |
| 26 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?      | Unknown  |
### aten.native_dropout.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128]> input = ?,<br>float p = 0.5,<br>Optional[bool] train = True         | Unknown  |
|  1 | Tensor<[1, 64, 12, 12]> input = ?,<br>float p = 0.25,<br>Optional[bool] train = True | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-12    | Unknown  |
|  1 | Tensor<[1, 12, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12      | Unknown  |
|  2 | Tensor<[1, 9, 2048]> input = ?,<br>List[int] normalized_shape = [2048],<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>float eps = 1e-12   | Unknown  |
|  3 | Tensor<[1, 9, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12   | Unknown  |
|  4 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12     | Unknown  |
|  5 | Tensor<[1, 9, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12       | Unknown  |
|  6 | Tensor<[1, 9, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12       | Unknown  |
|  7 | Tensor<[1, 9, 4096]> input = ?,<br>List[int] normalized_shape = [4096],<br>Optional[Tensor]<[4096]> weight = ?,<br>Optional[Tensor]<[4096]> bias = ?,<br>float eps = 1e-12   | Unknown  |
|  8 | Tensor<[1, 32, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05  | Unknown  |
|  9 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Unknown  |
| 10 | Tensor<[1, 256, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Unknown  |
| 11 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05   | Unknown  |
| 12 | Tensor<[1, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05       | Unknown  |
| 13 | Tensor<[1, 12, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Unknown  |
| 14 | Tensor<[1, 16, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>number other = 1 | Unknown  |
### aten.neg.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 32]> self = ?  | Unknown  |
|  1 | Tensor<[1, 32, 32, 64]> self = ? | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [7, 7],<br>Optional[int] dtype = torch.bool,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  |
|  2 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  |
|  3 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  |
|  4 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  |
|  5 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]      | Unknown  |
|  6 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
|  7 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]           | Unknown  |
|  8 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  |
|  9 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  |
| 10 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  |
| 11 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  |
| 12 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
| 13 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
| 14 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]      | Unknown  |
| 15 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>number exponent = 2   | Unknown  |
|  1 | Tensor<[1, 9, 8192]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  2 | Tensor<[1, 9, 4096]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  3 | Tensor<[1, 9, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  4 | Tensor<[1, 7, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  5 | Tensor<[1, 9, 16384]> self = ?,<br>number exponent = 3.0 | Unknown  |
|  6 | Tensor<[1, 12, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
### aten.pow.Tensor_Tensor
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>Tensor<[16]> exponent = ? | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 100, 192]> self = ?     | Unknown  |
|  1 | Tensor<[1, 32, 26, 26]> self = ?   | Unknown  |
|  2 | Tensor<[1, 64, 112, 112]> self = ? | Unknown  |
### aten.remainder.Scalar
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number other = 7 | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[1, 32, 1]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0   | Unknown  |
|  1 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0   | Unknown  |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0  | Unknown  |
|  3 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0 | Unknown  |
|  4 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0  | Unknown  |
|  5 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0  | Unknown  |
|  6 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Unknown  |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Unknown  |
|  2 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Unknown  |
|  3 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 100, 4]> self = ? | Unknown  |
### aten.silu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 32, 11008]> self = ? | Unknown  |
### aten.sin.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1            | Unknown  |
|  1 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = -1  | Unknown  |
|  2 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1           | Unknown  |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256          | Unknown  |
|  4 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1      | Unknown  |
|  5 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1           | Unknown  |
|  6 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1           | Unknown  |
|  7 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  8 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = -1     | Unknown  |
|  9 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
| 10 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
| 11 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
| 12 | Tensor<[1, 100, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1      | Unknown  |
| 13 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1       | Unknown  |
| 14 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
| 15 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1         | Unknown  |
| 16 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
| 17 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7     | Unknown  |
| 18 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7          | Unknown  |
| 19 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
| 20 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1            | Unknown  |
| 21 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2     | Unknown  |
| 22 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1             | Unknown  |
| 23 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
| 24 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32     | Unknown  |
| 25 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64   | Unknown  |
| 26 | Tensor<[1, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1           | Unknown  |
| 27 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1      | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1   | Unknown  |
|  1 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 1]> self = ?,<br>int dim = -1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>Tensor other = 1                          | Unknown  |
|  1 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  2 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                | Unknown  |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5              | Unknown  |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[65024, 4544]> self = ? | Unknown  |
|  1 | Tensor<[1024, 128]> self = ?   | Unknown  |
|  2 | Tensor<[4608, 1536]> self = ?  | Unknown  |
|  3 | Tensor<[4096, 128]> self = ?   | Unknown  |
|  4 | Tensor<[1000, 1280]> self = ?  | Unknown  |
|  5 | Tensor<[2, 768]> self = ?      | Unknown  |
|  6 | Tensor<[1024, 1024]> self = ?  | Unknown  |
|  7 | Tensor<[128, 9216]> self = ?   | Unknown  |
|  8 | Tensor<[768, 768]> self = ?    | Unknown  |
|  9 | Tensor<[1000, 512]> self = ?   | Unknown  |
| 10 | Tensor<[192, 192]> self = ?    | Unknown  |
| 11 | Tensor<[4096, 4096]> self = ?  | Unknown  |
| 12 | Tensor<[768, 128]> self = ?    | Unknown  |
| 13 | Tensor<[2048, 128]> self = ?   | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 9, 4096]> self = ?  | Unknown  |
|  1 | Tensor<[1, 32, 6144]> self = ? | Unknown  |
|  2 | Tensor<[1, 9, 16384]> self = ? | Unknown  |
|  3 | Tensor<[1, 9, 8192]> self = ?  | Unknown  |
|  4 | Tensor<[1, 7, 3072]> self = ?  | Unknown  |
|  5 | Tensor<[1, 9, 3072]> self = ?  | Unknown  |
|  6 | Tensor<[1, 12, 3072]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
|  1 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
|  2 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
|  3 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
|  4 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
|  5 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
|  6 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  |
|  7 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  |
|  8 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Unknown  |
|  9 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 10 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3    | Unknown  |
| 11 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
| 12 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 13 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
| 14 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1    | Unknown  |
| 15 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 16 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
| 17 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2   | Unknown  |
| 18 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.tril.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | Unknown  |
|  1 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2       | Unknown  |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1         | Unknown  |
|  3 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0  | Unknown  |
|  4 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 3    | Unknown  |
|  5 | Tensor<[1, 12]> self = ?,<br>int dim = 1         | Unknown  |
|  6 | Tensor<[1, 192]> self = ?,<br>int dim = 1        | Unknown  |
|  7 | Tensor<[1, 7]> self = ?,<br>int dim = 1          | Unknown  |
|  8 | Tensor<[1, 256]> self = ?,<br>int dim = 1        | Unknown  |
|  9 | Tensor<[7]> self = ?,<br>int dim = 0             | Unknown  |
| 10 | Tensor<[32, 32]> self = ?,<br>int dim = 0        | Unknown  |
| 11 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2     | Unknown  |
| 12 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1      | Unknown  |
| 13 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2      | Unknown  |
| 14 | Tensor<[1, 9]> self = ?,<br>int dim = 1          | Unknown  |
| 15 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2       | Unknown  |
| 16 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0  | Unknown  |
| 17 | Tensor<[32]> self = ?,<br>int dim = 0            | Unknown  |
| 18 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Unknown  |
| 19 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2      | Unknown  |
### aten.view.default
|     | ATen Input Variations                                                    | Status   |
|----:|:-------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]     | Unknown  |
|   1 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]       | Unknown  |
|   2 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]         | Unknown  |
|   3 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]             | Unknown  |
|   4 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]          | Unknown  |
|   5 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]             | Unknown  |
|   6 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768]         | Unknown  |
|   7 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [16, 9, 128]       | Unknown  |
|   8 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280]          | Unknown  |
|   9 | Tensor<[9, 16384]> self = ?,<br>List[int] size = [1, 9, 16384]           | Unknown  |
|  10 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]             | Unknown  |
|  11 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]               | Unknown  |
|  12 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]             | Unknown  |
|  13 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]           | Unknown  |
|  14 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]           | Unknown  |
|  15 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]         | Unknown  |
|  16 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]           | Unknown  |
|  17 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]           | Unknown  |
|  18 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]         | Unknown  |
|  19 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]         | Unknown  |
|  20 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]     | Unknown  |
|  21 | Tensor<[32, 4096]> self = ?,<br>List[int] size = [1, 32, 4096]           | Unknown  |
|  22 | Tensor<[32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]       | Unknown  |
|  23 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]       | Unknown  |
|  24 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]           | Unknown  |
|  25 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]           | Unknown  |
|  26 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445] | Unknown  |
|  27 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445] | Unknown  |
|  28 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [64, 9, 9]           | Unknown  |
|  29 | Tensor<[192]> self = ?,<br>List[int] size = [1, 192, 1, 1]               | Unknown  |
|  30 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16]       | Unknown  |
|  31 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]             | Unknown  |
|  32 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]     | Unknown  |
|  33 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]     | Unknown  |
|  34 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]         | Unknown  |
|  35 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]           | Unknown  |
|  36 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]            | Unknown  |
|  37 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]         | Unknown  |
|  38 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]             | Unknown  |
|  39 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]     | Unknown  |
|  40 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]       | Unknown  |
|  41 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]           | Unknown  |
|  42 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [64, 64, 9]         | Unknown  |
|  43 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]     | Unknown  |
|  44 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]               | Unknown  |
|  45 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]     | Unknown  |
|  46 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]         | Unknown  |
|  47 | Tensor<[9, 2048]> self = ?,<br>List[int] size = [1, 9, 2048]             | Unknown  |
|  48 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [32, 32, 128]     | Unknown  |
|  49 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256]   | Unknown  |
|  50 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197]   | Unknown  |
|  51 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]         | Unknown  |
|  52 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]             | Unknown  |
|  53 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]           | Unknown  |
|  54 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]                 | Unknown  |
|  55 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]        | Unknown  |
|  56 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]      | Unknown  |
|  57 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]    | Unknown  |
|  58 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64]       | Unknown  |
|  59 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]               | Unknown  |
|  60 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]           | Unknown  |
|  61 | Tensor<[32]> self = ?,<br>List[int] size = [1, 1, 32, 1]                 | Unknown  |
|  62 | Tensor<[32, 11008]> self = ?,<br>List[int] size = [1, 32, 11008]         | Unknown  |
|  63 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]         | Unknown  |
|  64 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]           | Unknown  |
|  65 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]     | Unknown  |
|  66 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]       | Unknown  |
|  67 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]         | Unknown  |
|  68 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16]       | Unknown  |
|  69 | Tensor<[42]> self = ?,<br>List[int] size = [1, 1, 1, 42]                 | Unknown  |
|  70 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]           | Unknown  |
|  71 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]       | Unknown  |
|  72 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [16, 128, 9]       | Unknown  |
|  73 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]           | Unknown  |
|  74 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]   | Unknown  |
|  75 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]                   | Unknown  |
|  76 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]           | Unknown  |
|  77 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]           | Unknown  |
|  78 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [64, 9, 64]         | Unknown  |
|  79 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]             | Unknown  |
|  80 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512]            | Unknown  |
|  81 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]           | Unknown  |
|  82 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]               | Unknown  |
|  83 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]         | Unknown  |
|  84 | Tensor<[32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128]     | Unknown  |
|  85 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]         | Unknown  |
|  86 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]             | Unknown  |
|  87 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [32, 4096]           | Unknown  |
|  88 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]         | Unknown  |
|  89 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]     | Unknown  |
|  90 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]   | Unknown  |
|  91 | Tensor<[1, 9, 8192]> self = ?,<br>List[int] size = [9, 8192]             | Unknown  |
|  92 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]              | Unknown  |
|  93 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]           | Unknown  |
|  94 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]             | Unknown  |
|  95 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196]   | Unknown  |
|  96 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]         | Unknown  |
|  97 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]     | Unknown  |
|  98 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64]         | Unknown  |
|  99 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [9, 2048]             | Unknown  |
| 100 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]         | Unknown  |
| 101 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]              | Unknown  |
| 102 | Tensor<[32, 32000]> self = ?,<br>List[int] size = [1, 32, 32000]         | Unknown  |
| 103 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]           | Unknown  |
| 104 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]     | Unknown  |
| 105 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]               | Unknown  |
| 106 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [32, 32, 32]       | Unknown  |
| 107 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]       | Unknown  |
| 108 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]         | Unknown  |
| 109 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]           | Unknown  |
| 110 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]    | Unknown  |
| 111 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]             | Unknown  |
| 112 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]            | Unknown  |
| 113 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [32, 128, 32]     | Unknown  |
| 114 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]             | Unknown  |
| 115 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]             | Unknown  |
| 116 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96]   | Unknown  |
| 117 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]           | Unknown  |
| 118 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]              | Unknown  |
| 119 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]           | Unknown  |
| 120 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]           | Unknown  |
| 121 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7]         | Unknown  |
| 122 | Tensor<[64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]         | Unknown  |
| 123 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]             | Unknown  |
| 124 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]             | Unknown  |
| 125 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]         | Unknown  |
| 126 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12]       | Unknown  |
| 127 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197]   | Unknown  |
| 128 | Tensor<[64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]           | Unknown  |
| 129 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64]         | Unknown  |
| 130 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]       | Unknown  |
| 131 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]           | Unknown  |
| 132 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]             | Unknown  |
| 133 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]     | Unknown  |
| 134 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]         | Unknown  |
| 135 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]           | Unknown  |
| 136 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]              | Unknown  |
| 137 | Tensor<[1, 9, 16384]> self = ?,<br>List[int] size = [9, 16384]           | Unknown  |
| 138 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]         | Unknown  |
| 139 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]            | Unknown  |
| 140 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]         | Unknown  |
| 141 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]         | Unknown  |
| 142 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]                     | Unknown  |
| 143 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]       | Unknown  |
| 144 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]       | Unknown  |
| 145 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]       | Unknown  |
| 146 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]   | Unknown  |
| 147 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]           | Unknown  |
| 148 | Tensor<[16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]       | Unknown  |
| 149 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]             | Unknown  |
| 150 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                    | Unknown  |
| 151 | Tensor<[1]> self = ?,<br>List[int] size = [1, 1, 1, 1]                   | Unknown  |
| 152 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64]       | Unknown  |
| 153 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9]         | Unknown  |
| 154 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12]       | Unknown  |
| 155 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]         | Unknown  |
| 156 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]     | Unknown  |
| 157 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]       | Unknown  |
| 158 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]        | Unknown  |
| 159 | Tensor<[9, 8192]> self = ?,<br>List[int] size = [1, 9, 8192]             | Unknown  |
| 160 | Tensor<[1, 32, 11008]> self = ?,<br>List[int] size = [32, 11008]         | Unknown  |
| 161 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]               | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 7]> condition = ?,<br>Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  |

