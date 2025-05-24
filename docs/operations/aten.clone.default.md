### aten.clone.default
|     | ATen Input Variations                                                                             | Status   | Isolated   | PCC   | Host   |
|----:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | 0      |
|   1 | Tensor<[1, 1, 1024]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
|   2 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Removed  | Done       | 1.0   | 0      |
|   3 | Tensor<[1, 1, 2048]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
|   4 | Tensor<[1, 1, 3072]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
|   5 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | 0      |
|   6 | Tensor<[1, 1, 4096]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
|   7 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       | 1.0   | 0      |
|   8 | Tensor<[1, 1, 512]> self = ?                                                                      | Unknown  | Done       | 1.0   | 0      |
|   9 | Tensor<[1, 1, 768]> self = ?                                                                      | Unknown  | Done       | 1.0   | 0      |
|  10 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
|  11 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | 0      |
|  12 | Tensor<[1, 10, 1024]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  13 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
|  14 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | 0      |
|  15 | Tensor<[1, 10, 2048]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  16 | Tensor<[1, 10, 3072]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  17 | Tensor<[1, 10, 4096]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  18 | Tensor<[1, 10, 512]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
|  19 | Tensor<[1, 10, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
|  20 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | 0      |
|  21 | Tensor<[1, 1024, 160]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  22 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
|  23 | Tensor<[1, 1024, 512]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  24 | Tensor<[1, 1024, 640]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  25 | Tensor<[1, 1024]> self = ?                                                                        | Removed  | Done       | 1.0   | 0      |
|  26 | Tensor<[1, 112, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
|  27 | Tensor<[1, 12, 1, 10]> self = ?                                                                   | Unknown  | Done       | 1.0   | 0      |
|  28 | Tensor<[1, 12, 1, 1]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  29 | Tensor<[1, 12, 1, 2]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  30 | Tensor<[1, 12, 1, 46]> self = ?                                                                   | Unknown  | Done       | 1.0   | 0      |
|  31 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  32 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  33 | Tensor<[1, 12, 10, 10]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  34 | Tensor<[1, 12, 12, 12]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  35 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
|  36 | Tensor<[1, 12, 128]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
|  37 | Tensor<[1, 12, 14, 14]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  38 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | 1.0   | 0      |
|  39 | Tensor<[1, 12, 16, 16]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  40 | Tensor<[1, 12, 197, 197]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
|  41 | Tensor<[1, 12, 25, 25]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  42 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | 0      |
|  43 | Tensor<[1, 12, 45, 45]> self = ?                                                                  | Unknown  | Done       | 1.0   | 0      |
|  44 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
|  45 | Tensor<[1, 12, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
|  46 | Tensor<[1, 12, 9, 9]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
|  47 | Tensor<[1, 1280]> self = ?                                                                        | Removed  | Done       | 1.0   | 0      |
|  48 | Tensor<[1, 128]> self = ?                                                                         | Removed  | Done       | 1.0   | 0      |
|  49 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  50 | Tensor<[1, 1370, 5120]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  51 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
|  52 | Tensor<[1, 14, 128]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
|  53 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
|  54 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
|  55 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
|  56 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
|  57 | Tensor<[1, 14, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
|  58 | Tensor<[1, 1445, 192]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  59 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
|  60 | Tensor<[1, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Removed  | Done       | 1.0   | 0      |
|  61 | Tensor<[1, 1500, 3072]> self = ?                                                                  | Unknown  | Done       | 1.0   | 0      |
|  62 | Tensor<[1, 1500, 768]> self = ?                                                                   | Unknown  | Done       | 1.0   | 0      |
|  63 | Tensor<[1, 1536]> self = ?                                                                        | Removed  | Done       | 1.0   | 0      |
|  64 | Tensor<[1, 16, 1, 10]> self = ?                                                                   | Unknown  | Done       | 1.0   | 0      |
|  65 | Tensor<[1, 16, 1, 1]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  66 | Tensor<[1, 16, 1, 2]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  67 | Tensor<[1, 16, 1, 6]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  68 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  69 | Tensor<[1, 16, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  70 | Tensor<[1, 16, 10, 10]> self = ?                                                                  | Unknown  | Done       | 1.0   | 0      |
|  71 | Tensor<[1, 16, 112, 112]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
|  72 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
|  73 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
|  74 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | 0      |
|  75 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Removed  | Unknown    | N/A   | N/A    |
|  76 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
|  77 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
|  78 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  79 | Tensor<[1, 16, 384, 384]> self = ?                                                                | Removed  | Unknown    | N/A   | N/A    |
|  80 | Tensor<[1, 16, 5, 5]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
|  81 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | 0      |
|  82 | Tensor<[1, 16, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
|  83 | Tensor<[1, 16, 9, 9]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
|  84 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
|  85 | Tensor<[1, 160, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | 0      |
|  86 | Tensor<[1, 16384, 128]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
|  87 | Tensor<[1, 16384, 32]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  88 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
|  89 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | 0      |
|  90 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Removed  | Done       | 1.0   | 0      |
|  91 | Tensor<[1, 196, 3072]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  92 | Tensor<[1, 196, 768]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
|  93 | Tensor<[1, 197, 1024]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  94 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
|  95 | Tensor<[1, 197, 3072]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  96 | Tensor<[1, 197, 4096]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
|  97 | Tensor<[1, 197, 768]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
|  98 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
|  99 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 100 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 101 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 102 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 103 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 104 | Tensor<[1, 2, 4096, 256]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
| 105 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 106 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 107 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 108 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 109 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
| 110 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | 0      |
| 111 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 112 | Tensor<[1, 2048]> self = ?                                                                        | Removed  | Done       | 1.0   | 0      |
| 113 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 114 | Tensor<[1, 24, 56, 56]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 115 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 116 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 117 | Tensor<[1, 25, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 118 | Tensor<[1, 256, 1024]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
| 119 | Tensor<[1, 256, 128, 128]> self = ?                                                               | Removed  | Done       | 1.0   | 0      |
| 120 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Removed  | Done       | 1.0   | 0      |
| 121 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 122 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 123 | Tensor<[1, 256, 256]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 124 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 125 | Tensor<[1, 256, 512]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 126 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 127 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 128 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Removed  | Done       | 1.0   | 0      |
| 129 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
| 130 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 131 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 132 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 133 | Tensor<[1, 3, 1445, 1445]> self = ?                                                               | Removed  | Done       | 1.0   | 0      |
| 134 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | 0      |
| 135 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 136 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 137 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 138 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 139 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
| 140 | Tensor<[1, 32, 1536]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 141 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 142 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Removed  | Unknown    | N/A   | N/A    |
| 143 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 144 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
| 145 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 146 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 147 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 148 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
| 149 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | 0      |
| 150 | Tensor<[1, 384, 1024]> self = ?                                                                   | Removed  | Unknown    | N/A   | N/A    |
| 151 | Tensor<[1, 384, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Unknown    | N/A   | N/A    |
| 152 | Tensor<[1, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Unknown    | N/A   | N/A    |
| 153 | Tensor<[1, 4, 3072]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
| 154 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 155 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 156 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 157 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 158 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 159 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 160 | Tensor<[1, 4, 768]> self = ?                                                                      | Unknown  | Done       | 1.0   | 0      |
| 161 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 162 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 163 | Tensor<[1, 40, 28, 28]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 164 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 165 | Tensor<[1, 4096, 256]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
| 166 | Tensor<[1, 4096, 64]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 167 | Tensor<[1, 4096]> self = ?                                                                        | Removed  | Done       | 1.0   | 0      |
| 168 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | 0      |
| 169 | Tensor<[1, 45, 768]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
| 170 | Tensor<[1, 49, 1024]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 171 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 172 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 173 | Tensor<[1, 49, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 174 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | 0      |
| 175 | Tensor<[1, 5, 1024, 256]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
| 176 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
| 177 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | 0      |
| 178 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | 0      |
| 179 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 180 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 181 | Tensor<[1, 50, 1024]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 182 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 183 | Tensor<[1, 50, 3072]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 184 | Tensor<[1, 50, 4096]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 185 | Tensor<[1, 50, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 186 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
| 187 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 188 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 189 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 190 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 191 | Tensor<[1, 59, 1024]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
| 192 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | 0      |
| 193 | Tensor<[1, 64, 1024]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 194 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 195 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 196 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 197 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
| 198 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 199 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
| 200 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 201 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 202 | Tensor<[1, 64, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 203 | Tensor<[1, 64, 9, 9]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 204 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 205 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 206 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 207 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
| 208 | Tensor<[1, 768, 196]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 209 | Tensor<[1, 768, 384]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 210 | Tensor<[1, 768]> self = ?                                                                         | Removed  | Done       | 1.0   | 0      |
| 211 | Tensor<[1, 8, 1, 10]> self = ?                                                                    | Unknown  | Done       | 1.0   | 0      |
| 212 | Tensor<[1, 8, 1, 1]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
| 213 | Tensor<[1, 8, 1, 2]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
| 214 | Tensor<[1, 8, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   | N/A    |
| 215 | Tensor<[1, 8, 10, 10]> self = ?                                                                   | Unknown  | Done       | 1.0   | 0      |
| 216 | Tensor<[1, 8, 2048, 256]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
| 217 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Removed  | Done       | 1.0   | 0      |
| 218 | Tensor<[1, 8, 256, 256]> self = ?                                                                 | Removed  | Done       | 1.0   | 0      |
| 219 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 220 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       | 1.0   | 0      |
| 221 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 222 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 223 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 224 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 225 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       | 1.0   | 0      |
| 226 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Removed  | Done       | 1.0   | 0      |
| 227 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | 0      |
| 228 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       | 1.0   | 0      |
| 229 | Tensor<[1, 80, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 230 | Tensor<[1, 9, 1024]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 231 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | 0      |
| 232 | Tensor<[1, 9, 128]> self = ?                                                                      | Removed  | Done       | 1.0   | 0      |
| 233 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 234 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | 0      |
| 235 | Tensor<[1, 9, 2048]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 236 | Tensor<[1, 9, 4096]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 237 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | 0      |
| 238 | Tensor<[1, 9, 768]> self = ?                                                                      | Removed  | Done       | 1.0   | 0      |
| 239 | Tensor<[1, s10 + 1]> self = ?                                                                     | Unknown  | Unknown    | N/A   | N/A    |
| 240 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | 0      |
| 241 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 242 | Tensor<[12, 50, 50]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 243 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 244 | Tensor<[16, 1, 60]> self = ?                                                                      | Unknown  | Done       | 1.0   | 0      |
| 245 | Tensor<[16, 1, s10 + 1]> self = ?                                                                 | Unknown  | Unknown    | N/A   | N/A    |
| 246 | Tensor<[16, 49, 192]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 247 | Tensor<[16, 49, 256]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 248 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 249 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 250 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 251 | Tensor<[16, 59, 59]> self = ?                                                                     | Unknown  | Done       | 1.0   | 0      |
| 252 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 253 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 254 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 255 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 256 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 257 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 258 | Tensor<[16, 64, 192]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 259 | Tensor<[16, 64, 256]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 260 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 261 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Unknown    | N/A   | N/A    |
| 262 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 263 | Tensor<[16, 7, 7]> self = ?                                                                       | Removed  | Done       | 1.0   | 0      |
| 264 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 265 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 266 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 267 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 268 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 269 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 270 | Tensor<[19, 19]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | 0      |
| 271 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 272 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 273 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Removed  | Done       | 1.0   | 0      |
| 274 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 275 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Done       | 1.0   | 0      |
| 276 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Done       | 1.0   | 0      |
| 277 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | 0      |
| 278 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 279 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 280 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | 0      |
| 281 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | 0      |
| 282 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 283 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Removed  | Done       | 1.0   | 0      |
| 284 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 285 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | 0      |
| 286 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 287 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 288 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 289 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Unknown    | N/A   | N/A    |
| 290 | Tensor<[38, 38]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | 0      |
| 291 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 292 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 293 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 294 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 295 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 296 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 297 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 298 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 299 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 300 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 301 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 302 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 303 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 304 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 305 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 306 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 307 | Tensor<[4, 49, 384]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 308 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Unknown    | N/A   | N/A    |
| 309 | Tensor<[4, 49, 512]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 310 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 311 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 312 | Tensor<[4, 64, 384]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 313 | Tensor<[4, 64, 512]> self = ?                                                                     | Removed  | Unknown    | N/A   | N/A    |
| 314 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 315 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Removed  | Done       | 1.0   | 0      |
| 316 | Tensor<[59, 1024]> self = ?                                                                       | Unknown  | Done       | 1.0   | 0      |
| 317 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 318 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 319 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 320 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 321 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 322 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 323 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 324 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 325 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 326 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 327 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 328 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | 0      |
| 329 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 330 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 331 | Tensor<[64, 49, 128]> self = ?                                                                    | Removed  | Done       | 1.0   | 0      |
| 332 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 333 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 334 | Tensor<[64, 49, 96]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 335 | Tensor<[64, 64, 128]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 336 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | 0      |
| 337 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 338 | Tensor<[64, 64, 96]> self = ?                                                                     | Removed  | Done       | 1.0   | 0      |
| 339 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | 0      |
| 340 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Unknown    | N/A   | N/A    |
| 341 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |
| 342 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | 0      |

