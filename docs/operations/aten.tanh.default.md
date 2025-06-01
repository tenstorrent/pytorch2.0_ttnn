### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.9999340602215017 | 0      |
|  1 | Tensor<[1, 1, 24576]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.9999383602310337 | 0      |
|  3 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.9999426794526608 | 0      |
|  4 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.9999419340680218 | 0      |
|  5 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.9999421365274581 | 0      |
|  6 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.999942699346781  | 0      |
|  7 | Tensor<[1, 256, 96]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.9999422315030826 | 0      |
|  9 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.9999423126508578 | 0      |
| 10 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.9999428956213338 | 0      |
| 11 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.9999415093024939 | 0      |
| 12 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.9999460010258441 | 0      |
| 13 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.9999410912971088 | 0      |
| 14 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.9999423334960957 | 0      |
| 15 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.999943027375464  | 0      |
| 16 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.9999415479532399 | 0      |
| 17 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.9999422924928079 | 0      |

