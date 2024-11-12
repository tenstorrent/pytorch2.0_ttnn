### aten.cos.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 160]> self = ?        | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 23, 40, 64]> self = ? | Fallback | Done       | True  |
|  2 | Tensor<[1, 32, 128]> self = ?    | Fallback | Unknown    | N/A   |

