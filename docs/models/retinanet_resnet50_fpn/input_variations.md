# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._unsafe_index.Tensor            |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._unsafe_view.default            |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                      |                 32 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.cat.default                     |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.clamp.default                   |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.clone.default                   |                 15 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.convolution.default             |                 43 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.div.Tensor                      |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.empty.memory_format             |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.exp.default                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default                  |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.fill.Scalar                     |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.max_pool2d_with_indices.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.mul.Tensor                      |                 26 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.new_full.default                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.permute.default                 |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.relu.default                    |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.rsqrt.default                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.rsub.Scalar                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.select.int                      |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.slice.Tensor                    |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.split_with_sizes.default        |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.stack.default                   |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.sub.Tensor                      |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.unbind.int                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.unsqueeze.default               |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.view.default                    |                 39 |           0 |         0 |          0 | ✘           |       0 |
***
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
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int] size = [1, 122400, 4]   | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int] size = [1, 122400, 91] | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int] size = [1, 1989, 4]       | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int] size = [1, 1989, 91]     | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int] size = [1, 7650, 4]       | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int] size = [1, 7650, 91]     | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int] size = [1, 30600, 4]      | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int] size = [1, 30600, 91]    | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int] size = [1, 567, 4]          | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int] size = [1, 567, 91]        | Unknown  | Done       |     1 |     -1 |
| 10 | Tensor<[100, 136]> self = ?,<br>List[int] size = [13600]                   | Unknown  | Done       |     1 |     -1 |
| 11 | Tensor<[13, 17]> self = ?,<br>List[int] size = [221]                       | Unknown  | Done       |     1 |     -1 |
| 12 | Tensor<[25, 34]> self = ?,<br>List[int] size = [850]                       | Unknown  | Done       |     1 |     -1 |
| 13 | Tensor<[50, 68]> self = ?,<br>List[int] size = [3400]                      | Unknown  | Done       |     1 |     -1 |
| 14 | Tensor<[7, 9]> self = ?,<br>List[int] size = [63]                          | Unknown  | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                         | Unknown  | Done       | 1        |      0 |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                               | Unknown  | Done       | 1        |      0 |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                      | Unknown  | Done       | 1        |      0 |
|  3 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Unknown  | Done       | 1        |      0 |
|  6 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  7 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                      | Unknown  | Done       | 1        |      0 |
|  9 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
| 10 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
| 11 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Unknown  | Done       | 1        |      0 |
| 12 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
| 13 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ? | Unknown  | Done       | 0.999998 |      0 |
| 14 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
| 15 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ? | Unknown  | Done       | 0.999998 |      0 |
| 16 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 17 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
| 18 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
| 19 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Unknown  | Done       | 1        |      0 |
| 20 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
| 21 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ? | Unknown  | Done       | 0.999998 |      0 |
| 22 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 23 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 24 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Unknown  | Done       | 1        |      0 |
| 25 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 26 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Unknown  | Done       | 0.999998 |      0 |
| 27 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?               | Unknown  | Done       | 0.999998 |      0 |
| 28 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  | Done       | 0.999998 |      0 |
| 29 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Unknown  | Done       | 0.999998 |      0 |
| 30 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Unknown  | Done       | 0.999998 |      0 |
| 31 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  | Done       | 0.999998 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 122400, 4]>, <[1, 30600, 4]>, <[1, 7650, 4]>, <[1, 1989, 4]>, <[1, 567, 4]>],<br>int dim = 1      | Unknown  | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 122400, 91]>, <[1, 30600, 91]>, <[1, 7650, 91]>, <[1, 1989, 91]>, <[1, 567, 91]>],<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[122400, 4]>, <[30600, 4]>, <[7650, 4]>, <[1989, 4]>, <[567, 4]>]                                     | Unknown  | Done       |     1 |      0 |
### aten.clamp.default
|    | ATen Input Variations                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[0, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1066              | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 800               | Unknown  | Fallback   |     1 |     -1 |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.9998391429065705 | 4      |
|  1 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999655910469484 | 4      |
|  2 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.9999645201641061 | 6      |
|  3 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999656698295113 | 4      |
|  4 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9998146461140298 | 4      |
|  5 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.999980571400005  | 4      |
|  6 | Tensor<[1, 128, 200, 272]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9998143712580773 | 4      |
|  7 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.9999537121212638 | 6      |
|  8 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999548912358134 | 4      |
|  9 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9995459772568163 | 4      |
| 10 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.9995441909882482 | 6      |
| 11 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999543638030807  | 6      |
| 12 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Fallback   | 1.0                | -1     |
| 13 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9995675129100987 | 6      |
| 14 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9995998893027614 | 6      |
| 15 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.9995508727852519 | 6      |
| 16 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9995687005938177 | 6      |
| 17 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.999965389480195  | 4      |
| 18 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999653570159377 | 4      |
| 19 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999965149815834  | 4      |
| 20 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9995534827260478 | 6      |
| 21 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999561940418396  | 6      |
| 22 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.9995588920557692 | 6      |
| 23 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9995550227105213 | 6      |
| 24 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.9999792583327229 | 4      |
| 25 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.9995494740677917 | 4      |
| 26 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.9995488333188073 | 6      |
| 27 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.9995478534600177 | 6      |
| 28 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Fallback   | 1.0                | -1     |
| 29 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.9995803206046965 | 6      |
| 30 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.9996217966014411 | 6      |
| 31 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999593321095548  | 6      |
| 32 | Tensor<[1, 3, 800, 1088]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | Unknown  | Unknown    | N/A                | N/A    |
| 33 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.9999291745248877 | 4      |
| 34 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999291131389926 | 4      |
| 35 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  | Done       | 0.9999292489142207 | 4      |
| 36 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.9999281276936957 | 6      |
| 37 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  | Done       | 0.999971358262238  | 4      |
| 38 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.9988581280665875 | 4      |
| 39 | Tensor<[1, 512, 50, 68]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Done       | 0.9988362600104423 | 4      |
| 40 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Unknown  | Unknown    | N/A                | N/A    |
| 41 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
| 42 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Unknown  | Unknown    | N/A                | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ?                           | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  | Done       | 0.9999954756695281 | 0      |
### aten.empty.memory_format
|    | ATen Input Variations                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [0],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Fallback   |     1 |     -1 |
|  1 | List[int] size = [],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  | Fallback   |     1 |     -1 |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[0, 1]> self = ? | Unknown  | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 136]> self = ?,<br>List[int] size = [100, 136] | Unknown  | Done       |     1 |      2 |
|  1 | Tensor<[1, 17]> self = ?,<br>List[int] size = [13, 17]    | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 34]> self = ?,<br>List[int] size = [25, 34]    | Unknown  | Done       |     1 |      2 |
|  3 | Tensor<[1, 68]> self = ?,<br>List[int] size = [50, 68]    | Unknown  | Done       |     1 |      2 |
|  4 | Tensor<[1, 9]> self = ?,<br>List[int] size = [7, 9]       | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[100, 1]> self = ?,<br>List[int] size = [100, 136] | Unknown  | Fallback   |     1 |     -1 |
|  6 | Tensor<[13, 1]> self = ?,<br>List[int] size = [13, 17]    | Unknown  | Fallback   |     1 |     -1 |
|  7 | Tensor<[25, 1]> self = ?,<br>List[int] size = [25, 34]    | Unknown  | Fallback   |     1 |     -1 |
|  8 | Tensor<[50, 1]> self = ?,<br>List[int] size = [50, 68]    | Unknown  | Fallback   |     1 |     -1 |
|  9 | Tensor<[7, 1]> self = ?,<br>List[int] size = [7, 9]       | Unknown  | Fallback   |     1 |     -1 |
### aten.fill.Scalar
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?,<br>number value = 114 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[]> self = ?,<br>number value = 120 | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[]> self = ?,<br>number value = 16  | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[]> self = ?,<br>number value = 32  | Unknown  | Fallback   |     1 |     -1 |
|  4 | Tensor<[]> self = ?,<br>number value = 61  | Unknown  | Fallback   |     1 |     -1 |
|  5 | Tensor<[]> self = ?,<br>number value = 64  | Unknown  | Fallback   |     1 |     -1 |
|  6 | Tensor<[]> self = ?,<br>number value = 8   | Unknown  | Fallback   |     1 |     -1 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 400, 544]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  | Fallback   |     1 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[0, 1]> other = ?                             | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                     | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[0]> self = ?,<br>Tensor other = 0.5                              | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                            | Unknown  | Fallback   | 1.0                | -1     |
|  5 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?   | Unknown  | Done       | 0.9999960582317254 | 0      |
|  6 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  | Done       | 0.9999960843418446 | 0      |
|  7 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Unknown  | Done       | 0.9999969907526353 | 0      |
|  8 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ? | Unknown  | Done       | 0.9999959050948689 | 0      |
|  9 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ? | Unknown  | Done       | 0.9999959821724913 | 0      |
| 10 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?   | Unknown  | Done       | 0.9999958650265414 | 0      |
| 11 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  | Done       | 0.9999959443933547 | 0      |
| 12 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Unknown  | Done       | 0.9999953468452447 | 0      |
| 13 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Unknown  | Done       | 0.9999960066213709 | 0      |
| 14 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Unknown  | Done       | 0.9999960868462769 | 0      |
| 15 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  | Done       | 0.9999959784574991 | 0      |
| 16 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor other = ?                  | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?          | Unknown  | Done       | 0.9999959936719269 | 0      |
| 18 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?        | Unknown  | Done       | 0.9999959499620042 | 0      |
| 19 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Unknown  | Done       | 0.9999966084577959 | 0      |
| 20 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ? | Unknown  | Done       | 0.9999957858927674 | 0      |
| 21 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.9999960933917068 | 0      |
| 22 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.99999612014397   | 0      |
| 23 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Unknown  | Done       | 0.9999978618146418 | 0      |
| 24 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Unknown  | Done       | 0.9999955846472579 | 0      |
| 25 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Unknown  | Done       | 0.9999958568411058 | 0      |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 800, 1066]> self = ?,<br>List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  | Fallback   |     1 |     -1 |
### aten.permute.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 4, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 9, 4, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 9, 4, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 9, 4, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Unknown  | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 9, 4, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]      | Unknown  | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 9, 91, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 9, 91, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 9, 91, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Unknown  | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 9, 91, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]     | Unknown  | Fallback   |     1 |     -1 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 50, 68]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 100, 136]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 200, 272]> self = ? | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 2048, 25, 34]> self = ?  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 100, 136]> self = ? | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 13, 17]> self = ?   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 200, 272]> self = ? | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 25, 34]> self = ?   | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 256, 50, 68]> self = ?   | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 256, 7, 9]> self = ?     | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 512, 100, 136]> self = ? | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[1, 512, 25, 34]> self = ?   | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[1, 512, 50, 68]> self = ?   | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[1, 64, 200, 272]> self = ?  | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[1, 64, 400, 544]> self = ?  | Unknown  | Done       |     1 |      0 |
### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ? | Unknown  | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 128, 1, 1]> self = ?  | Unknown  | Done       | 0.999992 |      0 |
|  2 | Tensor<[1, 2048, 1, 1]> self = ? | Unknown  | Done       | 0.999994 |      0 |
|  3 | Tensor<[1, 256, 1, 1]> self = ?  | Unknown  | Done       | 0.999999 |      0 |
|  4 | Tensor<[1, 512, 1, 1]> self = ?  | Unknown  | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 64, 1, 1]> self = ?   | Unknown  | Done       | 0.999996 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 0            | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 1            | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 2            | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 3            | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0  | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 3, 800, 1066]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | Done       |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4 | Unknown  | Fallback   | 1.0   | -1     |
|  8 | Tensor<[0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Done       | 1.0   | -1     |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1  | Unknown  | Fallback   |     1 |     -5 |
|  1 | Tensor<[1, 163206, 91]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1 | Unknown  | Fallback   |     1 |     -5 |
|  2 | Tensor<[163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567]                     | Unknown  | Fallback   |     1 |     -5 |
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
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Unknown  | Unknown    | N/A   | N/A    |
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
|  0 | Tensor<[0, 1, 4]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[0, 2, 2]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]   | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]       | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]       | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]       | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]           | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136] | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]     | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]     | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]         | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                            | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                    | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                    | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                            | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[13]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[17]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[221, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[221, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[25]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[3400, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                     | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[3400, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                     | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[34]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[50]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[63, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                       | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[63, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                       | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                       | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[68]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[7]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[850, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[850, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                        | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[9]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Unknown    | N/A   | N/A    |

