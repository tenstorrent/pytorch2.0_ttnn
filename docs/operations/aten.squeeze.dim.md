### aten.squeeze.dim
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0                         | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1       | Done     | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 14, 1]> self = ?,<br>int dim = -1            | Done     | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1            | Done     | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 256, 1]> self = ?,<br>int dim = -1           | Done     | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | -1     |
| 13 | Tensor<[3, 1370, 1, 1, 1280]> self = ?,<br>int dim = -2 | Done     | Done       | 1.0   | -1     |
| 14 | Tensor<[3, 197, 1, 1, 1024]> self = ?,<br>int dim = -2  | Done     | Done       | 1.0   | -1     |
| 15 | Tensor<[3, 197, 1, 1, 768]> self = ?,<br>int dim = -2   | Done     | Done       | 1.0   | -1     |
| 16 | Tensor<[3, 50, 1, 1, 1024]> self = ?,<br>int dim = -2   | Done     | Done       | 1.0   | -1     |
| 17 | Tensor<[3, 50, 1, 1, 768]> self = ?,<br>int dim = -2    | Done     | Done       | 1.0   | -1     |

