### aten._unsafe_view.default
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>List[int] size = [1, 1, 16, 64]         | Unknown  | Done       | True  |
|   1 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]           | Done     | Done       | True  |
|   2 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]         | Done     | Done       | True  |
|   3 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int] size = [1, 122400, 4]      | Unknown  | Done       | True  |
|   4 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int] size = [1, 122400, 91]    | Unknown  | Done       | True  |
|   5 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]         | Unknown  | Done       | True  |
|   6 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 768]            | Done     | Done       | True  |
|   7 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int] size = [1, 1989, 4]          | Unknown  | Done       | True  |
|   8 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int] size = [1, 1989, 91]        | Unknown  | Done       | True  |
|   9 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] size = [1, 14, 768]            | Done     | Done       | True  |
|  10 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] size = [1, 256, 768]    | None     | Fallback   | True  |
|  11 | Tensor<[1, 19, 16, 64]> self = ?,<br>List[int] size = [1, 19, 1024]           | Done     | Done       | True  |
|  12 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>List[int] size = [1, 2166, 4]          | Done     | Done       | True  |
|  13 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>List[int] size = [1, 2166, 91]        | Done     | Done       | True  |
|  14 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]          | Done     | Done       | True  |
|  15 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]         | Done     | Done       | True  |
|  16 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]              | Done     | Done       | True  |
|  17 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]            | Done     | Done       | True  |
|  18 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] size = [4, 49, 384]       | Done     | Done       | True  |
|  19 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] size = [4, 49, 512]       | Done     | Done       | True  |
|  20 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] size = [4, 64, 384]       | Done     | Done       | False |
|  21 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] size = [4, 64, 512]       | Done     | Done       | False |
|  22 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]   | Done     | Done       | True  |
|  23 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]   | Done     | Done       | True  |
|  24 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]   | Done     | Done       | True  |
|  25 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512]   | Done     | Done       | True  |
|  26 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]          | Done     | Done       | True  |
|  27 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91]        | Done     | Done       | True  |
|  28 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int] size = [1, 24, 768]            | Done     | Done       | True  |
|  29 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int] size = [1, 7650, 4]          | Unknown  | Done       | True  |
|  30 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int] size = [1, 7650, 91]        | Unknown  | Done       | True  |
|  31 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]            | Unknown  | Done       | True  |
|  32 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]           | Unknown  | Done       | True  |
|  33 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]           | Unknown  | Done       | True  |
|  34 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] size = [1, 3, 256, 256] | Unknown  | Fallback   | True  |
|  35 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>List[int] size = [1, 36, 4]              | Done     | Done       | True  |
|  36 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>List[int] size = [1, 36, 91]            | Done     | Done       | True  |
|  37 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]              | Done     | Done       | True  |
|  38 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]            | Done     | Done       | True  |
|  39 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536]           | Done     | Done       | True  |
|  40 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>List[int] size = [1, 5776, 4]          | Done     | Done       | True  |
|  41 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>List[int] size = [1, 5776, 91]        | Done     | Done       | True  |
|  42 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] size = [16, 49, 192]      | Done     | Done       | True  |
|  43 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] size = [16, 49, 256]      | Done     | Done       | True  |
|  44 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] size = [16, 64, 192]      | Done     | Done       | False |
|  45 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] size = [16, 64, 256]      | Done     | Done       | False |
|  46 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]   | Done     | Done       | True  |
|  47 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]   | Done     | Done       | True  |
|  48 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]   | Done     | Done       | False |
|  49 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256]   | Done     | Done       | False |
|  50 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]          | Unknown  | Done       | True  |
|  51 | Tensor<[1, 49, 24, 32]> self = ?,<br>List[int] size = [1, 49, 768]            | Done     | Done       | True  |
|  52 | Tensor<[1, 49, 32, 32]> self = ?,<br>List[int] size = [1, 49, 1024]           | Done     | Done       | True  |
|  53 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>List[int] size = [1, 5, 16, 64]         | Unknown  | Done       | True  |
|  54 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]             | Done     | Done       | True  |
|  55 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]           | Done     | Done       | True  |
|  56 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768]            | Done     | Done       | True  |
|  57 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int] size = [1, 30600, 4]         | Unknown  | Done       | True  |
|  58 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int] size = [1, 30600, 91]       | Unknown  | Done       | True  |
|  59 | Tensor<[1, 59, 16, 64]> self = ?,<br>List[int] size = [1, 59, 1024]           | Done     | Done       | True  |
|  60 | Tensor<[1, 64, 24, 32]> self = ?,<br>List[int] size = [1, 64, 768]            | Done     | Done       | True  |
|  61 | Tensor<[1, 64, 32, 32]> self = ?,<br>List[int] size = [1, 64, 1024]           | Done     | Done       | True  |
|  62 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544]             | Done     | Done       | True  |
|  63 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int] size = [1, 567, 4]             | Unknown  | Done       | True  |
|  64 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int] size = [1, 567, 91]           | Unknown  | Done       | True  |
|  65 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128]   | Done     | Done       | True  |
|  66 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]     | Done     | Done       | True  |
|  67 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] size = [64, 49, 128]      | Done     | Done       | True  |
|  68 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] size = [64, 49, 96]        | Done     | Done       | True  |
|  69 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] size = [1, 64, 64, 128]   | Done     | Done       | False |
|  70 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] size = [64, 64, 128]      | Done     | Done       | False |
|  71 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]     | Done     | Done       | False |
|  72 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] size = [64, 64, 96]        | Done     | Done       | False |
|  73 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] size = [1, 9, 768]              | Done     | Done       | True  |
|  74 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] size = [1, 9, 2048]            | Done     | Done       | True  |
|  75 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] size = [1, 9, 1024]             | Done     | Done       | True  |
|  76 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] size = [1, 9, 4096]             | Done     | Done       | True  |
|  77 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                          | Done     | Done       | True  |
|  78 | Tensor<[100, 136]> self = ?,<br>List[int] size = [13600]                      | Unknown  | Done       | True  |
|  79 | Tensor<[13, 17]> self = ?,<br>List[int] size = [221]                          | Unknown  | Done       | True  |
|  80 | Tensor<[16, 49, 6, 32]> self = ?,<br>List[int] size = [16, 49, 192]           | Done     | Done       | True  |
|  81 | Tensor<[16, 49, 8, 32]> self = ?,<br>List[int] size = [16, 49, 256]           | Done     | Done       | True  |
|  82 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int] size = [96, 32, 49]            | Done     | Done       | True  |
|  83 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int] size = [96, 32, 64]            | Done     | Done       | True  |
|  84 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int] size = [96, 49, 32]            | Done     | Done       | True  |
|  85 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int] size = [96, 64, 32]            | Done     | Done       | True  |
|  86 | Tensor<[16, 64, 6, 32]> self = ?,<br>List[int] size = [16, 64, 192]           | Done     | Done       | True  |
|  87 | Tensor<[16, 64, 8, 32]> self = ?,<br>List[int] size = [16, 64, 256]           | Done     | Done       | True  |
|  88 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int] size = [128, 32, 49]           | Done     | Done       | True  |
|  89 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int] size = [128, 32, 64]           | Done     | Done       | True  |
|  90 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int] size = [128, 49, 32]           | Done     | Done       | True  |
|  91 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int] size = [128, 64, 32]           | Done     | Done       | True  |
|  92 | Tensor<[19, 19]> self = ?,<br>List[int] size = [361]                          | Done     | Done       | True  |
|  93 | Tensor<[2, 2, 7, 7]> self = ?,<br>List[int] size = [4, 49]                    | Done     | Done       | True  |
|  94 | Tensor<[2, 2, 8, 8]> self = ?,<br>List[int] size = [4, 64]                    | Done     | Done       | True  |
|  95 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                              | Done     | Done       | True  |
|  96 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]                   | Done     | Done       | True  |
|  97 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]               | Done     | Done       | True  |
|  98 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, 7, 64]               | Done     | Done       | True  |
|  99 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                          | Done     | Done       | True  |
| 100 | Tensor<[25, 34]> self = ?,<br>List[int] size = [850]                          | Unknown  | Done       | True  |
| 101 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                              | Done     | Done       | True  |
| 102 | Tensor<[38, 38]> self = ?,<br>List[int] size = [1444]                         | Done     | Done       | True  |
| 103 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int] size = [48, 32, 49]            | Done     | Done       | True  |
| 104 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int] size = [48, 32, 64]            | Done     | Done       | True  |
| 105 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int] size = [48, 49, 32]            | Done     | Done       | True  |
| 106 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int] size = [48, 64, 32]            | Done     | Done       | True  |
| 107 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int] size = [64, 32, 49]            | Done     | Done       | True  |
| 108 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int] size = [64, 32, 64]            | Done     | Done       | True  |
| 109 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int] size = [64, 49, 32]            | Done     | Done       | True  |
| 110 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int] size = [64, 64, 32]            | Done     | Done       | True  |
| 111 | Tensor<[4, 4, 7, 7]> self = ?,<br>List[int] size = [16, 49]                   | Done     | Done       | True  |
| 112 | Tensor<[4, 4, 8, 8]> self = ?,<br>List[int] size = [16, 64]                   | Done     | Done       | True  |
| 113 | Tensor<[4, 49, 12, 32]> self = ?,<br>List[int] size = [4, 49, 384]            | Done     | Done       | True  |
| 114 | Tensor<[4, 49, 16, 32]> self = ?,<br>List[int] size = [4, 49, 512]            | Done     | Done       | True  |
| 115 | Tensor<[4, 64, 12, 32]> self = ?,<br>List[int] size = [4, 64, 384]            | Done     | Done       | True  |
| 116 | Tensor<[4, 64, 16, 32]> self = ?,<br>List[int] size = [4, 64, 512]            | Done     | Done       | True  |
| 117 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                             | Done     | Done       | True  |
| 118 | Tensor<[50, 68]> self = ?,<br>List[int] size = [3400]                         | Unknown  | Done       | True  |
| 119 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int] size = [192, 32, 49]           | Done     | Done       | True  |
| 120 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int] size = [192, 32, 64]           | Done     | Done       | True  |
| 121 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int] size = [192, 49, 32]           | Done     | Done       | True  |
| 122 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int] size = [192, 64, 32]           | Done     | Done       | True  |
| 123 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int] size = [256, 32, 49]           | Done     | Done       | True  |
| 124 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int] size = [256, 32, 64]           | Done     | Done       | True  |
| 125 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int] size = [256, 49, 32]           | Done     | Done       | True  |
| 126 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int] size = [256, 64, 32]           | Done     | Done       | True  |
| 127 | Tensor<[64, 49, 3, 32]> self = ?,<br>List[int] size = [64, 49, 96]            | Done     | Done       | True  |
| 128 | Tensor<[64, 49, 4, 32]> self = ?,<br>List[int] size = [64, 49, 128]           | Done     | Done       | True  |
| 129 | Tensor<[64, 64, 3, 32]> self = ?,<br>List[int] size = [64, 64, 96]            | Done     | Done       | True  |
| 130 | Tensor<[64, 64, 4, 32]> self = ?,<br>List[int] size = [64, 64, 128]           | Done     | Done       | True  |
| 131 | Tensor<[7, 9]> self = ?,<br>List[int] size = [63]                             | Unknown  | Done       | True  |
| 132 | Tensor<[8, 8, 7, 7]> self = ?,<br>List[int] size = [64, 49]                   | Done     | Done       | True  |
| 133 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] size = [64, 64]                   | Done     | Done       | False |

