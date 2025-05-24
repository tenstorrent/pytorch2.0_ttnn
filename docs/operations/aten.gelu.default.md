### aten.gelu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?      | Unknown  | Done       | 0.9999906322213115 | 0      |
|  1 | Tensor<[1, 10, 3072]> self = ?     | Removed  | Done       | 0.999991595294516  | 0      |
|  2 | Tensor<[1, 10, 768]> self = ?      | Removed  | Done       | 0.9999906516758909 | 0      |
|  3 | Tensor<[1, 1024, 512]> self = ?    | Done     | Done       | 0.9999912360753477 | 0      |
|  4 | Tensor<[1, 1024, 640]> self = ?    | Done     | Done       | 0.9999913072357289 | 0      |
|  5 | Tensor<[1, 1370, 5120]> self = ?   | Removed  | Done       | 0.9999913259883536 | 0      |
|  6 | Tensor<[1, 14, 14, 1536]> self = ? | Done     | Done       | 0.9999913290875401 | 0      |
|  7 | Tensor<[1, 14, 14, 2048]> self = ? | Done     | Done       | 0.999991381334453  | 0      |
|  8 | Tensor<[1, 1445, 768]> self = ?    | Removed  | Done       | 0.9999913012971479 | 0      |
|  9 | Tensor<[1, 1500, 3072]> self = ?   | Unknown  | Done       | 0.9999913435010012 | 0      |
| 10 | Tensor<[1, 16, 16, 1536]> self = ? | Done     | Done       | 0.9999913872518449 | 0      |
| 11 | Tensor<[1, 16, 16, 2048]> self = ? | Done     | Done       | 0.9999913556839048 | 0      |
| 12 | Tensor<[1, 16, 3072]> self = ?     | Removed  | Done       | 0.9999913380563634 | 0      |
| 13 | Tensor<[1, 16384, 128]> self = ?   | Done     | Done       | 0.9999913147727658 | 0      |
| 14 | Tensor<[1, 196, 3072]> self = ?    | Removed  | Done       | 0.9999912852369996 | 0      |
| 15 | Tensor<[1, 197, 3072]> self = ?    | Done     | Done       | 0.999991370405502  | 0      |
| 16 | Tensor<[1, 197, 4096]> self = ?    | Removed  | Done       | 0.9999913094973063 | 0      |
| 17 | Tensor<[1, 2048, 768]> self = ?    | Removed  | Done       | 0.9999913006626892 | 0      |
| 18 | Tensor<[1, 25, 3072]> self = ?     | Removed  | Done       | 0.9999914058377967 | 0      |
| 19 | Tensor<[1, 256, 1024]> self = ?    | Done     | Done       | 0.9999913502484054 | 0      |
| 20 | Tensor<[1, 256, 1280]> self = ?    | Removed  | Done       | 0.9999912852526798 | 0      |
| 21 | Tensor<[1, 256, 256]> self = ?     | Removed  | Done       | 0.9999914202223293 | 0      |
| 22 | Tensor<[1, 28, 28, 1024]> self = ? | Done     | Done       | 0.9999913564566496 | 0      |
| 23 | Tensor<[1, 28, 28, 768]> self = ?  | Done     | Done       | 0.9999914091540089 | 0      |
| 24 | Tensor<[1, 32, 32, 1024]> self = ? | Removed  | Done       | 0.9999913964960725 | 0      |
| 25 | Tensor<[1, 32, 32, 768]> self = ?  | Removed  | Done       | 0.9999913553706028 | 0      |
| 26 | Tensor<[1, 384, 4096]> self = ?    | Removed  | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 4, 3072]> self = ?      | Unknown  | Done       | 0.9999912800707934 | 0      |
| 28 | Tensor<[1, 4096, 256]> self = ?    | Done     | Done       | 0.9999913759749702 | 0      |
| 29 | Tensor<[1, 50, 3072]> self = ?     | Removed  | Done       | 0.9999912581133139 | 0      |
| 30 | Tensor<[1, 50, 4096]> self = ?     | Removed  | Done       | 0.999991370854801  | 0      |
| 31 | Tensor<[1, 56, 56, 384]> self = ?  | Done     | Done       | 0.9999913116650387 | 0      |
| 32 | Tensor<[1, 56, 56, 512]> self = ?  | Done     | Done       | 0.9999913420057422 | 0      |
| 33 | Tensor<[1, 64, 64, 384]> self = ?  | Removed  | Done       | 0.9999913620008676 | 0      |
| 34 | Tensor<[1, 64, 64, 512]> self = ?  | Removed  | Done       | 0.999991344204013  | 0      |
| 35 | Tensor<[1, 7, 7, 3072]> self = ?   | Done     | Done       | 0.9999912787060691 | 0      |
| 36 | Tensor<[1, 7, 7, 4096]> self = ?   | Done     | Done       | 0.9999913969079582 | 0      |
| 37 | Tensor<[1, 768, 1500]> self = ?    | Unknown  | Done       | 0.9999914189739351 | 0      |
| 38 | Tensor<[1, 768, 3000]> self = ?    | Unknown  | Done       | 0.9999913178198039 | 0      |
| 39 | Tensor<[1, 768, 384]> self = ?     | Done     | Done       | 0.9999912532086093 | 0      |
| 40 | Tensor<[1, 8, 8, 3072]> self = ?   | Done     | Done       | 0.9999912863943353 | 0      |
| 41 | Tensor<[1, 8, 8, 4096]> self = ?   | Done     | Done       | 0.9999914168526036 | 0      |

