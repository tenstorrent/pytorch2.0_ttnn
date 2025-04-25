### aten.expand.default
|     | ATen Input Variations                                                             | Status   | Isolated   | PCC   | Host   |
|----:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]           | Unknown  | Done       | 1.0   | 0      |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]               | Done     | Done       | 1.0   | 0      |
|   2 | Tensor<[1, 1, 1, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]                | Done     | Done       | 1.0   | 0      |
|   3 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 1, 24]                 | Removed  | Done       | 1.0   | -1     |
|   4 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24]                | Done     | Done       | 1.0   | 0      |
|   5 | Tensor<[1, 1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]                | Unknown  | Done       | 1.0   | 0      |
|   6 | Tensor<[1, 1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                | Unknown  | Done       | 1.0   | 0      |
|   7 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                 | Unknown  | Done       | 1.0   | -1     |
|   8 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]                | Unknown  | Done       | 1.0   | 0      |
|   9 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int] size = [1, 1, 1, 60]                 | Unknown  | Done       | 1.0   | -1     |
|  10 | Tensor<[1, 1, 1, 7]> self = ?,<br>List[int] size = [1, 1, 7, 7]                   | Done     | Unknown    | N/A   | N/A    |
|  11 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1]              | Unknown  | Done       | 1.0   | 0      |
|  12 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  13 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]                    | Removed  | Done       | 1.0   | -1     |
|  14 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, -1, -1]                    | Removed  | Done       | 1.0   | -1     |
|  15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]       | Removed  | Done       | 1.0   | -1     |
|  16 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]         | Removed  | Done       | 1.0   | -1     |
|  17 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]               | Removed  | Done       | 1.0   | -1     |
|  18 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]       | Removed  | Done       | 1.0   | -1     |
|  19 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]         | Removed  | Done       | 1.0   | -1     |
|  20 | Tensor<[1, 1, 192]> self = ?,<br>List[int] size = [1, -1, -1]                     | Removed  | Done       | 1.0   | -1     |
|  21 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]             | Removed  | Done       | 1.0   | -1     |
|  22 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]             | Removed  | Done       | 1.0   | -1     |
|  23 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]             | Removed  | Done       | 1.0   | -1     |
|  24 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]               | Unknown  | Done       | 1.0   | -1     |
|  25 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                       | Removed  | Done       | 1.0   | -1     |
|  26 | Tensor<[1, 1, 38, 38]> self = ?,<br>List[int] size = [1, 512, 38, 38]             | Done     | Done       | 1.0   | 0      |
|  27 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]               | Unknown  | Done       | 1.0   | -1     |
|  28 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                       | Unknown  | Done       | 1.0   | -1     |
|  29 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 256, 512]                   | Done     | Unknown    | N/A   | N/A    |
|  30 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]               | Unknown  | Done       | 1.0   | -1     |
|  31 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]             | Removed  | Done       | 1.0   | -1     |
|  32 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [1, 1, 7, 7]                   | Removed  | Unknown    | N/A   | N/A    |
|  33 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7]                   | Done     | Done       | 1.0   | 0      |
|  34 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]                     | Removed  | Done       | 1.0   | -1     |
|  35 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 196, 768]                   | Done     | Done       | 1.0   | 0      |
|  36 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [1, -1, -1]                   | Removed  | Done       | 1.0   | -1     |
|  37 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 7, 7]             | Done     | Done       | 1.0   | 0      |
|  38 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]                             | Removed  | Done       | 1.0   | -1     |
|  39 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10, 10]                            | Done     | Done       | 1.0   | 0      |
|  40 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]               | Unknown  | Done       | 1.0   | -1     |
|  41 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  42 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                 | Unknown  | Done       | 1.0   | -1     |
|  43 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | 1.0   | -1     |
|  44 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  45 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  46 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  47 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]             | Removed  | Done       | 1.0   | -1     |
|  48 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]             | Removed  | Done       | 1.0   | -1     |
|  49 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]             | Removed  | Done       | 1.0   | -1     |
|  50 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Removed  | Done       | 1.0   | -1     |
|  51 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]             | Removed  | Done       | 1.0   | -1     |
|  52 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]             | Removed  | Done       | 1.0   | -1     |
|  53 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]             | Removed  | Done       | 1.0   | -1     |
|  54 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]             | Removed  | Done       | 1.0   | -1     |
|  55 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]         | Removed  | Done       | 1.0   | -1     |
|  56 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]           | Removed  | Done       | 1.0   | -1     |
|  57 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [1, 12, 2, 64]               | Unknown  | Done       | 1.0   | -1     |
|  58 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]             | Removed  | Done       | 1.0   | -1     |
|  59 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]             | Removed  | Done       | 1.0   | -1     |
|  60 | Tensor<[1, 12, 257, 257]> self = ?,<br>List[int] size = [1, 12, 257, 257]         | Removed  | Unknown    | N/A   | N/A    |
|  61 | Tensor<[1, 12, 257, 64]> self = ?,<br>List[int] size = [1, 12, 257, 64]           | Removed  | Unknown    | N/A   | N/A    |
|  62 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | 1.0   | -1     |
|  63 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | 1.0   | -1     |
|  64 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]             | Unknown  | Done       | 1.0   | -1     |
|  65 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10]             | Removed  | Done       | 1.0   | -1     |
|  66 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12]             | Removed  | Done       | 1.0   | -1     |
|  67 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [1, 12, 64, 14]             | Removed  | Done       | 1.0   | -1     |
|  68 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [1, 12, 64, 16]             | Removed  | Done       | 1.0   | -1     |
|  69 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]           | Removed  | Done       | 1.0   | -1     |
|  70 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [1, 12, 64, 1]               | Unknown  | Done       | 1.0   | -1     |
|  71 | Tensor<[1, 12, 64, 257]> self = ?,<br>List[int] size = [1, 12, 64, 257]           | Removed  | Unknown    | N/A   | N/A    |
|  72 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [1, 12, 64, 25]             | Removed  | Done       | 1.0   | -1     |
|  73 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [1, 12, 64, 2]               | Unknown  | Done       | 1.0   | -1     |
|  74 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]             | Unknown  | Done       | 1.0   | -1     |
|  75 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]             | Unknown  | Done       | 1.0   | -1     |
|  76 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7]               | Removed  | Done       | 1.0   | -1     |
|  77 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [1, 12, 64, 9]               | Removed  | Done       | 1.0   | -1     |
|  78 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  79 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  80 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]               | Removed  | Done       | 1.0   | -1     |
|  81 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                 | Removed  | Done       | 1.0   | -1     |
|  82 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]               | Removed  | Done       | 1.0   | -1     |
|  83 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                 | Removed  | Done       | 1.0   | -1     |
|  84 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  85 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  86 | Tensor<[1, 120, 1, 1]> self = ?,<br>List[int] size = [1, 120, 28, 28]             | Done     | Done       | 1.0   | 0      |
|  87 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 10, 10]           | Done     | Done       | 1.0   | 0      |
|  88 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 12, 12]           | Done     | Done       | 1.0   | 0      |
|  89 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 7, 7]             | Done     | Done       | 1.0   | 0      |
|  90 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 8, 8]             | Done     | Done       | 1.0   | 0      |
|  91 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 9, 9]             | Done     | Done       | 1.0   | 0      |
|  92 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536, 8, 8]             | Done     | Done       | 1.0   | 0      |
|  93 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]               | Unknown  | Done       | 1.0   | -1     |
|  94 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  95 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                 | Unknown  | Done       | 1.0   | -1     |
|  96 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  97 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Done       | 1.0   | -1     |
|  98 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  99 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 100 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]             | Unknown  | Done       | 1.0   | -1     |
| 101 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]             | Unknown  | Done       | 1.0   | -1     |
| 102 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [1, 16, 128, 9]             | Removed  | Done       | 1.0   | -1     |
| 103 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [1, 16, 2, 64]               | Unknown  | Done       | 1.0   | -1     |
| 104 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]         | Removed  | Done       | 1.0   | -1     |
| 105 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]           | Removed  | Done       | 1.0   | -1     |
| 106 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Done       | 1.0   | -1     |
| 107 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Done       | 1.0   | -1     |
| 108 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]               | Unknown  | Done       | 1.0   | -1     |
| 109 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [1, 16, 64, 10]             | Unknown  | Done       | 1.0   | -1     |
| 110 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [1, 16, 64, 1]               | Unknown  | Done       | 1.0   | -1     |
| 111 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]           | Removed  | Done       | 1.0   | -1     |
| 112 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [1, 16, 64, 2]               | Unknown  | Done       | 1.0   | -1     |
| 113 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]               | Unknown  | Done       | 1.0   | -1     |
| 114 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]               | Unknown  | Done       | 1.0   | -1     |
| 115 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [1, 16, 64, 9]               | Removed  | Done       | 1.0   | -1     |
| 116 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 117 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 118 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]             | Removed  | Done       | 1.0   | -1     |
| 119 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]               | Removed  | Done       | 1.0   | -1     |
| 120 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                 | Removed  | Done       | 1.0   | -1     |
| 121 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
| 122 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 123 | Tensor<[1, 19]> self = ?,<br>List[int] size = [19, 19]                            | Done     | Done       | 1.0   | 0      |
| 124 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]                               | Removed  | Done       | 1.0   | -1     |
| 125 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]             | Removed  | Done       | 1.0   | -1     |
| 126 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]             | Removed  | Done       | 1.0   | -1     |
| 127 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]             | Removed  | Done       | 1.0   | -1     |
| 128 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]         | Removed  | Done       | 1.0   | -1     |
| 129 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]           | Removed  | Done       | 1.0   | -1     |
| 130 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]         | Removed  | Done       | 1.0   | -1     |
| 131 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]           | Removed  | Done       | 1.0   | -1     |
| 132 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]             | Removed  | Done       | 1.0   | -1     |
| 133 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048, 10, 10]           | Done     | Done       | 1.0   | 0      |
| 134 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048, 7, 7]             | Done     | Done       | 1.0   | 0      |
| 135 | Tensor<[1, 20]> self = ?,<br>List[int] size = [20, 20]                            | Done     | Done       | 1.0   | 0      |
| 136 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [1, 24, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 137 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 138 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 139 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 140 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 141 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 142 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 143 | Tensor<[1, 256, 1, 1]> self = ?,<br>List[int] size = [1, 256, 56, 56]             | Done     | Done       | 1.0   | 0      |
| 144 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                             | Removed  | Done       | 1.0   | -1     |
| 145 | Tensor<[1, 2]> self = ?,<br>List[int] size = [2, 2]                               | Done     | Done       | 1.0   | 0      |
| 146 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]       | Removed  | Done       | 1.0   | -1     |
| 147 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]           | Removed  | Done       | 1.0   | -1     |
| 148 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [1, 3, 64, 1445]           | Removed  | Done       | 1.0   | -1     |
| 149 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [1, 32, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 150 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [1, 32, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 151 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 152 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 153 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int] size = [1, 32, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 154 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 155 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 156 | Tensor<[1, 38]> self = ?,<br>List[int] size = [38, 38]                            | Done     | Done       | 1.0   | 0      |
| 157 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3, 3]                               | Done     | Done       | 1.0   | 0      |
| 158 | Tensor<[1, 480, 1, 1]> self = ?,<br>List[int] size = [1, 480, 14, 14]             | Done     | Done       | 1.0   | 0      |
| 159 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]           | Unknown  | Done       | 1.0   | 0      |
| 160 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]         | Removed  | Done       | 1.0   | -1     |
| 161 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]           | Removed  | Done       | 1.0   | -1     |
| 162 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]         | Removed  | Done       | 1.0   | -1     |
| 163 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]           | Removed  | Done       | 1.0   | -1     |
| 164 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]             | Removed  | Done       | 1.0   | -1     |
| 165 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]             | Removed  | Done       | 1.0   | -1     |
| 166 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]             | Removed  | Done       | 1.0   | -1     |
| 167 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]             | Removed  | Done       | 1.0   | -1     |
| 168 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512, 28, 28]             | Done     | Done       | 1.0   | 0      |
| 169 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512, 7, 7]               | Done     | Done       | 1.0   | 0      |
| 170 | Tensor<[1, 5]> self = ?,<br>List[int] size = [5, 5]                               | Done     | Done       | 1.0   | 0      |
| 171 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                 | Unknown  | Done       | 1.0   | -1     |
| 172 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                 | Unknown  | Done       | 1.0   | -1     |
| 173 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                   | Unknown  | Done       | 1.0   | -1     |
| 174 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                   | Unknown  | Done       | 1.0   | -1     |
| 175 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                 | Unknown  | Done       | 1.0   | -1     |
| 176 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 177 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]               | Unknown  | Done       | 1.0   | -1     |
| 178 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]               | Unknown  | Done       | 1.0   | -1     |
| 179 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [1, 6, 17, 64]               | Unknown  | Done       | 1.0   | -1     |
| 180 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]                 | Unknown  | Done       | 1.0   | -1     |
| 181 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]               | Unknown  | Done       | 1.0   | -1     |
| 182 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [1, 6, 64, 17]               | Unknown  | Done       | 1.0   | -1     |
| 183 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]                 | Unknown  | Done       | 1.0   | -1     |
| 184 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]                 | Unknown  | Done       | 1.0   | -1     |
| 185 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
| 186 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
| 187 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]                       | Removed  | Done       | 1.0   | -1     |
| 188 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                       | Removed  | Done       | 1.0   | -1     |
| 189 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [1, 64, 64, 9]               | Removed  | Done       | 1.0   | -1     |
| 190 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]               | Removed  | Done       | 1.0   | -1     |
| 191 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                 | Removed  | Done       | 1.0   | -1     |
| 192 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672, 14, 14]             | Done     | Done       | 1.0   | 0      |
| 193 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672, 7, 7]               | Done     | Done       | 1.0   | 0      |
| 194 | Tensor<[1, 72, 1, 1]> self = ?,<br>List[int] size = [1, 72, 28, 28]               | Done     | Done       | 1.0   | 0      |
| 195 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 14, 14]             | Done     | Done       | 1.0   | 0      |
| 196 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                 | Unknown  | Done       | 1.0   | -1     |
| 197 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                   | Unknown  | Done       | 1.0   | -1     |
| 198 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                   | Unknown  | Done       | 1.0   | -1     |
| 199 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                 | Unknown  | Done       | 1.0   | -1     |
| 200 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 201 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]               | Unknown  | Done       | 1.0   | -1     |
| 202 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]               | Unknown  | Done       | 1.0   | -1     |
| 203 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [1, 8, 2, 64]                 | Unknown  | Done       | 1.0   | -1     |
| 204 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [1, 8, 2048, 160]         | Removed  | Done       | 1.0   | -1     |
| 205 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]         | Removed  | Done       | 1.0   | -1     |
| 206 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [1, 8, 2048, 32]           | Removed  | Done       | 1.0   | -1     |
| 207 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]           | Removed  | Done       | 1.0   | -1     |
| 208 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]         | Removed  | Done       | 1.0   | -1     |
| 209 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]           | Removed  | Done       | 1.0   | -1     |
| 210 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]             | Removed  | Done       | 1.0   | -1     |
| 211 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [1, 8, 256, 96]             | Removed  | Done       | 1.0   | -1     |
| 212 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]           | Removed  | Done       | 1.0   | -1     |
| 213 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]             | Removed  | Done       | 1.0   | -1     |
| 214 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [1, 8, 32, 2048]           | Removed  | Done       | 1.0   | -1     |
| 215 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]             | Removed  | Done       | 1.0   | -1     |
| 216 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [1, 8, 64, 10]               | Unknown  | Done       | 1.0   | -1     |
| 217 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [1, 8, 64, 1]                 | Unknown  | Done       | 1.0   | -1     |
| 218 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [1, 8, 64, 2]                 | Unknown  | Done       | 1.0   | -1     |
| 219 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]             | Removed  | Done       | 1.0   | -1     |
| 220 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
| 221 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 8, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
| 222 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960, 7, 7]               | Done     | Done       | 1.0   | 0      |
| 223 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10]                            | Done     | Done       | 1.0   | 0      |
| 224 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16]                            | Done     | Done       | 1.0   | 0      |
| 225 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [16, 6, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 226 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 227 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 228 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 229 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 230 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 231 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 232 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [16, 8, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 233 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [16, 8, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 234 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 235 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 236 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int] size = [16, 8, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 237 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 238 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 239 | Tensor<[19, 1]> self = ?,<br>List[int] size = [19, 19]                            | Done     | Done       | 1.0   | 0      |
| 240 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7]                   | Done     | Done       | 1.0   | 0      |
| 241 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]                               | Done     | Done       | 1.0   | 0      |
| 242 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20]                            | Done     | Done       | 1.0   | 0      |
| 243 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, -1, -1]                     | Done     | Done       | 1.0   | 0      |
| 244 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                   | Removed  | Done       | 1.0   | -1     |
| 245 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                   | Removed  | Done       | 1.0   | -1     |
| 246 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, -1, -1]                     | Done     | Done       | 1.0   | 0      |
| 247 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]                               | Done     | Done       | 1.0   | 0      |
| 248 | Tensor<[38, 1]> self = ?,<br>List[int] size = [38, 38]                            | Done     | Done       | 1.0   | 0      |
| 249 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [4, 12, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 250 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 251 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 252 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 253 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 254 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 255 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 256 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [4, 16, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 257 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [4, 16, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 258 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 259 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 260 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int] size = [4, 16, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 261 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 262 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 263 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]                               | Done     | Done       | 1.0   | 0      |
| 264 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [64, 3, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 265 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 266 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 267 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 268 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 269 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 270 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 271 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [64, 4, 32, 49]             | Removed  | Done       | 1.0   | -1     |
| 272 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [64, 4, 32, 64]             | Removed  | Done       | 1.0   | -1     |
| 273 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]             | Removed  | Done       | 1.0   | -1     |
| 274 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]             | Removed  | Done       | 1.0   | -1     |
| 275 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int] size = [64, 4, 64, 32]              | Done     | Done       | 1.0   | 0      |
| 276 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]             | Removed  | Done       | 1.0   | -1     |
| 277 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]             | Removed  | Done       | 1.0   | -1     |
| 278 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]                            | Done     | Done       | 1.0   | 0      |

