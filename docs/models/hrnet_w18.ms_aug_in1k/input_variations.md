# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |          22 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default                             |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  2 | aten._unsafe_index.Tensor                         |                 31 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                                   |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  4 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.convolution.default                          |                 47 |          47 |         0 |          0 | ✅          |       1 |
|  7 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.relu.default                                 |                 19 |          19 |         0 |          0 | ✅          |       1 |
|  9 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      5 |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999992 |      5 |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999983 |      5 |
|  3 | Tensor<[1, 144, 7, 7]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      5 |
|  4 | Tensor<[1, 18, 14, 14]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      5 |
|  5 | Tensor<[1, 18, 28, 28]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.99999  |      5 |
|  6 | Tensor<[1, 18, 56, 56]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      5 |
|  7 | Tensor<[1, 18, 7, 7]> input = ?,<br>Optional[Tensor]<[18]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>Tensor<[18]> running_mean = ?,<br>Tensor<[18]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | Done     | Done       | 0.999994 |      5 |
|  8 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      5 |
|  9 | Tensor<[1, 256, 28, 28]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999982 |      5 |
| 10 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |      5 |
| 11 | Tensor<[1, 256, 7, 7]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      5 |
| 12 | Tensor<[1, 32, 56, 56]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      5 |
| 13 | Tensor<[1, 36, 14, 14]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999992 |      5 |
| 14 | Tensor<[1, 36, 28, 28]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.99999  |      5 |
| 15 | Tensor<[1, 36, 7, 7]> input = ?,<br>Optional[Tensor]<[36]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>Tensor<[36]> running_mean = ?,<br>Tensor<[36]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | Done     | Done       | 0.999988 |      5 |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |      5 |
| 17 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05       | Done     | Done       | 0.999986 |      5 |
| 18 | Tensor<[1, 64, 28, 28]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      5 |
| 19 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999986 |      5 |
| 20 | Tensor<[1, 72, 14, 14]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      5 |
| 21 | Tensor<[1, 72, 7, 7]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | Done     | Done       | 0.999994 |      5 |
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 18, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 18, 28, 28]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 18, 56, 56]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 18, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 36, 14, 14]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 36, 28, 28]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 36, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 72, 14, 14]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 72, 7, 7]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_46]  | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_14, _folded__to_copy_58]  | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_10]   | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_82]  | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_26, _folded__to_copy_106] | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_22]   | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 18, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_34]   | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2]      | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_6]    | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_42]  | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_13, _folded__to_copy_54]  | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_78]  | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_25, _folded__to_copy_102] | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_18]   | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 18, 28, 28]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_30]   | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_15, _folded__to_copy_62]    | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_21, _folded__to_copy_86]    | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 18, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_27, _folded__to_copy_110]   | None     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_50]  | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_66]  | None     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_22, _folded__to_copy_90]  | None     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_28, _folded__to_copy_114] | None     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_3, _folded__to_copy_14]   | None     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_26]   | None     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 36, 14, 14]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_38]   | None     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_70]    | None     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_23, _folded__to_copy_94]    | None     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 36, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_29, _folded__to_copy_118]   | None     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_18, _folded__to_copy_74]    | None     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_24, _folded__to_copy_98]    | None     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 72, 7, 7]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_30, _folded__to_copy_122]   | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ? | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ? | Done     | Done       | 0.999948 |      0 |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048]> self = ? | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999965 |      6 |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999824 |      4 |
|  2 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99998  |      4 |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999815 |      6 |
|  4 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[1024, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999979 |      4 |
|  5 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[144, 144, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999814 |      4 |
|  6 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[18, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999978 |      4 |
|  7 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[256, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999979 |      4 |
|  8 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[36, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.99998  |      4 |
|  9 | Tensor<[1, 144, 7, 7]> input = ?,<br>Tensor<[72, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.99998  |      4 |
| 10 | Tensor<[1, 18, 14, 14]> input = ?,<br>Tensor<[144, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999966 |      4 |
| 11 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999965 |      4 |
| 12 | Tensor<[1, 18, 28, 28]> input = ?,<br>Tensor<[72, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999964 |      4 |
| 13 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[128, 18, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999992 |      4 |
| 14 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999965 |      4 |
| 15 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[18, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999964 |      4 |
| 16 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[32, 18, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999991 |      4 |
| 17 | Tensor<[1, 18, 56, 56]> input = ?,<br>Tensor<[36, 18, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999965 |      4 |
| 18 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999552 |      6 |
| 19 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[18, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999542 |      4 |
| 20 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.99955  |      4 |
| 21 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999975 |      4 |
| 22 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999975 |      4 |
| 23 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999617 |      4 |
| 24 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999981 |      4 |
| 25 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[128, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999991 |      4 |
| 26 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999962 |      4 |
| 27 | Tensor<[1, 36, 14, 14]> input = ?,<br>Tensor<[144, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999941 |      4 |
| 28 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[18, 36, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999987 |      4 |
| 29 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[256, 36, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999987 |      4 |
| 30 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999946 |      4 |
| 31 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[36, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999941 |      4 |
| 32 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[64, 36, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999987 |      4 |
| 33 | Tensor<[1, 36, 28, 28]> input = ?,<br>Tensor<[72, 36, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999941 |      4 |
| 34 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.998883 |      6 |
| 35 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.99992  |      4 |
| 36 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999986 |      4 |
| 37 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999922 |      4 |
| 38 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999986 |      4 |
| 39 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999986 |      4 |
| 40 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.99992  |      4 |
| 41 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[128, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999986 |      4 |
| 42 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[144, 72, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999903 |      4 |
| 43 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[18, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999985 |      4 |
| 44 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[36, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999985 |      4 |
| 45 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[512, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Done     | Done       | 0.999986 |      4 |
| 46 | Tensor<[1, 72, 14, 14]> input = ?,<br>Tensor<[72, 72, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999902 |      4 |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       |     0 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 128, 14, 14]> self = ?  | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 128, 56, 56]> self = ?  | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 144, 7, 7]> self = ?    | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 18, 14, 14]> self = ?   | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 18, 28, 28]> self = ?   | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 18, 56, 56]> self = ?   | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 2048, 7, 7]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 256, 28, 28]> self = ?  | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 256, 56, 56]> self = ?  | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 256, 7, 7]> self = ?    | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 32, 56, 56]> self = ?   | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 36, 14, 14]> self = ?   | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 36, 28, 28]> self = ?   | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 512, 14, 14]> self = ?  | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 64, 28, 28]> self = ?   | Done     | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 72, 14, 14]> self = ?   | Done     | Done       | 1.0   | 0      |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 2048]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048] | Done     | Done       |     1 |     -1 |

