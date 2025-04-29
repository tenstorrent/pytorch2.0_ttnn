### aten.clone.default
|     | ATen Input Variations                                                                             | Status   | Isolated   | PCC   | Host   |
|----:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
|   1 | Tensor<[1, 1, 1024]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
|   2 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Removed  | Done       | 1.0   | -1     |
|   3 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Unknown  | Done       | 1.0   | -1     |
|   4 | Tensor<[1, 1, 2048]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
|   5 | Tensor<[1, 1, 3072]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
|   6 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
|   7 | Tensor<[1, 1, 4096]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
|   8 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | Done       | 1.0   | -1     |
|   9 | Tensor<[1, 1, 512]> self = ?                                                                      | Unknown  | Done       | 1.0   | -1     |
|  10 | Tensor<[1, 1, 768]> self = ?                                                                      | Unknown  | Done       | 1.0   | -1     |
|  11 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | -1     |
|  12 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | -1     |
|  13 | Tensor<[1, 10, 1024]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  14 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  15 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | -1     |
|  16 | Tensor<[1, 10, 2048]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  17 | Tensor<[1, 10, 3072]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  18 | Tensor<[1, 10, 4096]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  19 | Tensor<[1, 10, 512]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
|  20 | Tensor<[1, 10, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
|  21 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | -1     |
|  22 | Tensor<[1, 1024, 160]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
|  23 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
|  24 | Tensor<[1, 1024, 512]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
|  25 | Tensor<[1, 1024, 640]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
|  26 | Tensor<[1, 1024]> self = ?                                                                        | Removed  | Done       | 1.0   | -1     |
|  27 | Tensor<[1, 112, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
|  28 | Tensor<[1, 12, 1, 10]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
|  29 | Tensor<[1, 12, 1, 1]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  30 | Tensor<[1, 12, 1, 2]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  31 | Tensor<[1, 12, 1, 46]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
|  32 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  33 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  34 | Tensor<[1, 12, 10, 10]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  35 | Tensor<[1, 12, 12, 12]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  36 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  37 | Tensor<[1, 12, 128]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
|  38 | Tensor<[1, 12, 14, 14]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  39 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | 1.0   | -1     |
|  40 | Tensor<[1, 12, 16, 16]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  41 | Tensor<[1, 12, 197, 197]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
|  42 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  43 | Tensor<[1, 12, 25, 25]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  44 | Tensor<[1, 12, 257, 257]> self = ?                                                                | Removed  | Unknown    | N/A   | N/A    |
|  45 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | -1     |
|  46 | Tensor<[1, 12, 45, 45]> self = ?                                                                  | Unknown  | Done       | 1.0   | -1     |
|  47 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  48 | Tensor<[1, 12, 7, 7]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
|  49 | Tensor<[1, 12, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
|  50 | Tensor<[1, 12, 9, 9]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
|  51 | Tensor<[1, 1200, 1280]> self = ?                                                                  | Unknown  | Done       | 1.0   | -1     |
|  52 | Tensor<[1, 1200, 320]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
|  53 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
|  54 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
|  55 | Tensor<[1, 1280]> self = ?                                                                        | Removed  | Done       | 1.0   | -1     |
|  56 | Tensor<[1, 128]> self = ?                                                                         | Removed  | Done       | 1.0   | -1     |
|  57 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  58 | Tensor<[1, 1370, 5120]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  59 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  60 | Tensor<[1, 14, 128]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
|  61 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
|  62 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Removed  | Unknown    | N/A   | N/A    |
|  63 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
|  64 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
|  65 | Tensor<[1, 14, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
|  66 | Tensor<[1, 1445, 192]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
|  67 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
|  68 | Tensor<[1, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Removed  | Done       | 1.0   | -1     |
|  69 | Tensor<[1, 15, 1024]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  70 | Tensor<[1, 15, 512]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
|  71 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | -1     |
|  72 | Tensor<[1, 1500, 3072]> self = ?                                                                  | Unknown  | Done       | 1.0   | -1     |
|  73 | Tensor<[1, 1500, 768]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
|  74 | Tensor<[1, 1536]> self = ?                                                                        | Unknown  | Done       | 1.0   | -1     |
|  75 | Tensor<[1, 16, 1, 10]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
|  76 | Tensor<[1, 16, 1, 1]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  77 | Tensor<[1, 16, 1, 2]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  78 | Tensor<[1, 16, 1, 6]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  79 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                               | Unknown  | Unknown    | N/A   | N/A    |
|  80 | Tensor<[1, 16, 1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  81 | Tensor<[1, 16, 10, 10]> self = ?                                                                  | Unknown  | Done       | 1.0   | -1     |
|  82 | Tensor<[1, 16, 112, 112]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | -1     |
|  83 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  84 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
|  85 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | -1     |
|  86 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
|  87 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
|  88 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
|  89 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
|  90 | Tensor<[1, 16, 256, 256]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
|  91 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  92 | Tensor<[1, 16, 5, 5]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
|  93 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | -1     |
|  94 | Tensor<[1, 16, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
|  95 | Tensor<[1, 16, 9, 9]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
|  96 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
|  97 | Tensor<[1, 160, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | -1     |
|  98 | Tensor<[1, 16384, 128]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
|  99 | Tensor<[1, 16384, 32]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 100 | Tensor<[1, 18]> self = ?                                                                          | Removed  | Unknown    | N/A   | N/A    |
| 101 | Tensor<[1, 19, 1024]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 102 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 103 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | 1.0   | -1     |
| 104 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | 1.0   | -1     |
| 105 | Tensor<[1, 19, 4096]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 106 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Removed  | Done       | 1.0   | -1     |
| 107 | Tensor<[1, 19200, 256]> self = ?                                                                  | Unknown  | Done       | 1.0   | -1     |
| 108 | Tensor<[1, 19200, 64]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 109 | Tensor<[1, 196, 3072]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 110 | Tensor<[1, 196, 768]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 111 | Tensor<[1, 197, 1024]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 112 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 113 | Tensor<[1, 197, 3072]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 114 | Tensor<[1, 197, 4096]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 115 | Tensor<[1, 197, 768]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 116 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 117 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 118 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 119 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 120 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 121 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 122 | Tensor<[1, 2, 4096, 256]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
| 123 | Tensor<[1, 2, 4800, 300]> self = ?                                                                | Unknown  | Done       | 1.0   | -1     |
| 124 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 125 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 126 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 127 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 128 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | -1     |
| 129 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | -1     |
| 130 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 131 | Tensor<[1, 2048]> self = ?                                                                        | Removed  | Done       | 1.0   | -1     |
| 132 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 133 | Tensor<[1, 24, 3072]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 134 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 135 | Tensor<[1, 24, 56, 56]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 136 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 137 | Tensor<[1, 24, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 138 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 139 | Tensor<[1, 25, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 140 | Tensor<[1, 256, 1024]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 141 | Tensor<[1, 256, 128, 128]> self = ?                                                               | Removed  | Done       | 1.0   | -1     |
| 142 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Removed  | Done       | 1.0   | -1     |
| 143 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 144 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 145 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 146 | Tensor<[1, 256, 256]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 147 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 148 | Tensor<[1, 256, 512]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 149 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 150 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 151 | Tensor<[1, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | -1     |
| 152 | Tensor<[1, 257, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Unknown    | N/A   | N/A    |
| 153 | Tensor<[1, 257, 768]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 154 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Removed  | Done       | 1.0   | -1     |
| 155 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Removed  | Unknown    | N/A   | N/A    |
| 156 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 157 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
| 158 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 159 | Tensor<[1, 3, 1445, 1445]> self = ?                                                               | Removed  | Done       | 1.0   | -1     |
| 160 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | -1     |
| 161 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | -1     |
| 162 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
| 163 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 164 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 165 | Tensor<[1, 300, 2048]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 166 | Tensor<[1, 300, 512]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 167 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | -1     |
| 168 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | -1     |
| 169 | Tensor<[1, 32, 1536]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 170 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 171 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
| 172 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 173 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 174 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 175 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 176 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 177 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
| 178 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | 1.0   | -1     |
| 179 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | 1.0   | -1     |
| 180 | Tensor<[1, 4, 3072]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 181 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 182 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 183 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 184 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 185 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 186 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 187 | Tensor<[1, 4, 768]> self = ?                                                                      | Unknown  | Done       | 1.0   | -1     |
| 188 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 189 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       | 1.0   | -1     |
| 190 | Tensor<[1, 40, 28, 28]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 191 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 192 | Tensor<[1, 4096, 256]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 193 | Tensor<[1, 4096, 64]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 194 | Tensor<[1, 4096]> self = ?                                                                        | Removed  | Done       | 1.0   | -1     |
| 195 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | -1     |
| 196 | Tensor<[1, 45, 768]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 197 | Tensor<[1, 4800, 128]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 198 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
| 199 | Tensor<[1, 4800, 512]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 200 | Tensor<[1, 49, 1024]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 201 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 202 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 203 | Tensor<[1, 49, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 204 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
| 205 | Tensor<[1, 5, 1024, 256]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
| 206 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 207 | Tensor<[1, 5, 1200, 300]> self = ?                                                                | Unknown  | Done       | 1.0   | -1     |
| 208 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Done       | 1.0   | -1     |
| 209 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
| 210 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 211 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 212 | Tensor<[1, 50, 1024]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 213 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 214 | Tensor<[1, 50, 3072]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 215 | Tensor<[1, 50, 4096]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 216 | Tensor<[1, 50, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 217 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 218 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | Done       | 1.0   | -1     |
| 219 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
| 220 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 221 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Removed  | Unknown    | N/A   | N/A    |
| 222 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 223 | Tensor<[1, 59, 1024]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 224 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | Done       | 1.0   | -1     |
| 225 | Tensor<[1, 6, 1, 15]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 226 | Tensor<[1, 6, 1, 17]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 227 | Tensor<[1, 6, 1, 1]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 228 | Tensor<[1, 6, 1, 2]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 229 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   | N/A    |
| 230 | Tensor<[1, 6, 15, 15]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 231 | Tensor<[1, 64, 1024]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 232 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 233 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | 1.0   | -1     |
| 234 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 235 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 236 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 237 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 238 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 239 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 240 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 241 | Tensor<[1, 64, 768]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 242 | Tensor<[1, 64, 9, 9]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 243 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | -1     |
| 244 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 245 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 246 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 247 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 248 | Tensor<[1, 7, 768]> self = ?                                                                      | Removed  | Done       | 1.0   | -1     |
| 249 | Tensor<[1, 768, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Removed  | Unknown    | N/A   | N/A    |
| 250 | Tensor<[1, 768, 196]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 251 | Tensor<[1, 768, 384]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 252 | Tensor<[1, 768]> self = ?                                                                         | Removed  | Done       | 1.0   | -1     |
| 253 | Tensor<[1, 8, 1, 10]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 254 | Tensor<[1, 8, 1, 1]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 255 | Tensor<[1, 8, 1, 2]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 256 | Tensor<[1, 8, 1, s0 + 1]> self = ?                                                                | Unknown  | Unknown    | N/A   | N/A    |
| 257 | Tensor<[1, 8, 10, 10]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 258 | Tensor<[1, 8, 2048, 256]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
| 259 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Removed  | Done       | 1.0   | -1     |
| 260 | Tensor<[1, 8, 256, 256]> self = ?                                                                 | Removed  | Done       | 1.0   | -1     |
| 261 | Tensor<[1, 8, 300, 300]> self = ?                                                                 | Unknown  | Done       | 1.0   | -1     |
| 262 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 263 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       | 1.0   | -1     |
| 264 | Tensor<[1, 8, 768]> self = ?                                                                      | Removed  | Done       | 1.0   | -1     |
| 265 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 266 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 267 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 268 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 269 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       | 1.0   | -1     |
| 270 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Removed  | Done       | 1.0   | -1     |
| 271 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Unknown    | N/A   | N/A    |
| 272 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Removed  | Done       | 1.0   | -1     |
| 273 | Tensor<[1, 80, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 274 | Tensor<[1, 9, 1024]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 275 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | -1     |
| 276 | Tensor<[1, 9, 128]> self = ?                                                                      | Removed  | Done       | 1.0   | -1     |
| 277 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 278 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | -1     |
| 279 | Tensor<[1, 9, 2048]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 280 | Tensor<[1, 9, 4096]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 281 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       | 1.0   | -1     |
| 282 | Tensor<[1, 9, 768]> self = ?                                                                      | Removed  | Done       | 1.0   | -1     |
| 283 | Tensor<[1, s10 + 1]> self = ?                                                                     | Unknown  | Unknown    | N/A   | N/A    |
| 284 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | -1     |
| 285 | Tensor<[100, 1, 2048]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 286 | Tensor<[100, 1, 256]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 287 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Done       | 1.0   | -1     |
| 288 | Tensor<[12, 24, 24]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 289 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 290 | Tensor<[12, 50, 50]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 291 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 292 | Tensor<[16, 1, 60]> self = ?                                                                      | Unknown  | Done       | 1.0   | -1     |
| 293 | Tensor<[16, 1, s10 + 1]> self = ?                                                                 | Unknown  | Unknown    | N/A   | N/A    |
| 294 | Tensor<[16, 19, 19]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 295 | Tensor<[16, 49, 192]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 296 | Tensor<[16, 49, 256]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 297 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Unknown    | N/A   | N/A    |
| 298 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 299 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 300 | Tensor<[16, 59, 59]> self = ?                                                                     | Unknown  | Done       | 1.0   | -1     |
| 301 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 302 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 303 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 304 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 305 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 306 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 307 | Tensor<[16, 64, 192]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 308 | Tensor<[16, 64, 256]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 309 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 310 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 311 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 312 | Tensor<[16, 7, 7]> self = ?                                                                       | Removed  | Done       | 1.0   | -1     |
| 313 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 314 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 315 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 316 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 317 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 318 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 319 | Tensor<[19, 19]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | 1.0   | -1     |
| 320 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 321 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 322 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Removed  | Done       | 1.0   | -1     |
| 323 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 324 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Done       | 1.0   | -1     |
| 325 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Removed  | Done       | 1.0   | -1     |
| 326 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Removed  | Done       | 1.0   | -1     |
| 327 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 328 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 329 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Removed  | Done       | 1.0   | -1     |
| 330 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Removed  | Done       | 1.0   | -1     |
| 331 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 332 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Removed  | Done       | 1.0   | -1     |
| 333 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 334 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Removed  | Done       | 1.0   | -1     |
| 335 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 336 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 337 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Unknown    | N/A   | N/A    |
| 338 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 339 | Tensor<[38, 38]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | Done       | 1.0   | -1     |
| 340 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 341 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 342 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 343 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 344 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 345 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 346 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 347 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 348 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 349 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 350 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 351 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 352 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 353 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 354 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 355 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 356 | Tensor<[4, 49, 384]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 357 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 358 | Tensor<[4, 49, 512]> self = ?                                                                     | Removed  | Unknown    | N/A   | N/A    |
| 359 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 360 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 361 | Tensor<[4, 64, 384]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 362 | Tensor<[4, 64, 512]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 363 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Unknown    | N/A   | N/A    |
| 364 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Removed  | Done       | 1.0   | -1     |
| 365 | Tensor<[59, 1024]> self = ?                                                                       | Unknown  | Done       | 1.0   | -1     |
| 366 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 367 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 368 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 369 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 370 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 371 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 372 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 373 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 374 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 375 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 376 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 377 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Removed  | Unknown    | N/A   | N/A    |
| 378 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 379 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Removed  | Done       | 1.0   | -1     |
| 380 | Tensor<[64, 49, 128]> self = ?                                                                    | Removed  | Unknown    | N/A   | N/A    |
| 381 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 382 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Unknown    | N/A   | N/A    |
| 383 | Tensor<[64, 49, 96]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 384 | Tensor<[64, 64, 128]> self = ?                                                                    | Removed  | Done       | 1.0   | -1     |
| 385 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 386 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Removed  | Done       | 1.0   | -1     |
| 387 | Tensor<[64, 64, 96]> self = ?                                                                     | Removed  | Done       | 1.0   | -1     |
| 388 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Unknown    | N/A   | N/A    |
| 389 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Removed  | Done       | 1.0   | -1     |
| 390 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 391 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Removed  | Done       | 1.0   | -1     |
| 392 | Tensor<[920, 1, 2048]> self = ?                                                                   | Unknown  | Done       | 1.0   | -1     |
| 393 | Tensor<[920, 1, 256]> self = ?                                                                    | Unknown  | Done       | 1.0   | -1     |
| 394 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Unknown  | Done       | 1.0   | -1     |

