# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._softmax.default                             |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._to_copy.default                             |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten._unsafe_index.Tensor                         |                 20 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.add.Tensor                                   |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.addmm.default                                |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.bmm.default                                  |                  8 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.cat.default                                  |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.clone.default                                |                 19 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.convolution.default                          |                 25 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.div.Tensor                                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.expand.default                               |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.gelu.default                                 |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.mul.Tensor                                   |                 19 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.native_layer_norm.default                    |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.permute.default                              |                 21 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.relu.default                                 |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.rsub.Scalar                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.select.int                                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.sigmoid.default                              |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.slice.Tensor                                 |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.squeeze.dim                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.t.default                                    |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.transpose.int                                |                 16 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.unsqueeze.default                            |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.view.default                                 |                 78 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 120, 160]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  | Done       | 0.999988 |      0 |
|  1 | Tensor<[1, 32, 30, 40]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Unknown  | Done       | 0.99999  |      0 |
|  2 | Tensor<[1, 32, 60, 80]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Unknown  | Done       | 0.99999  |      0 |
|  3 | Tensor<[1, 64, 120, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  | Done       | 0.999986 |      0 |
|  4 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Unknown  | Done       | 0.99999  |      0 |
|  5 | Tensor<[1, 64, 60, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Unknown  | Done       | 0.999987 |      0 |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999594 |      0 |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Done       | 0.999596 |      0 |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Done       | 0.999595 |      0 |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Done       | 0.999597 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.float32  | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 64, 15, 20]> self = ?,<br>Optional[int] dtype = torch.float32    | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.float32  | Unknown  | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Unknown  | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.float32    | Unknown  | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Unknown  | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.float32    | Unknown  | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_21] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_22] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_21] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_22] | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_3]     | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_4]     | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_3]     | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_4]     | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_27] | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_28] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_27] | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_28] | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_10]    | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_9]     | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_10]    | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_9]     | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_15]   | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_16]   | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_15]   | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_16]   | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?         | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ? | Unknown  | Done       | 0.999976 |      0 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[300, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?    | Unknown  | Done       | 0.999982 |      0 |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Unknown  | Done       | 0.999979 |      0 |
|  3 | Tensor<[128]> self = ?,<br>Tensor<[4800, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Unknown  | Done       | 0.99997  |      0 |
|  4 | Tensor<[2048]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Unknown  | Done       | 0.99997  |      0 |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Unknown  | Done       | 0.999985 |      0 |
|  6 | Tensor<[320]> self = ?,<br>Tensor<[1200, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ? | Unknown  | Done       | 0.999962 |      0 |
|  7 | Tensor<[320]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?   | Unknown  | Done       | 0.999973 |      0 |
|  8 | Tensor<[320]> self = ?,<br>Tensor<[300, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?    | Unknown  | Done       | 0.999977 |      0 |
|  9 | Tensor<[512]> self = ?,<br>Tensor<[300, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Unknown  | Done       | 0.99992  |      0 |
| 10 | Tensor<[512]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Unknown  | Done       | 0.99997  |      0 |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Unknown  | Done       | 0.999979 |      0 |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[19200, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Unknown  | Done       | 0.999974 |      0 |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Unknown  | Done       | 0.999985 |      0 |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[300, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?        | Unknown  | Done       | 0.999985 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ? | Unknown  | Done       | 0.999976 |      0 |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?  | Unknown  | Done       | 0.999986 |      0 |
|  2 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?  | Unknown  | Done       | 0.999976 |      0 |
|  3 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?   | Unknown  | Done       | 0.999986 |      0 |
|  4 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?  | Unknown  | Done       | 0.999976 |      0 |
|  5 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?   | Unknown  | Done       | 0.999986 |      0 |
|  6 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?   | Unknown  | Done       | 0.99998  |      0 |
|  7 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?    | Unknown  | Done       | 0.999986 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 64, 120, 160]>, <[1, 64, 120, 160]>],<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 64, 30, 40]>, <[1, 64, 30, 40]>],<br>int dim = 1     | Unknown  | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[1, 64, 60, 80]>, <[1, 64, 60, 80]>],<br>int dim = 1     | Unknown  | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?                                                          | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1200, 1280]> self = ?                                                             | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 1200, 320]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 19200, 256]> self = ?                                                             | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 19200, 64]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 2, 4800, 300]> self = ?                                                           | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 300, 2048]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 300, 512]> self = ?                                                               | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[1, 4800, 128]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[1, 4800, 512]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
| 15 | Tensor<[1, 5, 1200, 300]> self = ?                                                           | Unknown  | Done       |     1 |      0 |
| 16 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
| 17 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
| 18 | Tensor<[1, 8, 300, 300]> self = ?                                                            | Unknown  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 128, 120, 160]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999812 |      1 |
|  1 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999816 |      1 |
|  2 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999604 |      1 |
|  3 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[320, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999813 |      1 |
|  4 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999978 |      1 |
|  5 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999815 |      1 |
|  6 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | Unknown  | Done       | 0.999983 |      1 |
|  7 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | Unknown  | Done       | 0.999984 |      1 |
|  8 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | Unknown  | Done       | 0.999983 |      1 |
|  9 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999   |      1 |
| 10 | Tensor<[1, 32, 120, 160]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.99996  |      1 |
| 11 | Tensor<[1, 32, 30, 40]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.99996  |      1 |
| 12 | Tensor<[1, 32, 60, 80]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Done       | 0.999961 |      1 |
| 13 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999786 |      1 |
| 14 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[512, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999397 |      1 |
| 15 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[64, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999973 |      1 |
| 16 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.99997  |      1 |
| 17 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | Unknown  | Done       | 0.999983 |      1 |
| 18 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999918 |      1 |
| 19 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999918 |      1 |
| 20 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999002 |      1 |
| 21 | Tensor<[1, 64, 30, 40]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999919 |      1 |
| 22 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[1, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Fallback   | 1        |     -1 |
| 23 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Fallback   | 1        |     -1 |
| 24 | Tensor<[1, 64, 60, 80]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999919 |      1 |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0   | Unknown  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]       | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]       | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]       | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]       | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Unknown  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]       | Unknown  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]       | Unknown  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Unknown  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Unknown  | Done       |     1 |     -1 |
| 14 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]       | Unknown  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1200, 1280]> self = ? | Unknown  | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 19200, 256]> self = ? | Unknown  | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 300, 2048]> self = ?  | Unknown  | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 4800, 512]> self = ?  | Unknown  | Done       | 0.999991 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                   | Unknown  | Done       | 0.9999985733058784 | 0      |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                   | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ? | Unknown  | Done       | 0.9999959801900722 | 0      |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?         | Unknown  | Done       | 0.9999959246980075 | 0      |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?            | Unknown  | Done       | 0.9999957977579713 | 0      |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                   | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?         | Unknown  | Done       | 0.9999959201978406 | 0      |
|  7 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?            | Unknown  | Done       | 0.9999958393038825 | 0      |
|  8 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                     | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?     | Unknown  | Done       | 0.9999959692503947 | 0      |
| 10 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?            | Unknown  | Done       | 0.9999958132245993 | 0      |
| 11 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?               | Unknown  | Done       | 0.9999961459563738 | 0      |
| 12 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                   | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?         | Unknown  | Done       | 0.9999959581705232 | 0      |
| 14 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?            | Unknown  | Done       | 0.9999959553205282 | 0      |
| 15 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                     | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?     | Unknown  | Done       | 0.999995977920064  | 0      |
| 17 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?            | Unknown  | Done       | 0.9999960757146447 | 0      |
| 18 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?               | Unknown  | Done       | 0.9999961476973892 | 0      |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.998806 |      3 |
|  1 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05    | Unknown  | Done       | 0.999788 |      3 |
|  2 | Tensor<[1, 300, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | 0.999655 |      3 |
|  3 | Tensor<[1, 300, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | 0.998848 |      3 |
|  4 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | 0.998625 |      3 |
|  5 | Tensor<[1, 300, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Unknown  | Done       | 0.999795 |      3 |
|  6 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.99957  |      3 |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Unknown  | Done       |     1 |      0 |
| 15 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  | Done       |     1 |      0 |
| 16 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       |     1 |      0 |
| 17 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       |     1 |      0 |
| 18 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Unknown  | Done       |     1 |      0 |
| 19 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]         | Unknown  | Done       |     1 |      0 |
| 20 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Unknown  | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 120, 160]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 30, 40]> self = ?   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 32, 60, 80]> self = ?   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 64, 120, 160]> self = ? | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 64, 30, 40]> self = ?   | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 64, 480, 640]> self = ? | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 64, 60, 80]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0   | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1   | Unknown  | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 480, 640]> self = ? | Unknown  | Done       | 0.999755 |      0 |
|  1 | Tensor<[1, 2, 120, 160]> self = ? | Unknown  | Done       | 0.999754 |      0 |
|  2 | Tensor<[1, 2, 30, 40]> self = ?   | Unknown  | Done       | 0.99975  |      0 |
|  3 | Tensor<[1, 2, 60, 80]> self = ?   | Unknown  | Done       | 0.999758 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       |     1 |     -1 |
### aten.squeeze.dim
|    | ATen Input Variations                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[128, 128]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[128, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1280, 320]> self = ? | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[2048, 512]> self = ? | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[256, 64]> self = ?   | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[320, 1280]> self = ? | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[320, 320]> self = ?  | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[512, 128]> self = ?  | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[512, 2048]> self = ? | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[512, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[64, 256]> self = ?   | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[64, 64]> self = ?    | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
| 15 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1   | Unknown  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]       | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]       | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]       | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]    | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]     | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]         | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]    | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]     | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]    | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]    | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]  | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]  | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Unknown  | Done       |     1 |      0 |
| 15 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]       | Unknown  | Done       |     1 |      0 |
| 16 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Unknown  | Done       |     1 |      0 |
| 17 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Unknown  | Done       |     1 |      0 |
| 18 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]   | Unknown  | Done       |     1 |      0 |
| 19 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]   | Unknown  | Done       |     1 |      0 |
| 20 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]         | Unknown  | Done       |     1 |      0 |
| 21 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]       | Unknown  | Done       |     1 |      0 |
| 22 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]   | Unknown  | Done       |     1 |      0 |
| 23 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]     | Unknown  | Done       |     1 |      0 |
| 24 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]       | Unknown  | Done       |     1 |      0 |
| 25 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]   | Unknown  | Done       |     1 |      0 |
| 26 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]   | Unknown  | Done       |     1 |      0 |
| 27 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200] | Unknown  | Done       |     1 |      0 |
| 28 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160] | Unknown  | Done       |     1 |      0 |
| 29 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]      | Unknown  | Done       |     1 |      0 |
| 30 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]           | Unknown  | Done       |     1 |      0 |
| 31 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]         | Unknown  | Done       |     1 |      0 |
| 32 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]      | Unknown  | Done       |     1 |      0 |
| 33 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]           | Unknown  | Done       |     1 |      0 |
| 34 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]      | Unknown  | Done       |     1 |      0 |
| 35 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]      | Unknown  | Done       |     1 |      0 |
| 36 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]           | Unknown  | Done       |     1 |      0 |
| 37 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]       | Unknown  | Done       |     1 |      0 |
| 38 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]             | Unknown  | Done       |     1 |      0 |
| 39 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]      | Unknown  | Done       |     1 |      0 |
| 40 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]    | Unknown  | Done       |     1 |      0 |
| 41 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]     | Unknown  | Done       |     1 |      0 |
| 42 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]    | Unknown  | Done       |     1 |      0 |
| 43 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]    | Unknown  | Done       |     1 |      0 |
| 44 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]     | Unknown  | Done       |     1 |      0 |
| 45 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]         | Unknown  | Done       |     1 |      0 |
| 46 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]    | Unknown  | Done       |     1 |      0 |
| 47 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]         | Unknown  | Done       |     1 |      0 |
| 48 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]   | Unknown  | Done       |     1 |      0 |
| 49 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]     | Unknown  | Done       |     1 |      0 |
| 50 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]       | Unknown  | Done       |     1 |      0 |
| 51 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]       | Unknown  | Done       |     1 |      0 |
| 52 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]     | Unknown  | Done       |     1 |      0 |
| 53 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]    | Unknown  | Done       |     1 |      0 |
| 54 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]    | Unknown  | Done       |     1 |      0 |
| 55 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]   | Unknown  | Done       |     1 |      0 |
| 56 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]       | Unknown  | Done       |     1 |      0 |
| 57 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]   | Unknown  | Done       |     1 |      0 |
| 58 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]     | Unknown  | Done       |     1 |      0 |
| 59 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]       | Unknown  | Done       |     1 |      0 |
| 60 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]       | Unknown  | Done       |     1 |      0 |
| 61 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]       | Unknown  | Done       |     1 |      0 |
| 62 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]         | Unknown  | Done       |     1 |      0 |
| 63 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]       | Unknown  | Done       |     1 |      0 |
| 64 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Unknown  | Done       |     1 |      0 |
| 65 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Unknown  | Done       |     1 |      0 |
| 66 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Unknown  | Done       |     1 |      0 |
| 67 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]           | Unknown  | Done       |     1 |      0 |
| 68 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]         | Unknown  | Done       |     1 |      0 |
| 69 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]           | Unknown  | Done       |     1 |      0 |
| 70 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]           | Unknown  | Done       |     1 |      0 |
| 71 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Unknown  | Done       |     1 |      0 |
| 72 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]         | Unknown  | Done       |     1 |      0 |
| 73 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]         | Unknown  | Done       |     1 |      0 |
| 74 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Unknown  | Done       |     1 |      0 |
| 75 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Unknown  | Done       |     1 |      0 |
| 76 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Unknown  | Done       |     1 |      0 |
| 77 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Unknown  | Done       |     1 |      0 |

