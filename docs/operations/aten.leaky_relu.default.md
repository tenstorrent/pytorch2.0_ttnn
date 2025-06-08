### aten.leaky_relu.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1024, 16, 16]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       | 0.9999999292762844 | 0      |
|  1 | Tensor<[1, 128, 128, 128]> self = ?,<br>number negative_slope = 0.1 | Done     | Done       | 0.9999999294603623 | 0      |
|  2 | Tensor<[1, 128, 1536]> self = ?,<br>number negative_slope = 0.1     | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 128, 32, 32]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.9999999292668729 | 0      |
|  4 | Tensor<[1, 128, 64, 64]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.999999929885411  | 0      |
|  5 | Tensor<[1, 256, 16, 16]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.9999999303079122 | 0      |
|  6 | Tensor<[1, 256, 32, 32]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.9999999296836319 | 0      |
|  7 | Tensor<[1, 256, 384]> self = ?,<br>number negative_slope = 0.1      | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 256, 64, 64]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.9999999291144108 | 0      |
|  9 | Tensor<[1, 32, 24576]> self = ?                                     | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 32, 24576]> self = ?,<br>number negative_slope = 0.1     | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 32, 256, 256]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       | 0.9999999291060458 | 0      |
| 12 | Tensor<[1, 32, 512, 512]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       | 0.9999999293223464 | 0      |
| 13 | Tensor<[1, 512, 16, 16]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.999999929773682  | 0      |
| 14 | Tensor<[1, 512, 32, 32]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       | 0.9999999282386344 | 0      |
| 15 | Tensor<[1, 512, 96]> self = ?,<br>number negative_slope = 0.1       | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 64, 128, 128]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       | 0.9999999295807198 | 0      |
| 17 | Tensor<[1, 64, 256, 256]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       | 0.9999999292342346 | 0      |
| 18 | Tensor<[1, 64, 6144]> self = ?,<br>number negative_slope = 0.1      | Unknown  | Unknown    | N/A                | N/A    |

