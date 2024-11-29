### aten.clone.default
|     | ATen Input Variations                                                                             | Status   | Isolated   | PCC   |
|----:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
|   1 | Tensor<[1, 1, 1024]> self = ?                                                                     | Unknown  | Done       | True  |
|   2 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Done     | Done       | True  |
|   3 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Done     | Done       | True  |
|   4 | Tensor<[1, 1, 2048]> self = ?                                                                     | Unknown  | Done       | True  |
|   5 | Tensor<[1, 1, 3072]> self = ?                                                                     | Done     | Done       | True  |
|   6 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
|   7 | Tensor<[1, 1, 4096]> self = ?                                                                     | Unknown  | Done       | True  |
|   8 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       | True  |
|   9 | Tensor<[1, 1, 512]> self = ?                                                                      | Unknown  | Done       | True  |
|  10 | Tensor<[1, 1, 768]> self = ?                                                                      | Done     | Done       | True  |
|  11 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
|  12 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
|  13 | Tensor<[1, 10, 1024]> self = ?                                                                    | Done     | Done       | True  |
|  14 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  15 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  16 | Tensor<[1, 10, 2048]> self = ?                                                                    | Done     | Done       | True  |
|  17 | Tensor<[1, 10, 3072]> self = ?                                                                    | Done     | Done       | True  |
|  18 | Tensor<[1, 10, 4096]> self = ?                                                                    | Done     | Done       | True  |
|  19 | Tensor<[1, 10, 512]> self = ?                                                                     | Done     | Done       | True  |
|  20 | Tensor<[1, 10, 768]> self = ?                                                                     | Done     | Done       | True  |
|  21 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
|  22 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | Done       | True  |
|  23 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       | True  |
|  24 | Tensor<[1, 1024, 160]> self = ?                                                                   | Done     | Done       | True  |
|  25 | Tensor<[1, 1024, 2560]> self = ?                                                                  | Unknown  | Done       | True  |
|  26 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
|  27 | Tensor<[1, 1024, 512]> self = ?                                                                   | Done     | Done       | True  |
|  28 | Tensor<[1, 1024, 640]> self = ?                                                                   | Done     | Done       | True  |
|  29 | Tensor<[1, 1024]> self = ?                                                                        | Done     | Done       | True  |
|  30 | Tensor<[1, 112, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
|  31 | Tensor<[1, 12, 1, 10]> self = ?                                                                   | Unknown  | Done       | True  |
|  32 | Tensor<[1, 12, 1, 1]> self = ?                                                                    | Unknown  | Done       | True  |
|  33 | Tensor<[1, 12, 1, 2]> self = ?                                                                    | Unknown  | Done       | True  |
|  34 | Tensor<[1, 12, 1, 46]> self = ?                                                                   | Unknown  | Done       | True  |
|  35 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   |
|  36 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   |
|  37 | Tensor<[1, 12, 10, 10]> self = ?                                                                  | Done     | Done       | True  |
|  38 | Tensor<[1, 12, 12, 12]> self = ?                                                                  | Done     | Done       | True  |
|  39 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  40 | Tensor<[1, 12, 128]> self = ?                                                                     | Done     | Done       | True  |
|  41 | Tensor<[1, 12, 14, 14]> self = ?                                                                  | Done     | Done       | True  |
|  42 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
|  43 | Tensor<[1, 12, 16, 16]> self = ?                                                                  | Done     | Done       | True  |
|  44 | Tensor<[1, 12, 197, 197]> self = ?                                                                | Done     | Done       | True  |
|  45 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  46 | Tensor<[1, 12, 25, 25]> self = ?                                                                  | Done     | Done       | True  |
|  47 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | True  |
|  48 | Tensor<[1, 12, 45, 45]> self = ?                                                                  | Unknown  | Done       | True  |
|  49 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  50 | Tensor<[1, 12, 7, 7]> self = ?                                                                    | Done     | Done       | True  |
|  51 | Tensor<[1, 12, 768]> self = ?                                                                     | Done     | Done       | True  |
|  52 | Tensor<[1, 12, 9, 9]> self = ?                                                                    | Done     | Done       | True  |
|  53 | Tensor<[1, 1200, 1280]> self = ?                                                                  | Done     | Done       | True  |
|  54 | Tensor<[1, 1200, 320]> self = ?                                                                   | Done     | Done       | True  |
|  55 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
|  56 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
|  57 | Tensor<[1, 1280, 16, 16]> self = ?                                                                | Unknown  | Done       | True  |
|  58 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
|  59 | Tensor<[1, 1280, 8, 8]> self = ?                                                                  | Unknown  | Done       | True  |
|  60 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
|  61 | Tensor<[1, 1280]> self = ?                                                                        | Done     | Done       | True  |
|  62 | Tensor<[1, 128]> self = ?                                                                         | Done     | Done       | True  |
|  63 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
|  64 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
|  65 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Done     | Done       | True  |
|  66 | Tensor<[1, 1370, 5120]> self = ?                                                                  | Done     | Done       | True  |
|  67 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  68 | Tensor<[1, 14, 128]> self = ?                                                                     | Done     | Done       | True  |
|  69 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Done     | Done       | True  |
|  70 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Done     | Done       | True  |
|  71 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Done     | Done       | True  |
|  72 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Done     | Done       | True  |
|  73 | Tensor<[1, 14, 768]> self = ?                                                                     | Done     | Done       | True  |
|  74 | Tensor<[1, 1445, 192]> self = ?                                                                   | Done     | Done       | True  |
|  75 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
|  76 | Tensor<[1, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Done     | Done       | True  |
|  77 | Tensor<[1, 15, 1024]> self = ?                                                                    | Done     | Done       | True  |
|  78 | Tensor<[1, 15, 512]> self = ?                                                                     | Done     | Done       | True  |
|  79 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
|  80 | Tensor<[1, 1500, 3072]> self = ?                                                                  | Done     | Done       | True  |
|  81 | Tensor<[1, 1500, 768]> self = ?                                                                   | Done     | Done       | True  |
|  82 | Tensor<[1, 1536]> self = ?                                                                        | Done     | Done       | True  |
|  83 | Tensor<[1, 16, 1, 10]> self = ?                                                                   | Unknown  | Done       | True  |
|  84 | Tensor<[1, 16, 1, 1]> self = ?                                                                    | Unknown  | Done       | True  |
|  85 | Tensor<[1, 16, 1, 2]> self = ?                                                                    | Unknown  | Done       | True  |
|  86 | Tensor<[1, 16, 1, 6]> self = ?                                                                    | Unknown  | Done       | True  |
|  87 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   |
|  88 | Tensor<[1, 16, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   |
|  89 | Tensor<[1, 16, 10, 10]> self = ?                                                                  | Done     | Done       | True  |
|  90 | Tensor<[1, 16, 112, 112]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
|  91 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  92 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Done     | Done       | True  |
|  93 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  94 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Done     | Done       | True  |
|  95 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Done     | Done       | True  |
|  96 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Done     | Done       | True  |
|  97 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
|  98 | Tensor<[1, 16, 197, 197]> self = ?                                                                | Done     | Done       | True  |
|  99 | Tensor<[1, 16, 256, 256]> self = ?                                                                | Done     | Done       | True  |
| 100 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Done     | Done       | True  |
| 101 | Tensor<[1, 16, 5, 5]> self = ?                                                                    | Unknown  | Done       | True  |
| 102 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 103 | Tensor<[1, 16, 768]> self = ?                                                                     | Done     | Done       | True  |
| 104 | Tensor<[1, 16, 9, 9]> self = ?                                                                    | Done     | Done       | True  |
| 105 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 106 | Tensor<[1, 160, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 107 | Tensor<[1, 16384, 128]> self = ?                                                                  | Done     | Done       | True  |
| 108 | Tensor<[1, 16384, 32]> self = ?                                                                   | Done     | Done       | True  |
| 109 | Tensor<[1, 19, 1024]> self = ?                                                                    | Done     | Done       | True  |
| 110 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 111 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
| 112 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
| 113 | Tensor<[1, 19, 4096]> self = ?                                                                    | Done     | Done       | True  |
| 114 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Done     | Done       | True  |
| 115 | Tensor<[1, 19200, 256]> self = ?                                                                  | Done     | Done       | True  |
| 116 | Tensor<[1, 19200, 64]> self = ?                                                                   | Done     | Done       | True  |
| 117 | Tensor<[1, 196, 3072]> self = ?                                                                   | Done     | Done       | True  |
| 118 | Tensor<[1, 196, 768]> self = ?                                                                    | Done     | Done       | True  |
| 119 | Tensor<[1, 197, 1024]> self = ?                                                                   | Done     | Done       | True  |
| 120 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 121 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 122 | Tensor<[1, 197, 3072]> self = ?                                                                   | Done     | Done       | True  |
| 123 | Tensor<[1, 197, 4096]> self = ?                                                                   | Done     | Done       | True  |
| 124 | Tensor<[1, 197, 768]> self = ?                                                                    | Done     | Done       | True  |
| 125 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 126 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 127 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 128 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 129 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 130 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 131 | Tensor<[1, 2, 4096, 256]> self = ?                                                                | Done     | Done       | True  |
| 132 | Tensor<[1, 2, 4800, 300]> self = ?                                                                | Done     | Done       | True  |
| 133 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 134 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 135 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 136 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 137 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
| 138 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
| 139 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 140 | Tensor<[1, 2048]> self = ?                                                                        | Done     | Done       | True  |
| 141 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 142 | Tensor<[1, 24, 3072]> self = ?                                                                    | Done     | Done       | True  |
| 143 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 144 | Tensor<[1, 24, 56, 56]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 145 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 146 | Tensor<[1, 24, 768]> self = ?                                                                     | Done     | Done       | True  |
| 147 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 148 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
| 149 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
| 150 | Tensor<[1, 25, 768]> self = ?                                                                     | Done     | Done       | True  |
| 151 | Tensor<[1, 256, 1024]> self = ?                                                                   | Done     | Done       | True  |
| 152 | Tensor<[1, 256, 128, 128]> self = ?                                                               | Done     | Done       | True  |
| 153 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Done     | Done       | True  |
| 154 | Tensor<[1, 256, 1280]> self = ?                                                                   | Unknown  | Done       | True  |
| 155 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 156 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 157 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 158 | Tensor<[1, 256, 256]> self = ?                                                                    | Done     | Done       | True  |
| 159 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 160 | Tensor<[1, 256, 5120]> self = ?                                                                   | Unknown  | Done       | True  |
| 161 | Tensor<[1, 256, 512]> self = ?                                                                    | Done     | Done       | True  |
| 162 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 163 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 164 | Tensor<[1, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     | Done       | True  |
| 165 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Done     | Done       | True  |
| 166 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Done     | Done       | True  |
| 167 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Done     | Done       | True  |
| 168 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Done     | Done       | True  |
| 169 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Done     | Done       | True  |
| 170 | Tensor<[1, 3, 1445, 1445]> self = ?                                                               | Done     | Done       | True  |
| 171 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
| 172 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 173 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 174 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 175 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 176 | Tensor<[1, 300, 2048]> self = ?                                                                   | Done     | Done       | True  |
| 177 | Tensor<[1, 300, 512]> self = ?                                                                    | Done     | Done       | True  |
| 178 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 179 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 180 | Tensor<[1, 32, 1536]> self = ?                                                                    | Done     | Done       | True  |
| 181 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 182 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Done     | Done       | True  |
| 183 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Done     | Done       | True  |
| 184 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Done     | Done       | True  |
| 185 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Done     | Done       | True  |
| 186 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 187 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 188 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 189 | Tensor<[1, 320, 64, 64]> self = ?                                                                 | Unknown  | Done       | True  |
| 190 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 191 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
| 192 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
| 193 | Tensor<[1, 4, 3072]> self = ?                                                                     | Unknown  | Done       | True  |
| 194 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 195 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 196 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 197 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 198 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 199 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 200 | Tensor<[1, 4, 768]> self = ?                                                                      | Unknown  | Done       | True  |
| 201 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 202 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 203 | Tensor<[1, 40, 28, 28]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 204 | Tensor<[1, 4096, 1280]> self = ?                                                                  | Unknown  | Done       | True  |
| 205 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 206 | Tensor<[1, 4096, 256]> self = ?                                                                   | Done     | Done       | True  |
| 207 | Tensor<[1, 4096, 320]> self = ?                                                                   | Unknown  | Done       | True  |
| 208 | Tensor<[1, 4096, 64]> self = ?                                                                    | Done     | Done       | True  |
| 209 | Tensor<[1, 4096]> self = ?                                                                        | Done     | Done       | True  |
| 210 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 211 | Tensor<[1, 45, 768]> self = ?                                                                     | Unknown  | Done       | True  |
| 212 | Tensor<[1, 4800, 128]> self = ?                                                                   | Done     | Done       | True  |
| 213 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 214 | Tensor<[1, 4800, 512]> self = ?                                                                   | Done     | Done       | True  |
| 215 | Tensor<[1, 49, 1024]> self = ?                                                                    | Done     | Done       | True  |
| 216 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 217 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 218 | Tensor<[1, 49, 768]> self = ?                                                                     | Done     | Done       | True  |
| 219 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 220 | Tensor<[1, 5, 1024, 256]> self = ?                                                                | Done     | Done       | True  |
| 221 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  | Done       | True  |
| 222 | Tensor<[1, 5, 1200, 300]> self = ?                                                                | Done     | Done       | True  |
| 223 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | True  |
| 224 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 225 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 226 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 227 | Tensor<[1, 50, 1024]> self = ?                                                                    | Done     | Done       | True  |
| 228 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 229 | Tensor<[1, 50, 3072]> self = ?                                                                    | Done     | Done       | True  |
| 230 | Tensor<[1, 50, 4096]> self = ?                                                                    | Done     | Done       | True  |
| 231 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | True  |
| 232 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
| 233 | Tensor<[1, 50, 768]> self = ?                                                                     | Done     | Done       | True  |
| 234 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Done     | Done       | True  |
| 235 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 236 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Done     | Done       | True  |
| 237 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Done     | Done       | True  |
| 238 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Done     | Done       | True  |
| 239 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Done     | Done       | True  |
| 240 | Tensor<[1, 59, 1024]> self = ?                                                                    | Unknown  | Done       | True  |
| 241 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 242 | Tensor<[1, 6, 1, 15]> self = ?                                                                    | Unknown  | Done       | True  |
| 243 | Tensor<[1, 6, 1, 17]> self = ?                                                                    | Unknown  | Done       | True  |
| 244 | Tensor<[1, 6, 1, 1]> self = ?                                                                     | Unknown  | Done       | True  |
| 245 | Tensor<[1, 6, 1, 2]> self = ?                                                                     | Unknown  | Done       | True  |
| 246 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   |
| 247 | Tensor<[1, 6, 15, 15]> self = ?                                                                   | Done     | Done       | True  |
| 248 | Tensor<[1, 64, 1024]> self = ?                                                                    | Done     | Done       | True  |
| 249 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Done     | Done       | True  |
| 250 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 251 | Tensor<[1, 64, 1280]> self = ?                                                                    | Unknown  | Done       | True  |
| 252 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 253 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 254 | Tensor<[1, 64, 5120]> self = ?                                                                    | Unknown  | Done       | True  |
| 255 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Done     | Done       | True  |
| 256 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Done     | Done       | True  |
| 257 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Done     | Done       | True  |
| 258 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 259 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Done     | Done       | True  |
| 260 | Tensor<[1, 64, 768]> self = ?                                                                     | Done     | Done       | True  |
| 261 | Tensor<[1, 64, 9, 9]> self = ?                                                                    | Done     | Done       | True  |
| 262 | Tensor<[1, 640, 32, 32]> self = ?                                                                 | Unknown  | Done       | True  |
| 263 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 264 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 265 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Done     | Done       | True  |
| 266 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Done     | Done       | True  |
| 267 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Done     | Done       | True  |
| 268 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Done     | Done       | True  |
| 269 | Tensor<[1, 7, 768]> self = ?                                                                      | Done     | Done       | True  |
| 270 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | True  |
| 271 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | True  |
| 272 | Tensor<[1, 768, 196]> self = ?                                                                    | Done     | Done       | True  |
| 273 | Tensor<[1, 768, 384]> self = ?                                                                    | Done     | Done       | True  |
| 274 | Tensor<[1, 768]> self = ?                                                                         | Done     | Done       | True  |
| 275 | Tensor<[1, 8, 1, 10]> self = ?                                                                    | Unknown  | Done       | True  |
| 276 | Tensor<[1, 8, 1, 1]> self = ?                                                                     | Unknown  | Done       | True  |
| 277 | Tensor<[1, 8, 1, 2]> self = ?                                                                     | Unknown  | Done       | True  |
| 278 | Tensor<[1, 8, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   |
| 279 | Tensor<[1, 8, 10, 10]> self = ?                                                                   | Done     | Done       | True  |
| 280 | Tensor<[1, 8, 2048, 256]> self = ?                                                                | Done     | Done       | True  |
| 281 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Done     | Done       | True  |
| 282 | Tensor<[1, 8, 256, 256]> self = ?                                                                 | Done     | Done       | True  |
| 283 | Tensor<[1, 8, 300, 300]> self = ?                                                                 | Done     | Done       | True  |
| 284 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 285 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | Done       | True  |
| 286 | Tensor<[1, 8, 768]> self = ?                                                                      | Done     | Done       | True  |
| 287 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Done     | Done       | True  |
| 288 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Done     | Done       | True  |
| 289 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Done     | Done       | True  |
| 290 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 291 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | Done       | True  |
| 292 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Done     | Done       | True  |
| 293 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 294 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | Done       | True  |
| 295 | Tensor<[1, 80, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 296 | Tensor<[1, 9, 1024]> self = ?                                                                     | Done     | Done       | True  |
| 297 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 298 | Tensor<[1, 9, 128]> self = ?                                                                      | Done     | Done       | True  |
| 299 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 300 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 301 | Tensor<[1, 9, 2048]> self = ?                                                                     | Done     | Done       | True  |
| 302 | Tensor<[1, 9, 4096]> self = ?                                                                     | Done     | Done       | True  |
| 303 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 304 | Tensor<[1, 9, 768]> self = ?                                                                      | Done     | Done       | True  |
| 305 | Tensor<[1, s10 + 1]> self = ?                                                                     | Unknown  | Unknown    | N/A   |
| 306 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 307 | Tensor<[100, 1, 2048]> self = ?                                                                   | Done     | Done       | True  |
| 308 | Tensor<[100, 1, 256]> self = ?                                                                    | Done     | Done       | True  |
| 309 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       | True  |
| 310 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 311 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 312 | Tensor<[12, 24, 24]> self = ?                                                                     | Done     | Done       | True  |
| 313 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 314 | Tensor<[12, 50, 50]> self = ?                                                                     | Done     | Done       | True  |
| 315 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 316 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 317 | Tensor<[16, 1, 60]> self = ?                                                                      | Unknown  | Done       | True  |
| 318 | Tensor<[16, 1, s10 + 1]> self = ?                                                                 | Unknown  | Unknown    | N/A   |
| 319 | Tensor<[16, 19, 19]> self = ?                                                                     | Done     | Done       | True  |
| 320 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
| 321 | Tensor<[16, 49, 192]> self = ?                                                                    | Done     | Done       | True  |
| 322 | Tensor<[16, 49, 256]> self = ?                                                                    | Done     | Done       | True  |
| 323 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 324 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 325 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 326 | Tensor<[16, 59, 59]> self = ?                                                                     | Unknown  | Done       | True  |
| 327 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 328 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 329 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 330 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 331 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 332 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 333 | Tensor<[16, 64, 192]> self = ?                                                                    | Done     | Done       | True  |
| 334 | Tensor<[16, 64, 256]> self = ?                                                                    | Done     | Done       | True  |
| 335 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 336 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 337 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 338 | Tensor<[16, 7, 7]> self = ?                                                                       | Done     | Done       | True  |
| 339 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 340 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 341 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 342 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 343 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 344 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 345 | Tensor<[19, 19]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 346 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 347 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 348 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Done       | True  |
| 349 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Unknown  | Done       | True  |
| 350 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       | True  |
| 351 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | Done       | True  |
| 352 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 353 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 354 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 355 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 356 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | Done       | True  |
| 357 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | Done       | True  |
| 358 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 359 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Done       | True  |
| 360 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 361 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | Done       | True  |
| 362 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 363 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 364 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 365 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 366 | Tensor<[38, 38]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 367 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 368 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 369 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 370 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 371 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 372 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 373 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 374 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 375 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 376 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 377 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 378 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 379 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 380 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 381 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 382 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 383 | Tensor<[4, 49, 384]> self = ?                                                                     | Done     | Done       | True  |
| 384 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 385 | Tensor<[4, 49, 512]> self = ?                                                                     | Done     | Done       | True  |
| 386 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 387 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 388 | Tensor<[4, 64, 384]> self = ?                                                                     | Done     | Done       | True  |
| 389 | Tensor<[4, 64, 512]> self = ?                                                                     | Done     | Done       | True  |
| 390 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 391 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Done       | True  |
| 392 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | True  |
| 393 | Tensor<[59, 1024]> self = ?                                                                       | Unknown  | Done       | True  |
| 394 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 395 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 396 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 397 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 398 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 399 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 400 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 401 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 402 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 403 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 404 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 405 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Done     | Done       | True  |
| 406 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 407 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Done     | Done       | True  |
| 408 | Tensor<[64, 49, 128]> self = ?                                                                    | Done     | Done       | True  |
| 409 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 410 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 411 | Tensor<[64, 49, 96]> self = ?                                                                     | Done     | Done       | True  |
| 412 | Tensor<[64, 64, 128]> self = ?                                                                    | Done     | Done       | True  |
| 413 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 414 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | Done       | True  |
| 415 | Tensor<[64, 64, 96]> self = ?                                                                     | Done     | Done       | True  |
| 416 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | Done       | True  |
| 417 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 418 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | Done       | True  |
| 419 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 420 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |
| 421 | Tensor<[920, 1, 2048]> self = ?                                                                   | Done     | Done       | True  |
| 422 | Tensor<[920, 1, 256]> self = ?                                                                    | Done     | Done       | True  |
| 423 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | Done       | True  |

