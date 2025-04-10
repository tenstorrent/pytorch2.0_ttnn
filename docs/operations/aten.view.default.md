### aten.view.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10]                            | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]                          | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [1, 256, 512]             | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16] | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512]                       | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]               | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 9216]> self = ?,<br>List[int] size = [1, 64, 12, 12]               | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                | Done     | Done       | 1.0   | 0      |

