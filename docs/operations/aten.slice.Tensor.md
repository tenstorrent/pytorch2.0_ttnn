### aten.slice.Tensor
|     | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   |
|----:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[0, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Unknown    | N/A   |
|   1 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2           | Unknown  | Unknown    | N/A   |
|   2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Unknown    | N/A   |
|   3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2           | Unknown  | Unknown    | N/A   |
|   4 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Unknown    | N/A   |
|   5 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Unknown    | N/A   |
|   6 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Unknown    | N/A   |
|   7 | Tensor<[0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Unknown    | N/A   |
|   8 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|   9 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  10 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  11 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  12 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  13 | Tensor<[1, 1, 1, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  14 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  15 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  16 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                                    | Unknown  | Done       | True  |
|  17 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 6                                     | Unknown  | Done       | True  |
|  18 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
|  19 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?                            | Unknown  | Failed     | N/A   |
|  20 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  21 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  22 | Tensor<[1, 1, 1, 25]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  23 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  24 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  25 | Tensor<[1, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  26 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  27 | Tensor<[1, 1, 1, 46]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  28 | Tensor<[1, 1, 1, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  29 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  30 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  31 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  32 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  33 | Tensor<[1, 1, 1, 8]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Unknown    | N/A   |
|  34 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
|  35 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
|  36 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
|  37 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  38 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  39 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                  | Unknown  | Done       | True  |
|  40 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  41 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  42 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  43 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  44 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
|  45 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
|  46 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  47 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  48 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  49 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                     | Unknown  | Done       | True  |
|  50 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
|  51 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  52 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  53 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  54 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  55 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  56 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
|  57 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
|  58 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  59 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  60 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 45                                 | Fallback | Done       | True  |
|  61 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 5                                  | Fallback | Done       | True  |
|  62 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Removed  | Unknown    | N/A   |
|  63 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 45,<br>Optional[int] end = 46                                | Unknown  | Done       | True  |
|  64 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 5,<br>Optional[int] end = 6                                  | Unknown  | Done       | True  |
|  65 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?                    | Unknown  | Failed     | N/A   |
|  66 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Removed  | Unknown    | N/A   |
|  67 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
|  68 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  69 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  70 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Removed  | Fallback   | True  |
|  71 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
|  72 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
|  73 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  74 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                                   | None     | Fallback   | True  |
|  75 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  76 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  77 | Tensor<[1, 1, 5, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 5                                     | None     | Fallback   | True  |
|  78 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  79 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  80 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  81 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                     | Unknown  | Fallback   | True  |
|  82 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                      | Fallback | Done       | True  |
|  83 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                    | Done     | Done       | True  |
|  84 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
|  85 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
|  86 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   |
|  87 | Tensor<[1, 100, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  88 | Tensor<[1, 102, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                   | Done     | Unknown    | N/A   |
|  89 | Tensor<[1, 102, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 38                                  | Done     | Unknown    | N/A   |
|  90 | Tensor<[1, 102, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 38,<br>Optional[int] end = 102                                 | Done     | Unknown    | N/A   |
|  91 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                               | Unknown  | Unknown    | N/A   |
|  92 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                             | Unknown  | Unknown    | N/A   |
|  93 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 768                             | Unknown  | Unknown    | N/A   |
|  94 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 1024                            | Unknown  | Unknown    | N/A   |
|  95 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 384                                 | Fallback | Unknown    | N/A   |
|  96 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 384,<br>Optional[int] end = 640                               | Fallback | Unknown    | N/A   |
|  97 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 640,<br>Optional[int] end = 1024                              | Fallback | Unknown    | N/A   |
|  98 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 640,<br>Optional[int] end = 896                               | Fallback | Unknown    | N/A   |
|  99 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 896,<br>Optional[int] end = 1024                              | Fallback | Unknown    | N/A   |
| 100 | Tensor<[1, 1024, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512                                 | Done     | Done       | True  |
| 101 | Tensor<[1, 1024, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 1024                              | Fallback | Done       | True  |
| 102 | Tensor<[1, 1072, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                   | Done     | Unknown    | N/A   |
| 103 | Tensor<[1, 1072, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 432                                 | Done     | Unknown    | N/A   |
| 104 | Tensor<[1, 1072, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 432,<br>Optional[int] end = 1072                                | Done     | Unknown    | N/A   |
| 105 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512                                 | Done     | Unknown    | N/A   |
| 106 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 704                               | Done     | Unknown    | N/A   |
| 107 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 704,<br>Optional[int] end = 896                               | Done     | Unknown    | N/A   |
| 108 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 896,<br>Optional[int] end = 1088                              | Fallback | Unknown    | N/A   |
| 109 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 110 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 111 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 112 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 56                                   | Done     | Done       | True  |
| 113 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 56,<br>Optional[int] end = 112                                 | Fallback | Done       | True  |
| 114 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 115 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 116 | Tensor<[1, 118, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 117 | Tensor<[1, 118, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 118                                 | Done     | Unknown    | N/A   |
| 118 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 119 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 120 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 121 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 122 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 123 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 124 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 125 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 126 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 127 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 128 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 129 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   |
| 130 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 131 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 132 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   |
| 133 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 134 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 135 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 136 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 60                                   | Done     | Done       | True  |
| 137 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 60,<br>Optional[int] end = 120                                 | Fallback | Done       | True  |
| 138 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 139 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 140 | Tensor<[1, 122, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 141 | Tensor<[1, 122, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Unknown    | N/A   |
| 142 | Tensor<[1, 122, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 122                                 | Done     | Unknown    | N/A   |
| 143 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                   | Done     | Unknown    | N/A   |
| 144 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 28                                  | Done     | Unknown    | N/A   |
| 145 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 28,<br>Optional[int] end = 42                                  | Done     | Unknown    | N/A   |
| 146 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 42,<br>Optional[int] end = 56                                  | Done     | Unknown    | N/A   |
| 147 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 56,<br>Optional[int] end = 124                                 | Fallback | Unknown    | N/A   |
| 148 | Tensor<[1, 128, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                 | Fallback | Done       | True  |
| 149 | Tensor<[1, 128, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 128                               | Done     | Done       | True  |
| 150 | Tensor<[1, 128, 224, 224]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                 | Done     | Done       | True  |
| 151 | Tensor<[1, 128, 224, 224]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 128                               | Fallback | Done       | True  |
| 152 | Tensor<[1, 128, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                   | Fallback | Unknown    | N/A   |
| 153 | Tensor<[1, 128, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 128                                 | Done     | Unknown    | N/A   |
| 154 | Tensor<[1, 1280, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512                                   | Fallback | Unknown    | N/A   |
| 155 | Tensor<[1, 1280, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1024,<br>Optional[int] end = 1280                               | Done     | Unknown    | N/A   |
| 156 | Tensor<[1, 1280, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 1024                                | Done     | Unknown    | N/A   |
| 157 | Tensor<[1, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Unknown    | N/A   |
| 158 | Tensor<[1, 1280]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Unknown    | N/A   |
| 159 | Tensor<[1, 12]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 160 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 161 | Tensor<[1, 14, 14, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 162 | Tensor<[1, 14, 14, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 163 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 164 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 165 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 166 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 167 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 168 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 169 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 170 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 171 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 172 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 173 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 174 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 175 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                   | Done     | Unknown    | N/A   |
| 176 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 38                                  | Done     | Unknown    | N/A   |
| 177 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 38,<br>Optional[int] end = 78                                  | Done     | Unknown    | N/A   |
| 178 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 78,<br>Optional[int] end = 142                                 | Done     | Unknown    | N/A   |
| 179 | Tensor<[1, 144, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 180 | Tensor<[1, 144, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 144                                 | Done     | Unknown    | N/A   |
| 181 | Tensor<[1, 144, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 182 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 768                                   | Done     | Unknown    | N/A   |
| 183 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1216,<br>Optional[int] end = 1440                               | Fallback | Unknown    | N/A   |
| 184 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 992                                 | Done     | Unknown    | N/A   |
| 185 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 992,<br>Optional[int] end = 1216                                | Done     | Unknown    | N/A   |
| 186 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 187 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = 9223372036854775807                 | Done     | Done       | True  |
| 188 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 189 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807                     | Done     | Done       | True  |
| 190 | Tensor<[1, 152, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 191 | Tensor<[1, 152, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Unknown    | N/A   |
| 192 | Tensor<[1, 152, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 152                                 | Done     | Unknown    | N/A   |
| 193 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 192                                   | Fallback | Unknown    | N/A   |
| 194 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                   | Fallback | Unknown    | N/A   |
| 195 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1280,<br>Optional[int] end = 1536                               | Fallback | Unknown    | N/A   |
| 196 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 512                                 | Fallback | Unknown    | N/A   |
| 197 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 768                                 | Done     | Unknown    | N/A   |
| 198 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 1536                                | Fallback | Unknown    | N/A   |
| 199 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 1280                                | Done     | Unknown    | N/A   |
| 200 | Tensor<[1, 156, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 201 | Tensor<[1, 156, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 156                                 | Done     | Unknown    | N/A   |
| 202 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 203 | Tensor<[1, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 204 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 205 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 206 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 207 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 208 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                                   | Done     | Done       | True  |
| 209 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 8,<br>Optional[int] end = 16                                  | Fallback | Done       | True  |
| 210 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 211 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 212 | Tensor<[1, 16, 16, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 213 | Tensor<[1, 16, 16, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 214 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 215 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 216 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 217 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 218 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 219 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 220 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 221 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 222 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 223 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 224 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 225 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 226 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 227 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 228 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 229 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 230 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 231 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 232 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 233 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 234 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   |
| 235 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 236 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 237 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   |
| 238 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 239 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 80                                     | Done     | Done       | True  |
| 240 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 160                                   | Fallback | Done       | True  |
| 241 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 242 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 243 | Tensor<[1, 160, 73, 73]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                   | Fallback | Unknown    | N/A   |
| 244 | Tensor<[1, 160, 73, 73]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 160                                 | Fallback | Unknown    | N/A   |
| 245 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 246 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 247 | Tensor<[1, 172, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 248 | Tensor<[1, 172, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Unknown    | N/A   |
| 249 | Tensor<[1, 172, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 172                                 | Done     | Unknown    | N/A   |
| 250 | Tensor<[1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 251 | Tensor<[1, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 252 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 253 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 92                                   | Done     | Done       | True  |
| 254 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 92,<br>Optional[int] end = 184                                 | Fallback | Done       | True  |
| 255 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 256 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 257 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 258 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = -57,<br>Optional[int] end = 9223372036854775807                | Fallback | Done       | True  |
| 259 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Fallback | Done       | True  |
| 260 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 147                                | Fallback | Done       | True  |
| 261 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 147,<br>Optional[int] end = 185                                | Fallback | Done       | True  |
| 262 | Tensor<[1, 192, 71, 71]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 96                                   | Fallback | Unknown    | N/A   |
| 263 | Tensor<[1, 192, 71, 71]> self = ?,<br>int dim = 1,<br>Optional[int] start = 96,<br>Optional[int] end = 192                                 | Fallback | Unknown    | N/A   |
| 264 | Tensor<[1, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 265 | Tensor<[1, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 266 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Unknown    | N/A   |
| 267 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Unknown    | N/A   |
| 268 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 269 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                      | Fallback | Unknown    | N/A   |
| 270 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                                    | Done     | Unknown    | N/A   |
| 271 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807                    | Fallback | Unknown    | N/A   |
| 272 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Unknown    | N/A   |
| 273 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                       | Fallback | Unknown    | N/A   |
| 274 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                                     | Done     | Unknown    | N/A   |
| 275 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807                     | Fallback | Unknown    | N/A   |
| 276 | Tensor<[1, 19]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 277 | Tensor<[1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 278 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 279 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 280 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 281 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 282 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 283 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 100                                  | Done     | Done       | True  |
| 284 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 100,<br>Optional[int] end = 200                                | Fallback | Done       | True  |
| 285 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 286 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 287 | Tensor<[1, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Removed  | Fallback   | True  |
| 288 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 289 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Unknown    | N/A   |
| 290 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 90                                  | Done     | Unknown    | N/A   |
| 291 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 90,<br>Optional[int] end = 218                                 | Done     | Unknown    | N/A   |
| 292 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 293 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 294 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 295 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 296 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 297 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 298 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Done     | Done       | True  |
| 299 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 300 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Done     | Done       | True  |
| 301 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 302 | Tensor<[1, 236, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 303 | Tensor<[1, 236, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 236                                 | Done     | Unknown    | N/A   |
| 304 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 305 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 12                                    | Done     | Done       | True  |
| 306 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 12,<br>Optional[int] end = 24                                   | Fallback | Done       | True  |
| 307 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 308 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 309 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 310 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 120                                  | Done     | Done       | True  |
| 311 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 120,<br>Optional[int] end = 240                                | Fallback | Done       | True  |
| 312 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 313 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 314 | Tensor<[1, 24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 315 | Tensor<[1, 24]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 316 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
| 317 | Tensor<[1, 256, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                | Done     | Done       | True  |
| 318 | Tensor<[1, 256, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                              | Fallback | Done       | True  |
| 319 | Tensor<[1, 256, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Fallback | Unknown    | N/A   |
| 320 | Tensor<[1, 256, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                                | Done     | Unknown    | N/A   |
| 321 | Tensor<[1, 256, 64, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Fallback | Done       | True  |
| 322 | Tensor<[1, 256, 64, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                                | Done     | Done       | True  |
| 323 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 324 | Tensor<[1, 25]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 325 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 326 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 112,<br>Optional[int] end = 128                                | Done     | Unknown    | N/A   |
| 327 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 262                                | Fallback | Unknown    | N/A   |
| 328 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 32                                  | Done     | Unknown    | N/A   |
| 329 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 32,<br>Optional[int] end = 48                                  | Done     | Unknown    | N/A   |
| 330 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 48,<br>Optional[int] end = 64                                  | Done     | Unknown    | N/A   |
| 331 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 80                                  | Done     | Unknown    | N/A   |
| 332 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 96                                  | Done     | Unknown    | N/A   |
| 333 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 96,<br>Optional[int] end = 112                                 | Done     | Unknown    | N/A   |
| 334 | Tensor<[1, 276, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 335 | Tensor<[1, 276, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 276                                 | Done     | Unknown    | N/A   |
| 336 | Tensor<[1, 28, 28, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 337 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 338 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 339 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 340 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 341 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 342 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 343 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 344 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 345 | Tensor<[1, 28, 28, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 346 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 347 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 348 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 349 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 350 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 351 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Unknown    | N/A   |
| 352 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 168,<br>Optional[int] end = 296                                | Done     | Unknown    | N/A   |
| 353 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 90                                  | Done     | Unknown    | N/A   |
| 354 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 90,<br>Optional[int] end = 168                                 | Done     | Unknown    | N/A   |
| 355 | Tensor<[1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 356 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 357 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 358 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 359 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 360 | Tensor<[1, 304, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 361 | Tensor<[1, 304, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 304                                | Done     | Unknown    | N/A   |
| 362 | Tensor<[1, 304, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Unknown    | N/A   |
| 363 | Tensor<[1, 310, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 364 | Tensor<[1, 310, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Unknown    | N/A   |
| 365 | Tensor<[1, 310, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 310                                 | Done     | Unknown    | N/A   |
| 366 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 367 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 368 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 369 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 370 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 371 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 372 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 373 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 374 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 375 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 376 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Unknown    | N/A   |
| 377 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 378 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 379 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 380 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 381 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 382 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                          | Unknown  | Unknown    | N/A   |
| 383 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 384 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Unknown    | N/A   |
| 385 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 386 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 100,<br>Optional[int] end = 120                                | Done     | Unknown    | N/A   |
| 387 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 120,<br>Optional[int] end = 140                                | Done     | Unknown    | N/A   |
| 388 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 140,<br>Optional[int] end = 160                                | Done     | Unknown    | N/A   |
| 389 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 328                                | Fallback | Unknown    | N/A   |
| 390 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 40                                  | Done     | Unknown    | N/A   |
| 391 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 60                                  | Done     | Unknown    | N/A   |
| 392 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 60,<br>Optional[int] end = 80                                  | Done     | Unknown    | N/A   |
| 393 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 100                                 | Done     | Unknown    | N/A   |
| 394 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 395 | Tensor<[1, 360, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 396 | Tensor<[1, 360, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 360                                 | Done     | Unknown    | N/A   |
| 397 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 398 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 112,<br>Optional[int] end = 368                                | Done     | Unknown    | N/A   |
| 399 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Unknown    | N/A   |
| 400 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 112                                 | Done     | Unknown    | N/A   |
| 401 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 192                                  | Fallback | Unknown    | N/A   |
| 402 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 96                                   | Fallback | Unknown    | N/A   |
| 403 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 288                                | Fallback | Unknown    | N/A   |
| 404 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 384                                | Fallback | Unknown    | N/A   |
| 405 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 288,<br>Optional[int] end = 384                                | Fallback | Unknown    | N/A   |
| 406 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 96,<br>Optional[int] end = 192                                 | Fallback | Unknown    | N/A   |
| 407 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 408 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 409 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                    | Done     | Done       | True  |
| 410 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 40                                   | Fallback | Done       | True  |
| 411 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 412 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 413 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 414 | Tensor<[1, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                                             | Fallback | Done       | True  |
| 415 | Tensor<[1, 4150, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 416 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 417 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = 9223372036854775807                 | Fallback | Done       | True  |
| 418 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -100                                   | Done     | Done       | True  |
| 419 | Tensor<[1, 428, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 420 | Tensor<[1, 428, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 428                                | Done     | Unknown    | N/A   |
| 421 | Tensor<[1, 428, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Unknown    | N/A   |
| 422 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Fallback | Unknown    | N/A   |
| 423 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                                | Done     | Unknown    | N/A   |
| 424 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 320                                | Fallback | Unknown    | N/A   |
| 425 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 448                                | Done     | Unknown    | N/A   |
| 426 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                   | Done     | Unknown    | N/A   |
| 427 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 320                                | Done     | Unknown    | N/A   |
| 428 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 448                                | Fallback | Unknown    | N/A   |
| 429 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 192                                 | Done     | Unknown    | N/A   |
| 430 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 431 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Unknown    | N/A   |
| 432 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 112,<br>Optional[int] end = 210                                | Done     | Unknown    | N/A   |
| 433 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Unknown    | N/A   |
| 434 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 210,<br>Optional[int] end = 466                                | Done     | Unknown    | N/A   |
| 435 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 112                                 | Done     | Unknown    | N/A   |
| 436 | Tensor<[1, 46]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 437 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | True  |
| 438 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 439 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                                  | Done     | Done       | True  |
| 440 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 24,<br>Optional[int] end = 48                                 | Fallback | Done       | True  |
| 441 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 442 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 443 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 444 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 240                                  | Done     | Done       | True  |
| 445 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 240,<br>Optional[int] end = 480                                | Fallback | Done       | True  |
| 446 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 447 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 448 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 449 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 450 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 451 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 452 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
| 453 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
| 454 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 455 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 456 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 457 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                     | Unknown  | Done       | True  |
| 458 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 459 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
| 460 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
| 461 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 462 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
| 463 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                        | Fallback | Done       | True  |
| 464 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 50                                       | Done     | Done       | True  |
| 465 | Tensor<[1, 512, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Fallback | Unknown    | N/A   |
| 466 | Tensor<[1, 512, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Unknown    | N/A   |
| 467 | Tensor<[1, 512, 32, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Fallback | Done       | True  |
| 468 | Tensor<[1, 512, 32, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Done       | True  |
| 469 | Tensor<[1, 512, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Done       | True  |
| 470 | Tensor<[1, 512, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Fallback | Done       | True  |
| 471 | Tensor<[1, 512, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                    | Fallback | Unknown    | N/A   |
| 472 | Tensor<[1, 512, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                  | Fallback | Unknown    | N/A   |
| 473 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 474 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 12                                           | Fallback | Done       | True  |
| 475 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                           | Fallback | Unknown    | N/A   |
| 476 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                           | Fallback | Unknown    | N/A   |
| 477 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 25                                           | None     | Fallback   | True  |
| 478 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                          | Done     | Done       | True  |
| 479 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                                            | Fallback | Unknown    | N/A   |
| 480 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9                                            | None     | Fallback   | True  |
| 481 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 482 | Tensor<[1, 514]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 10                                           | Fallback | Done       | True  |
| 483 | Tensor<[1, 54, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                    | Done     | Unknown    | N/A   |
| 484 | Tensor<[1, 54, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 54                                   | Done     | Unknown    | N/A   |
| 485 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 486 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 224                                | Done     | Unknown    | N/A   |
| 487 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 224,<br>Optional[int] end = 544                                | Done     | Unknown    | N/A   |
| 488 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Unknown    | N/A   |
| 489 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 490 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 491 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 492 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 493 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 494 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 495 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 496 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 497 | Tensor<[1, 59]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 498 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 499 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 500 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 501 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 502 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 503 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
| 504 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 505 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 506 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 507 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 508 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 509 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 510 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 511 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 512 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Done       | True  |
| 513 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 514 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 515 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 516 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 517 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 518 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 519 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 520 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 521 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 522 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 523 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 524 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 525 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                                      | Fallback | Done       | True  |
| 526 | Tensor<[1, 60]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 527 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>Optional[int] start = 59,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | True  |
| 528 | Tensor<[1, 62, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                    | Done     | Unknown    | N/A   |
| 529 | Tensor<[1, 62, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 62                                   | Done     | Unknown    | N/A   |
| 530 | Tensor<[1, 64, 256, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                  | Fallback | Done       | True  |
| 531 | Tensor<[1, 64, 256, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 32,<br>Optional[int] end = 64                                 | Done     | Done       | True  |
| 532 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 533 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 534 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Unknown    | N/A   |
| 535 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Unknown    | N/A   |
| 536 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Unknown    | N/A   |
| 537 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 538 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 539 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Unknown    | N/A   |
| 540 | Tensor<[1, 640]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 541 | Tensor<[1, 640]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 542 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Unknown    | N/A   |
| 543 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 544 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 120,<br>Optional[int] end = 160                                | Done     | Unknown    | N/A   |
| 545 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 200                                | Done     | Unknown    | N/A   |
| 546 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 200,<br>Optional[int] end = 240                                | Done     | Unknown    | N/A   |
| 547 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 240,<br>Optional[int] end = 280                                | Done     | Unknown    | N/A   |
| 548 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 280,<br>Optional[int] end = 320                                | Done     | Unknown    | N/A   |
| 549 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 654                                | Fallback | Unknown    | N/A   |
| 550 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 80                                  | Done     | Unknown    | N/A   |
| 551 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 120                                 | Done     | Unknown    | N/A   |
| 552 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 553 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 336                                  | Done     | Done       | True  |
| 554 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 336,<br>Optional[int] end = 672                                | Fallback | Done       | True  |
| 555 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 556 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 557 | Tensor<[1, 6]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 558 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 5,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Done       | True  |
| 559 | Tensor<[1, 7, 14, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 560 | Tensor<[1, 7, 14, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 561 | Tensor<[1, 7, 14, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 562 | Tensor<[1, 7, 14, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 563 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 564 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 565 | Tensor<[1, 7, 7, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 566 | Tensor<[1, 7, 7, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 567 | Tensor<[1, 7, 7, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 568 | Tensor<[1, 7, 7, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 569 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 570 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                                     | Done     | Done       | True  |
| 571 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 572 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                     | Fallback | Done       | True  |
| 573 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                   | Done     | Done       | True  |
| 574 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 575 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 36                                    | Done     | Done       | True  |
| 576 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 36,<br>Optional[int] end = 72                                   | Fallback | Done       | True  |
| 577 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 578 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 579 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Unknown    | N/A   |
| 580 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 416                                | Done     | Unknown    | N/A   |
| 581 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 416,<br>Optional[int] end = 576                                | Done     | Unknown    | N/A   |
| 582 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 576,<br>Optional[int] end = 736                                | Fallback | Unknown    | N/A   |
| 583 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Unknown    | N/A   |
| 584 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 224                                | Done     | Unknown    | N/A   |
| 585 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 224,<br>Optional[int] end = 420                                | Done     | Unknown    | N/A   |
| 586 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Unknown    | N/A   |
| 587 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 420,<br>Optional[int] end = 740                                | Done     | Unknown    | N/A   |
| 588 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 589 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 590 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                             | Fallback | Done       | True  |
| 591 | Tensor<[1, 78, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                    | Done     | Unknown    | N/A   |
| 592 | Tensor<[1, 78, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 78                                   | Done     | Unknown    | N/A   |
| 593 | Tensor<[1, 78, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                    | Done     | Unknown    | N/A   |
| 594 | Tensor<[1, 78, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 78                                   | Done     | Unknown    | N/A   |
| 595 | Tensor<[1, 782, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                    | Done     | Unknown    | N/A   |
| 596 | Tensor<[1, 782, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 320                                  | Done     | Unknown    | N/A   |
| 597 | Tensor<[1, 782, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 782                                  | Fallback | Unknown    | N/A   |
| 598 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 599 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   |
| 600 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Unknown    | N/A   |
| 601 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
| 602 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 603 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 604 | Tensor<[1, 8, 16, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 605 | Tensor<[1, 8, 16, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Unknown    | N/A   |
| 606 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Unknown    | N/A   |
| 607 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Unknown    | N/A   |
| 608 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   |
| 609 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   |
| 610 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   |
| 611 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   |
| 612 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Unknown    | N/A   |
| 613 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Unknown    | N/A   |
| 614 | Tensor<[1, 8, 8, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Unknown    | N/A   |
| 615 | Tensor<[1, 8, 8, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Unknown    | N/A   |
| 616 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Unknown    | N/A   |
| 617 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Unknown    | N/A   |
| 618 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 619 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 620 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 621 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 622 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 623 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 624 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 625 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                    | Done     | Done       | True  |
| 626 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 80                                   | Fallback | Done       | True  |
| 627 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 628 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 629 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 630 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 631 | Tensor<[1, 800, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                    | Done     | Unknown    | N/A   |
| 632 | Tensor<[1, 800, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 800                                  | Done     | Unknown    | N/A   |
| 633 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Fallback | Unknown    | N/A   |
| 634 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Unknown    | N/A   |
| 635 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 640                                | Fallback | Unknown    | N/A   |
| 636 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 640,<br>Optional[int] end = 896                                | Done     | Unknown    | N/A   |
| 637 | Tensor<[1, 8]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Removed  | Unknown    | N/A   |
| 638 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Removed  | Unknown    | N/A   |
| 639 | Tensor<[1, 94, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                    | Done     | Unknown    | N/A   |
| 640 | Tensor<[1, 94, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 94                                   | Done     | Unknown    | N/A   |
| 641 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 642 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 480                                    | Done     | Done       | True  |
| 643 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 480,<br>Optional[int] end = 960                                  | Fallback | Done       | True  |
| 644 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 645 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 646 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Unknown    | N/A   |
| 647 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Unknown    | N/A   |
| 648 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Unknown    | N/A   |
| 649 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 650 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Unknown    | N/A   |
| 651 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Unknown    | N/A   |
| 652 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Unknown    | N/A   |
| 653 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s10> start = ?,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
| 654 | Tensor<[10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 655 | Tensor<[15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 656 | Tensor<[17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 657 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
| 658 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
| 659 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Removed  | Fallback   | True  |
| 660 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                          | Fallback | Done       | True  |
| 661 | Tensor<[24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Removed  | Fallback   | True  |
| 662 | Tensor<[25]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 663 | Tensor<[2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
| 664 | Tensor<[3234, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
| 665 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                                           | Done     | Done       | True  |
| 666 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 667 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 668 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 669 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 670 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807                         | Done     | Done       | True  |
| 671 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 672 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 673 | Tensor<[3234]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 674 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
| 675 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                          | Done     | Done       | True  |
| 676 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 4                                          | Fallback | Done       | True  |
| 677 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 4,<br>Optional[int] end = 5                                          | Fallback | Done       | True  |
| 678 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ?                              | Unknown  | Failed     | N/A   |
| 679 | Tensor<[8732, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
| 680 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                                           | Done     | Done       | True  |
| 681 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 682 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 683 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 684 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 685 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807                         | Done     | Done       | True  |
| 686 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 687 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 688 | Tensor<[8732]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 689 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |

