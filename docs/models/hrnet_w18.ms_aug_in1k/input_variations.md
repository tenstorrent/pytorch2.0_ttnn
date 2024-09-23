# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |          22 |
|  1 | aten._to_copy.default                             |                  3 |           3 |
|  2 | aten._unsafe_index.Tensor                         |                 37 |          31 |
|  3 | aten.add.Tensor                                   |                 12 |          12 |
|  4 | aten.addmm.default                                |                  1 |           1 |
|  5 | aten.arange.default                               |                  3 |           3 |
|  6 | aten.clone.default                                |                  1 |           1 |
|  7 | aten.convolution.default                          |                 47 |          47 |
|  8 | aten.mean.dim                                     |                  1 |           1 |
|  9 | aten.mul.Tensor                                   |                  6 |           6 |
| 10 | aten.relu.default                                 |                 19 |          19 |
| 11 | aten.t.default                                    |                  1 |           1 |
| 12 | aten.unsqueeze.default                            |                  3 |           3 |
| 13 | aten.view.default                                 |                  1 |           1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  3 | Tensor<[1, 144, 7, 7]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Done     |
|  4 | Tensor<[1, 18, 14, 14]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
|  5 | Tensor<[1, 18, 28, 28]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
|  6 | Tensor<[1, 18, 56, 56]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
|  7 | Tensor<[1, 18, 7, 7]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | Done     |
|  8 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  9 | Tensor<[1, 256, 28, 28]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
| 10 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
| 11 | Tensor<[1, 256, 7, 7]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Done     |
| 12 | Tensor<[1, 32, 56, 56]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
| 13 | Tensor<[1, 36, 14, 14]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
| 14 | Tensor<[1, 36, 28, 28]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
| 15 | Tensor<[1, 36, 7, 7]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | Done     |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
| 17 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | Done     |
| 18 | Tensor<[1, 64, 28, 28]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
| 19 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
| 20 | Tensor<[1, 72, 14, 14]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
| 21 | Tensor<[1, 72, 7, 7]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[14]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Done     |
|  1 | Tensor<[28]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Done     |
|  2 | Tensor<[56]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Done     |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']               | Unknown  |
|  1 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_11), Proxy(_to_copy_default_23)] | Done     |
|  2 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_14), Proxy(_to_copy_default_29)] | Done     |
|  3 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_2), Proxy(_to_copy_default_5)]   | Done     |
|  4 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_20), Proxy(_to_copy_default_41)] | Done     |
|  5 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_26), Proxy(_to_copy_default_53)] | Done     |
|  6 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_5), Proxy(_to_copy_default_11)]  | Done     |
|  7 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_8), Proxy(_to_copy_default_17)]  | Done     |
|  8 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']               | Unknown  |
|  9 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default), Proxy(_to_copy_default_1)]     | Done     |
| 10 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_1), Proxy(_to_copy_default_3)]   | Done     |
| 11 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_10), Proxy(_to_copy_default_21)] | Done     |
| 12 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_13), Proxy(_to_copy_default_27)] | Done     |
| 13 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_19), Proxy(_to_copy_default_39)] | Done     |
| 14 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_25), Proxy(_to_copy_default_51)] | Done     |
| 15 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_4), Proxy(_to_copy_default_9)]   | Done     |
| 16 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_7), Proxy(_to_copy_default_15)]  | Done     |
| 17 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']                 | Unknown  |
| 18 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_15), Proxy(_to_copy_default_31)]   | Done     |
| 19 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_21), Proxy(_to_copy_default_43)]   | Done     |
| 20 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_27), Proxy(_to_copy_default_55)]   | Done     |
| 21 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']               | Unknown  |
| 22 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_12), Proxy(_to_copy_default_25)] | Done     |
| 23 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_16), Proxy(_to_copy_default_33)] | Done     |
| 24 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_22), Proxy(_to_copy_default_45)] | Done     |
| 25 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_28), Proxy(_to_copy_default_57)] | Done     |
| 26 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_3), Proxy(_to_copy_default_7)]   | Done     |
| 27 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_6), Proxy(_to_copy_default_13)]  | Done     |
| 28 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_9), Proxy(_to_copy_default_19)]  | Done     |
| 29 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']                 | Unknown  |
| 30 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_17), Proxy(_to_copy_default_35)]   | Done     |
| 31 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_23), Proxy(_to_copy_default_47)]   | Done     |
| 32 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_29), Proxy(_to_copy_default_59)]   | Done     |
| 33 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']                 | Unknown  |
| 34 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_18), Proxy(_to_copy_default_37)]   | Done     |
| 35 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_24), Proxy(_to_copy_default_49)]   | Done     |
| 36 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_30), Proxy(_to_copy_default_61)]   | Done     |
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
|  0 | number<> end = 14,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
|  1 | number<> end = 28,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
|  2 | number<> end = 56,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 2048]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  2 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  4 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[1024, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
|  5 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[144, 144, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
|  6 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[18, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
|  7 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[256, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
|  8 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[36, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
|  9 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[72, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 10 | Tensor<[1, 18, 14, 14]> input = ?,<br>Tensor<[144, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 11 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 12 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[72, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 13 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[128, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 14 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 15 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 16 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[32, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 17 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[36, 18, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 18 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 19 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[18, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 20 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 21 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 22 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 23 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 24 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 25 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[128, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 26 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 27 | Tensor<[1, 36, 14, 14]> input = ?,<br>Tensor<[144, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 28 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[18, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 29 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[256, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 30 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 31 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 32 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[64, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 33 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[72, 36, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 34 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 35 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 36 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 37 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 38 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 39 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 40 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 41 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[128, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 42 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[144, 72, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 43 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[18, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 44 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[36, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 45 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[512, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 46 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[72, 72, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
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
|  0 | Tensor<[14]> self = ?,<br>int<> dim = -1 | Done     |
|  1 | Tensor<[28]> self = ?,<br>int<> dim = -1 | Done     |
|  2 | Tensor<[56]> self = ?,<br>int<> dim = -1 | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int]<> size = [1, 2048] | Done     |

