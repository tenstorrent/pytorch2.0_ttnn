### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>Optional[int] dtype = torch.float32      | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 128]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 32768]> self = ?,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Unknown    | N/A   | N/A    |

