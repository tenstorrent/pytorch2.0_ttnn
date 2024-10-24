### aten.clone.default
|     | ATen Input Variations                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|----:|:--------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|   0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   1 | Tensor<[1, 1, 1024]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   2 | Tensor<[1, 1, 16384, 256]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
|   3 | Tensor<[1, 1, 19200, 300]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
|   4 | Tensor<[1, 1, 2048]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   5 | Tensor<[1, 1, 3072]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|   6 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   7 | Tensor<[1, 1, 4096]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   8 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   9 | Tensor<[1, 1, 512]> self = ?                                                                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  10 | Tensor<[1, 1, 768]> self = ?                                                                      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  11 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  12 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  13 | Tensor<[1, 10, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  14 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  15 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  16 | Tensor<[1, 10, 2048]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  17 | Tensor<[1, 10, 3072]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  18 | Tensor<[1, 10, 4096]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  19 | Tensor<[1, 10, 512]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  20 | Tensor<[1, 10, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  21 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  22 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  23 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  24 | Tensor<[1, 1024, 160]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  25 | Tensor<[1, 1024, 2560]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  26 | Tensor<[1, 1024, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  27 | Tensor<[1, 1024, 512]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  28 | Tensor<[1, 1024, 640]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  29 | Tensor<[1, 1024]> self = ?                                                                        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  30 | Tensor<[1, 112, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  31 | Tensor<[1, 12, 1, 10]> self = ?                                                                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  32 | Tensor<[1, 12, 1, 1]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  33 | Tensor<[1, 12, 1, 2]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  34 | Tensor<[1, 12, 1, 46]> self = ?                                                                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  35 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  36 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  37 | Tensor<[1, 12, 10, 10]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  38 | Tensor<[1, 12, 12, 12]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  39 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  40 | Tensor<[1, 12, 128]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  41 | Tensor<[1, 12, 14, 14]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  42 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  43 | Tensor<[1, 12, 16, 16]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  44 | Tensor<[1, 12, 197, 197]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  45 | Tensor<[1, 12, 201, 201]> self = ?                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  46 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  47 | Tensor<[1, 12, 25, 25]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  48 | Tensor<[1, 12, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  49 | Tensor<[1, 12, 45, 45]> self = ?                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  50 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  51 | Tensor<[1, 12, 7, 7]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  52 | Tensor<[1, 12, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  53 | Tensor<[1, 12, 9, 9]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  54 | Tensor<[1, 1200, 1280]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  55 | Tensor<[1, 1200, 320]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  56 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  57 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  58 | Tensor<[1, 1280, 16, 16]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  59 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  60 | Tensor<[1, 1280, 8, 8]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  61 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  62 | Tensor<[1, 1280]> self = ?                                                                        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  63 | Tensor<[1, 128]> self = ?                                                                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  64 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  65 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  66 | Tensor<[1, 1370, 1280]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  67 | Tensor<[1, 1370, 5120]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  68 | Tensor<[1, 14, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  69 | Tensor<[1, 14, 128]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  70 | Tensor<[1, 14, 14, 1536]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  71 | Tensor<[1, 14, 14, 2048]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  72 | Tensor<[1, 14, 14, 384]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  73 | Tensor<[1, 14, 14, 512]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  74 | Tensor<[1, 14, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  75 | Tensor<[1, 1445, 192]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  76 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  77 | Tensor<[1, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  78 | Tensor<[1, 15, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  79 | Tensor<[1, 15, 512]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  80 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  81 | Tensor<[1, 1500, 3072]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  82 | Tensor<[1, 1500, 768]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  83 | Tensor<[1, 1536]> self = ?                                                                        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  84 | Tensor<[1, 16, 1, 10]> self = ?                                                                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  85 | Tensor<[1, 16, 1, 1]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  86 | Tensor<[1, 16, 1, 2]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  87 | Tensor<[1, 16, 1, 6]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  88 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  89 | Tensor<[1, 16, 1, s10 + 1]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  90 | Tensor<[1, 16, 10, 10]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  91 | Tensor<[1, 16, 112, 112]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  92 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  93 | Tensor<[1, 16, 16, 1536]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  94 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  95 | Tensor<[1, 16, 16, 2048]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  96 | Tensor<[1, 16, 16, 384]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  97 | Tensor<[1, 16, 16, 512]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  98 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  99 | Tensor<[1, 16, 197, 197]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 100 | Tensor<[1, 16, 256, 256]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 101 | Tensor<[1, 16, 32, 32]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 102 | Tensor<[1, 16, 5, 5]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 103 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 104 | Tensor<[1, 16, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 105 | Tensor<[1, 16, 9, 9]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 106 | Tensor<[1, 160, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 107 | Tensor<[1, 160, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 108 | Tensor<[1, 16384, 128]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 109 | Tensor<[1, 16384, 32]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 110 | Tensor<[1, 19, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 111 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 112 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 113 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 114 | Tensor<[1, 19, 4096]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 115 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 116 | Tensor<[1, 19200, 256]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 117 | Tensor<[1, 19200, 64]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 118 | Tensor<[1, 196, 3072]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 119 | Tensor<[1, 196, 768]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 120 | Tensor<[1, 197, 1024]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 121 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 122 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 123 | Tensor<[1, 197, 3072]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 124 | Tensor<[1, 197, 4096]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 125 | Tensor<[1, 197, 768]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 126 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 127 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 128 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 129 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 130 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 131 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 132 | Tensor<[1, 2, 4096, 256]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 133 | Tensor<[1, 2, 4800, 300]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 134 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 135 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 136 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 137 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 138 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 139 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 140 | Tensor<[1, 201, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 141 | Tensor<[1, 201, 768]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 142 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 143 | Tensor<[1, 2048]> self = ?                                                                        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 144 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 145 | Tensor<[1, 24, 3072]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 146 | Tensor<[1, 24, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 147 | Tensor<[1, 24, 56, 56]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 148 | Tensor<[1, 24, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 149 | Tensor<[1, 24, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 150 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 151 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 152 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 153 | Tensor<[1, 25, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 154 | Tensor<[1, 256, 100]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 155 | Tensor<[1, 256, 1024]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 156 | Tensor<[1, 256, 128, 128]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 157 | Tensor<[1, 256, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.channels_last         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 158 | Tensor<[1, 256, 1280]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 159 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 160 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 161 | Tensor<[1, 256, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 162 | Tensor<[1, 256, 256]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 163 | Tensor<[1, 256, 5, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 164 | Tensor<[1, 256, 5120]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 165 | Tensor<[1, 256, 512]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 166 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 167 | Tensor<[1, 256, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 168 | Tensor<[1, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 169 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 170 | Tensor<[1, 28, 28, 1024]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 171 | Tensor<[1, 28, 28, 192]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 172 | Tensor<[1, 28, 28, 256]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 173 | Tensor<[1, 28, 28, 768]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 174 | Tensor<[1, 3, 1445, 1445]> self = ?                                                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 175 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 176 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 177 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 178 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 179 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 180 | Tensor<[1, 300, 2048]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 181 | Tensor<[1, 300, 512]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 182 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 183 | Tensor<[1, 32, 128, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 184 | Tensor<[1, 32, 1536]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 185 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 186 | Tensor<[1, 32, 32, 1024]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 187 | Tensor<[1, 32, 32, 192]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 188 | Tensor<[1, 32, 32, 256]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 189 | Tensor<[1, 32, 32, 768]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 190 | Tensor<[1, 32, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 191 | Tensor<[1, 32, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 192 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 193 | Tensor<[1, 320, 64, 64]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 194 | Tensor<[1, 320, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 195 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 196 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 197 | Tensor<[1, 4, 3072]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 198 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 199 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 200 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 201 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 202 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 203 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 204 | Tensor<[1, 4, 768]> self = ?                                                                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 205 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 206 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 207 | Tensor<[1, 40, 28, 28]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 208 | Tensor<[1, 4096, 1280]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 209 | Tensor<[1, 4096, 2, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 210 | Tensor<[1, 4096, 256]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 211 | Tensor<[1, 4096, 320]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 212 | Tensor<[1, 4096, 64]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 213 | Tensor<[1, 4096]> self = ?                                                                        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 214 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 215 | Tensor<[1, 45, 768]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 216 | Tensor<[1, 4800, 128]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 217 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 218 | Tensor<[1, 4800, 512]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 219 | Tensor<[1, 49, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 220 | Tensor<[1, 49, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 221 | Tensor<[1, 49, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 222 | Tensor<[1, 49, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 223 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 224 | Tensor<[1, 5, 1024, 256]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 225 | Tensor<[1, 5, 1024]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 226 | Tensor<[1, 5, 1200, 300]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 227 | Tensor<[1, 5, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 228 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 229 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 230 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 231 | Tensor<[1, 50, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 232 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 233 | Tensor<[1, 50, 3072]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 234 | Tensor<[1, 50, 4096]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 235 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 236 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 237 | Tensor<[1, 50, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 238 | Tensor<[1, 512, 1, 1]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 239 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 240 | Tensor<[1, 56, 56, 128]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 241 | Tensor<[1, 56, 56, 384]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 242 | Tensor<[1, 56, 56, 512]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 243 | Tensor<[1, 56, 56, 96]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 244 | Tensor<[1, 59, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 245 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 246 | Tensor<[1, 6, 1, 15]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 247 | Tensor<[1, 6, 1, 17]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 248 | Tensor<[1, 6, 1, 1]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 249 | Tensor<[1, 6, 1, 2]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 250 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 251 | Tensor<[1, 6, 15, 15]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 252 | Tensor<[1, 64, 1024]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 253 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 254 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 255 | Tensor<[1, 64, 1280]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 256 | Tensor<[1, 64, 24, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 257 | Tensor<[1, 64, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 258 | Tensor<[1, 64, 5120]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 259 | Tensor<[1, 64, 64, 128]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 260 | Tensor<[1, 64, 64, 384]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 261 | Tensor<[1, 64, 64, 512]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 262 | Tensor<[1, 64, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 263 | Tensor<[1, 64, 64, 96]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 264 | Tensor<[1, 64, 768]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 265 | Tensor<[1, 64, 9, 9]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 266 | Tensor<[1, 640, 32, 32]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 267 | Tensor<[1, 640, 32, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 268 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 269 | Tensor<[1, 7, 4544]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 270 | Tensor<[1, 7, 7, 1024]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 271 | Tensor<[1, 7, 7, 3072]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 272 | Tensor<[1, 7, 7, 4096]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 273 | Tensor<[1, 7, 7, 768]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 274 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 275 | Tensor<[1, 7, 768]> self = ?                                                                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 276 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 277 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 278 | Tensor<[1, 768, 196]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 279 | Tensor<[1, 768, 384]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 280 | Tensor<[1, 768]> self = ?                                                                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 281 | Tensor<[1, 8, 1, 10]> self = ?                                                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 282 | Tensor<[1, 8, 1, 1]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 283 | Tensor<[1, 8, 1, 2]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 284 | Tensor<[1, 8, 1, s0 + 1]> self = ?                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 285 | Tensor<[1, 8, 10, 10]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 286 | Tensor<[1, 8, 2048, 256]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 287 | Tensor<[1, 8, 256, 2048]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 288 | Tensor<[1, 8, 256, 256]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 289 | Tensor<[1, 8, 300, 300]> self = ?                                                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 290 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 291 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 292 | Tensor<[1, 8, 768]> self = ?                                                                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 293 | Tensor<[1, 8, 8, 1024]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 294 | Tensor<[1, 8, 8, 3072]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 295 | Tensor<[1, 8, 8, 4096]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 296 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 297 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 298 | Tensor<[1, 8, 8, 768]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 299 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 300 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 301 | Tensor<[1, 80, 100]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 302 | Tensor<[1, 80, 14, 14]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 303 | Tensor<[1, 9, 1024]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 304 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 305 | Tensor<[1, 9, 128]> self = ?                                                                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 306 | Tensor<[1, 9, 16, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 307 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 308 | Tensor<[1, 9, 2048]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 309 | Tensor<[1, 9, 4096]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 310 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 311 | Tensor<[1, 9, 768]> self = ?                                                                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 312 | Tensor<[1, s0, 768]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 313 | Tensor<[1, s10 + 1]> self = ?                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 314 | Tensor<[10, 10]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 315 | Tensor<[100, 1, 2048]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 316 | Tensor<[100, 1, 256]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 317 | Tensor<[100, 136]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 318 | Tensor<[100, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 319 | Tensor<[12, 1, 1]> self = ?                                                                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 320 | Tensor<[12, 1, 24]> self = ?                                                                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 321 | Tensor<[12, 1, 2]> self = ?                                                                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 322 | Tensor<[12, 1, s0 + 1]> self = ?                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 323 | Tensor<[12, 1, s10 + 1]> self = ?                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 324 | Tensor<[12, 1, s2 + 1]> self = ?                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 325 | Tensor<[12, 1, s4 + 1]> self = ?                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 326 | Tensor<[12, 1, s6 + 1]> self = ?                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 327 | Tensor<[12, 1, s8 + 1]> self = ?                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 328 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 329 | Tensor<[12, 24, 24]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 330 | Tensor<[12, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 331 | Tensor<[12, 50, 50]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 332 | Tensor<[12, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 333 | Tensor<[13, 17]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 334 | Tensor<[16, 1, 60]> self = ?                                                                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 335 | Tensor<[16, 1, s10 + 1]> self = ?                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 336 | Tensor<[16, 19, 19]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 337 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 338 | Tensor<[16, 49, 192]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 339 | Tensor<[16, 49, 256]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 340 | Tensor<[16, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 341 | Tensor<[16, 49, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 342 | Tensor<[16, 49, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 343 | Tensor<[16, 59, 59]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 344 | Tensor<[16, 6, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 345 | Tensor<[16, 6, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 346 | Tensor<[16, 6, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 347 | Tensor<[16, 6, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 348 | Tensor<[16, 6, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 349 | Tensor<[16, 6, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 350 | Tensor<[16, 64, 192]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 351 | Tensor<[16, 64, 256]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 352 | Tensor<[16, 64, 6, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 353 | Tensor<[16, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 354 | Tensor<[16, 64, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 355 | Tensor<[16, 7, 7]> self = ?                                                                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 356 | Tensor<[16, 8, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 357 | Tensor<[16, 8, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 358 | Tensor<[16, 8, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 359 | Tensor<[16, 8, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 360 | Tensor<[16, 8, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 361 | Tensor<[16, 8, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 362 | Tensor<[19, 19]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 363 | Tensor<[2, 2, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 364 | Tensor<[2, 2, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 365 | Tensor<[2, 2]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 366 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 367 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 368 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 369 | Tensor<[20, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 370 | Tensor<[24, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 371 | Tensor<[24, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 372 | Tensor<[25, 34]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 373 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 374 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 375 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 376 | Tensor<[3, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 377 | Tensor<[3, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 378 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 379 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 380 | Tensor<[3, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 381 | Tensor<[32, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 382 | Tensor<[32, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 383 | Tensor<[38, 38]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 384 | Tensor<[4, 12, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 385 | Tensor<[4, 12, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 386 | Tensor<[4, 12, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 387 | Tensor<[4, 12, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 388 | Tensor<[4, 12, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 389 | Tensor<[4, 12, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 390 | Tensor<[4, 16, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 391 | Tensor<[4, 16, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 392 | Tensor<[4, 16, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 393 | Tensor<[4, 16, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 394 | Tensor<[4, 16, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 395 | Tensor<[4, 16, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 396 | Tensor<[4, 4, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 397 | Tensor<[4, 4, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 398 | Tensor<[4, 49, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 399 | Tensor<[4, 49, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 400 | Tensor<[4, 49, 384]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 401 | Tensor<[4, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 402 | Tensor<[4, 49, 512]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 403 | Tensor<[4, 64, 12, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 404 | Tensor<[4, 64, 16, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 405 | Tensor<[4, 64, 384]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 406 | Tensor<[4, 64, 512]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 407 | Tensor<[4, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 408 | Tensor<[5, 5]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 409 | Tensor<[50, 68]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 410 | Tensor<[59, 1024]> self = ?                                                                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 411 | Tensor<[6, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 412 | Tensor<[6, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 413 | Tensor<[64, 3, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 414 | Tensor<[64, 3, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 415 | Tensor<[64, 3, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 416 | Tensor<[64, 3, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 417 | Tensor<[64, 3, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 418 | Tensor<[64, 3, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 419 | Tensor<[64, 4, 32, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 420 | Tensor<[64, 4, 32, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 421 | Tensor<[64, 4, 49, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 422 | Tensor<[64, 4, 49, 49]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 423 | Tensor<[64, 4, 64, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 424 | Tensor<[64, 4, 64, 64]> self = ?                                                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 425 | Tensor<[64, 49, 128]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 426 | Tensor<[64, 49, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 427 | Tensor<[64, 49, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 428 | Tensor<[64, 49, 96]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 429 | Tensor<[64, 64, 128]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 430 | Tensor<[64, 64, 3, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 431 | Tensor<[64, 64, 4, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 432 | Tensor<[64, 64, 96]> self = ?                                                                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 433 | Tensor<[7, 9]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 434 | Tensor<[8, 49, 49]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 435 | Tensor<[8, 64, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 436 | Tensor<[8, 8, 7, 7]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 437 | Tensor<[8, 8, 8, 8]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 438 | Tensor<[920, 1, 2048]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 439 | Tensor<[920, 1, 256]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 440 | Tensor<[920, 8, 32]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format           | Done     | N/A                 | N/A          | N/A               | N/A                |

