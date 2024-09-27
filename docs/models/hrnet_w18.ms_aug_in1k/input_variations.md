# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |           0 |         0 |          0 | ✘           |                  0 |
|  1 | aten._to_copy.default                             |                  3 |           0 |         0 |          0 | ✘           |                  0 |
|  2 | aten._unsafe_index.Tensor                         |                  6 |           0 |         0 |          0 | ✘           |                  0 |
|  3 | aten.add.Tensor                                   |                 12 |          12 |         0 |          0 | ✅          |                  1 |
|  4 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  5 | aten.arange.default                               |                  3 |           0 |         0 |          0 | ✘           |                  0 |
|  6 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  7 | aten.convolution.default                          |                 47 |           0 |         0 |          0 | ✘           |                  0 |
|  8 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  9 | aten.mul.Tensor                                   |                  6 |           6 |         0 |          0 | ✅          |                  1 |
| 10 | aten.relu.default                                 |                 19 |          19 |         0 |          0 | ✅          |                  1 |
| 11 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |                  1 |
| 12 | aten.unsqueeze.default                            |                  3 |           0 |         0 |          0 | ✘           |                  0 |
| 13 | aten.view.default                                 |                  1 |           0 |         0 |          1 | ✘           |                  0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | None     |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
|  3 | Tensor<[1, 144, 7, 7]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  4 | Tensor<[1, 18, 14, 14]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
|  5 | Tensor<[1, 18, 28, 28]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
|  6 | Tensor<[1, 18, 56, 56]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
|  7 | Tensor<[1, 18, 7, 7]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | None     |
|  8 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | None     |
|  9 | Tensor<[1, 256, 28, 28]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
| 10 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
| 11 | Tensor<[1, 256, 7, 7]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
| 12 | Tensor<[1, 32, 56, 56]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 13 | Tensor<[1, 36, 14, 14]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 14 | Tensor<[1, 36, 28, 28]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 15 | Tensor<[1, 36, 7, 7]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | None     |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
| 17 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | None     |
| 18 | Tensor<[1, 64, 28, 28]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 19 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 20 | Tensor<[1, 72, 14, 14]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 21 | Tensor<[1, 72, 7, 7]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | None     |
### aten._to_copy.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[14]> self = ?,<br>Optional[int]<> dtype = torch.int64 | None     |
|  1 | Tensor<[28]> self = ?,<br>Optional[int]<> dtype = torch.int64 | None     |
|  2 | Tensor<[56]> self = ?,<br>Optional[int]<> dtype = torch.int64 | None     |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])'] | None     |
|  1 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])'] | None     |
|  2 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']   | None     |
|  3 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])'] | None     |
|  4 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']   | None     |
|  5 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']   | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?   | Done     |
|  1 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ? | Done     |
|  2 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?     | Done     |
|  3 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?   | Done     |
|  4 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ? | Done     |
|  5 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ? | Done     |
|  6 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?   | Done     |
|  7 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ? | Done     |
|  8 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?   | Done     |
|  9 | Tensor<[14]> self = ?,<br>Tensor<> other = 0.0                           | Done     |
| 10 | Tensor<[28]> self = ?,<br>Tensor<> other = 0.0                           | Done     |
| 11 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.0                           | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ? | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 14,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
|  1 | number<> end = 28,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
|  2 | number<> end = 56,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | None     |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 2048]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | None     |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | None     |
|  2 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | None     |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
|  4 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[1024, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
|  5 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[144, 144, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
|  6 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[18, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
|  7 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[256, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
|  8 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[36, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
|  9 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[72, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 10 | Tensor<[1, 18, 14, 14]> input = ?,<br>Tensor<[144, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 11 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 12 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[72, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 13 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[128, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 14 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 15 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 16 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[32, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 17 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[36, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 18 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 19 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[18, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 20 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 21 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 22 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 23 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 24 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 25 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[128, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 26 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 27 | Tensor<[1, 36, 14, 14]> input = ?,<br>Tensor<[144, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 28 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[18, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 29 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[256, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 30 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 31 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 32 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[64, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 33 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[72, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 34 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | None     |
| 35 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | None     |
| 36 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 37 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 38 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 39 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 40 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 41 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[128, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 42 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[144, 72, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 43 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[18, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 44 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[36, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
| 45 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[512, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | None     |
| 46 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[72, 72, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[14]> self = ?,<br>Tensor<> other = 0.5   | Done     |
|  1 | Tensor<[28]> self = ?,<br>Tensor<> other = 0.25  | Done     |
|  2 | Tensor<[28]> self = ?,<br>Tensor<> other = 0.5   | Done     |
|  3 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.125 | Done     |
|  4 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.25  | Done     |
|  5 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.5   | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?   | Done     |
|  1 | Tensor<[1, 128, 14, 14]> self = ?  | Done     |
|  2 | Tensor<[1, 128, 56, 56]> self = ?  | Done     |
|  3 | Tensor<[1, 144, 7, 7]> self = ?    | Done     |
|  4 | Tensor<[1, 18, 14, 14]> self = ?   | Done     |
|  5 | Tensor<[1, 18, 28, 28]> self = ?   | Done     |
|  6 | Tensor<[1, 18, 56, 56]> self = ?   | Done     |
|  7 | Tensor<[1, 2048, 7, 7]> self = ?   | Done     |
|  8 | Tensor<[1, 256, 28, 28]> self = ?  | Done     |
|  9 | Tensor<[1, 256, 56, 56]> self = ?  | Done     |
| 10 | Tensor<[1, 256, 7, 7]> self = ?    | Done     |
| 11 | Tensor<[1, 32, 56, 56]> self = ?   | Done     |
| 12 | Tensor<[1, 36, 14, 14]> self = ?   | Done     |
| 13 | Tensor<[1, 36, 28, 28]> self = ?   | Done     |
| 14 | Tensor<[1, 512, 14, 14]> self = ?  | Done     |
| 15 | Tensor<[1, 64, 112, 112]> self = ? | Done     |
| 16 | Tensor<[1, 64, 28, 28]> self = ?   | Done     |
| 17 | Tensor<[1, 64, 56, 56]> self = ?   | Done     |
| 18 | Tensor<[1, 72, 14, 14]> self = ?   | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 2048]> self = ? | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[14]> self = ?,<br>int<> dim = -1 | None     |
|  1 | Tensor<[28]> self = ?,<br>int<> dim = -1 | None     |
|  2 | Tensor<[56]> self = ?,<br>int<> dim = -1 | None     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int]<> size = [1, 2048] | Fallback |

