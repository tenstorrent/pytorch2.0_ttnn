### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.9999434613657454 | 0      |
|  1 | Tensor<[1, 1, 24576]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.9999384468546819 | 0      |
|  3 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.999941340085494  | 0      |
|  4 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.99994152446745   | 0      |
|  5 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.9999406717080676 | 0      |
|  6 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.9999425285034483 | 0      |
|  7 | Tensor<[1, 256, 96]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.9999420071469822 | 0      |
|  9 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.9999420760873787 | 0      |
| 10 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.9999427185549469 | 0      |
| 11 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.9999429781592108 | 0      |
| 12 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.9999384705991579 | 0      |
| 13 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.9999433971174541 | 0      |
| 14 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.99994189445311   | 0      |
| 15 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.9999424933147247 | 0      |
| 16 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.9999416166762574 | 0      |
| 17 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.9999420744117408 | 0      |

