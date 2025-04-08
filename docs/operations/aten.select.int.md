### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1     | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0            | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0    | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1370, 768]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0            | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1     | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1     | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 257, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 2   | Done     | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 3, 300, 300]> self = ?,<br>int dim = 0,<br>int index = 0   | Removed  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0   | Removed  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0   | Removed  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 1 | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 2 | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Done       | 1.0   | 0      |
| 27 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Done       | 1.0   | 0      |
| 28 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Done     | Done       | 1.0   | 0      |
| 29 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Done       | 1.0   | 0      |
| 31 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1            | Unknown  | Done       | 1.0   | 0      |
| 32 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Done       | 1.0   | 0      |
| 33 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0                | Removed  | Fallback   | 1.0   | -1     |
| 34 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 35 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 36 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 37 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 38 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 39 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 40 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 41 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 42 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 43 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 44 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 45 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 46 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 47 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 48 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 49 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 50 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 51 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 52 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 53 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 54 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 55 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 56 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 57 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 58 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 59 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 60 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 61 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0  | Done     | Done       | 1.0   | 0      |
| 62 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1  | Done     | Done       | 1.0   | 0      |
| 63 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2  | Done     | Done       | 1.0   | 0      |
| 64 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
| 65 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1   | Done     | Done       | 1.0   | 0      |
| 66 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2   | Done     | Done       | 1.0   | 0      |
| 67 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 68 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 69 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 70 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 71 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 72 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 73 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 74 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 75 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 76 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 77 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 78 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 79 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
| 80 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1   | Done     | Done       | 1.0   | 0      |
| 81 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2   | Done     | Done       | 1.0   | 0      |
| 82 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0    | Done     | Done       | 1.0   | 0      |
| 83 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1    | Done     | Done       | 1.0   | 0      |
| 84 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2    | Done     | Done       | 1.0   | 0      |
| 85 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 86 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 87 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 88 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 89 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 90 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 91 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 92 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 93 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 94 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 95 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 96 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 97 | Tensor<[6, 1, 100, 4]> self = ?,<br>int dim = 0,<br>int index = -1    | Unknown  | Done       | 1.0   | 0      |
| 98 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1   | Unknown  | Done       | 1.0   | 0      |

