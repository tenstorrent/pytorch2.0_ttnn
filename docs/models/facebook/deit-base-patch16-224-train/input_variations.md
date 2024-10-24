# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax_backward_data.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._to_copy.default                   |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten._unsafe_view.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  4 | aten.add.Tensor                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.addmm.default                      |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.bmm.default                        |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  7 | aten.cat.default                        |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.clone.default                      |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  9 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.detach.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.div.Tensor                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.expand.default                     |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.gelu.default                       |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 15 | aten.gelu_backward.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.mm.default                         |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 17 | aten.native_layer_norm.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 18 | aten.native_layer_norm_backward.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.permute.default                    |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 20 | aten.select.int                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.select_backward.default            |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.slice.Tensor                       |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 23 | aten.slice_backward.default             |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.sum.dim_IntList                    |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.t.default                          |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 26 | aten.transpose.int                      |                  7 |           4 |         0 |          0 | 🚧          |    0.57 |
| 27 | aten.view.default                       |                 17 |          17 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 197]> grad_output = ?,<br>Tensor<[1, 12, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                           | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | None     | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[197, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 196, 768]>],<br>int dim = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?                                                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 768, 14, 14]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[List[int]] bias_sizes = [768],<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.detach.default
|    | ATen Input Variations              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 197]> self = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 3072]> grad_output = ?,<br>Tensor<[1, 197, 3072]> self = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[197, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[3072, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 3072]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 768]> grad_out = ?,<br>Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 197, 1]> mean = ?,<br>Tensor<[1, 197, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.select.int
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.select_backward.default
|    | ATen Input Variations                                                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 1,<br>int index = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 197, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 768],<br>int dim = 1,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1           | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True   | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[197, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[197, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1000, 768]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[197, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[197, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[3072, 768]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[768, 1000]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[768, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[768, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[12, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[12, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[12, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | Done     | N/A                 | N/A          | N/A               | N/A                |

