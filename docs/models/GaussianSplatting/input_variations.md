# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.add.Tensor                 |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  1 | aten.bmm.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.cat.default                |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.ceil.default               |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.clamp.default              |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  5 | aten.clamp_min.default          |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  6 | aten.copy.default               |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  7 | aten.div.Tensor                 |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  8 | aten.exp.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.expand.default             |                  2 |           1 |         1 |          0 | ✅          |       1 |
| 10 | aten.eye.m                      |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.ge.Scalar                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.linalg_vector_norm.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.maximum.default            |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.mm.default                 |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 15 | aten.mul.Tensor                 |                 27 |          26 |         1 |          0 | ✅          |       1 |
| 16 | aten.neg.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 17 | aten.ones_like.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.permute.default            |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 19 | aten.pow.Tensor_Scalar          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 20 | aten.reciprocal.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 21 | aten.rsub.Scalar                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 22 | aten.select.int                 |                 30 |          30 |         0 |          0 | ✅          |       1 |
| 23 | aten.select_scatter.default     |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.sigmoid.default            |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 25 | aten.slice.Tensor               |                 15 |          10 |         5 |          0 | ✅          |       1 |
| 26 | aten.slice_scatter.default      |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 27 | aten.sqrt.default               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 28 | aten.stack.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 29 | aten.sub.Tensor                 |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 30 | aten.transpose.int              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 31 | aten.unsqueeze.default          |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 32 | aten.view.default               |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 33 | aten.zeros.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten.add.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1e-06           | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 2, 2]> self = ?,<br>Tensor<[1, 2, 2]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384, 1]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384, 3]> self = ?,<br>Tensor other = 0.5             | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384, 3]> self = ?,<br>Tensor<[1, 3]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16384]> self = ?,<br>Tensor other = 1                  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?         | Done     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3, 3]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[16384, 1, 3]>, <[16384, 24, 3]>],<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[16384, 3]>, <[16384, 1]>],<br>int dim = -1       | Done     | Unknown    | N/A   | N/A    |
### aten.ceil.default
|    | ATen Input Variations    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.clamp.default
|    | ATen Input Variations                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>Optional[number] min = 1e-12,<br>Optional[number] max = ?                       | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 3]> self = ?,<br>Optional[number] min = 0.0                                                      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384]> self = ?,<br>Optional[number] min = -0.4681396484375,<br>Optional[number] max = 0.4681396484375 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 255.0                          | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384]> self = ?,<br>Optional[number] min = 0.1                                                         | Done     | Unknown    | N/A   | N/A    |
### aten.clamp_min.default
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>number min = 1e-12 | Removed  | Unknown    | N/A   | N/A    |
### aten.copy.default
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> src = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?       | Done     | Unknown    | N/A   | N/A    |
### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 3]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>List[int] size = [16384, 4]       | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384, 3, 3] | Removed  | Unknown    | N/A   | N/A    |
### aten.eye.m
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | int n = 2,<br>int m = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
### aten.ge.Scalar
|    | ATen Input Variations                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ?,<br>number other = 0.2 | Done     | Unknown    | N/A   | N/A    |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 4]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True | None     | Unknown    | N/A   | N/A    |
### aten.maximum.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 3]> self = ?,<br>Tensor<[3, 3]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 4]> self = ?,<br>Tensor<[4, 4]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[49152, 3]> self = ?,<br>Tensor<[3, 3]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -0.4570457994644658 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -0.5900435899266435 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -1.0925484305920792 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.31539156525252005 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.3731763325901154  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.4886025119029199  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.5462742152960396  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.0                 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.0925484305920792  | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.445305721320277   | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2                   | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2.0                 | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2.890611442640554   | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 3                   | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 4                   | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ?       | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 3]> other = ?       | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[16384, 3]> self = ?,<br>Tensor other = 0.28209479177387814 | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> other = ?       | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[16384]> self = ?,<br>Tensor other = 0.5                    | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[16384]> self = ?,<br>Tensor other = 1                      | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[16384]> self = ?,<br>Tensor other = 2                      | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[16384]> self = ?,<br>Tensor other = 256                    | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[16384]> self = ?,<br>Tensor other = 3.0                    | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?             | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[16384]> self = ?,<br>Tensor<[]> other = ?                  | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0.3                     | Done     | Unknown    | N/A   | N/A    |
### aten.neg.default
|    | ATen Input Variations    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.ones_like.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 25, 3]> self = ?,<br>List[int] dims = [0, 2, 1] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] dims = [0, 2, 1]  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[3, 3]> self = ?,<br>List[int] dims = [1, 0]            | Done     | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ?,<br>number exponent = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.reciprocal.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384]> self = ?    | Done     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ?,<br>number other = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 2, 2]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 2, 2]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384, 2]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384, 2]> self = ?,<br>int dim = 1,<br>int index = 1      | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 0  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 1  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 10 | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 11 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 12 | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 13 | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 14 | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 15 | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 2  | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 3  | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 4  | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 5  | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 6  | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 7  | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 8  | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 9  | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>int index = 2   | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>int index = 1      | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>int index = 2      | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 1      | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 2      | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 3      | Done     | Unknown    | N/A   | N/A    |
### aten.select_scatter.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384]> src = ?,<br>int dim = 1,<br>int index = 0       | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384]> src = ?,<br>int dim = 1,<br>int index = 1       | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3]> src = ?,<br>int dim = 1,<br>int index = 0 | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3]> src = ?,<br>int dim = 1,<br>int index = 1 | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3]> src = ?,<br>int dim = 1,<br>int index = 2 | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384]> src = ?,<br>int dim = 1,<br>int index = 0       | None     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384]> src = ?,<br>int dim = 1,<br>int index = 1       | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384]> src = ?,<br>int dim = 1,<br>int index = 2       | None     | Unknown    | N/A   | N/A    |
### aten.sigmoid.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 3                          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384, 2, 3]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 2                   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16384, 3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                      | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 2                      | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 3                      | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[16384, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807   | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[16384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[3, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 3                          | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[4, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807       | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[4, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 3                          | Done     | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3, 3]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
### aten.sqrt.default
|    | ATen Input Variations    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[16384]>, <[16384]>],<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16384, 3]> self = ?,<br>Tensor<[3]> other = ?        | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16384]> self = ?,<br>Tensor other = 1.0              | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?       | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 3, 3]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[2, 2]> self = ?,<br>int dim = 0  | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384, 3, 3] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [49152, 3]    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[49152, 3]> self = ?,<br>List[int] size = [16384, 3, 3]    | Done     | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [16384, 3, 3],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Unknown    | N/A   | N/A    |

