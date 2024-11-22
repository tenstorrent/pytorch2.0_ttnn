### aten.clone.default
|     | ATen Input Variations                                                                             | Status   | Isolated   | PCC   |
|----:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
|   1 | Tensor<[1, 1, 1024]> self = ?                                                                     | Unknown  | Fallback   | True  |
|   2 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Unknown  | Fallback   | True  |
|   3 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Unknown  | Fallback   | True  |
|   4 | Tensor<[1, 1, 2048]> self = ?                                                                     | Unknown  | Fallback   | True  |
|   5 | Tensor<[1, 1, 3072]> self = ?                                                                     | Unknown  | Fallback   | True  |
|   6 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
|   7 | Tensor<[1, 1, 4096]> self = ?                                                                     | Unknown  | Fallback   | True  |
|   8 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Fallback   | True  |
|   9 | Tensor<[1, 1, 512]> self = ?                                                                      | Unknown  | Fallback   | True  |
|  10 | Tensor<[1, 1, 768]> self = ?                                                                      | Unknown  | Fallback   | True  |
|  11 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
|  12 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
|  13 | Tensor<[1, 10, 1024]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  14 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  15 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
|  16 | Tensor<[1, 10, 2048]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  17 | Tensor<[1, 10, 3072]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  18 | Tensor<[1, 10, 4096]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  19 | Tensor<[1, 10, 512]> self = ?                                                                     | Unknown  | Fallback   | True  |
|  20 | Tensor<[1, 10, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
|  21 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Fallback   | True  |
|  22 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Fallback   | True  |
|  23 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Fallback   | True  |
|  24 | Tensor<[1, 1024, 160]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  25 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
|  26 | Tensor<[1, 1024, 512]> self = ?                                                                   | Removed  | Fallback   | True  |
|  27 | Tensor<[1, 1024, 640]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  28 | Tensor<[1, 1024]> self = ?                                                                        | Removed  | Fallback   | True  |
|  29 | Tensor<[1, 112, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
|  30 | Tensor<[1, 12, 1, 10]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  31 | Tensor<[1, 12, 1, 1]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  32 | Tensor<[1, 12, 1, 2]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  33 | Tensor<[1, 12, 1, 46]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  34 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   |
|  35 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   |
|  36 | Tensor<[1, 12, 10, 10]> self = ?                                                                  | Removed  | Fallback   | True  |
|  37 | Tensor<[1, 12, 12, 12]> self = ?                                                                  | Removed  | Fallback   | True  |
|  38 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  39 | Tensor<[1, 12, 128]> self = ?                                                                     | Removed  | Fallback   | True  |
|  40 | Tensor<[1, 12, 14, 14]> self = ?                                                                  | Removed  | Fallback   | True  |
|  41 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
|  42 | Tensor<[1, 12, 16, 16]> self = ?                                                                  | Removed  | Fallback   | True  |
|  43 | Tensor<[1, 12, 197, 197]> self = ?                                                                | Removed  | Fallback   | True  |
|  44 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  45 | Tensor<[1, 12, 25, 25]> self = ?                                                                  | Removed  | Fallback   | True  |
|  46 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Fallback   | True  |
|  47 | Tensor<[1, 12, 45, 45]> self = ?                                                                  | Unknown  | Fallback   | True  |
|  48 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  49 | Tensor<[1, 12, 7, 7]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  50 | Tensor<[1, 12, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
|  51 | Tensor<[1, 12, 9, 9]> self = ?                                                                    | Removed  | Fallback   | True  |
|  52 | Tensor<[1, 1200, 1280]> self = ?                                                                  | Unknown  | Fallback   | True  |
|  53 | Tensor<[1, 1200, 320]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  54 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
|  55 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
|  56 | Tensor<[1, 1280, 8, 8]> self = ?                                                                  | Unknown  | Fallback   | True  |
|  57 | Tensor<[1, 1280, s0, s1]> self = ?                                                                | Unknown  | Unknown    | N/A   |
|  58 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Unknown    | N/A   |
|  59 | Tensor<[1, 1280, s1, s2]> self = ?                                                                | Unknown  | Unknown    | N/A   |
|  60 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Unknown    | N/A   |
|  61 | Tensor<[1, 1280]> self = ?                                                                        | Removed  | Fallback   | True  |
|  62 | Tensor<[1, 128]> self = ?                                                                         | Removed  | Fallback   | True  |
|  63 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
|  64 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
|  65 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Removed  | Fallback   | True  |
|  66 | Tensor<[1, 1370, 5120]> self = ?                                                                  | Removed  | Fallback   | True  |
|  67 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  68 | Tensor<[1, 14, 128]> self = ?                                                                     | Removed  | Fallback   | True  |
|  69 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Removed  | Fallback   | True  |
|  70 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Removed  | Fallback   | True  |
|  71 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Removed  | Fallback   | True  |
|  72 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Removed  | Fallback   | True  |
|  73 | Tensor<[1, 14, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
|  74 | Tensor<[1, 1445, 192]> self = ?                                                                   | Removed  | Fallback   | True  |
|  75 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
|  76 | Tensor<[1, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Removed  | Fallback   | True  |
|  77 | Tensor<[1, 15, 1024]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  78 | Tensor<[1, 15, 512]> self = ?                                                                     | Unknown  | Fallback   | True  |
|  79 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Fallback   | True  |
|  80 | Tensor<[1, 1500, 3072]> self = ?                                                                  | Unknown  | Fallback   | True  |
|  81 | Tensor<[1, 1500, 768]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  82 | Tensor<[1, 1536]> self = ?                                                                        | Removed  | Fallback   | True  |
|  83 | Tensor<[1, 16, 1, 10]> self = ?                                                                   | Unknown  | Fallback   | True  |
|  84 | Tensor<[1, 16, 1, 1]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  85 | Tensor<[1, 16, 1, 2]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  86 | Tensor<[1, 16, 1, 6]> self = ?                                                                    | Unknown  | Fallback   | True  |
|  87 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   |
|  88 | Tensor<[1, 16, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   |
|  89 | Tensor<[1, 16, 10, 10]> self = ?                                                                  | Unknown  | Fallback   | True  |
|  90 | Tensor<[1, 16, 112, 112]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Fallback   | True  |
|  91 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  92 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Removed  | Fallback   | True  |
|  93 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Fallback   | True  |
|  94 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Removed  | Fallback   | True  |
|  95 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Removed  | Fallback   | True  |
|  96 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Removed  | Fallback   | True  |
|  97 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
|  98 | Tensor<[1, 16, 197, 197]> self = ?                                                                | Removed  | Fallback   | True  |
|  99 | Tensor<[1, 16, 256, 256]> self = ?                                                                | Removed  | Fallback   | True  |
| 100 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Removed  | Fallback   | True  |
| 101 | Tensor<[1, 16, 5, 5]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 102 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 103 | Tensor<[1, 16, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
| 104 | Tensor<[1, 16, 9, 9]> self = ?                                                                    | Removed  | Fallback   | True  |
| 105 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 106 | Tensor<[1, 160, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Fallback   | True  |
| 107 | Tensor<[1, 16384, 128]> self = ?                                                                  | Unknown  | Fallback   | True  |
| 108 | Tensor<[1, 16384, 32]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 109 | Tensor<[1, 19, 1024]> self = ?                                                                    | Removed  | Fallback   | True  |
| 110 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 111 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 112 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
| 113 | Tensor<[1, 19, 4096]> self = ?                                                                    | Removed  | Fallback   | True  |
| 114 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Removed  | Fallback   | True  |
| 115 | Tensor<[1, 19200, 256]> self = ?                                                                  | Unknown  | Fallback   | True  |
| 116 | Tensor<[1, 19200, 64]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 117 | Tensor<[1, 196, 3072]> self = ?                                                                   | Removed  | Fallback   | True  |
| 118 | Tensor<[1, 196, 768]> self = ?                                                                    | Removed  | Fallback   | True  |
| 119 | Tensor<[1, 197, 1024]> self = ?                                                                   | Removed  | Fallback   | True  |
| 120 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 121 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 122 | Tensor<[1, 197, 3072]> self = ?                                                                   | Removed  | Fallback   | True  |
| 123 | Tensor<[1, 197, 4096]> self = ?                                                                   | Removed  | Fallback   | True  |
| 124 | Tensor<[1, 197, 768]> self = ?                                                                    | Removed  | Fallback   | True  |
| 125 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 126 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 127 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 128 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 129 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 130 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 131 | Tensor<[1, 2, 4096, 256]> self = ?                                                                | Unknown  | Fallback   | True  |
| 132 | Tensor<[1, 2, 4800, 300]> self = ?                                                                | Unknown  | Fallback   | True  |
| 133 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 134 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 135 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 136 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 137 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 138 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
| 139 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 140 | Tensor<[1, 2048]> self = ?                                                                        | Removed  | Fallback   | True  |
| 141 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 142 | Tensor<[1, 24, 3072]> self = ?                                                                    | Removed  | Fallback   | True  |
| 143 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 144 | Tensor<[1, 24, 56, 56]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 145 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 146 | Tensor<[1, 24, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
| 147 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 148 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 149 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
| 150 | Tensor<[1, 25, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
| 151 | Tensor<[1, 256, 1024]> self = ?                                                                   | Removed  | Fallback   | True  |
| 152 | Tensor<[1, 256, 128, 128]> self = ?                                                               | Unknown  | Fallback   | True  |
| 153 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Unknown  | Fallback   | True  |
| 154 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 155 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 156 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 157 | Tensor<[1, 256, 256]> self = ?                                                                    | Removed  | Fallback   | True  |
| 158 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 159 | Tensor<[1, 256, 512]> self = ?                                                                    | Removed  | Fallback   | True  |
| 160 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 161 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 162 | Tensor<[1, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Fallback   | True  |
| 163 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Removed  | Fallback   | True  |
| 164 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Removed  | Fallback   | True  |
| 165 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Removed  | Fallback   | True  |
| 166 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Removed  | Fallback   | True  |
| 167 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Removed  | Fallback   | True  |
| 168 | Tensor<[1, 3, 1445, 1445]> self = ?                                                               | Removed  | Fallback   | True  |
| 169 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Fallback   | True  |
| 170 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 171 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 172 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 173 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 174 | Tensor<[1, 300, 2048]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 175 | Tensor<[1, 300, 512]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 176 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 177 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 178 | Tensor<[1, 32, 1536]> self = ?                                                                    | Removed  | Fallback   | True  |
| 179 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 180 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Removed  | Fallback   | True  |
| 181 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Removed  | Fallback   | True  |
| 182 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Removed  | Fallback   | True  |
| 183 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Removed  | Fallback   | True  |
| 184 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 185 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 186 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 187 | Tensor<[1, 320, 64, 64]> self = ?                                                                 | Unknown  | Fallback   | True  |
| 188 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 189 | Tensor<[1, 320, s1, s2]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 190 | Tensor<[1, 320, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Unknown    | N/A   |
| 191 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 192 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
| 193 | Tensor<[1, 4, 3072]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 194 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 195 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 196 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 197 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 198 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 199 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 200 | Tensor<[1, 4, 768]> self = ?                                                                      | Unknown  | Fallback   | True  |
| 201 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 202 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 203 | Tensor<[1, 40, 28, 28]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 204 | Tensor<[1, 4096, 1280]> self = ?                                                                  | Unknown  | Fallback   | True  |
| 205 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 206 | Tensor<[1, 4096, 256]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 207 | Tensor<[1, 4096, 320]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 208 | Tensor<[1, 4096, 64]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 209 | Tensor<[1, 4096]> self = ?                                                                        | Removed  | Fallback   | True  |
| 210 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 211 | Tensor<[1, 45, 768]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 212 | Tensor<[1, 4800, 128]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 213 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 214 | Tensor<[1, 4800, 512]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 215 | Tensor<[1, 49, 1024]> self = ?                                                                    | Removed  | Fallback   | True  |
| 216 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 217 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 218 | Tensor<[1, 49, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
| 219 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 220 | Tensor<[1, 5, 1024, 256]> self = ?                                                                | Unknown  | Fallback   | True  |
| 221 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 222 | Tensor<[1, 5, 1200, 300]> self = ?                                                                | Unknown  | Fallback   | True  |
| 223 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Fallback   | True  |
| 224 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 225 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 226 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 227 | Tensor<[1, 50, 1024]> self = ?                                                                    | Removed  | Fallback   | True  |
| 228 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 229 | Tensor<[1, 50, 3072]> self = ?                                                                    | Removed  | Fallback   | True  |
| 230 | Tensor<[1, 50, 4096]> self = ?                                                                    | Removed  | Fallback   | True  |
| 231 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 232 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Fallback   | True  |
| 233 | Tensor<[1, 50, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
| 234 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Removed  | Fallback   | True  |
| 235 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 236 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Removed  | Fallback   | True  |
| 237 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Removed  | Fallback   | True  |
| 238 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Removed  | Fallback   | True  |
| 239 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Removed  | Fallback   | True  |
| 240 | Tensor<[1, 59, 1024]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 241 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 242 | Tensor<[1, 6, 1, 15]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 243 | Tensor<[1, 6, 1, 17]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 244 | Tensor<[1, 6, 1, 1]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 245 | Tensor<[1, 6, 1, 2]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 246 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   |
| 247 | Tensor<[1, 6, 15, 15]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 248 | Tensor<[1, 64, 1024]> self = ?                                                                    | Removed  | Fallback   | True  |
| 249 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Removed  | Fallback   | True  |
| 250 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Fallback   | True  |
| 251 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 252 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 253 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Removed  | Fallback   | True  |
| 254 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Removed  | Fallback   | True  |
| 255 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Removed  | Fallback   | True  |
| 256 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 257 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Removed  | Fallback   | True  |
| 258 | Tensor<[1, 64, 768]> self = ?                                                                     | Removed  | Fallback   | True  |
| 259 | Tensor<[1, 64, 9, 9]> self = ?                                                                    | Removed  | Fallback   | True  |
| 260 | Tensor<[1, 640, s0, s1]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 261 | Tensor<[1, 640, s0, s1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Unknown    | N/A   |
| 262 | Tensor<[1, 640, s1, s2]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 263 | Tensor<[1, 640, s1, s2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Unknown    | N/A   |
| 264 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Fallback   | True  |
| 265 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Removed  | Fallback   | True  |
| 266 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Removed  | Fallback   | True  |
| 267 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Removed  | Fallback   | True  |
| 268 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Removed  | Fallback   | True  |
| 269 | Tensor<[1, 7, 768]> self = ?                                                                      | Unknown  | Fallback   | True  |
| 270 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Fallback   | True  |
| 271 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Fallback   | True  |
| 272 | Tensor<[1, 768, 196]> self = ?                                                                    | Removed  | Fallback   | True  |
| 273 | Tensor<[1, 768, 384]> self = ?                                                                    | Removed  | Fallback   | True  |
| 274 | Tensor<[1, 768]> self = ?                                                                         | Removed  | Fallback   | True  |
| 275 | Tensor<[1, 8, 1, 10]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 276 | Tensor<[1, 8, 1, 1]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 277 | Tensor<[1, 8, 1, 2]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 278 | Tensor<[1, 8, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   |
| 279 | Tensor<[1, 8, 10, 10]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 280 | Tensor<[1, 8, 2048, 256]> self = ?                                                                | Removed  | Fallback   | True  |
| 281 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Removed  | Fallback   | True  |
| 282 | Tensor<[1, 8, 256, 256]> self = ?                                                                 | Removed  | Fallback   | True  |
| 283 | Tensor<[1, 8, 300, 300]> self = ?                                                                 | Unknown  | Fallback   | True  |
| 284 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 285 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Fallback   | True  |
| 286 | Tensor<[1, 8, 768]> self = ?                                                                      | Removed  | Fallback   | True  |
| 287 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Removed  | Fallback   | True  |
| 288 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Removed  | Fallback   | True  |
| 289 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Removed  | Fallback   | True  |
| 290 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 291 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Fallback   | True  |
| 292 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Removed  | Fallback   | True  |
| 293 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Fallback   | True  |
| 294 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Fallback   | True  |
| 295 | Tensor<[1, 80, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 296 | Tensor<[1, 9, 1024]> self = ?                                                                     | Removed  | Fallback   | True  |
| 297 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Fallback   | True  |
| 298 | Tensor<[1, 9, 128]> self = ?                                                                      | Removed  | Fallback   | True  |
| 299 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 300 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Fallback   | True  |
| 301 | Tensor<[1, 9, 2048]> self = ?                                                                     | Removed  | Fallback   | True  |
| 302 | Tensor<[1, 9, 4096]> self = ?                                                                     | Removed  | Fallback   | True  |
| 303 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Fallback   | True  |
| 304 | Tensor<[1, 9, 768]> self = ?                                                                      | Removed  | Fallback   | True  |
| 305 | Tensor<[1, s0*s1, 1280]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 306 | Tensor<[1, s0*s1, 2560]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 307 | Tensor<[1, s0*s1, 5120]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 308 | Tensor<[1, s0*s1, 640]> self = ?                                                                  | Unknown  | Unknown    | N/A   |
| 309 | Tensor<[1, s1*s2, 1280]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 310 | Tensor<[1, s1*s2, 2560]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 311 | Tensor<[1, s1*s2, 320]> self = ?                                                                  | Unknown  | Unknown    | N/A   |
| 312 | Tensor<[1, s1*s2, 5120]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 313 | Tensor<[1, s1*s2, 640]> self = ?                                                                  | Unknown  | Unknown    | N/A   |
| 314 | Tensor<[1, s10 + 1]> self = ?                                                                     | Unknown  | Unknown    | N/A   |
| 315 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 316 | Tensor<[100, 1, 2048]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 317 | Tensor<[100, 1, 256]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 318 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Fallback   | True  |
| 319 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Fallback   | True  |
| 320 | Tensor<[1152]> self = ?                                                                           | Removed  | Unknown    | N/A   |
| 321 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Fallback   | True  |
| 322 | Tensor<[12, 24, 24]> self = ?                                                                     | Removed  | Fallback   | True  |
| 323 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 324 | Tensor<[12, 50, 50]> self = ?                                                                     | Removed  | Fallback   | True  |
| 325 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 326 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 327 | Tensor<[1536]> self = ?                                                                           | Removed  | Unknown    | N/A   |
| 328 | Tensor<[16, 1, 60]> self = ?                                                                      | Unknown  | Fallback   | True  |
| 329 | Tensor<[16, 1, s10 + 1]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 330 | Tensor<[16, 19, 19]> self = ?                                                                     | Removed  | Fallback   | True  |
| 331 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Fallback   | True  |
| 332 | Tensor<[16, 49, 192]> self = ?                                                                    | Removed  | Fallback   | True  |
| 333 | Tensor<[16, 49, 256]> self = ?                                                                    | Removed  | Fallback   | True  |
| 334 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 335 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 336 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 337 | Tensor<[16, 59, 59]> self = ?                                                                     | Unknown  | Fallback   | True  |
| 338 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 339 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 340 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 341 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 342 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 343 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 344 | Tensor<[16, 64, 192]> self = ?                                                                    | Removed  | Fallback   | True  |
| 345 | Tensor<[16, 64, 256]> self = ?                                                                    | Removed  | Fallback   | True  |
| 346 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 347 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 348 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 349 | Tensor<[16, 7, 7]> self = ?                                                                       | Removed  | Fallback   | True  |
| 350 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 351 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 352 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 353 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 354 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 355 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 356 | Tensor<[19, 19]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 357 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 358 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 359 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Fallback   | True  |
| 360 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  | Fallback   | True  |
| 361 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Fallback   | True  |
| 362 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Fallback   | True  |
| 363 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 364 | Tensor<[2304]> self = ?                                                                           | Removed  | Unknown    | N/A   |
| 365 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 366 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 367 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 368 | Tensor<[288]> self = ?                                                                            | Removed  | Unknown    | N/A   |
| 369 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Fallback   | True  |
| 370 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Fallback   | True  |
| 371 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 372 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Fallback   | True  |
| 373 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 374 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Fallback   | True  |
| 375 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 376 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 377 | Tensor<[3072]> self = ?                                                                           | Removed  | Unknown    | N/A   |
| 378 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 379 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 380 | Tensor<[38, 38]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 381 | Tensor<[384]> self = ?                                                                            | Removed  | Unknown    | N/A   |
| 382 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 383 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 384 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 385 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 386 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 387 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 388 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 389 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 390 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 391 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 392 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 393 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 394 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 395 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 396 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 397 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 398 | Tensor<[4, 49, 384]> self = ?                                                                     | Removed  | Fallback   | True  |
| 399 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 400 | Tensor<[4, 49, 512]> self = ?                                                                     | Removed  | Fallback   | True  |
| 401 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 402 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 403 | Tensor<[4, 64, 384]> self = ?                                                                     | Removed  | Fallback   | True  |
| 404 | Tensor<[4, 64, 512]> self = ?                                                                     | Removed  | Fallback   | True  |
| 405 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 406 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Fallback   | True  |
| 407 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Fallback   | True  |
| 408 | Tensor<[576]> self = ?                                                                            | Removed  | Unknown    | N/A   |
| 409 | Tensor<[59, 1024]> self = ?                                                                       | Unknown  | Fallback   | True  |
| 410 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 411 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 412 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 413 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 414 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 415 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 416 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 417 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 418 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 419 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 420 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 421 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Removed  | Fallback   | True  |
| 422 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 423 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Removed  | Fallback   | True  |
| 424 | Tensor<[64, 49, 128]> self = ?                                                                    | Removed  | Fallback   | True  |
| 425 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 426 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 427 | Tensor<[64, 49, 96]> self = ?                                                                     | Removed  | Fallback   | True  |
| 428 | Tensor<[64, 64, 128]> self = ?                                                                    | Removed  | Fallback   | True  |
| 429 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 430 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Fallback   | True  |
| 431 | Tensor<[64, 64, 96]> self = ?                                                                     | Removed  | Fallback   | True  |
| 432 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Fallback   | True  |
| 433 | Tensor<[768]> self = ?                                                                            | Removed  | Unknown    | N/A   |
| 434 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 435 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Fallback   | True  |
| 436 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 437 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Fallback   | True  |
| 438 | Tensor<[920, 1, 2048]> self = ?                                                                   | Unknown  | Fallback   | True  |
| 439 | Tensor<[920, 1, 256]> self = ?                                                                    | Unknown  | Fallback   | True  |
| 440 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Fallback   | True  |

