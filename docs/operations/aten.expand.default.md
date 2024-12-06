### aten.expand.default
|     | ATen Input Variations                                                             | Status   | Isolated   | PCC   | Host   |
|----:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]           | Unknown  | Unknown    | N/A   | N/A    |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]               | Done     | Unknown    | N/A   | N/A    |
|   2 | Tensor<[1, 1, 1, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]                | Done     | Unknown    | N/A   | N/A    |
|   3 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 1, 24]                 | Removed  | Unknown    | N/A   | N/A    |
|   4 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24]                | Done     | Unknown    | N/A   | N/A    |
|   5 | Tensor<[1, 1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]                | Done     | Unknown    | N/A   | N/A    |
|   6 | Tensor<[1, 1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                | Unknown  | Unknown    | N/A   | N/A    |
|   7 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                 | Unknown  | Unknown    | N/A   | N/A    |
|   8 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]                | Done     | Unknown    | N/A   | N/A    |
|   9 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int] size = [1, 1, 1, 60]                 | Unknown  | Unknown    | N/A   | N/A    |
|  10 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int] size = [-1, 8, -1, -1]              | Done     | Unknown    | N/A   | N/A    |
|  11 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  12 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]                    | Removed  | Unknown    | N/A   | N/A    |
|  13 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 196, 1024]                 | Done     | Unknown    | N/A   | N/A    |
|  14 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, -1, -1]                    | Removed  | Unknown    | N/A   | N/A    |
|  15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]       | Removed  | Unknown    | N/A   | N/A    |
|  16 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]         | Removed  | Unknown    | N/A   | N/A    |
|  17 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]               | Removed  | Unknown    | N/A   | N/A    |
|  18 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]       | Unknown  | Unknown    | N/A   | N/A    |
|  19 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]         | Unknown  | Unknown    | N/A   | N/A    |
|  20 | Tensor<[1, 1, 192]> self = ?,<br>List[int] size = [1, -1, -1]                     | Removed  | Unknown    | N/A   | N/A    |
|  21 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]             | Removed  | Unknown    | N/A   | N/A    |
|  22 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]             | Unknown  | Unknown    | N/A   | N/A    |
|  23 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]             | Removed  | Unknown    | N/A   | N/A    |
|  24 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]               | Removed  | Unknown    | N/A   | N/A    |
|  25 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                       | Removed  | Unknown    | N/A   | N/A    |
|  26 | Tensor<[1, 1, 38, 38]> self = ?,<br>List[int] size = [1, 512, 38, 38]             | Done     | Unknown    | N/A   | N/A    |
|  27 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]               | Unknown  | Unknown    | N/A   | N/A    |
|  28 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                       | Unknown  | Unknown    | N/A   | N/A    |
|  29 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]               | Unknown  | Unknown    | N/A   | N/A    |
|  30 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]             | Unknown  | Unknown    | N/A   | N/A    |
|  31 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7]                   | Done     | Unknown    | N/A   | N/A    |
|  32 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]                     | Removed  | Unknown    | N/A   | N/A    |
|  33 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 196, 768]                   | Done     | Unknown    | N/A   | N/A    |
|  34 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [1, -1, -1]                   | Removed  | Unknown    | N/A   | N/A    |
|  35 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 7, 7]             | None     | Unknown    | N/A   | N/A    |
|  36 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]                             | Removed  | Unknown    | N/A   | N/A    |
|  37 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10, 10]                            | Done     | Unknown    | N/A   | N/A    |
|  38 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]               | Unknown  | Unknown    | N/A   | N/A    |
|  39 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                 | Unknown  | Unknown    | N/A   | N/A    |
|  40 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                 | Unknown  | Unknown    | N/A   | N/A    |
|  41 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Unknown    | N/A   | N/A    |
|  42 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Unknown    | N/A   | N/A    |
|  43 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  44 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  45 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]             | Removed  | Unknown    | N/A   | N/A    |
|  46 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]             | Removed  | Unknown    | N/A   | N/A    |
|  47 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]             | Removed  | Unknown    | N/A   | N/A    |
|  48 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Removed  | Unknown    | N/A   | N/A    |
|  49 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]             | Removed  | Unknown    | N/A   | N/A    |
|  50 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]             | Removed  | Unknown    | N/A   | N/A    |
|  51 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]             | Removed  | Unknown    | N/A   | N/A    |
|  52 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]             | Removed  | Unknown    | N/A   | N/A    |
|  53 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]         | Removed  | Unknown    | N/A   | N/A    |
|  54 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]           | Removed  | Unknown    | N/A   | N/A    |
|  55 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [1, 12, 2, 64]               | Unknown  | Unknown    | N/A   | N/A    |
|  56 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]             | Removed  | Unknown    | N/A   | N/A    |
|  57 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]             | Removed  | Unknown    | N/A   | N/A    |
|  58 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Unknown    | N/A   | N/A    |
|  59 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Unknown    | N/A   | N/A    |
|  60 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]             | Unknown  | Unknown    | N/A   | N/A    |
|  61 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10]             | Removed  | Unknown    | N/A   | N/A    |
|  62 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12]             | Removed  | Unknown    | N/A   | N/A    |
|  63 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [1, 12, 64, 14]             | Removed  | Unknown    | N/A   | N/A    |
|  64 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [1, 12, 64, 16]             | Removed  | Unknown    | N/A   | N/A    |
|  65 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]           | Removed  | Unknown    | N/A   | N/A    |
|  66 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [1, 12, 64, 1]               | Unknown  | Unknown    | N/A   | N/A    |
|  67 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [1, 12, 64, 25]             | Removed  | Unknown    | N/A   | N/A    |
|  68 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [1, 12, 64, 2]               | Unknown  | Unknown    | N/A   | N/A    |
|  69 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]             | Unknown  | Unknown    | N/A   | N/A    |
|  70 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]             | Unknown  | Unknown    | N/A   | N/A    |
|  71 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7]               | Removed  | Unknown    | N/A   | N/A    |
|  72 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [1, 12, 64, 9]               | Removed  | Unknown    | N/A   | N/A    |
|  73 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  74 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  75 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]               | Removed  | Unknown    | N/A   | N/A    |
|  76 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                 | Removed  | Unknown    | N/A   | N/A    |
|  77 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]               | Removed  | Unknown    | N/A   | N/A    |
|  78 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                 | Removed  | Unknown    | N/A   | N/A    |
|  79 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  80 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  81 | Tensor<[1, 120, 1, 1]> self = ?,<br>List[int] size = [1, 120, 28, 28]             | None     | Unknown    | N/A   | N/A    |
|  82 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 10, 10]           | None     | Unknown    | N/A   | N/A    |
|  83 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 12, 12]           | Unknown  | Unknown    | N/A   | N/A    |
|  84 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 7, 7]             | None     | Unknown    | N/A   | N/A    |
|  85 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 8, 8]             | None     | Unknown    | N/A   | N/A    |
|  86 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280, 9, 9]             | None     | Unknown    | N/A   | N/A    |
|  87 | Tensor<[1, 136]> self = ?,<br>List[int] size = [100, 136]                         | Done     | Unknown    | N/A   | N/A    |
|  88 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536, 8, 8]             | None     | Unknown    | N/A   | N/A    |
|  89 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]               | Unknown  | Unknown    | N/A   | N/A    |
|  90 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                 | Unknown  | Unknown    | N/A   | N/A    |
|  91 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                 | Unknown  | Unknown    | N/A   | N/A    |
|  92 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Unknown    | N/A   | N/A    |
|  93 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Unknown    | N/A   | N/A    |
|  94 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  95 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  96 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]             | Unknown  | Unknown    | N/A   | N/A    |
|  97 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]             | Unknown  | Unknown    | N/A   | N/A    |
|  98 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [1, 16, 128, 9]             | Removed  | Unknown    | N/A   | N/A    |
|  99 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]         | Removed  | Unknown    | N/A   | N/A    |
| 100 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]           | Removed  | Unknown    | N/A   | N/A    |
| 101 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [1, 16, 2, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 102 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]         | Removed  | Unknown    | N/A   | N/A    |
| 103 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]           | Removed  | Unknown    | N/A   | N/A    |
| 104 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Unknown    | N/A   | N/A    |
| 105 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 106 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 107 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [1, 16, 64, 10]             | Unknown  | Unknown    | N/A   | N/A    |
| 108 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]           | Removed  | Unknown    | N/A   | N/A    |
| 109 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [1, 16, 64, 1]               | Unknown  | Unknown    | N/A   | N/A    |
| 110 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]           | Removed  | Unknown    | N/A   | N/A    |
| 111 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [1, 16, 64, 2]               | Unknown  | Unknown    | N/A   | N/A    |
| 112 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]               | Unknown  | Unknown    | N/A   | N/A    |
| 113 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]               | Unknown  | Unknown    | N/A   | N/A    |
| 114 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [1, 16, 64, 9]               | Removed  | Unknown    | N/A   | N/A    |
| 115 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 116 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 117 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]             | Removed  | Unknown    | N/A   | N/A    |
| 118 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]               | Removed  | Unknown    | N/A   | N/A    |
| 119 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                 | Removed  | Unknown    | N/A   | N/A    |
| 120 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
| 121 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 122 | Tensor<[1, 16]> self = ?,<br>List[int] size = [12, 16]                            | Done     | Unknown    | N/A   | N/A    |
| 123 | Tensor<[1, 17]> self = ?,<br>List[int] size = [13, 17]                            | Done     | Unknown    | N/A   | N/A    |
| 124 | Tensor<[1, 19]> self = ?,<br>List[int] size = [19, 19]                            | Done     | Unknown    | N/A   | N/A    |
| 125 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]                               | Unknown  | Unknown    | N/A   | N/A    |
| 126 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 127 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]             | Unknown  | Unknown    | N/A   | N/A    |
| 128 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]             | Removed  | Unknown    | N/A   | N/A    |
| 129 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]         | Removed  | Unknown    | N/A   | N/A    |
| 130 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]           | Removed  | Unknown    | N/A   | N/A    |
| 131 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]         | Unknown  | Unknown    | N/A   | N/A    |
| 132 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]           | Unknown  | Unknown    | N/A   | N/A    |
| 133 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]             | Unknown  | Unknown    | N/A   | N/A    |
| 134 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048, 10, 10]           | None     | Unknown    | N/A   | N/A    |
| 135 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048, 7, 7]             | None     | Unknown    | N/A   | N/A    |
| 136 | Tensor<[1, 20]> self = ?,<br>List[int] size = [20, 20]                            | Done     | Unknown    | N/A   | N/A    |
| 137 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [1, 24, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 138 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [1, 24, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 139 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 140 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 141 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int] size = [1, 24, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 142 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 143 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 144 | Tensor<[1, 256, 1, 1]> self = ?,<br>List[int] size = [1, 256, 56, 56]             | None     | Unknown    | N/A   | N/A    |
| 145 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                             | Removed  | Unknown    | N/A   | N/A    |
| 146 | Tensor<[1, 2]> self = ?,<br>List[int] size = [2, 2]                               | Done     | Unknown    | N/A   | N/A    |
| 147 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]       | Removed  | Unknown    | N/A   | N/A    |
| 148 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]           | Removed  | Unknown    | N/A   | N/A    |
| 149 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [1, 3, 64, 1445]           | Removed  | Unknown    | N/A   | N/A    |
| 150 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [1, 32, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 151 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [1, 32, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 152 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 153 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 154 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int] size = [1, 32, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 155 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 156 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 157 | Tensor<[1, 34]> self = ?,<br>List[int] size = [25, 34]                            | Done     | Unknown    | N/A   | N/A    |
| 158 | Tensor<[1, 38]> self = ?,<br>List[int] size = [38, 38]                            | Done     | Unknown    | N/A   | N/A    |
| 159 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3, 3]                               | Done     | Unknown    | N/A   | N/A    |
| 160 | Tensor<[1, 480, 1, 1]> self = ?,<br>List[int] size = [1, 480, 14, 14]             | None     | Unknown    | N/A   | N/A    |
| 161 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]           | Unknown  | Unknown    | N/A   | N/A    |
| 162 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]         | Removed  | Unknown    | N/A   | N/A    |
| 163 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]           | Removed  | Unknown    | N/A   | N/A    |
| 164 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]         | Unknown  | Unknown    | N/A   | N/A    |
| 165 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]           | Unknown  | Unknown    | N/A   | N/A    |
| 166 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 167 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]             | Unknown  | Unknown    | N/A   | N/A    |
| 168 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]             | Removed  | Unknown    | N/A   | N/A    |
| 169 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]             | Unknown  | Unknown    | N/A   | N/A    |
| 170 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512, 28, 28]             | None     | Unknown    | N/A   | N/A    |
| 171 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512, 7, 7]               | None     | Unknown    | N/A   | N/A    |
| 172 | Tensor<[1, 512, 1]> self = ?,<br>List[int] size = [1, 512, 256]                   | None     | Unknown    | N/A   | N/A    |
| 173 | Tensor<[1, 5]> self = ?,<br>List[int] size = [5, 5]                               | Done     | Unknown    | N/A   | N/A    |
| 174 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                 | Unknown  | Unknown    | N/A   | N/A    |
| 175 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                 | Unknown  | Unknown    | N/A   | N/A    |
| 176 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                   | Unknown  | Unknown    | N/A   | N/A    |
| 177 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                   | Unknown  | Unknown    | N/A   | N/A    |
| 178 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                 | Unknown  | Unknown    | N/A   | N/A    |
| 179 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 180 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]               | Unknown  | Unknown    | N/A   | N/A    |
| 181 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 182 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [1, 6, 17, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 183 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]                 | Unknown  | Unknown    | N/A   | N/A    |
| 184 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]               | Unknown  | Unknown    | N/A   | N/A    |
| 185 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [1, 6, 64, 17]               | Unknown  | Unknown    | N/A   | N/A    |
| 186 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]                 | Unknown  | Unknown    | N/A   | N/A    |
| 187 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]                 | Unknown  | Unknown    | N/A   | N/A    |
| 188 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
| 189 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
| 190 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]                       | Removed  | Unknown    | N/A   | N/A    |
| 191 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                       | Removed  | Unknown    | N/A   | N/A    |
| 192 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [1, 64, 64, 9]               | Removed  | Unknown    | N/A   | N/A    |
| 193 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]               | Removed  | Unknown    | N/A   | N/A    |
| 194 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                 | Removed  | Unknown    | N/A   | N/A    |
| 195 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672, 14, 14]             | None     | Unknown    | N/A   | N/A    |
| 196 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672, 7, 7]               | None     | Unknown    | N/A   | N/A    |
| 197 | Tensor<[1, 68]> self = ?,<br>List[int] size = [50, 68]                            | Done     | Unknown    | N/A   | N/A    |
| 198 | Tensor<[1, 72, 1, 1]> self = ?,<br>List[int] size = [1, 72, 28, 28]               | None     | Unknown    | N/A   | N/A    |
| 199 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 14, 14]             | None     | Unknown    | N/A   | N/A    |
| 200 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                 | Unknown  | Unknown    | N/A   | N/A    |
| 201 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                   | Unknown  | Unknown    | N/A   | N/A    |
| 202 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                   | Unknown  | Unknown    | N/A   | N/A    |
| 203 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                 | Unknown  | Unknown    | N/A   | N/A    |
| 204 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 205 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]               | Unknown  | Unknown    | N/A   | N/A    |
| 206 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 207 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [1, 8, 2, 64]                 | Unknown  | Unknown    | N/A   | N/A    |
| 208 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [1, 8, 2048, 160]         | Removed  | Unknown    | N/A   | N/A    |
| 209 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]         | Removed  | Unknown    | N/A   | N/A    |
| 210 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [1, 8, 2048, 32]           | Removed  | Unknown    | N/A   | N/A    |
| 211 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]           | Removed  | Unknown    | N/A   | N/A    |
| 212 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]         | Removed  | Unknown    | N/A   | N/A    |
| 213 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]           | Removed  | Unknown    | N/A   | N/A    |
| 214 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 215 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [1, 8, 256, 96]             | Removed  | Unknown    | N/A   | N/A    |
| 216 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]           | Unknown  | Unknown    | N/A   | N/A    |
| 217 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]             | Unknown  | Unknown    | N/A   | N/A    |
| 218 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [1, 8, 32, 2048]           | Removed  | Unknown    | N/A   | N/A    |
| 219 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]             | Removed  | Unknown    | N/A   | N/A    |
| 220 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [1, 8, 64, 10]               | Unknown  | Unknown    | N/A   | N/A    |
| 221 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [1, 8, 64, 1]                 | Unknown  | Unknown    | N/A   | N/A    |
| 222 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [1, 8, 64, 2]                 | Unknown  | Unknown    | N/A   | N/A    |
| 223 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]             | Unknown  | Unknown    | N/A   | N/A    |
| 224 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
| 225 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 8, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
| 226 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960, 7, 7]               | None     | Unknown    | N/A   | N/A    |
| 227 | Tensor<[1, 9]> self = ?,<br>List[int] size = [7, 9]                               | Done     | Unknown    | N/A   | N/A    |
| 228 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10]                            | None     | Unknown    | N/A   | N/A    |
| 229 | Tensor<[100, 1]> self = ?,<br>List[int] size = [100, 136]                         | None     | Unknown    | N/A   | N/A    |
| 230 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16]                            | None     | Unknown    | N/A   | N/A    |
| 231 | Tensor<[13, 1]> self = ?,<br>List[int] size = [13, 17]                            | None     | Unknown    | N/A   | N/A    |
| 232 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [16, 6, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 233 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [16, 6, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 234 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 235 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 236 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int] size = [16, 6, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 237 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 238 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 239 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [16, 8, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 240 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [16, 8, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 241 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 242 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 243 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int] size = [16, 8, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 244 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 245 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 246 | Tensor<[19, 1]> self = ?,<br>List[int] size = [19, 19]                            | None     | Unknown    | N/A   | N/A    |
| 247 | Tensor<[1]> self = ?,<br>List[int] size = [1]                                     | Unknown  | Unknown    | N/A   | N/A    |
| 248 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7]                   | Done     | Unknown    | N/A   | N/A    |
| 249 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]                               | None     | Unknown    | N/A   | N/A    |
| 250 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20]                            | None     | Unknown    | N/A   | N/A    |
| 251 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, -1, -1]                     | Done     | Unknown    | N/A   | N/A    |
| 252 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                   | Removed  | Unknown    | N/A   | N/A    |
| 253 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                   | Removed  | Unknown    | N/A   | N/A    |
| 254 | Tensor<[25, 1]> self = ?,<br>List[int] size = [25, 34]                            | None     | Unknown    | N/A   | N/A    |
| 255 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, -1, -1]                     | Done     | Unknown    | N/A   | N/A    |
| 256 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]                               | None     | Unknown    | N/A   | N/A    |
| 257 | Tensor<[38, 1]> self = ?,<br>List[int] size = [38, 38]                            | None     | Unknown    | N/A   | N/A    |
| 258 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [4, 12, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 259 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [4, 12, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 260 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 261 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 262 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int] size = [4, 12, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 263 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 264 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 265 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [4, 16, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 266 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [4, 16, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 267 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 268 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 269 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int] size = [4, 16, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 270 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 271 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 272 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]                               | None     | Unknown    | N/A   | N/A    |
| 273 | Tensor<[50, 1]> self = ?,<br>List[int] size = [50, 68]                            | None     | Unknown    | N/A   | N/A    |
| 274 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [64, 3, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 275 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [64, 3, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 276 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 277 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 278 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int] size = [64, 3, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 279 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 280 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 281 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [64, 4, 32, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 282 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [64, 4, 32, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 283 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 284 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]             | Removed  | Unknown    | N/A   | N/A    |
| 285 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int] size = [64, 4, 64, 32]              | None     | Unknown    | N/A   | N/A    |
| 286 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]             | Removed  | Unknown    | N/A   | N/A    |
| 287 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]             | Removed  | Unknown    | N/A   | N/A    |
| 288 | Tensor<[7, 1]> self = ?,<br>List[int] size = [7, 9]                               | None     | Unknown    | N/A   | N/A    |
| 289 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]                            | Done     | Unknown    | N/A   | N/A    |

