### aten.clone.default
|     | ATen Input Variations                                                                             | Status   |
|----:|:--------------------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Done     |
|   1 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Done     |
|   2 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
|   3 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     |
|   4 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|   5 | Tensor<[1, 10, 768]> self = ?                                                                     | Done     |
|   6 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  |
|   7 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  |
|   8 | Tensor<[1, 1024, 160]> self = ?                                                                   | Done     |
|   9 | Tensor<[1, 1024, 2560]> self = ?                                                                  | Done     |
|  10 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  11 | Tensor<[1, 1024, 512]> self = ?                                                                   | Done     |
|  12 | Tensor<[1, 1024, 640]> self = ?                                                                   | Done     |
|  13 | Tensor<[1, 1024]> self = ?                                                                        | Done     |
|  14 | Tensor<[1, 12, 10, 10]> self = ?                                                                  | Done     |
|  15 | Tensor<[1, 12, 14, 14]> self = ?                                                                  | Done     |
|  16 | Tensor<[1, 12, 16, 16]> self = ?                                                                  | Done     |
|  17 | Tensor<[1, 12, 197, 197]> self = ?                                                                | Done     |
|  18 | Tensor<[1, 12, 201, 201]> self = ?                                                                | Unknown  |
|  19 | Tensor<[1, 12, 25, 25]> self = ?                                                                  | Done     |
|  20 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  21 | Tensor<[1, 12, 7, 7]> self = ?                                                                    | Unknown  |
|  22 | Tensor<[1, 12, 9, 9]> self = ?                                                                    | Done     |
|  23 | Tensor<[1, 1200, 1280]> self = ?                                                                  | Done     |
|  24 | Tensor<[1, 1200, 320]> self = ?                                                                   | Done     |
|  25 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  26 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  27 | Tensor<[1, 1280, 16, 16]> self = ?                                                                | Done     |
|  28 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
|  29 | Tensor<[1, 1280, 8, 8]> self = ?                                                                  | Done     |
|  30 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  31 | Tensor<[1, 1280]> self = ?                                                                        | Done     |
|  32 | Tensor<[1, 128]> self = ?                                                                         | Done     |
|  33 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
|  34 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
|  35 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Done     |
|  36 | Tensor<[1, 1370, 5120]> self = ?                                                                  | Done     |
|  37 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  38 | Tensor<[1, 14, 128]> self = ?                                                                     | Done     |
|  39 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Done     |
|  40 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Done     |
|  41 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Done     |
|  42 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Done     |
|  43 | Tensor<[1, 14, 768]> self = ?                                                                     | Done     |
|  44 | Tensor<[1, 1445, 192]> self = ?                                                                   | Done     |
|  45 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  46 | Tensor<[1, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Done     |
|  47 | Tensor<[1, 1536]> self = ?                                                                        | Done     |
|  48 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  49 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Done     |
|  50 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  51 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Done     |
|  52 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Done     |
|  53 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Done     |
|  54 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  55 | Tensor<[1, 16, 197, 197]> self = ?                                                                | Done     |
|  56 | Tensor<[1, 16, 256, 256]> self = ?                                                                | Done     |
|  57 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Done     |
|  58 | Tensor<[1, 16, 768]> self = ?                                                                     | Done     |
|  59 | Tensor<[1, 16, 9, 9]> self = ?                                                                    | Done     |
|  60 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  61 | Tensor<[1, 16384, 128]> self = ?                                                                  | Done     |
|  62 | Tensor<[1, 16384, 32]> self = ?                                                                   | Done     |
|  63 | Tensor<[1, 19, 1024]> self = ?                                                                    | Done     |
|  64 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  65 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
|  66 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     |
|  67 | Tensor<[1, 19, 4096]> self = ?                                                                    | Done     |
|  68 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Done     |
|  69 | Tensor<[1, 19200, 256]> self = ?                                                                  | Done     |
|  70 | Tensor<[1, 19200, 64]> self = ?                                                                   | Done     |
|  71 | Tensor<[1, 196, 3072]> self = ?                                                                   | Done     |
|  72 | Tensor<[1, 196, 768]> self = ?                                                                    | Done     |
|  73 | Tensor<[1, 197, 1024]> self = ?                                                                   | Done     |
|  74 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  75 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  76 | Tensor<[1, 197, 3072]> self = ?                                                                   | Done     |
|  77 | Tensor<[1, 197, 4096]> self = ?                                                                   | Done     |
|  78 | Tensor<[1, 197, 768]> self = ?                                                                    | Done     |
|  79 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
|  80 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
|  81 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  82 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  83 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  84 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  85 | Tensor<[1, 2, 4096, 256]> self = ?                                                                | Done     |
|  86 | Tensor<[1, 2, 4800, 300]> self = ?                                                                | Done     |
|  87 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  88 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  89 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  90 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
|  91 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
|  92 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     |
|  93 | Tensor<[1, 201, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
|  94 | Tensor<[1, 201, 768]> self = ?                                                                    | Unknown  |
|  95 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
|  96 | Tensor<[1, 2048]> self = ?                                                                        | Done     |
|  97 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Done     |
|  98 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Done     |
|  99 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 100 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 101 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
| 102 | Tensor<[1, 25, 768]> self = ?                                                                     | Done     |
| 103 | Tensor<[1, 256, 1024]> self = ?                                                                   | Done     |
| 104 | Tensor<[1, 256, 128, 128]> self = ?                                                               | Done     |
| 105 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Done     |
| 106 | Tensor<[1, 256, 1280]> self = ?                                                                   | Done     |
| 107 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 108 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 109 | Tensor<[1, 256, 256]> self = ?                                                                    | Done     |
| 110 | Tensor<[1, 256, 5120]> self = ?                                                                   | Done     |
| 111 | Tensor<[1, 256, 512]> self = ?                                                                    | Done     |
| 112 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 113 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 114 | Tensor<[1, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     |
| 115 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Done     |
| 116 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Done     |
| 117 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Done     |
| 118 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Done     |
| 119 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Done     |
| 120 | Tensor<[1, 3, 1445, 1445]> self = ?                                                               | Done     |
| 121 | Tensor<[1, 3, 16, 16, 85]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
| 122 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 123 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 124 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 125 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 126 | Tensor<[1, 3, 32, 32, 85]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
| 127 | Tensor<[1, 3, 64, 64, 85]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
| 128 | Tensor<[1, 300, 2048]> self = ?                                                                   | Done     |
| 129 | Tensor<[1, 300, 512]> self = ?                                                                    | Done     |
| 130 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 131 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 132 | Tensor<[1, 32, 1536]> self = ?                                                                    | Done     |
| 133 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 134 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Done     |
| 135 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Done     |
| 136 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Done     |
| 137 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Done     |
| 138 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Done     |
| 139 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Done     |
| 140 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 141 | Tensor<[1, 320, 64, 64]> self = ?                                                                 | Done     |
| 142 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 143 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 144 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     |
| 145 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 146 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 147 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 148 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 149 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 150 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 151 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 152 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 153 | Tensor<[1, 4096, 1280]> self = ?                                                                  | Done     |
| 154 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 155 | Tensor<[1, 4096, 256]> self = ?                                                                   | Done     |
| 156 | Tensor<[1, 4096, 320]> self = ?                                                                   | Done     |
| 157 | Tensor<[1, 4096, 64]> self = ?                                                                    | Done     |
| 158 | Tensor<[1, 4096]> self = ?                                                                        | Done     |
| 159 | Tensor<[1, 4800, 128]> self = ?                                                                   | Done     |
| 160 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 161 | Tensor<[1, 4800, 512]> self = ?                                                                   | Done     |
| 162 | Tensor<[1, 49, 1024]> self = ?                                                                    | Done     |
| 163 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 164 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 165 | Tensor<[1, 49, 768]> self = ?                                                                     | Done     |
| 166 | Tensor<[1, 5, 1024, 256]> self = ?                                                                | Done     |
| 167 | Tensor<[1, 5, 1200, 300]> self = ?                                                                | Done     |
| 168 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 169 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 170 | Tensor<[1, 50, 1024]> self = ?                                                                    | Done     |
| 171 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 172 | Tensor<[1, 50, 3072]> self = ?                                                                    | Done     |
| 173 | Tensor<[1, 50, 4096]> self = ?                                                                    | Done     |
| 174 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
| 175 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  |
| 176 | Tensor<[1, 50, 768]> self = ?                                                                     | Done     |
| 177 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Done     |
| 178 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 179 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Done     |
| 180 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Done     |
| 181 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Done     |
| 182 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Done     |
| 183 | Tensor<[1, 64, 1024]> self = ?                                                                    | Done     |
| 184 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Done     |
| 185 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 186 | Tensor<[1, 64, 1280]> self = ?                                                                    | Done     |
| 187 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 188 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 189 | Tensor<[1, 64, 5120]> self = ?                                                                    | Done     |
| 190 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Done     |
| 191 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Done     |
| 192 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Done     |
| 193 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 194 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Done     |
| 195 | Tensor<[1, 64, 768]> self = ?                                                                     | Done     |
| 196 | Tensor<[1, 64, 9, 9]> self = ?                                                                    | Done     |
| 197 | Tensor<[1, 640, 32, 32]> self = ?                                                                 | Done     |
| 198 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 199 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 200 | Tensor<[1, 7, 4544]> self = ?                                                                     | Unknown  |
| 201 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Done     |
| 202 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Done     |
| 203 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Done     |
| 204 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Done     |
| 205 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  |
| 206 | Tensor<[1, 7, 768]> self = ?                                                                      | Unknown  |
| 207 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  |
| 208 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  |
| 209 | Tensor<[1, 768, 196]> self = ?                                                                    | Done     |
| 210 | Tensor<[1, 768, 384]> self = ?                                                                    | Done     |
| 211 | Tensor<[1, 768]> self = ?                                                                         | Done     |
| 212 | Tensor<[1, 8, 2048, 256]> self = ?                                                                | Unknown  |
| 213 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Unknown  |
| 214 | Tensor<[1, 8, 256, 256]> self = ?                                                                 | Done     |
| 215 | Tensor<[1, 8, 300, 300]> self = ?                                                                 | Done     |
| 216 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 217 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     |
| 218 | Tensor<[1, 8, 768]> self = ?                                                                      | Done     |
| 219 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Done     |
| 220 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Done     |
| 221 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Done     |
| 222 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 223 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     |
| 224 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Done     |
| 225 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
| 226 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     |
| 227 | Tensor<[1, 9, 1024]> self = ?                                                                     | Done     |
| 228 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 229 | Tensor<[1, 9, 128]> self = ?                                                                      | Done     |
| 230 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 231 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 232 | Tensor<[1, 9, 2048]> self = ?                                                                     | Done     |
| 233 | Tensor<[1, 9, 4096]> self = ?                                                                     | Done     |
| 234 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 235 | Tensor<[1, 9, 768]> self = ?                                                                      | Done     |
| 236 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     |
| 237 | Tensor<[100, 1, 2048]> self = ?                                                                   | Unknown  |
| 238 | Tensor<[100, 1, 256]> self = ?                                                                    | Unknown  |
| 239 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  |
| 240 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  |
| 241 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 242 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 243 | Tensor<[12, 50, 50]> self = ?                                                                     | Done     |
| 244 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 245 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  |
| 246 | Tensor<[16, 19, 19]> self = ?                                                                     | Done     |
| 247 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     |
| 248 | Tensor<[16, 49, 192]> self = ?                                                                    | Done     |
| 249 | Tensor<[16, 49, 256]> self = ?                                                                    | Done     |
| 250 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 251 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 252 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 253 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 254 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 255 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 256 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Done     |
| 257 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 258 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Done     |
| 259 | Tensor<[16, 64, 192]> self = ?                                                                    | Done     |
| 260 | Tensor<[16, 64, 256]> self = ?                                                                    | Done     |
| 261 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 262 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 263 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 264 | Tensor<[16, 7, 7]> self = ?                                                                       | Done     |
| 265 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 266 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 267 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 268 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Done     |
| 269 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 270 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Done     |
| 271 | Tensor<[19, 19]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     |
| 272 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 273 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 274 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Done     |
| 275 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     |
| 276 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     |
| 277 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     |
| 278 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 279 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 280 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  |
| 281 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     |
| 282 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     |
| 283 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 284 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Done     |
| 285 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 286 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     |
| 287 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 288 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 289 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 290 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 291 | Tensor<[38, 38]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     |
| 292 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 293 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 294 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 295 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Done     |
| 296 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 297 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Done     |
| 298 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 299 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 300 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 301 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Done     |
| 302 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 303 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Done     |
| 304 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 305 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 306 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 307 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 308 | Tensor<[4, 49, 384]> self = ?                                                                     | Done     |
| 309 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 310 | Tensor<[4, 49, 512]> self = ?                                                                     | Done     |
| 311 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 312 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 313 | Tensor<[4, 64, 384]> self = ?                                                                     | Done     |
| 314 | Tensor<[4, 64, 512]> self = ?                                                                     | Done     |
| 315 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 316 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Done     |
| 317 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  |
| 318 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 319 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 320 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 321 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 322 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 323 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Done     |
| 324 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 325 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Done     |
| 326 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 327 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 328 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 329 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Done     |
| 330 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 331 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Done     |
| 332 | Tensor<[64, 49, 128]> self = ?                                                                    | Done     |
| 333 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 334 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 335 | Tensor<[64, 49, 96]> self = ?                                                                     | Done     |
| 336 | Tensor<[64, 64, 128]> self = ?                                                                    | Done     |
| 337 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 338 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     |
| 339 | Tensor<[64, 64, 96]> self = ?                                                                     | Done     |
| 340 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  |
| 341 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 342 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     |
| 343 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 344 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     |
| 345 | Tensor<[920, 1, 2048]> self = ?                                                                   | Unknown  |
| 346 | Tensor<[920, 1, 256]> self = ?                                                                    | Unknown  |
| 347 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  |

