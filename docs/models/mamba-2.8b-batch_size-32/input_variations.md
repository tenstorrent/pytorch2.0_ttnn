# High Level Operations Status
|    | Operations                    |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._unsafe_view.default     |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor               |                  5 |           0 |         5 |          0 | ✅          |       1 |
|  2 | aten.bmm.default              |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  3 | aten.clone.default            |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  4 | aten.convolution.default      |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  5 | aten.embedding.default        |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  6 | aten.exp.default              |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  7 | aten.mean.dim                 |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  8 | aten.mm.default               |                  5 |           0 |         5 |          0 | ✅          |       1 |
|  9 | aten.mul.Tensor               |                 10 |           3 |         7 |          0 | ✅          |       1 |
| 10 | aten.neg.default              |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 11 | aten.permute.default          |                 15 |           5 |        10 |          0 | ✅          |       1 |
| 12 | aten.pow.Tensor_Scalar        |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 13 | aten.rsqrt.default            |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 14 | aten.select.int               |                 66 |           0 |        66 |          0 | ✅          |       1 |
| 15 | aten.silu.default             |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 16 | aten.slice.Tensor             |                  6 |           0 |         6 |          0 | ✅          |       1 |
| 17 | aten.softplus.default         |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 18 | aten.split_with_sizes.default |                  2 |           0 |         2 |          0 | ✅          |       1 |
| 19 | aten.stack.default            |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 20 | aten.t.default                |                  5 |           0 |         5 |          0 | ✅          |       1 |
| 21 | aten.unsqueeze.default        |                  7 |           4 |         3 |          0 | ✅          |       1 |
| 22 | aten.view.default             |                 16 |           0 |        16 |          0 | ✅          |       1 |
| 23 | aten.zeros.default            |                  1 |           0 |         1 |          0 | ✅          |       1 |
***
### aten._unsafe_view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 5120]> self = ?,<br>List[int] size = [1056, 5120] | Removed  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 1]> self = ?,<br>Tensor other = 1e-05                | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 33, 2560]> self = ?,<br>Tensor<[32, 33, 2560]> other = ? | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 33, 5120]> self = ?,<br>Tensor<[32, 33, 5120]> other = ? | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 33, 5120]> self = ?,<br>Tensor<[5120]> other = ?         | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 5120, 16]> self = ?,<br>Tensor<[32, 5120, 16]> other = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 5120, 16]> self = ?,<br>Tensor<[32, 16, 1]> mat2 = ? | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, s0, s1]> self = ?,<br>Tensor<[32, s1, 1]> mat2 = ?   | Removed  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 5120]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 5120, 33]> input = ?,<br>Tensor<[5120, 1, 4]> weight = ?,<br>Optional[Tensor]<[5120]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 5120 | Removed  | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[50280, 2560]> weight = ?,<br>Tensor<[32, 33]> indices = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 5120, 16]> self = ? | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[5120, 16]> self = ?         | Removed  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 2560]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Removed  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1056, 160]> self = ?,<br>Tensor<[160, 5120]> mat2 = ?    | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1056, 2560]> self = ?,<br>Tensor<[2560, 10240]> mat2 = ? | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1056, 2560]> self = ?,<br>Tensor<[2560, 50280]> mat2 = ? | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1056, 5120]> self = ?,<br>Tensor<[5120, 192]> mat2 = ?   | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1056, 5120]> self = ?,<br>Tensor<[5120, 2560]> mat2 = ?  | Removed  | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 2560]> self = ?,<br>Tensor<[2560]> other = ?                | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 33, 2560]> self = ?,<br>Tensor<[32, 33, 1]> other = ?           | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 33, 5120, 16]> self = ?,<br>Tensor<[32, 33, 5120, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 33, 5120, 1]> self = ?,<br>Tensor<[1, 1, 5120, 16]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 33, 5120, 1]> self = ?,<br>Tensor<[32, 33, 1, 16]> other = ?    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 33, 5120, 1]> self = ?,<br>Tensor<[32, 33, 1, s2]> other = ?    | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 33, 5120, s2]> self = ?,<br>Tensor<[32, 33, 5120, 1]> other = ? | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 33, 5120]> self = ?,<br>Tensor<[32, 33, 5120]> other = ?        | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 33, 5120]> self = ?,<br>Tensor<[5120]> other = ?                | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 5120, 16]> self = ?,<br>Tensor<[32, 5120, 16]> other = ?        | Removed  | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[5120, 16]> self = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 16]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 1, s1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 16, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 33, 16, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 33, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2, 3] | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 33, 5120]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 33, s2, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 5120, 16]> self = ?,<br>List[int] dims = [0, 1, 2]       | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2]        | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 5120, 33]> self = ?,<br>List[int] dims = [0, 2, 1]       | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, s0, 1]> self = ?,<br>List[int] dims = [0, 1, 2]          | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, s0, s1]> self = ?,<br>List[int] dims = [0, 1, 2]         | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[32, s1, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[5120, 16, 1, 1]> self = ?,<br>List[int] dims = [2, 3, 0, 1]  | Done     | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 2560]> self = ?,<br>number exponent = 2 | Removed  | Unknown    | N/A   | N/A    |
### aten.rsqrt.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 1]> self = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 0        | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 1        | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 10       | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 11       | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 12       | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 13       | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 14       | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 15       | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 16       | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 17       | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 18       | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 19       | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 2        | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 20       | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 21       | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 22       | Removed  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 23       | Removed  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 24       | Removed  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 25       | Removed  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 26       | Removed  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 27       | Removed  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 28       | Removed  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 29       | Removed  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 3        | Removed  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 30       | Removed  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 31       | Removed  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 32       | Removed  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 4        | Removed  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 5        | Removed  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 6        | Removed  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 7        | Removed  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 8        | Removed  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 9        | Removed  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 0  | Removed  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 1  | Removed  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 10 | Removed  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 11 | Removed  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 12 | Removed  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 13 | Removed  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 14 | Removed  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 15 | Removed  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 16 | Removed  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 17 | Removed  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 18 | Removed  | Unknown    | N/A   | N/A    |
| 44 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 19 | Removed  | Unknown    | N/A   | N/A    |
| 45 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 2  | Removed  | Unknown    | N/A   | N/A    |
| 46 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 20 | Removed  | Unknown    | N/A   | N/A    |
| 47 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 21 | Removed  | Unknown    | N/A   | N/A    |
| 48 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 22 | Removed  | Unknown    | N/A   | N/A    |
| 49 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 23 | Removed  | Unknown    | N/A   | N/A    |
| 50 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 24 | Removed  | Unknown    | N/A   | N/A    |
| 51 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 25 | Removed  | Unknown    | N/A   | N/A    |
| 52 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 26 | Removed  | Unknown    | N/A   | N/A    |
| 53 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 27 | Removed  | Unknown    | N/A   | N/A    |
| 54 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 28 | Removed  | Unknown    | N/A   | N/A    |
| 55 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 29 | Removed  | Unknown    | N/A   | N/A    |
| 56 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 3  | Removed  | Unknown    | N/A   | N/A    |
| 57 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 30 | Removed  | Unknown    | N/A   | N/A    |
| 58 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 31 | Removed  | Unknown    | N/A   | N/A    |
| 59 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 32 | Removed  | Unknown    | N/A   | N/A    |
| 60 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 4  | Removed  | Unknown    | N/A   | N/A    |
| 61 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 5  | Removed  | Unknown    | N/A   | N/A    |
| 62 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 6  | Removed  | Unknown    | N/A   | N/A    |
| 63 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 7  | Removed  | Unknown    | N/A   | N/A    |
| 64 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 8  | Removed  | Unknown    | N/A   | N/A    |
| 65 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 9  | Removed  | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 5120]> self = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 33, 5120, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 5120, 36]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 5120, 36]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 5120, 36]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 33                      | Removed  | Unknown    | N/A   | N/A    |
### aten.softplus.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 5120]> self = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 33, 10240]> self = ?,<br>List[int] split_sizes = [5120, 5120],<br>int dim = -1 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 33, 192]> self = ?,<br>List[int] split_sizes = [160, 16, 16],<br>int dim = -1  | Removed  | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>, <[32, 5120]>],<br>int dim = 1 | Removed  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[10240, 2560]> self = ? | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[192, 5120]> self = ?   | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2560, 5120]> self = ?  | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[50280, 2560]> self = ? | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[5120, 160]> self = ?   | Removed  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 16]> self = ?,<br>int dim = 2       | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 3   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 33, 5120]> self = ?,<br>int dim = 3 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 33, s2]> self = ?,<br>int dim = 3   | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, s1]> self = ?,<br>int dim = 2       | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[5120, 16, 1]> self = ?,<br>int dim = 3  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[5120, 16]> self = ?,<br>int dim = 2     | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1056, 10240]> self = ?,<br>List[int] size = [32, 33, 10240] | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1056, 192]> self = ?,<br>List[int] size = [32, 33, 192]     | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1056, 2560]> self = ?,<br>List[int] size = [32, 33, 2560]   | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1056, 50280]> self = ?,<br>List[int] size = [32, 33, 50280] | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1056, 5120]> self = ?,<br>List[int] size = [32, 33, 5120]   | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 16, 1]> self = ?,<br>List[int] size = [32, 16, 1]       | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 33, 160]> self = ?,<br>List[int] size = [1056, 160]     | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 33, 2560]> self = ?,<br>List[int] size = [1056, 2560]   | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 33, 5120]> self = ?,<br>List[int] size = [1056, 5120]   | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 5120, 16]> self = ?,<br>List[int] size = [32, 5120, 16] | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, 5120, 1]> self = ?,<br>List[int] size = [32, 5120, 1]   | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 5120, 1]> self = ?,<br>List[int] size = [32, 5120]      | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, s0, 1]> self = ?,<br>List[int] size = [32, <s0>, 1]     | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[32, s0, 1]> self = ?,<br>List[int] size = [32, <s0>]        | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[32, s0, s1]> self = ?,<br>List[int] size = [32, <s0>, <s1>] | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[32, s1, 1]> self = ?,<br>List[int] size = [32, <s1>, 1]     | Removed  | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [32, 5120, 16],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Unknown    | N/A   | N/A    |

