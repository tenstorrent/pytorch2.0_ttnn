# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._unsafe_index.Tensor                         |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default                         |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                                   |                 14 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.cat.default                                  |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.clamp.default                                |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.clone.default                                |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.convolution.default                          |                 45 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.div.Tensor                                   |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.empty.memory_format                          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.exp.default                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.expand.default                               |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.fill.Scalar                                  |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.max_pool2d_with_indices.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mul.Tensor                                   |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.native_group_norm.default                    |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.new_full.default                             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.permute.default                              |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.relu.default                                 |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.rsub.Scalar                                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.select.int                                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.slice.Tensor                                 |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.split_with_sizes.default                     |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.stack.default                                |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.sub.Tensor                                   |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.unbind.int                                   |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.unsqueeze.default                            |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.view.default                                 |                 33 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 128, 100, 136]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 128, 200, 272]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 256, 100, 136]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 256, 200, 272]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 256, 50, 68]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 512, 100, 136]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 512, 25, 34]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 512, 50, 68]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 64, 200, 272]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 64, 400, 544]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 25, 34]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_5] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 50, 68]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_7] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_2] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_3] | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_2] | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_3] | Unknown  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int] size = [1, 122400, 4]   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int] size = [1, 122400, 91] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int] size = [1, 1989, 4]       | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int] size = [1, 1989, 91]     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int] size = [1, 7650, 4]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int] size = [1, 7650, 91]     | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int] size = [1, 30600, 4]      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int] size = [1, 30600, 91]    | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int] size = [1, 567, 4]          | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int] size = [1, 567, 91]        | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[100, 136]> self = ?,<br>List[int] size = [13600]                   | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[13, 17]> self = ?,<br>List[int] size = [221]                       | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[25, 34]> self = ?,<br>List[int] size = [850]                       | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[50, 68]> self = ?,<br>List[int] size = [3400]                      | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[7, 9]> self = ?,<br>List[int] size = [63]                          | Unknown  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                               | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?     | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?               | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 122400, 4]>, <[1, 30600, 4]>, <[1, 7650, 4]>, <[1, 1989, 4]>, <[1, 567, 4]>],<br>int dim = 1      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 122400, 91]>, <[1, 30600, 91]>, <[1, 7650, 91]>, <[1, 1989, 91]>, <[1, 567, 91]>],<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[122400, 4]>, <[30600, 4]>, <[7650, 4]>, <[1989, 4]>, <[567, 4]>]                                     | Unknown  | Unknown    | N/A   | N/A    |
### aten.clamp.default
|    | ATen Input Variations                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1066              | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 800               | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 128, 200, 272]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 3, 800, 1088]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 512, 50, 68]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ?                           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.empty.memory_format
|    | ATen Input Variations                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [0],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 136]> self = ?,<br>List[int] size = [100, 136] | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 17]> self = ?,<br>List[int] size = [13, 17]    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 34]> self = ?,<br>List[int] size = [25, 34]    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 68]> self = ?,<br>List[int] size = [50, 68]    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 9]> self = ?,<br>List[int] size = [7, 9]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[100, 1]> self = ?,<br>List[int] size = [100, 136] | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[13, 1]> self = ?,<br>List[int] size = [13, 17]    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[25, 1]> self = ?,<br>List[int] size = [25, 34]    | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[50, 1]> self = ?,<br>List[int] size = [50, 68]    | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[7, 1]> self = ?,<br>List[int] size = [7, 9]       | Unknown  | Unknown    | N/A   | N/A    |
### aten.fill.Scalar
|    | ATen Input Variations                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[]> self = ?,<br>number value = 114 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[]> self = ?,<br>number value = 120 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[]> self = ?,<br>number value = 16  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[]> self = ?,<br>number value = 32  | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[]> self = ?,<br>number value = 61  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[]> self = ?,<br>number value = 64  | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[]> self = ?,<br>number value = 8   | Unknown  | Unknown    | N/A   | N/A    |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 400, 544]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[0, 1]> other = ?                      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[]> other = ?                          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?              | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[0]> self = ?,<br>Tensor other = 0.5                       | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                     | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 100, 136]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 13600,<br>int group = 32,<br>float eps = 1e-05 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 13, 17]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 221,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 256, 25, 34]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 850,<br>int group = 32,<br>float eps = 1e-05     | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 256, 50, 68]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 3400,<br>int group = 32,<br>float eps = 1e-05    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 256, 7, 9]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>int N = 1,<br>int C = 256,<br>int HxW = 63,<br>int group = 32,<br>float eps = 1e-05        | Unknown  | Unknown    | N/A   | N/A    |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3, 800, 1066]> self = ?,<br>List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 9, 4, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 9, 4, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 9, 4, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 9, 4, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 9, 4, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]      | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 9, 91, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 9, 91, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 9, 91, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 9, 91, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]     | Unknown  | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 50, 68]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 128, 100, 136]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 128, 200, 272]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 2048, 25, 34]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 256, 100, 136]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 256, 13, 17]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 256, 200, 272]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 256, 25, 34]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 256, 50, 68]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 256, 7, 9]> self = ?     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 512, 100, 136]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 512, 25, 34]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 512, 50, 68]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 64, 200, 272]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 64, 400, 544]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 0            | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 1            | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 2            | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 3            | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 3, 800, 1066]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   | N/A    |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 163206, 91]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567]                     | Unknown  | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[0, 1]>, <[0, 1]>, <[0, 1]>, <[0, 1]>],<br>int dim = 2     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[0, 2]>, <[0, 2]>],<br>int dim = 2                         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[0]>, <[0]>, <[0]>, <[0]>],<br>int dim = 1                 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[13600]>, <[13600]>, <[13600]>, <[13600]>],<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [<[221]>, <[221]>, <[221]>, <[221]>],<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [<[3400]>, <[3400]>, <[3400]>, <[3400]>],<br>int dim = 1     | Unknown  | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[63]>, <[63]>, <[63]>, <[63]>],<br>int dim = 1             | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[850]>, <[850]>, <[850]>, <[850]>],<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.unbind.int
|    | ATen Input Variations                   | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0]> self = ?,<br>int dim = 1           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[3]> self = ?,<br>int dim = 1           | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1, 4]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[0, 2, 2]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]       | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]       | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]           | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136] | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]     | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]     | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]         | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                            | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                    | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                    | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                            | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[13]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[17]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[221, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[221, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[25]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[3400, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                     | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[3400, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                     | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[34]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
| 24 | Tensor<[50]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
| 25 | Tensor<[63, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                       | Unknown  | Done       | 1.0   | -1     |
| 26 | Tensor<[63, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                       | Unknown  | Done       | 1.0   | -1     |
| 27 | Tensor<[68]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
| 28 | Tensor<[7]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Done       | 1.0   | -1     |
| 29 | Tensor<[850, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Unknown  | Done       | 1.0   | -1     |
| 30 | Tensor<[850, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Unknown  | Done       | 1.0   | -1     |
| 31 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                        | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[9]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Done       | 1.0   | -1     |

