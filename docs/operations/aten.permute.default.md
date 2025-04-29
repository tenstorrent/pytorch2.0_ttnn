### aten.permute.default
|     | ATen Input Variations                                                           | Status   | Isolated   | PCC   | Host   |
|----:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | Done     | Done       | 1.0   | -1     |
|   1 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|   2 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | Done     | Done       | 1.0   | -1     |
|   3 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|   4 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | 1.0   | -1     |
|   5 | Tensor<[1, 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | 1.0   | -1     |
|   6 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | 1.0   | -1     |
|   7 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | 1.0   | -1     |
|   8 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | 1.0   | -1     |
|   9 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Unknown  | Done       | 1.0   | -1     |
|  10 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  11 | Tensor<[1, 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | 1.0   | -1     |
|  12 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | Done     | Done       | 1.0   | -1     |
|  13 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  14 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | Done     | Done       | 1.0   | -1     |
|  15 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  16 | Tensor<[1, 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | 1.0   | -1     |
|  17 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  18 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  19 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  20 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  21 | Tensor<[1, 1024, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
|  22 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  23 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | 1.0   | -1     |
|  24 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  25 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  26 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  27 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  28 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  29 | Tensor<[1, 12, 257, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  30 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
|  31 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  32 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | 1.0   | -1     |
|  33 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  | Done       | 1.0   | -1     |
|  34 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | 1.0   | -1     |
|  35 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  | Done       | 1.0   | -1     |
|  36 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Done     | Done       | 1.0   | -1     |
|  37 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  | Done       | 1.0   | -1     |
|  38 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Done       | 1.0   | -1     |
|  39 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Done       | 1.0   | -1     |
|  40 | Tensor<[1, 1280, 1369]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Done       | 1.0   | -1     |
|  41 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  42 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  43 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Done       | 1.0   | -1     |
|  44 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | 1.0   | -1     |
|  45 | Tensor<[1, 16, 1370, 80]> self = ?,<br>List[int] dims = [2, 0, 1, 3]            | Done     | Done       | 1.0   | -1     |
|  46 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] dims = [0, 5, 1, 3, 2, 4] | Done     | Done       | 1.0   | -1     |
|  47 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | 1.0   | -1     |
|  48 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  49 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  50 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  51 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | 1.0   | -1     |
|  52 | Tensor<[1, 16, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  53 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  54 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
|  55 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Done       | 1.0   | -1     |
|  56 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | 1.0   | -1     |
|  57 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Done       | 1.0   | -1     |
|  58 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  59 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Unknown  | Done       | 1.0   | -1     |
|  60 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | 1.0   | -1     |
|  61 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  62 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  63 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  64 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  65 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  66 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  67 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  68 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  | Done       | 1.0   | -1     |
|  69 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  70 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  71 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  72 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
|  73 | Tensor<[1, 2048, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | 1.0   | -1     |
|  74 | Tensor<[1, 2048, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  75 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Done       | 1.0   | -1     |
|  76 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  77 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  78 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  79 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Done       | 1.0   | -1     |
|  80 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  81 | Tensor<[1, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
|  82 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Done       | 1.0   | -1     |
|  83 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  84 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
|  85 | Tensor<[1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | 1.0   | -1     |
|  86 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
|  87 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  88 | Tensor<[1, 256, 512]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
|  89 | Tensor<[1, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | 1.0   | -1     |
|  90 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  91 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  92 | Tensor<[1, 256, 8, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
|  93 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Unknown  | Done       | 1.0   | -1     |
|  94 | Tensor<[1, 257, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  95 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
|  96 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | Done     | Done       | 1.0   | -1     |
|  97 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Done       | 1.0   | -1     |
|  98 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
|  99 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
| 100 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
| 101 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
| 102 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | Done       | 1.0   | -1     |
| 103 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | 1.0   | -1     |
| 104 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
| 105 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | 1.0   | -1     |
| 106 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | 1.0   | -1     |
| 107 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  | Done       | 1.0   | -1     |
| 108 | Tensor<[1, 37, 37, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
| 109 | Tensor<[1, 4, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Unknown  | Done       | 1.0   | -1     |
| 110 | Tensor<[1, 4, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Unknown  | Done       | 1.0   | -1     |
| 111 | Tensor<[1, 4, 4, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  | Done       | 1.0   | -1     |
| 112 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 113 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 114 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 115 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 116 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 117 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 118 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 119 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 120 | Tensor<[1, 4, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Unknown  | Done       | 1.0   | -1     |
| 121 | Tensor<[1, 4, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Unknown  | Done       | 1.0   | -1     |
| 122 | Tensor<[1, 4, 91, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Unknown  | Done       | 1.0   | -1     |
| 123 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
| 124 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | 1.0   | -1     |
| 125 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
| 126 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
| 127 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | 1.0   | -1     |
| 128 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  | Done       | 1.0   | -1     |
| 129 | Tensor<[1, 49, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 130 | Tensor<[1, 49, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 131 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
| 132 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Unknown  | Done       | 1.0   | -1     |
| 133 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | 1.0   | -1     |
| 134 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
| 135 | Tensor<[1, 512, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
| 136 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Done     | Done       | 1.0   | -1     |
| 137 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Done     | Done       | 1.0   | -1     |
| 138 | Tensor<[1, 6, 4, 19, 19]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  | Done       | 1.0   | -1     |
| 139 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Done     | Done       | 1.0   | -1     |
| 140 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Done     | Done       | 1.0   | -1     |
| 141 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Done     | Done       | 1.0   | -1     |
| 142 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Done     | Done       | 1.0   | -1     |
| 143 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Done     | Done       | 1.0   | -1     |
| 144 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Done     | Done       | 1.0   | -1     |
| 145 | Tensor<[1, 6, 91, 19, 19]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Unknown  | Done       | 1.0   | -1     |
| 146 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Done     | Done       | 1.0   | -1     |
| 147 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Done     | Done       | 1.0   | -1     |
| 148 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Done     | Done       | 1.0   | -1     |
| 149 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Done     | Done       | 1.0   | -1     |
| 150 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Done       | 1.0   | -1     |
| 151 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | 1.0   | -1     |
| 152 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 153 | Tensor<[1, 64, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 154 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Unknown  | Done       | 1.0   | -1     |
| 155 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
| 156 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | 1.0   | -1     |
| 157 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Done       | 1.0   | -1     |
| 158 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | 1.0   | -1     |
| 159 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Done       | 1.0   | -1     |
| 160 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Done     | Done       | 1.0   | -1     |
| 161 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | 1.0   | -1     |
| 162 | Tensor<[1, 768, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Unknown    | N/A   | N/A    |
| 163 | Tensor<[1, 768, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | 1.0   | -1     |
| 164 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | 1.0   | -1     |
| 165 | Tensor<[1, 8, 2048, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
| 166 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | 1.0   | -1     |
| 167 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
| 168 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | 1.0   | -1     |
| 169 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 170 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | Done     | Done       | 1.0   | -1     |
| 171 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Done       | 1.0   | -1     |
| 172 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 173 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | Done     | Done       | 1.0   | -1     |
| 174 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Done     | Done       | 1.0   | -1     |
| 175 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | Done     | Done       | 1.0   | -1     |
| 176 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | Done     | Done       | 1.0   | -1     |
| 177 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | 1.0   | -1     |
| 178 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | 1.0   | -1     |
| 179 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | 1.0   | -1     |
| 180 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | 1.0   | -1     |
| 181 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | 1.0   | -1     |
| 182 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | 1.0   | -1     |
| 183 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Unknown  | Done       | 1.0   | -1     |
| 184 | Tensor<[10, 10, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Unknown  | Done       | 1.0   | -1     |
| 185 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  | Done       | 1.0   | -1     |
| 186 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  | Done       | 1.0   | -1     |
| 187 | Tensor<[16, 49, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 188 | Tensor<[16, 49, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 189 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 190 | Tensor<[16, 64, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 191 | Tensor<[17, 17, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  | Done       | 1.0   | -1     |
| 192 | Tensor<[2, 2, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | 1.0   | -1     |
| 193 | Tensor<[2, 2, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | 1.0   | -1     |
| 194 | Tensor<[2, 2, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | 1.0   | -1     |
| 195 | Tensor<[2, 2, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | 1.0   | -1     |
| 196 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | 1.0   | -1     |
| 197 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | 1.0   | -1     |
| 198 | Tensor<[4, 49, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 199 | Tensor<[4, 49, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 200 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 201 | Tensor<[4, 64, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 202 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | 1.0   | -1     |
| 203 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | 1.0   | -1     |
| 204 | Tensor<[49, 49, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 205 | Tensor<[49, 49, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 206 | Tensor<[49, 49, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 207 | Tensor<[49, 49, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 208 | Tensor<[49, 49, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 209 | Tensor<[49, 49, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 210 | Tensor<[49, 49, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 211 | Tensor<[49, 49, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 212 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 213 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 214 | Tensor<[64, 64, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 215 | Tensor<[64, 64, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 216 | Tensor<[64, 64, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 217 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 218 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | Done     | Done       | 1.0   | -1     |
| 219 | Tensor<[64, 64, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | 1.0   | -1     |
| 220 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 221 | Tensor<[64, 64, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 222 | Tensor<[64, 64, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 223 | Tensor<[64, 64, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | 1.0   | -1     |
| 224 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | 1.0   | -1     |
| 225 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | 1.0   | -1     |
| 226 | Tensor<[s0 + 1, s0 + 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]            | Unknown  | Unknown    | N/A   | N/A    |
| 227 | Tensor<[s0 + 1, s0 + 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]            | Unknown  | Unknown    | N/A   | N/A    |
| 228 | Tensor<[s0 + 1, s0 + 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 229 | Tensor<[s0 + 1, s0 + 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]             | Unknown  | Unknown    | N/A   | N/A    |

