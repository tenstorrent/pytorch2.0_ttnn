### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.9999441590695851 | 0      |
|  1 | Tensor<[1, 1, 24576]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.9999468966840436 | 0      |
|  3 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.9999425455053311 | 0      |
|  4 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.9999425821277004 | 0      |
|  5 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.9999418406618629 | 0      |
|  6 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.9999409730151466 | 0      |
|  7 | Tensor<[1, 256, 96]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.999942353111038  | 0      |
|  9 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.9999419346816402 | 0      |
| 10 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.9999420042278947 | 0      |
| 11 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.9999417135177009 | 0      |
| 12 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.9999471650591742 | 0      |
| 13 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.9999332923839521 | 0      |
| 14 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.9999422226992297 | 0      |
| 15 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.9999431385381625 | 0      |
| 16 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.9999416110732184 | 0      |
| 17 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.9999424682940667 | 0      |

