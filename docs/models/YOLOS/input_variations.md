# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default          |                  4 |           2 |         0 |          0 | 🚧          |     0.5 |
|  2 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  3 | aten.add.Tensor                |                 12 |          12 |         0 |          0 | ✅          |     1   |
|  4 | aten.addmm.default             |                  6 |           6 |         0 |          0 | ✅          |     1   |
|  5 | aten.arange.default            |                  4 |           0 |         0 |          0 | ✘           |     0   |
|  6 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  7 | aten.cat.default               |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  8 | aten.clamp.default             |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  9 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 10 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 11 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 12 | aten.expand.default            |                  5 |           0 |         5 |          0 | ✅          |     1   |
| 13 | aten.floor.default             |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 14 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 15 | aten.mul.Tensor                |                 10 |          10 |         0 |          0 | ✅          |     1   |
| 16 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 17 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 18 | aten.relu.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 19 | aten.rsub.Scalar               |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 20 | aten.select.int                |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 21 | aten.sigmoid.default           |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 22 | aten.slice.Tensor              |                  9 |           3 |         6 |          0 | ✅          |     1   |
| 23 | aten.sub.Tensor                |                 12 |          12 |         0 |          0 | ✅          |     1   |
| 24 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 25 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 26 | aten.unsqueeze.default         |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 27 | aten.view.default              |                 21 |          21 |         0 |          0 | ✅          |     1   |
***
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   |     PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.99957 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[int] dtype = torch.int64       | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[int] dtype = torch.int64       | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 192, 50, 83]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 192, 50, 83]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 1, 1, 1]>, <[1, 192, 1, 1]>, <[1, 1, 32, 1]>, <[1, 1, 1, 42]>] | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                   | Done     | Done       | 0.999988 |      0 |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                    | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                      | Done     | Done       | 0.999997 |      0 |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                    | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                      | Done     | Done       | 0.999986 |      0 |
|  5 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                   | Done     | Done       | 0.999987 |      0 |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                    | Done     | Done       | 0.999997 |      0 |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                      | Done     | Done       | 0.999999 |      0 |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                    | Done     | Done       | 0.999995 |      0 |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                      | Done     | Done       | 0.999981 |      0 |
| 10 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?     | Done     | Done       | 0.999998 |      0 |
| 11 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[192]> self = ?,<br>Tensor<[100, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?  | Done     | Done       | 0.999972 |      0 |
|  1 | Tensor<[192]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ? | Done     | Done       | 0.999976 |      0 |
|  2 | Tensor<[192]> self = ?,<br>Tensor<[1445, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  3 | Tensor<[4]> self = ?,<br>Tensor<[100, 192]> mat1 = ?,<br>Tensor<[192, 4]> mat2 = ?      | Done     | Done       | 0.999974 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ? | Done     | Done       | 0.999976 |      0 |
|  5 | Tensor<[92]> self = ?,<br>Tensor<[100, 192]> mat1 = ?,<br>Tensor<[192, 92]> mat2 = ?    | Done     | Done       | 0.999971 |      0 |
### aten.arange.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False   | None     | Fallback   |     1 |     -1 |
|  1 | number end = 192,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   |     1 |     -1 |
|  2 | number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Fallback   |     1 |     -1 |
|  3 | number end = 42,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                               | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ? | Done     | Done       | 0.999963 |      0 |
|  1 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?   | Done     | Done       | 0.999986 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 192]>, <[1, 1344, 192]>, <[1, 100, 192]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clamp.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 82 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 49 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1445, 192]> self = ?                                                             | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last     | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 3, 1445, 1445]> self = ?                                                         | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 512, 672]> input = ?,<br>Tensor<[192, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0 | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 192]> self = ?,<br>List[int] size = [1, -1, -1]               | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [1, -1, -1]             | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445] | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]     | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [1, 3, 64, 1445]     | Removed  | Done       |     1 |     -1 |
### aten.floor.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 32, 1]> self = ? | Done     | Done       |     1 |      0 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1445, 768]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75               | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763  | Done     | Done       | 0.999997 |      0 |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?    | Done     | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75               | Done     | Done       | 0.999999 |      0 |
|  5 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                | Done     | Done       | 0.999997 |      0 |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625              | Done     | Done       | 0.999997 |      0 |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?    | Done     | Done       | 0.999998 |      0 |
|  8 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ? | Done     | Done       | 0.999996 |      0 |
|  9 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ? | Done     | Done       | 0.999995 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1445, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 192]> self = ? | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999994 |      0 |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0 | Done     | Done       | 0.999974 |      0 |
|  2 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0 | Done     | Done       | 0.999975 |      0 |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      1 |
### aten.sigmoid.default
|    | ATen Input Variations        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 100, 4]> self = ? | Done     | Done       | 0.999767 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = 9223372036854775807 | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 4150, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = 9223372036854775807 | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -100                   | Done     | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0             | Done     | Done       | 0.999985 |      0 |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75            | Done     | Done       | 0.999967 |      0 |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5              | Done     | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                | Done     | Done       | 0.999989 |      0 |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25             | Done     | Done       | 0.999989 |      0 |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ? | Done     | Done       | 0.999998 |      0 |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0             | Done     | Done       | 0.999975 |      0 |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75            | Done     | Done       | 0.999991 |      0 |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5              | Done     | Done       | 1        |      0 |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                | Done     | Done       | 0.999994 |      0 |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25             | Done     | Done       | 0.999993 |      0 |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ? | Done     | Done       | 0.999999 |      0 |
### aten.t.default
|    | ATen Input Variations       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[192, 192]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[192, 768]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[4, 192]> self = ?   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[768, 192]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[92, 192]> self = ?  | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 4150, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 192]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]           | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1, 1445, 3, 64]    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]         | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] size = [1, 1445, 192]    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]         | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]    | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]    | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445] | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]     | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]     | Done     | Done       |     1 |      0 |
| 10 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]           | Done     | Done       |     1 |      0 |
| 11 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]               | Done     | Done       |     1 |      0 |
| 12 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]             | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]         | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]         | Done     | Done       |     1 |      0 |
| 15 | Tensor<[192]> self = ?,<br>List[int] size = [1, 192, 1, 1]               | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1]> self = ?,<br>List[int] size = [1, 1, 1, 1]                   | Done     | Done       |     1 |      0 |
| 17 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445] | Done     | Done       |     1 |      0 |
| 18 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]     | Done     | Done       |     1 |      0 |
| 19 | Tensor<[32]> self = ?,<br>List[int] size = [1, 1, 32, 1]                 | Done     | Done       |     1 |      0 |
| 20 | Tensor<[42]> self = ?,<br>List[int] size = [1, 1, 1, 42]                 | Done     | Done       |     1 |      0 |

