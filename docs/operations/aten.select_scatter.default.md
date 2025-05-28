### aten.select_scatter.default
|    | ATen Input Variations                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[720, 1280]> src = ?,<br>int dim = 0,<br>int index = 0                       | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 51865]> self = ?,<br>Tensor<[1, 51865]> src = ?,<br>int dim = 1,<br>int index = -1        | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[3, 300, 300]> src = ?,<br>int dim = 0,<br>int index = 0   | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[3, 320, 320]> src = ?,<br>int dim = 0,<br>int index = 0   | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 3, 720, 1280]> self = ?,<br>Tensor<[3, 720, 1280]> src = ?,<br>int dim = 0,<br>int index = 0 | Unknown  | Unknown    | N/A   | N/A    |

