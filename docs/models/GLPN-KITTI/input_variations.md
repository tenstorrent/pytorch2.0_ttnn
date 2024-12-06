# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax.default                             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten._to_copy.default                             |                 20 |          10 |         0 |          0 | 🚧          |    0.5  |
|  3 | aten._unsafe_index.Tensor                         |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.add.Tensor                                   |                 19 |          18 |         0 |          0 | 🚧          |    0.95 |
|  5 | aten.addmm.default                                |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  6 | aten.arange.default                               |                 10 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.bmm.default                                  |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  8 | aten.cat.default                                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  9 | aten.ceil.default                                 |                 10 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.clamp.default                                |                 20 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.clone.default                                |                 19 |          19 |         0 |          0 | ✅          |    1    |
| 12 | aten.convolution.default                          |                 25 |          21 |         0 |          0 | 🚧          |    0.84 |
| 13 | aten.div.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 14 | aten.expand.default                               |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.gelu.default                                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 16 | aten.mul.Tensor                                   |                 24 |          21 |         0 |          0 | 🚧          |    0.88 |
| 17 | aten.native_layer_norm.default                    |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 18 | aten.permute.default                              |                 21 |          21 |         0 |          0 | ✅          |    1    |
| 19 | aten.relu.default                                 |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 20 | aten.rsub.Scalar                                  |                 10 |          10 |         0 |          0 | ✅          |    1    |
| 21 | aten.select.int                                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 22 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 23 | aten.slice.Tensor                                 |                  9 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.squeeze.dim                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 25 | aten.sub.Tensor                                   |                 20 |          19 |         0 |          0 | 🚧          |    0.95 |
| 26 | aten.t.default                                    |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 27 | aten.transpose.int                                |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 28 | aten.unsqueeze.default                            |                  8 |           7 |         0 |          0 | 🚧          |    0.88 |
| 29 | aten.view.default                                 |                 78 |          78 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 120, 160]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 30, 40]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 60, 80]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 120, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 60, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Unknown    | N/A   | N/A    |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 15, 20]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[120]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[160]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[240]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[30]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[320]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[40]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[480]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[60]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[640]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[80]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[240, 1]>, <[320]>] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[30, 1]>, <[40]>]     | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[480, 1]>, <[640]>] | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[60, 1]>, <[80]>]     | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[120, 1]>, <[160]>]   | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?         | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                               | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                              | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                               | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                               | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                               | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[300, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[128]> self = ?,<br>Tensor<[4800, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2048]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[320]> self = ?,<br>Tensor<[1200, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[320]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[320]> self = ?,<br>Tensor<[300, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[512]> self = ?,<br>Tensor<[300, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[512]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[19200, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[300, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     | Unknown    | N/A   | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number end = 120,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  1 | number end = 160,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  2 | number end = 240,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  3 | number end = 30,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Unknown    | N/A   | N/A    |
|  4 | number end = 320,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  5 | number end = 40,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Unknown    | N/A   | N/A    |
|  6 | number end = 480,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  7 | number end = 60,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Unknown    | N/A   | N/A    |
|  8 | number end = 640,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  9 | number end = 80,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 64, 120, 160]>, <[1, 64, 120, 160]>],<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 64, 30, 40]>, <[1, 64, 30, 40]>],<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 64, 60, 80]>, <[1, 64, 60, 80]>],<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
### aten.ceil.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[120]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[160]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[240]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[30]> self = ?   | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[320]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[40]> self = ?   | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[480]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[60]> self = ?   | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[640]> self = ?  | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[80]> self = ?   | None     | Unknown    | N/A   | N/A    |
### aten.clamp.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[120]> self = ?,<br>Optional[number] min = 0.0                              | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[120]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 59  | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[160]> self = ?,<br>Optional[number] min = 0.0                              | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[160]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 79  | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[240]> self = ?,<br>Optional[number] min = 0.0                              | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[240]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 119 | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[30]> self = ?,<br>Optional[number] min = 0.0                               | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[30]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 14   | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[320]> self = ?,<br>Optional[number] min = 0.0                              | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 159 | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[40]> self = ?,<br>Optional[number] min = 0.0                               | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[40]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 19   | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[480]> self = ?,<br>Optional[number] min = 0.0                              | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[480]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 239 | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[60]> self = ?,<br>Optional[number] min = 0.0                               | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[60]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 29   | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[640]> self = ?,<br>Optional[number] min = 0.0                              | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[640]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 319 | None     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[80]> self = ?,<br>Optional[number] min = 0.0                               | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[80]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 39   | None     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?                                                          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1200, 1280]> self = ?                                                             | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1200, 320]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 19200, 256]> self = ?                                                             | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 19200, 64]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 2, 4800, 300]> self = ?                                                           | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 300, 2048]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 300, 512]> self = ?                                                               | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 4800, 128]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 4800, 512]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 5, 1200, 300]> self = ?                                                           | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 8, 300, 300]> self = ?                                                            | Done     | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128, 120, 160]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[320, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 32, 120, 160]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 32, 30, 40]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 32, 60, 80]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[512, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[64, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 64, 30, 40]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[1, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 64, 60, 80]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0   | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]       | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]       | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]       | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]       | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]       | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]       | Unknown  | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1200, 1280]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 19200, 256]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 300, 2048]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 4800, 512]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ? | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?         | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?            | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?         | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?            | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?     | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?            | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?               | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?         | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?            | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?     | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?            | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?               | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 300, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 300, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 300, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 120, 160]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 30, 40]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 60, 80]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 120, 160]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 64, 30, 40]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 64, 480, 640]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 64, 60, 80]> self = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[120, 1]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[160]> self = ?,<br>number other = 1.0    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[240, 1]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[30, 1]> self = ?,<br>number other = 1.0  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[320]> self = ?,<br>number other = 1.0    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[40]> self = ?,<br>number other = 1.0     | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[480, 1]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[60, 1]> self = ?,<br>number other = 1.0  | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[640]> self = ?,<br>number other = 1.0    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[80]> self = ?,<br>number other = 1.0     | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Unknown    | N/A   | N/A    |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 480, 640]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 2, 120, 160]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 2, 30, 40]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 2, 60, 80]> self = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
### aten.squeeze.dim
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[120]> self = ?,<br>Tensor other = 0.5            | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[160]> self = ?,<br>Tensor other = 0.5            | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[240]> self = ?,<br>Tensor other = 0.5            | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[30]> self = ?,<br>Tensor other = 0.5             | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[320]> self = ?,<br>Tensor other = 0.5            | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?       | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[40]> self = ?,<br>Tensor other = 0.5             | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?         | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[480]> self = ?,<br>Tensor other = 0.5            | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?   | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[60]> self = ?,<br>Tensor other = 0.5             | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[640]> self = ?,<br>Tensor other = 0.5            | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?       | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[80]> self = ?,<br>Tensor other = 0.5             | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?         | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[128, 128]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[128, 512]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1280, 320]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2048, 512]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[256, 64]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[320, 1280]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[320, 320]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[512, 128]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[512, 2048]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[512, 512]> self = ?  | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[64, 256]> self = ?   | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[64, 64]> self = ?    | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[120]> self = ?,<br>int dim = 1         | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[240]> self = ?,<br>int dim = 1         | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[30]> self = ?,<br>int dim = 1          | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[480]> self = ?,<br>int dim = 1         | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[60]> self = ?,<br>int dim = 1          | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]     | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]         | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]     | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]    | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]  | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]  | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]       | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]   | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]   | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]         | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]       | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]   | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]     | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]   | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]   | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200] | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160] | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]      | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]           | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]         | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]      | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]           | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]      | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]      | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]           | Done     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]       | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]             | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]      | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]    | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]     | Done     | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]    | Done     | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]    | Done     | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]     | Done     | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]         | Done     | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]    | Done     | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]         | Done     | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]   | Done     | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]     | Done     | Unknown    | N/A   | N/A    |
| 50 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]       | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
| 52 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]     | Done     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]    | Done     | Unknown    | N/A   | N/A    |
| 54 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]    | Done     | Unknown    | N/A   | N/A    |
| 55 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]   | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
| 57 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]   | Done     | Unknown    | N/A   | N/A    |
| 58 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]     | Done     | Unknown    | N/A   | N/A    |
| 59 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]       | Done     | Unknown    | N/A   | N/A    |
| 60 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]       | Done     | Unknown    | N/A   | N/A    |
| 61 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]       | Done     | Unknown    | N/A   | N/A    |
| 62 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]         | Done     | Unknown    | N/A   | N/A    |
| 63 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]       | Done     | Unknown    | N/A   | N/A    |
| 64 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Unknown    | N/A   | N/A    |
| 65 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Done     | Unknown    | N/A   | N/A    |
| 66 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Done     | Unknown    | N/A   | N/A    |
| 67 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]           | Done     | Unknown    | N/A   | N/A    |
| 68 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]         | Done     | Unknown    | N/A   | N/A    |
| 69 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]           | Done     | Unknown    | N/A   | N/A    |
| 70 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]           | Done     | Unknown    | N/A   | N/A    |
| 71 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Done     | Unknown    | N/A   | N/A    |
| 72 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]         | Done     | Unknown    | N/A   | N/A    |
| 73 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]         | Done     | Unknown    | N/A   | N/A    |
| 74 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Done     | Unknown    | N/A   | N/A    |
| 75 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Done     | Unknown    | N/A   | N/A    |
| 76 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Done     | Unknown    | N/A   | N/A    |
| 77 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Done     | Unknown    | N/A   | N/A    |

