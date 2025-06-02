### aten.squeeze.dim
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 24576]> self = ?,<br>int dim = 0          | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1       | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 14, 1]> self = ?,<br>int dim = -1            | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1            | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 384, 1]> self = ?,<br>int dim = -1           | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[1]> self = ?,<br>int dim = 0                    | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[3, 1370, 1, 1, 1280]> self = ?,<br>int dim = -2 | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[3, 197, 1, 1, 1024]> self = ?,<br>int dim = -2  | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[3, 197, 1, 1, 768]> self = ?,<br>int dim = -2   | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[3, 50, 1, 1, 1024]> self = ?,<br>int dim = -2   | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[3, 50, 1, 1, 768]> self = ?,<br>int dim = -2    | Done     | Done       | 1.0   | 0      |

