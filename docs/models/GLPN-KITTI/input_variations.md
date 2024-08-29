# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |
|  1 | aten._softmax.default                             |                  1 |
|  2 | aten._to_copy.default                             |                  1 |
|  3 | aten._unsafe_index.Tensor                         |                  5 |
|  4 | aten.add.Tensor                                   |                  2 |
|  5 | aten.addmm.default                                |                  1 |
|  6 | aten.arange.default                               |                  1 |
|  7 | aten.bmm.default                                  |                  1 |
|  8 | aten.cat.default                                  |                  1 |
|  9 | aten.ceil.default                                 |                  1 |
| 10 | aten.clamp.default                                |                 11 |
| 11 | aten.clone.default                                |                  2 |
| 12 | aten.convolution.default                          |                 11 |
| 13 | aten.div.Tensor                                   |                  1 |
| 14 | aten.expand.default                               |                 15 |
| 15 | aten.gelu.default                                 |                  1 |
| 16 | aten.mul.Tensor                                   |                  3 |
| 17 | aten.native_layer_norm.default                    |                  4 |
| 18 | aten.permute.default                              |                  3 |
| 19 | aten.relu.default                                 |                  1 |
| 20 | aten.rsub.Scalar                                  |                  1 |
| 21 | aten.select.int                                   |                  2 |
| 22 | aten.sigmoid.default                              |                  1 |
| 23 | aten.slice.Tensor                                 |                  3 |
| 24 | aten.squeeze.dim                                  |                  1 |
| 25 | aten.sub.Tensor                                   |                  2 |
| 26 | aten.t.default                                    |                  1 |
| 27 | aten.transpose.int                                |                  2 |
| 28 | aten.unsqueeze.default                            |                  1 |
| 29 | aten.view.default                                 |                 59 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[30]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_16, _to_copy_14] | Unknown  |
|  1 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_1, _to_copy_2]     | Unknown  |
|  2 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_19, _to_copy_18] | Unknown  |
|  3 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_6]     | Unknown  |
|  4 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_11, _to_copy_10]   | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ? | Unknown  |
|  1 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                         | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 30,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [convolution_84, add_86],<br>int dim = 1 | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[30]> self = ?   | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[120]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 59  | Unknown  |
|  1 | Tensor<[160]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 79  | Unknown  |
|  2 | Tensor<[240]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 119 | Unknown  |
|  3 | Tensor<[30]> self = ?,<br>Optional[number] min = 0.0                                  | Unknown  |
|  4 | Tensor<[30]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 14   | Unknown  |
|  5 | Tensor<[320]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 159 | Unknown  |
|  6 | Tensor<[40]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 19   | Unknown  |
|  7 | Tensor<[480]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 239 | Unknown  |
|  8 | Tensor<[60]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 29   | Unknown  |
|  9 | Tensor<[640]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 319 | Unknown  |
| 10 | Tensor<[80]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 39   | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?                                                          | Unknown  |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  1 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  2 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | Unknown  |
|  3 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | Unknown  |
|  4 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | Unknown  |
|  5 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  6 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  7 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  8 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | Unknown  |
|  9 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
| 10 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Unknown  |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Unknown  |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]       | Unknown  |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]       | Unknown  |
|  4 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]       | Unknown  |
|  5 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Unknown  |
|  6 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Unknown  |
|  7 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]       | Unknown  |
|  8 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Unknown  |
|  9 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Unknown  |
| 10 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]       | Unknown  |
| 11 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]       | Unknown  |
| 12 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Unknown  |
| 13 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Unknown  |
| 14 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]       | Unknown  |
### aten.gelu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 19200, 256]> self = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10        | Unknown  |
|  1 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ? | Unknown  |
|  2 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                   | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05    | Unknown  |
|  2 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Unknown  |
|  3 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  |
|  1 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
|  2 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  |
### aten.relu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 64, 30, 40]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[30, 1]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  |
|  1 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 2, 30, 40]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1    | Unknown  |
|  2 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1    | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ? | Unknown  |
|  1 | Tensor<[30]> self = ?,<br>Tensor other = 0.5           | Unknown  |
### aten.t.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[64, 64]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
|  1 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                 | Status   |
|---:|:--------------------------------------|:---------|
|  0 | Tensor<[30]> self = ?,<br>int dim = 1 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300] | Unknown  |
|  1 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]       | Unknown  |
|  2 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]         | Unknown  |
|  3 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]     | Unknown  |
|  4 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]    | Unknown  |
|  5 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]    | Unknown  |
|  6 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]  | Unknown  |
|  7 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]  | Unknown  |
|  8 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]       | Unknown  |
|  9 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Unknown  |
| 10 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]         | Unknown  |
| 11 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]       | Unknown  |
| 12 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]   | Unknown  |
| 13 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]     | Unknown  |
| 14 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]       | Unknown  |
| 15 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]   | Unknown  |
| 16 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]   | Unknown  |
| 17 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200] | Unknown  |
| 18 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160] | Unknown  |
| 19 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]           | Unknown  |
| 20 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]         | Unknown  |
| 21 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]           | Unknown  |
| 22 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]           | Unknown  |
| 23 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]             | Unknown  |
| 24 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]    | Unknown  |
| 25 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]     | Unknown  |
| 26 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]    | Unknown  |
| 27 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]         | Unknown  |
| 28 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]         | Unknown  |
| 29 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]   | Unknown  |
| 30 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]     | Unknown  |
| 31 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]       | Unknown  |
| 32 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]       | Unknown  |
| 33 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]     | Unknown  |
| 34 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]    | Unknown  |
| 35 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]    | Unknown  |
| 36 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]   | Unknown  |
| 37 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]       | Unknown  |
| 38 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]   | Unknown  |
| 39 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]     | Unknown  |
| 40 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]       | Unknown  |
| 41 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]       | Unknown  |
| 42 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]       | Unknown  |
| 43 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]         | Unknown  |
| 44 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]       | Unknown  |
| 45 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Unknown  |
| 46 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Unknown  |
| 47 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Unknown  |
| 48 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]           | Unknown  |
| 49 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]         | Unknown  |
| 50 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]           | Unknown  |
| 51 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]           | Unknown  |
| 52 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Unknown  |
| 53 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]         | Unknown  |
| 54 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]         | Unknown  |
| 55 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Unknown  |
| 56 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Unknown  |
| 57 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Unknown  |
| 58 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Unknown  |

