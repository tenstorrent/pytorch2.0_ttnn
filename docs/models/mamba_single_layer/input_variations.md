# High Level Operations Status
|    | Operations                    |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.add.Tensor               |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  1 | aten.bmm.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.convolution.default      |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.embedding.default        |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.exp.default              |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  5 | aten.mean.dim                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.mm.default               |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  7 | aten.mul.Tensor               |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  8 | aten.neg.default              |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  9 | aten.permute.default          |                 10 |           9 |         1 |          0 | ✅          |       1 |
| 10 | aten.pow.Tensor_Scalar        |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.rsqrt.default            |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.select.int               |                 66 |          66 |         0 |          0 | ✅          |       1 |
| 13 | aten.silu.default             |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.slice.Tensor             |                  6 |           1 |         5 |          0 | ✅          |       1 |
| 15 | aten.softplus.default         |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.split_with_sizes.default |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 17 | aten.stack.default            |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.t.default                |                  5 |           1 |         4 |          0 | ✅          |       1 |
| 19 | aten.unsqueeze.default        |                  5 |           3 |         2 |          0 | ✅          |       1 |
| 20 | aten.view.default             |                 12 |          12 |         0 |          0 | ✅          |       1 |
| 21 | aten.zeros.default            |                  1 |           0 |         1 |          0 | ✅          |       1 |
***
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 1]> self = ?,<br>Tensor other = 1e-05               | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 2560]> self = ?,<br>Tensor<[1, 33, 2560]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[1, 33, 5120]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[5120]> other = ?        | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 5120, 16]> self = ?,<br>Tensor<[1, 5120, 16]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5120, 16]> self = ?,<br>Tensor<[1, 16, 1]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5120, 33]> input = ?,<br>Tensor<[5120, 1, 4]> weight = ?,<br>Optional[Tensor]<[5120]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [3],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 5120 | Done     | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[50280, 2560]> weight = ?,<br>Tensor<[1, 33]> indices = ? | Done     | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 5120, 16]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[5120, 16]> self = ?        | Removed  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 2560]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Done     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[33, 160]> self = ?,<br>Tensor<[160, 5120]> mat2 = ?    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[33, 2560]> self = ?,<br>Tensor<[2560, 10240]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[33, 2560]> self = ?,<br>Tensor<[2560, 50280]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[33, 5120]> self = ?,<br>Tensor<[5120, 192]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[33, 5120]> self = ?,<br>Tensor<[5120, 2560]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 2560]> self = ?,<br>Tensor<[1, 33, 1]> other = ?           | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 2560]> self = ?,<br>Tensor<[2560]> other = ?               | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120, 16]> self = ?,<br>Tensor<[1, 33, 5120, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 5120, 1]> self = ?,<br>Tensor<[1, 1, 5120, 16]> other = ?  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 33, 5120, 1]> self = ?,<br>Tensor<[1, 33, 1, 16]> other = ?    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[1, 33, 5120]> other = ?        | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[5120]> other = ?               | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 5120, 16]> self = ?,<br>Tensor<[1, 5120, 16]> other = ?        | Done     | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[5120, 16]> self = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 16, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2, 3] | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 33, 5120]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 5120, 16]> self = ?,<br>List[int] dims = [0, 1, 2]       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 5120, 16]> self = ?,<br>List[int] dims = [1, 2, 0]       | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 5120, 33]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[5120, 1, 1]> self = ?,<br>List[int] dims = [2, 0, 1]        | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[5120, 16, 1, 1]> self = ?,<br>List[int] dims = [2, 3, 0, 1] | Removed  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 2560]> self = ?,<br>number exponent = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 1        | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 10       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 11       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 12       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 13       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 14       | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 15       | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 16       | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 17       | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 18       | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 19       | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 2        | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 20       | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 21       | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 22       | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 23       | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 24       | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 25       | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 26       | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 27       | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 28       | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 29       | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 3        | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 30       | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 31       | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 32       | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 4        | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 5        | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 6        | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 7        | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 8        | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 1,<br>int index = 9        | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 0  | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 1  | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 10 | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 11 | Done     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 12 | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 13 | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 14 | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 15 | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 16 | Done     | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 17 | Done     | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 18 | Done     | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 19 | Done     | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 2  | Done     | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 20 | Done     | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 21 | Done     | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 22 | Done     | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 23 | Done     | Unknown    | N/A   | N/A    |
| 50 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 24 | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 25 | Done     | Unknown    | N/A   | N/A    |
| 52 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 26 | Done     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 27 | Done     | Unknown    | N/A   | N/A    |
| 54 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 28 | Done     | Unknown    | N/A   | N/A    |
| 55 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 29 | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 3  | Done     | Unknown    | N/A   | N/A    |
| 57 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 30 | Done     | Unknown    | N/A   | N/A    |
| 58 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 31 | Done     | Unknown    | N/A   | N/A    |
| 59 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 32 | Done     | Unknown    | N/A   | N/A    |
| 60 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 4  | Done     | Unknown    | N/A   | N/A    |
| 61 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 5  | Done     | Unknown    | N/A   | N/A    |
| 62 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 6  | Done     | Unknown    | N/A   | N/A    |
| 63 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 7  | Done     | Unknown    | N/A   | N/A    |
| 64 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 8  | Done     | Unknown    | N/A   | N/A    |
| 65 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 1,<br>int index = 9  | Done     | Unknown    | N/A   | N/A    |
### aten.silu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 5120]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 5120, 36]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 5120, 36]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 5120, 36]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 33                      | Done     | Unknown    | N/A   | N/A    |
### aten.softplus.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 5120]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 10240]> self = ?,<br>List[int] split_sizes = [5120, 5120],<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 192]> self = ?,<br>List[int] split_sizes = [160, 16, 16],<br>int dim = -1  | Done     | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>, <[1, 5120]>],<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[10240, 2560]> self = ? | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[192, 5120]> self = ?   | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2560, 5120]> self = ?  | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[50280, 2560]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[5120, 160]> self = ?   | Removed  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16]> self = ?,<br>int dim = 2       | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 3   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120]> self = ?,<br>int dim = 3 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[5120, 16, 1]> self = ?,<br>int dim = 3 | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[5120, 16]> self = ?,<br>int dim = 2    | Removed  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 160]> self = ?,<br>List[int] size = [33, 160]      | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 2560]> self = ?,<br>List[int] size = [33, 2560]    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120]> self = ?,<br>List[int] size = [33, 5120]    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 5120, 1]> self = ?,<br>List[int] size = [1, 5120]      | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 5120, 1]> self = ?,<br>List[int] size = [5120, 1, 1]   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1]       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[33, 10240]> self = ?,<br>List[int] size = [1, 33, 10240]  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[33, 192]> self = ?,<br>List[int] size = [1, 33, 192]      | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[33, 2560]> self = ?,<br>List[int] size = [1, 33, 2560]    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[33, 50280]> self = ?,<br>List[int] size = [1, 33, 50280]  | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[33, 5120]> self = ?,<br>List[int] size = [1, 33, 5120]    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[5120, 16, 1]> self = ?,<br>List[int] size = [1, 5120, 16] | Done     | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 5120, 16],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Unknown    | N/A   | N/A    |

