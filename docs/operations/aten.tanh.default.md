### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.9999415111131815 | 0      |
|  1 | Tensor<[1, 1, 24576]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.9999408790639404 | 0      |
|  3 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.9999395033990951 | 0      |
|  4 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.9999425173624764 | 0      |
|  5 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.9999424695161071 | 0      |
|  6 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.9999414002122743 | 0      |
|  7 | Tensor<[1, 256, 96]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.9999424115884368 | 0      |
|  9 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.9999424099226852 | 0      |
| 10 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.99994200821271   | 0      |
| 11 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.9999427205178452 | 0      |
| 12 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.9999413744994846 | 0      |
| 13 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.9999439505532582 | 0      |
| 14 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.9999427035194335 | 0      |
| 15 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.9999420319336025 | 0      |
| 16 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.9999419543182608 | 0      |
| 17 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.9999421283553387 | 0      |

