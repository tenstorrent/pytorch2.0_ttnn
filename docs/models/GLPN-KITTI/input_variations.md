# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax.default                             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten._to_copy.default                             |                 10 |          10 |         0 |          0 | ✅          |    1    |
|  3 | aten._unsafe_index.Tensor                         |                 20 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.add.Tensor                                   |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  5 | aten.addmm.default                                |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  6 | aten.bmm.default                                  |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  7 | aten.cat.default                                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  8 | aten.clone.default                                |                 19 |          19 |         0 |          0 | ✅          |    1    |
|  9 | aten.convolution.default                          |                 25 |          23 |         0 |          0 | 🚧          |    0.92 |
| 10 | aten.div.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 11 | aten.expand.default                               |                 15 |           0 |        15 |          0 | ✅          |    1    |
| 12 | aten.gelu.default                                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 13 | aten.mul.Tensor                                   |                 19 |          19 |         0 |          0 | ✅          |    1    |
| 14 | aten.native_layer_norm.default                    |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 15 | aten.permute.default                              |                 21 |          21 |         0 |          0 | ✅          |    1    |
| 16 | aten.relu.default                                 |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 17 | aten.rsub.Scalar                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 18 | aten.select.int                                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 19 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 20 | aten.slice.Tensor                                 |                  9 |           0 |         9 |          0 | ✅          |    1    |
| 21 | aten.squeeze.dim                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 22 | aten.t.default                                    |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 23 | aten.transpose.int                                |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 24 | aten.unsqueeze.default                            |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 25 | aten.view.default                                 |                 78 |          78 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 120, 160]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999992 |      1 |
|  1 | Tensor<[1, 32, 30, 40]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999991 |      1 |
|  2 | Tensor<[1, 32, 60, 80]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999989 |      1 |
|  3 | Tensor<[1, 64, 120, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999993 |      1 |
|  4 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.99999  |      1 |
|  5 | Tensor<[1, 64, 60, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999989 |      1 |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999595 |      0 |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999595 |      0 |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999598 |      0 |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999597 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 64, 15, 20]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_21] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_22] | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_21] | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_22] | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_3]     | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_4]     | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_3]     | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_4]     | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_27] | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_28] | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_27] | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_28] | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_10]    | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_9]     | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_10]    | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_9]     | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_15]   | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_16]   | None     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_15]   | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_16]   | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?       | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?         | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?       | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ? | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ? | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ? | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?     | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ? | Done     | Done       | 0.999976 |      0 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[300, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     | Done       | 0.999979 |      0 |
|  3 | Tensor<[128]> self = ?,<br>Tensor<[4800, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     | Done       | 0.99997  |      0 |
|  4 | Tensor<[2048]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     | Done       | 0.99997  |      0 |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     | Done       | 0.999985 |      0 |
|  6 | Tensor<[320]> self = ?,<br>Tensor<[1200, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ? | Done     | Done       | 0.999961 |      0 |
|  7 | Tensor<[320]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?   | Done     | Done       | 0.999973 |      0 |
|  8 | Tensor<[320]> self = ?,<br>Tensor<[300, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?    | Done     | Done       | 0.999976 |      0 |
|  9 | Tensor<[512]> self = ?,<br>Tensor<[300, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     | Done       | 0.99992  |      0 |
| 10 | Tensor<[512]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | Done       | 0.99997  |      0 |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     | Done       | 0.999979 |      0 |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[19200, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | Done       | 0.999974 |      0 |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | Done       | 0.999985 |      0 |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[300, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     | Done       | 0.999985 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ? | Done     | Done       | 0.999976 |      0 |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?  | Done     | Done       | 0.999986 |      0 |
|  2 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?  | Done     | Done       | 0.999976 |      0 |
|  3 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?   | Done     | Done       | 0.999986 |      0 |
|  4 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?  | Done     | Done       | 0.999976 |      0 |
|  5 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?   | Done     | Done       | 0.999986 |      0 |
|  6 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?   | Done     | Done       | 0.99998  |      0 |
|  7 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?    | Done     | Done       | 0.999986 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 64, 120, 160]>, <[1, 64, 120, 160]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 64, 30, 40]>, <[1, 64, 30, 40]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[1, 64, 60, 80]>, <[1, 64, 60, 80]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?                                                          | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1200, 1280]> self = ?                                                             | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1200, 320]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 19200, 256]> self = ?                                                             | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 19200, 64]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 2, 4800, 300]> self = ?                                                           | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 300, 2048]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 300, 512]> self = ?                                                               | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 4800, 128]> self = ?                                                              | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 4800, 512]> self = ?                                                              | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 5, 1200, 300]> self = ?                                                           | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 8, 300, 300]> self = ?                                                            | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 128, 120, 160]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999812 |      3 |
|  1 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999817 |      3 |
|  2 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999605 |      3 |
|  3 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[320, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999815 |      3 |
|  4 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999979 |      3 |
|  5 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999815 |      3 |
|  6 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | Done     | Done       | 0.999983 |      3 |
|  7 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | Done     | Done       | 0.999984 |      3 |
|  8 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | Done     | Done       | 0.999983 |      3 |
|  9 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.9999   |      3 |
| 10 | Tensor<[1, 32, 120, 160]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999961 |      3 |
| 11 | Tensor<[1, 32, 30, 40]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.99996  |      3 |
| 12 | Tensor<[1, 32, 60, 80]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.99996  |      3 |
| 13 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999786 |      3 |
| 14 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[512, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999397 |      3 |
| 15 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[64, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999973 |      3 |
| 16 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.99997  |      3 |
| 17 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | Done     | Done       | 0.999983 |      3 |
| 18 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999919 |      3 |
| 19 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999919 |      3 |
| 20 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.998983 |      3 |
| 21 | Tensor<[1, 64, 30, 40]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.99992  |      3 |
| 22 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[1, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Fallback   | 1        |     -1 |
| 23 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | 1        |     -1 |
| 24 | Tensor<[1, 64, 60, 80]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999919 |      3 |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0   | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]       | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]       | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]       | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]       | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]       | Removed  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]       | Removed  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Removed  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Removed  | Done       |     1 |     -1 |
| 14 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]       | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1200, 1280]> self = ? | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 19200, 256]> self = ? | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[1, 300, 2048]> self = ?  | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 4800, 512]> self = ?  | Done     | Done       | 0.999991 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                   | Done     | Done       | 0.9999985492583693 | 0      |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                   | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ? | Done     | Done       | 0.9999959936944236 | 0      |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?         | Done     | Done       | 0.9999962934408971 | 0      |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?            | Done     | Done       | 0.9999960829647273 | 0      |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                   | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?         | Done     | Done       | 0.9999960157730196 | 0      |
|  7 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?            | Done     | Done       | 0.999996047249881  | 0      |
|  8 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                     | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?     | Done     | Done       | 0.9999960191529932 | 0      |
| 10 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?            | Done     | Done       | 0.9999950951403191 | 0      |
| 11 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?               | Done     | Done       | 0.9999966669937088 | 0      |
| 12 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?         | Done     | Done       | 0.9999959509594869 | 0      |
| 14 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?            | Done     | Done       | 0.9999957814925838 | 0      |
| 15 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?     | Done     | Done       | 0.9999959759516732 | 0      |
| 17 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?            | Done     | Done       | 0.9999962318650699 | 0      |
| 18 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?               | Done     | Done       | 0.9999961780723695 | 0      |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
|  1 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | N/A   |      1 |
|  2 | Tensor<[1, 300, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |      1 |
|  3 | Tensor<[1, 300, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |      1 |
|  4 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |      1 |
|  5 | Tensor<[1, 300, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | N/A   |      1 |
|  6 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Done       |     1 |      0 |
| 19 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       |     1 |      0 |
| 20 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 120, 160]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 30, 40]> self = ?   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 32, 60, 80]> self = ?   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 64, 120, 160]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 64, 30, 40]> self = ?   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 64, 480, 640]> self = ? | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 64, 60, 80]> self = ?   | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       |     1 |     -1 |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 480, 640]> self = ? | Done     | Done       | 0.999755 |      0 |
|  1 | Tensor<[1, 2, 120, 160]> self = ? | Done     | Done       | 0.999752 |      0 |
|  2 | Tensor<[1, 2, 30, 40]> self = ?   | Done     | Done       | 0.999754 |      0 |
|  3 | Tensor<[1, 2, 60, 80]> self = ?   | Done     | Done       | 0.999753 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
### aten.squeeze.dim
|    | ATen Input Variations                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[128, 128]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[128, 512]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1280, 320]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[2048, 512]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[256, 64]> self = ?   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[320, 1280]> self = ? | Done     | Done       |     1 |      0 |
|  6 | Tensor<[320, 320]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[512, 128]> self = ?  | Done     | Done       |     1 |      0 |
|  8 | Tensor<[512, 2048]> self = ? | Done     | Done       |     1 |      0 |
|  9 | Tensor<[512, 512]> self = ?  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[64, 256]> self = ?   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[64, 64]> self = ?    | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1   | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1   | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]       | Done     | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]    | Done     | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]     | Done     | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]         | Done     | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]    | Done     | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]     | Done     | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]    | Done     | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]    | Done     | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]  | Done     | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]  | Done     | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]       | Done     | Done       | 1.0   | -1     |
| 16 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]   | Done     | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]   | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]         | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]       | Done     | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]   | Done     | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]     | Done     | Done       | 1.0   | -1     |
| 24 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]       | Done     | Done       | 1.0   | -1     |
| 25 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]   | Done     | Done       | 1.0   | -1     |
| 26 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]   | Done     | Done       | 1.0   | -1     |
| 27 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200] | Done     | Done       | 1.0   | -1     |
| 28 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160] | Done     | Done       | 1.0   | -1     |
| 29 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]      | Done     | Done       | 1.0   | -1     |
| 30 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]           | Done     | Done       | 1.0   | -1     |
| 31 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]         | Done     | Done       | 1.0   | -1     |
| 32 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]      | Done     | Done       | 1.0   | -1     |
| 33 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]           | Done     | Done       | 1.0   | -1     |
| 34 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]      | Done     | Done       | 1.0   | -1     |
| 35 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]      | Done     | Done       | 1.0   | -1     |
| 36 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]           | Done     | Done       | 1.0   | -1     |
| 37 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]       | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]             | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]      | Done     | Done       | 1.0   | -1     |
| 40 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]    | Done     | Done       | 1.0   | -1     |
| 41 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]     | Done     | Done       | 1.0   | -1     |
| 42 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]    | Done     | Done       | 1.0   | -1     |
| 43 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]    | Done     | Done       | 1.0   | -1     |
| 44 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]     | Done     | Done       | 1.0   | -1     |
| 45 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]         | Done     | Done       | 1.0   | -1     |
| 46 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]    | Done     | Done       | 1.0   | -1     |
| 47 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]         | Done     | Done       | 1.0   | -1     |
| 48 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]   | Done     | Done       | 1.0   | -1     |
| 49 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]     | Done     | Done       | 1.0   | -1     |
| 50 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]       | Done     | Done       | 1.0   | -1     |
| 51 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]       | Done     | Done       | 1.0   | -1     |
| 52 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]     | Done     | Done       | 1.0   | -1     |
| 53 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]    | Done     | Done       | 1.0   | -1     |
| 54 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]    | Done     | Done       | 1.0   | -1     |
| 55 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]   | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
| 57 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]   | Done     | Unknown    | N/A   | N/A    |
| 58 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]     | Done     | Done       | 1.0   | -1     |
| 59 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]       | Done     | Done       | 1.0   | -1     |
| 60 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]       | Done     | Done       | 1.0   | -1     |
| 61 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]       | Done     | Done       | 1.0   | -1     |
| 62 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]         | Done     | Done       | 1.0   | -1     |
| 63 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]       | Done     | Unknown    | N/A   | N/A    |
| 64 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Unknown    | N/A   | N/A    |
| 65 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Done     | Done       | 1.0   | -1     |
| 66 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Done     | Done       | 1.0   | -1     |
| 67 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]           | Done     | Done       | 1.0   | -1     |
| 68 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]         | Done     | Done       | 1.0   | -1     |
| 69 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]           | Done     | Done       | 1.0   | -1     |
| 70 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]           | Done     | Done       | 1.0   | -1     |
| 71 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Done     | Unknown    | N/A   | N/A    |
| 72 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]         | Done     | Done       | 1.0   | -1     |
| 73 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]         | Done     | Done       | 1.0   | -1     |
| 74 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Done     | Done       | 1.0   | -1     |
| 75 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Done     | Done       | 1.0   | -1     |
| 76 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Done     | Done       | 1.0   | -1     |
| 77 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Done     | Done       | 1.0   | -1     |

