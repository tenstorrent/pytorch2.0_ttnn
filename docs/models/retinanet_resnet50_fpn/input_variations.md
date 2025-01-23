# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._unsafe_index.Tensor            |                  6 |           0 |         4 |          0 | 🚧          |    0.67 |
|  1 | aten._unsafe_view.default            |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  2 | aten.add.Tensor                      |                 30 |          29 |         1 |          0 | ✅          |    1    |
|  3 | aten.cat.default                     |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  4 | aten.clone.default                   |                 15 |          10 |         0 |          0 | 🚧          |    0.67 |
|  5 | aten.convolution.default             |                 43 |          40 |         0 |          0 | 🚧          |    0.93 |
|  6 | aten.div.Tensor                      |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  7 | aten.empty.memory_format             |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.expand.default                  |                 10 |           5 |         0 |          0 | 🚧          |    0.5  |
|  9 | aten.fill.Scalar                     |                  7 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.full.default                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.max_pool2d_with_indices.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.mul.Tensor                      |                 22 |          18 |         3 |          0 | 🚧          |    0.95 |
| 13 | aten.new_full.default                |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 14 | aten.permute.default                 |                 10 |          10 |         0 |          0 | ✅          |    1    |
| 15 | aten.relu.default                    |                 15 |          15 |         0 |          0 | ✅          |    1    |
| 16 | aten.rsqrt.default                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 17 | aten.rsub.Scalar                     |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 18 | aten.select.int                      |                  2 |           0 |         2 |          0 | ✅          |    1    |
| 19 | aten.slice.Tensor                    |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 20 | aten.split_with_sizes.default        |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.stack.default                   |                  5 |           4 |         0 |          0 | 🚧          |    0.8  |
| 22 | aten.sub.Tensor                      |                  7 |           6 |         1 |          0 | ✅          |    1    |
| 23 | aten.unsqueeze.default               |                  3 |           0 |         3 |          0 | ✅          |    1    |
| 24 | aten.view.default                    |                 37 |          37 |         0 |          0 | ✅          |    1    |
***
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 256, 25, 34]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_5] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 50, 68]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_7] | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_2] | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_3] | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_2] | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_3] | Removed  | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int] size = [1, 122400, 4]   | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int] size = [1, 122400, 91] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int] size = [1, 1989, 4]       | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int] size = [1, 1989, 91]     | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int] size = [1, 7650, 4]       | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int] size = [1, 7650, 91]     | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int] size = [1, 30600, 4]      | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int] size = [1, 30600, 91]    | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int] size = [1, 567, 4]          | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int] size = [1, 567, 91]        | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[100, 136]> self = ?,<br>List[int] size = [13600]                   | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[13, 17]> self = ?,<br>List[int] size = [221]                       | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[25, 34]> self = ?,<br>List[int] size = [850]                       | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[50, 68]> self = ?,<br>List[int] size = [3400]                      | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[7, 9]> self = ?,<br>List[int] size = [63]                          | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                      | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1        |      0 |
|  4 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                      | Done     | Done       | 1        |      0 |
|  7 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  9 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1        |      0 |
| 10 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 11 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ? | Done     | Done       | 0.999998 |      0 |
| 12 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 13 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ? | Done     | Done       | 0.999998 |      0 |
| 14 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 15 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 16 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?   | Removed  | Done       | 0.999998 |      0 |
| 17 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1        |      0 |
| 18 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 19 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ? | Done     | Done       | 0.999998 |      0 |
| 20 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 21 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 22 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1        |      0 |
| 23 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 24 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | Done       | 0.999998 |      0 |
| 25 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?               | Done     | Done       | 0.999998 |      0 |
| 26 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Done     | Done       | 0.999998 |      0 |
| 27 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Done     | Done       | 0.999998 |      0 |
| 28 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.999998 |      0 |
| 29 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Done     | Done       | 0.999998 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 122400, 4]>, <[1, 30600, 4]>, <[1, 7650, 4]>, <[1, 1989, 4]>, <[1, 567, 4]>],<br>int dim = 1      | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 122400, 91]>, <[1, 30600, 91]>, <[1, 7650, 91]>, <[1, 1989, 91]>, <[1, 567, 91]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[122400, 4]>, <[30600, 4]>, <[7650, 4]>, <[1989, 4]>, <[567, 4]>]                                     | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | Done       |     1 |      0 |
| 10 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | None     | Done       |     1 |      0 |
| 11 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | None     | Done       |     1 |      0 |
| 12 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | None     | Done       |     1 |      0 |
| 13 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | None     | Done       |     1 |      0 |
| 14 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | None     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999839 |      4 |
|  1 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999966 |      4 |
|  2 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999964 |      6 |
|  3 | Tensor<[1, 1024, 50, 68]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999966 |      4 |
|  4 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999815 |      4 |
|  5 | Tensor<[1, 128, 100, 136]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999981 |      4 |
|  6 | Tensor<[1, 128, 200, 272]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999813 |      4 |
|  7 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999954 |      6 |
|  8 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999955 |      4 |
|  9 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999546 |      4 |
| 10 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999544 |      6 |
| 11 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999542 |      6 |
| 12 | Tensor<[1, 256, 100, 136]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | 1        |     -1 |
| 13 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999562 |      6 |
| 14 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999596 |      6 |
| 15 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999571 |      6 |
| 16 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99957  |      6 |
| 17 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999965 |      4 |
| 18 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999965 |      4 |
| 19 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999965 |      4 |
| 20 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999558 |      6 |
| 21 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999561 |      6 |
| 22 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999556 |      6 |
| 23 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999552 |      6 |
| 24 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999979 |      4 |
| 25 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99955  |      4 |
| 26 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999546 |      6 |
| 27 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999544 |      6 |
| 28 | Tensor<[1, 256, 50, 68]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | 1        |     -1 |
| 29 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.99961  |      6 |
| 30 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[36, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999616 |      6 |
| 31 | Tensor<[1, 256, 7, 9]> input = ?,<br>Tensor<[819, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[819]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.99958  |      6 |
| 32 | Tensor<[1, 3, 800, 1088]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1            | None     | Fallback   | 1        |     -1 |
| 33 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999929 |      4 |
| 34 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999929 |      4 |
| 35 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999929 |      4 |
| 36 | Tensor<[1, 512, 100, 136]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999928 |      6 |
| 37 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999971 |      4 |
| 38 | Tensor<[1, 512, 25, 34]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99886  |      4 |
| 39 | Tensor<[1, 512, 50, 68]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.998843 |      4 |
| 40 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999988 |      4 |
| 41 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999988 |      4 |
| 42 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.99992  |      4 |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Removed  | Done       | 0.999994 |      0 |
### aten.empty.memory_format
|    | ATen Input Variations                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   |     0 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 136]> self = ?,<br>List[int] size = [100, 136] | Done     | Done       |     1 |      2 |
|  1 | Tensor<[1, 17]> self = ?,<br>List[int] size = [13, 17]    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 34]> self = ?,<br>List[int] size = [25, 34]    | Done     | Done       |     1 |      2 |
|  3 | Tensor<[1, 68]> self = ?,<br>List[int] size = [50, 68]    | Done     | Done       |     1 |      2 |
|  4 | Tensor<[1, 9]> self = ?,<br>List[int] size = [7, 9]       | Done     | Done       |     1 |      0 |
|  5 | Tensor<[100, 1]> self = ?,<br>List[int] size = [100, 136] | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[13, 1]> self = ?,<br>List[int] size = [13, 17]    | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[25, 1]> self = ?,<br>List[int] size = [25, 34]    | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[50, 1]> self = ?,<br>List[int] size = [50, 68]    | None     | Fallback   |     1 |     -1 |
|  9 | Tensor<[7, 1]> self = ?,<br>List[int] size = [7, 9]       | None     | Fallback   |     1 |     -1 |
### aten.fill.Scalar
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?,<br>number value = 114 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[]> self = ?,<br>number value = 120 | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[]> self = ?,<br>number value = 16  | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[]> self = ?,<br>number value = 32  | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[]> self = ?,<br>number value = 61  | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[]> self = ?,<br>number value = 64  | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[]> self = ?,<br>number value = 8   | None     | Fallback   |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.float32 | Done     | Unknown    | N/A   | N/A    |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 400, 544]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Done     | Done       |     1 |      4 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[]> other = ?                                 | None     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?   | Done     | Done       | 0.9999966634733333 | 0      |
|  2 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.9999958796343195 | 0      |
|  3 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | Done       | 0.9999983018264501 | 0      |
|  4 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ? | Done     | Done       | 0.9999960255990176 | 0      |
|  5 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ? | Done     | Done       | 0.9999961330180186 | 0      |
|  6 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?   | Done     | Done       | 0.9999946057864963 | 0      |
|  7 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999959368853902 | 0      |
|  8 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | Done       | 0.9999960719783937 | 0      |
|  9 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Done     | Done       | 0.9999957854194542 | 0      |
| 10 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Done     | Done       | 0.9999957006593055 | 0      |
| 11 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999959367778298 | 0      |
| 12 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor other = ?                  | Removed  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?          | Removed  | Done       | 0.9999959357761573 | 0      |
| 14 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?        | Removed  | Done       | 0.9999959683692647 | 0      |
| 15 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Done     | Done       | 0.9999960154716525 | 0      |
| 16 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ? | Done     | Done       | 0.9999960441669792 | 0      |
| 17 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999961319982164 | 0      |
| 18 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999960461055162 | 0      |
| 19 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | Done       | 0.9999969229528943 | 0      |
| 20 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Done     | Done       | 0.9999962719596235 | 0      |
| 21 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?   | Done     | Done       | 0.9999959965845276 | 0      |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 800, 1066]> self = ?,<br>List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
### aten.permute.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 4, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 9, 4, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 9, 4, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 9, 4, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 9, 4, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]      | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 9, 91, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 9, 91, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 9, 91, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 9, 91, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]     | Done     | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 50, 68]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 100, 136]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 200, 272]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2048, 25, 34]> self = ?  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 100, 136]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 13, 17]> self = ?   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 200, 272]> self = ? | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 25, 34]> self = ?   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 256, 50, 68]> self = ?   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 256, 7, 9]> self = ?     | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 512, 100, 136]> self = ? | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 512, 25, 34]> self = ?   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 512, 50, 68]> self = ?   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 64, 200, 272]> self = ?  | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 64, 400, 544]> self = ?  | Done     | Done       |     1 |      0 |
### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ? | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 128, 1, 1]> self = ?  | Done     | Done       | 0.999993 |      0 |
|  2 | Tensor<[1, 2048, 1, 1]> self = ? | Done     | Done       | 0.999997 |      0 |
|  3 | Tensor<[1, 256, 1, 1]> self = ?  | Done     | Done       | 0.999997 |      0 |
|  4 | Tensor<[1, 512, 1, 1]> self = ?  | Done     | Done       | 0.999993 |      0 |
|  5 | Tensor<[1, 64, 1, 1]> self = ?   | Done     | Done       | 0.999992 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0 | Removed  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0  | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 3, 800, 1066]> self = ?,<br>int dim = 0,<br>int index = 0 | Removed  | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1  | None     | Fallback   |     1 |     -5 |
|  1 | Tensor<[1, 163206, 91]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1 | None     | Fallback   |     1 |     -5 |
|  2 | Tensor<[163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567]                     | None     | Fallback   |     1 |     -5 |
### aten.stack.default
|    | ATen Input Variations                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[13600]>, <[13600]>, <[13600]>, <[13600]>],<br>int dim = 1 | None     | Fallback   |     1 |     -1 |
|  1 | List[Tensor] tensors = [<[221]>, <[221]>, <[221]>, <[221]>],<br>int dim = 1         | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[3400]>, <[3400]>, <[3400]>, <[3400]>],<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[63]>, <[63]>, <[63]>, <[63]>],<br>int dim = 1             | Done     | Done       |     1 |      0 |
|  4 | List[Tensor] tensors = [<[850]>, <[850]>, <[850]>, <[850]>],<br>int dim = 1         | Done     | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.999997 |      0 |
|  2 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Removed  | Done       | 0.999998 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[3]> self = ?,<br>int dim = 1           | Removed  | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]   | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]       | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]       | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]       | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]           | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136] | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]     | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]     | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]     | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]         | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                            | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                    | Done     | Done       |     1 |     -1 |
| 14 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                    | Done     | Done       |     1 |     -1 |
| 15 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                            | Done     | Done       |     1 |     -1 |
| 16 | Tensor<[13]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       |     1 |     -1 |
| 17 | Tensor<[17]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       |     1 |     -1 |
| 18 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Done     | Done       |     1 |     -1 |
| 19 | Tensor<[221, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Done     | Done       |     1 |     -1 |
| 20 | Tensor<[221, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Done     | Done       |     1 |     -1 |
| 21 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       |     1 |     -1 |
| 22 | Tensor<[25]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       |     1 |     -1 |
| 23 | Tensor<[3400, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                     | Done     | Done       |     1 |     -1 |
| 24 | Tensor<[3400, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                     | Done     | Done       |     1 |     -1 |
| 25 | Tensor<[34]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       |     1 |     -1 |
| 26 | Tensor<[50]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       |     1 |     -1 |
| 27 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       |     1 |     -1 |
| 28 | Tensor<[63, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                       | Done     | Done       |     1 |     -1 |
| 29 | Tensor<[63, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                       | Done     | Done       |     1 |     -1 |
| 30 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                       | Done     | Done       |     1 |     -1 |
| 31 | Tensor<[68]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       |     1 |     -1 |
| 32 | Tensor<[7]> self = ?,<br>List[int] size = [-1, 1]                              | Done     | Done       |     1 |     -1 |
| 33 | Tensor<[850, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Done     | Done       |     1 |     -1 |
| 34 | Tensor<[850, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Done     | Done       |     1 |     -1 |
| 35 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                        | Done     | Done       |     1 |     -1 |
| 36 | Tensor<[9]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       |     1 |     -1 |

