# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.addmm.default              |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  1 | aten.detach.default             |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  2 | aten.mm.default                 |                 16 |          16 |         0 |          0 | ✅          |       1 |
|  3 | aten.relu.default               |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  4 | aten.sum.dim_IntList            |                  5 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.t.default                  |                 13 |          13 |         0 |          0 | ✅          |       1 |
|  6 | aten.threshold_backward.default |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.view.default               |                  5 |           5 |         0 |          0 | ✅          |       1 |
***
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[128]> self = ?,<br>Tensor<[1, 64]> mat1 = ?,<br>Tensor<[64, 128]> mat2 = ?   | Done     | Done       | 0.999987 |     -1 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 784]> mat1 = ?,<br>Tensor<[784, 128]> mat2 = ? | Done     | Done       | 0.999965 |     -1 |
|  2 | Tensor<[12]> self = ?,<br>Tensor<[1, 3]> mat1 = ?,<br>Tensor<[3, 12]> mat2 = ?       | Done     | Done       | 0.999998 |     -1 |
|  3 | Tensor<[12]> self = ?,<br>Tensor<[1, 64]> mat1 = ?,<br>Tensor<[64, 12]> mat2 = ?     | Done     | Done       | 0.999972 |     -1 |
|  4 | Tensor<[3]> self = ?,<br>Tensor<[1, 12]> mat1 = ?,<br>Tensor<[12, 3]> mat2 = ?       | Done     | Done       | 0.999975 |     -1 |
|  5 | Tensor<[64]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 64]> mat2 = ?   | Done     | Done       | 0.999981 |     -1 |
|  6 | Tensor<[64]> self = ?,<br>Tensor<[1, 12]> mat1 = ?,<br>Tensor<[12, 64]> mat2 = ?     | Done     | Done       | 0.99999  |     -1 |
|  7 | Tensor<[784]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 784]> mat2 = ? | Done     | Done       | 0.999979 |     -1 |
### aten.detach.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ? | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12]> self = ?  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 64]> self = ?  | Removed  | Done       |     1 |     -1 |
### aten.mm.default
|    | ATen Input Variations                                     | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 64]> mat2 = ?  | Done     | Done       | 0.999984 |     -1 |
|  1 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 784]> mat2 = ? | Done     | Done       | 0.999982 |     -1 |
|  2 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 3]> mat2 = ?     | Done     | Done       | 0.999995 |     -1 |
|  3 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 64]> mat2 = ?    | Done     | Done       | 0.999995 |     -1 |
|  4 | Tensor<[1, 3]> self = ?,<br>Tensor<[3, 12]> mat2 = ?      | Done     | Done       | 0.999992 |     -1 |
|  5 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 128]> mat2 = ?   | Done     | Done       | 0.999985 |     -1 |
|  6 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 12]> mat2 = ?    | Done     | Done       | 0.999992 |     -1 |
|  7 | Tensor<[1, 784]> self = ?,<br>Tensor<[784, 128]> mat2 = ? | Done     | Done       | 0.999971 |     -1 |
|  8 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 3]> mat2 = ?      | Done     | Done       | 0.999993 |     -1 |
|  9 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?     | Done     | Done       | 0.999995 |     -1 |
| 10 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?    | Done     | Done       | 0.999993 |     -1 |
| 11 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 784]> mat2 = ?   | Done     | Done       | 0.999992 |     -1 |
| 12 | Tensor<[3, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?      | Done     | Done       | 0.999997 |     -1 |
| 13 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?    | Done     | Done       | 0.999992 |     -1 |
| 14 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?     | Done     | Done       | 0.999993 |     -1 |
| 15 | Tensor<[784, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?   | Done     | Done       | 0.999992 |     -1 |
### aten.relu.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ? | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12]> self = ?  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 64]> self = ?  | Done     | Done       |     1 |     -1 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 12]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 3]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 784]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?   | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12]> self = ?    | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 3]> self = ?     | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 64]> self = ?    | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 784]> self = ?   | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[12, 3]> self = ?    | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[12, 64]> self = ?   | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[128, 64]> self = ?  | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[128, 784]> self = ? | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[3, 12]> self = ?    | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[64, 128]> self = ?  | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[64, 12]> self = ?   | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[784, 128]> self = ? | Done     | Done       |     1 |     -1 |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> grad_output = ?,<br>Tensor<[1, 128]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 12]> grad_output = ?,<br>Tensor<[1, 12]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 64]> grad_output = ?,<br>Tensor<[1, 64]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12]> self = ?,<br>List[int] size = [12]   | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3]     | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 64]> self = ?,<br>List[int] size = [64]   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 784]> self = ?,<br>List[int] size = [784] | Done     | Done       |     1 |     -1 |

