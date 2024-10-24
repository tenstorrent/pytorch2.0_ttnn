# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_functional.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._softmax.default                            |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten._softmax_backward_data.default              |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten._to_copy.default                            |                 12 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten._unsafe_index.Tensor                        |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten._unsafe_index_put.default                   |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten._unsafe_view.default                        |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.add.Tensor                                  |                 27 |          17 |         0 |          0 | 🚧          |    0.63 |
|  8 | aten.addmm.default                               |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  9 | aten.arange.default                              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.bmm.default                                 |                 15 |           8 |         0 |          0 | 🚧          |    0.53 |
| 11 | aten.cat.default                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.ceil.default                                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.clamp.default                               |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.clone.default                               |                 23 |          21 |         0 |          0 | 🚧          |    0.91 |
| 15 | aten.convolution.default                         |                 13 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.convolution_backward.default                |                 13 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.detach.default                              |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.div.Tensor                                  |                 11 |          11 |         0 |          0 | ✅          |    1    |
| 19 | aten.expand.default                              |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.gelu.default                                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 21 | aten.gelu_backward.default                       |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.mm.default                                  |                 35 |           4 |         0 |          0 | 🚧          |    0.11 |
| 23 | aten.mul.Tensor                                  |                 10 |          10 |         0 |          0 | ✅          |    1    |
| 24 | aten.native_batch_norm_backward.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.native_layer_norm.default                   |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 26 | aten.native_layer_norm_backward.default          |                  7 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.new_zeros.default                           |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.permute.default                             |                 41 |          25 |         0 |          0 | 🚧          |    0.61 |
| 29 | aten.rand.default                                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.relu.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 31 | aten.rsub.Scalar                                 |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 32 | aten.slice.Tensor                                |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 33 | aten.sub.Tensor                                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 34 | aten.sum.dim_IntList                             |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 35 | aten.t.default                                   |                 26 |          14 |         0 |          0 | 🚧          |    0.54 |
| 36 | aten.threshold_backward.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 37 | aten.transpose.int                               |                 37 |          16 |         0 |          0 | 🚧          |    0.43 |
| 38 | aten.unsqueeze.default                           |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 39 | aten.view.default                                |                112 |          77 |         0 |          0 | 🚧          |    0.69 |
***
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 256]> grad_output = ?,<br>Tensor<[1, 1, 16384, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 2, 4096, 256]> grad_output = ?,<br>Tensor<[1, 2, 4096, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 5, 1024, 256]> grad_output = ?,<br>Tensor<[1, 5, 1024, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 8, 256, 256]> grad_output = ?,<br>Tensor<[1, 8, 256, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 256, 64, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 256, 64, 64]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                            | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[256]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided                                                | None     | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]   | None     | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_index_put.default
|    | ATen Input Variations                                                                                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>],<br>Tensor<[1, 256, 128, 128]> values = ?,<br>bool accumulate = True   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[]> self = ?,<br>Tensor other = 1                                     | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 128]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[160]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[1024, 640]> mat1 = ?,<br>Tensor<[640, 160]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[160]> self = ?,<br>Tensor<[256, 160]> mat1 = ?,<br>Tensor<[160, 160]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 256]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[256]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 256]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[256]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[32]> self = ?,<br>Tensor<[16384, 128]> mat1 = ?,<br>Tensor<[128, 32]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[32]> self = ?,<br>Tensor<[16384, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[32]> self = ?,<br>Tensor<[256, 32]> mat1 = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[640]> self = ?,<br>Tensor<[1024, 160]> mat1 = ?,<br>Tensor<[160, 640]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[256, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[4096, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[4096, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number end = 128,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 256, 128, 128]>, <[1, 256, 128, 128]>, <[1, 256, 128, 128]>, <[1, 256, 128, 128]>],<br>int dim = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.ceil.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128]> self = ?  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clamp.default
|    | ATen Input Variations                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128]> self = ?,<br>Optional[number] min = 0.0                              | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 127 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 15  | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 31  | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 63  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?                                                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 160]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1024, 640]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 16384, 128]> self = ?                                                             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 16384, 32]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 2, 4096, 256]> self = ?                                                           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 256, 1024]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 256, 128, 128]> self = ?                                                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 256, 256]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 4096, 256]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 4096, 64]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 5, 1024, 256]> self = ?                                                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 8, 256, 256]> self = ?                                                            | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[150]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256     | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[640]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640     | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 16, 16]> grad_output = ?,<br>Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [1024],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024,<br>List[bool] output_mask = [True, True, True] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 128, 128, 128]> grad_output = ?,<br>Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [128],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128,<br>List[bool] output_mask = [True, True, True]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 150, 128, 128]> grad_output = ?,<br>Tensor<[1, 256, 128, 128]> input = ?,<br>Tensor<[150, 256, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [150],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 160, 16, 16]> grad_output = ?,<br>Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[160, 160, 2, 2]> weight = ?,<br>Optional[List[int]] bias_sizes = [160],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 160, 32, 32]> grad_output = ?,<br>Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[160, 64, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [160],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 128, 128]> grad_output = ?,<br>Tensor<[1, 1024, 128, 128]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 16, 16]> grad_output = ?,<br>Tensor<[1, 160, 32, 32]> input = ?,<br>Tensor<[256, 160, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [256],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 256, 64, 64]> grad_output = ?,<br>Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [256],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256,<br>List[bool] output_mask = [True, True, True]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 32, 128, 128]> grad_output = ?,<br>Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 7, 7]> weight = ?,<br>Optional[List[int]] bias_sizes = [32],<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 32, 16, 16]> grad_output = ?,<br>Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[32, 32, 8, 8]> weight = ?,<br>Optional[List[int]] bias_sizes = [32],<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 64, 16, 16]> grad_output = ?,<br>Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[64, 64, 4, 4]> weight = ?,<br>Optional[List[int]] bias_sizes = [64],<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 64, 64, 64]> grad_output = ?,<br>Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [64],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 640, 32, 32]> grad_output = ?,<br>Tensor<[1, 640, 32, 32]> input = ?,<br>Tensor<[640, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [640],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 640,<br>List[bool] output_mask = [True, True, True]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.detach.default
|    | ATen Input Variations               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 2, 4096, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 128, 128]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 5, 1024, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 8, 256, 256]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 640]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 128]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 1024]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 4096, 256]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu_backward.default
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 640]> grad_output = ?,<br>Tensor<[1, 1024, 640]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 128]> grad_output = ?,<br>Tensor<[1, 16384, 128]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 1024]> grad_output = ?,<br>Tensor<[1, 256, 1024]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 4096, 256]> grad_output = ?,<br>Tensor<[1, 4096, 256]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 640]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1024, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 160]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[128, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 640]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 160]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[16384, 128]> self = ?,<br>Tensor<[128, 32]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 128]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 256]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[256, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[256, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[256, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[256, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[256, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 128]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 16384]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 32]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[4096, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 4096]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 256]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[640, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[128]> self = ?,<br>Tensor other = 0.125                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[128]> self = ?,<br>Tensor other = 0.25                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                      | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_batch_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> grad_out = ?,<br>Tensor<[1, 256, 128, 128]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> running_mean = ?,<br>Optional[Tensor]<[256]> running_var = ?,<br>Optional[Tensor]<[256]> save_mean = ?,<br>Optional[Tensor]<[256]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>float eps = 1e-05  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>float eps = 1e-05  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 256, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>float eps = 1e-05      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 160]> grad_out = ?,<br>Tensor<[1, 1024, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Tensor<[1, 1024, 1]> mean = ?,<br>Tensor<[1, 1024, 1]> rstd = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[bool] output_mask = [True, True, True] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 32]> grad_out = ?,<br>Tensor<[1, 16384, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Tensor<[1, 16384, 1]> mean = ?,<br>Tensor<[1, 16384, 1]> rstd = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[bool] output_mask = [True, True, True]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 160]> grad_out = ?,<br>Tensor<[1, 256, 160]> input = ?,<br>List[int] normalized_shape = [160],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 256]> grad_out = ?,<br>Tensor<[1, 256, 256]> input = ?,<br>List[int] normalized_shape = [256],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 256, 32]> grad_out = ?,<br>Tensor<[1, 256, 32]> input = ?,<br>List[int] normalized_shape = [32],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[bool] output_mask = [True, True, True]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 64]> grad_out = ?,<br>Tensor<[1, 256, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[bool] output_mask = [True, True, True]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 4096, 64]> grad_out = ?,<br>Tensor<[1, 4096, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Tensor<[1, 4096, 1]> mean = ?,<br>Tensor<[1, 4096, 1]> rstd = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[bool] output_mask = [True, True, True]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 128, 128],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 32, 32],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 64, 64],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.rand.default
|    | ATen Input Variations                                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.relu.default
|    | ATen Input Variations               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128, 1]> self = ?,<br>number other = 1.0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[128]> self = ?,<br>number other = 1.0    | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 768  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 1024 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[128]> self = ?,<br>Tensor other = 0.5            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16384, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 4096, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1024, 160]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1024, 640]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[16384, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[16384, 32]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[256, 1024]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[256, 160]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[256, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[256, 32]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[256, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[4096, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[4096, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024, 160]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024, 256]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1024, 640]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[128, 32]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[160, 1024]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[160, 160]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[160, 256]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[160, 640]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[16384, 128]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[16384, 256]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[16384, 32]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[256, 1024]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[256, 160]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[256, 256]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[256, 32]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[256, 64]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[32, 128]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[32, 16384]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[32, 256]> self = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[32, 32]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[4096, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[4096, 64]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[64, 256]> self = ?    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[64, 4096]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[64, 64]> self = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[640, 160]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 128, 128]> grad_output = ?,<br>Tensor<[1, 256, 128, 128]> self = ?,<br>number threshold = 0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 16384, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 16384, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 2, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 4096, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 5, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 8, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[2, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[2, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[2, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[2, 4096, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[5, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[5, 1024, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[5, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[5, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[8, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[8, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[8, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[128]> self = ?,<br>int dim = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|     | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|----:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|   0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256] | Done     | N/A                 | N/A          | N/A               | N/A                |
|   1 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|   2 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|   3 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [256]                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   4 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|   5 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]   | None     | N/A                 | N/A          | N/A               | N/A                |
|   6 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|   7 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|   8 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|   9 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  10 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1024, 256]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  11 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  12 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  13 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  14 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  15 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  16 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  17 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  18 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] size = [1, 256, 256]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  19 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  20 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]     | None     | N/A                 | N/A          | N/A               | N/A                |
|  21 | Tensor<[1, 160, 256]> self = ?,<br>List[int] size = [1, 160, 16, 16]     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  22 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  23 | Tensor<[1, 160]> self = ?,<br>List[int] size = [160]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  24 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]   | None     | N/A                 | N/A          | N/A               | N/A                |
|  25 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  26 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  27 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [16384, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  28 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  29 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  30 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  31 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  32 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  33 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  34 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  35 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  36 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] size = [1, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  37 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  38 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  39 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16384] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  40 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]     | None     | N/A                 | N/A          | N/A               | N/A                |
|  41 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  42 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  43 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  44 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  45 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  46 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  47 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  48 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  49 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[int] size = [1, 256, 1024]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  50 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  51 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  52 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  53 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  54 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  55 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  56 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  57 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  58 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  59 | Tensor<[1, 256]> self = ?,<br>List[int] size = [256]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  60 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  61 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]       | None     | N/A                 | N/A          | N/A               | N/A                |
|  62 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  63 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  64 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 16, 16]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  65 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] size = [1, 1024, 160]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  66 | Tensor<[1, 32]> self = ?,<br>List[int] size = [32]                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  67 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  68 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  69 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  70 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  71 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  72 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  73 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  74 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  75 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  76 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]       | None     | N/A                 | N/A          | N/A               | N/A                |
|  77 | Tensor<[1, 64, 256]> self = ?,<br>List[int] size = [1, 64, 16, 16]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  78 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  79 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 4096, 64]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  80 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  81 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  82 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  83 | Tensor<[1, 640]> self = ?,<br>List[int] size = [640]                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  84 | Tensor<[1, 64]> self = ?,<br>List[int] size = [64]                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  85 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  86 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  87 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  88 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  89 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  90 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  91 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  92 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  93 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  94 | Tensor<[2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  95 | Tensor<[2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  96 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  97 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  98 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  99 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 100 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 101 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 102 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 103 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 104 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 105 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 106 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 107 | Tensor<[5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 108 | Tensor<[5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 109 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 110 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 111 | Tensor<[8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]       | Unknown  | N/A                 | N/A          | N/A               | N/A                |

