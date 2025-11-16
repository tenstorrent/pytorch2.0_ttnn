### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.9999928993404277 | 0      |
|  1 | Tensor<[1, 1, 25088]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.9999926350040017 | 0      |
|  3 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.9999927733691897 | 0      |
|  4 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.9999927073879193 | 0      |
|  5 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.9999926705936303 | 0      |
|  6 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.9999924937481266 | 0      |
|  7 | Tensor<[1, 256, 98]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.999992646616676  | 0      |
|  9 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.9999926353335741 | 0      |
| 10 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.9999927860532136 | 0      |
| 11 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.9999927319945633 | 0      |
| 12 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.9999926548805321 | 0      |
| 13 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.9999927015986088 | 0      |
| 14 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.9999926632672276 | 0      |
| 15 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.9999926340496459 | 0      |
| 16 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.9999926152925069 | 0      |
| 17 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.9999927124210738 | 0      |

