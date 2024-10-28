### aten.slice.Tensor
|     | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   |
|----:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[0, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
|   1 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2           | Unknown  | Fallback   | True  |
|   2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Fallback   | True  |
|   3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2           | Unknown  | Fallback   | True  |
|   4 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Fallback   | True  |
|   5 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Fallback   | True  |
|   6 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4           | Unknown  | Fallback   | True  |
|   7 | Tensor<[0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
|   8 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|   9 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  10 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  11 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  12 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  13 | Tensor<[1, 1, 1, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  14 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  15 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  16 | Tensor<[1, 1, 1, 201]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  17 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                                    | Unknown  | Done       | True  |
|  18 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 6                                     | Unknown  | Done       | True  |
|  19 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
|  20 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?                            | Unknown  | Failed     | N/A   |
|  21 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  22 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  23 | Tensor<[1, 1, 1, 25]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  24 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  25 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  26 | Tensor<[1, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  27 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  28 | Tensor<[1, 1, 1, 46]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  29 | Tensor<[1, 1, 1, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  30 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  31 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  32 | Tensor<[1, 1, 1, 6]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  33 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
|  34 | Tensor<[1, 1, 1, 8]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
|  35 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
|  36 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
|  37 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
|  38 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  39 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  40 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                  | Done     | Done       | True  |
|  41 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Fallback   | True  |
|  42 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Fallback   | True  |
|  43 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>int dim = 4,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Fallback   | True  |
|  44 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  45 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  46 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  47 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  48 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
|  49 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
|  50 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  51 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  52 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  53 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                     | Unknown  | Done       | True  |
|  54 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
|  55 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  56 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  57 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  58 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  59 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  60 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
|  61 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
|  62 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  63 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  64 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 45                                 | Unknown  | Done       | True  |
|  65 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 5                                  | Unknown  | Done       | True  |
|  66 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Removed  | Fallback   | True  |
|  67 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 45,<br>Optional[int] end = 46                                | Unknown  | Done       | True  |
|  68 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 5,<br>Optional[int] end = 6                                  | Unknown  | Done       | True  |
|  69 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?                    | Unknown  | Failed     | N/A   |
|  70 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Removed  | Fallback   | True  |
|  71 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
|  72 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  73 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
|  74 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Removed  | Fallback   | True  |
|  75 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
|  76 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
|  77 | Tensor<[1, 1, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
|  78 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                                   | Unknown  | Fallback   | True  |
|  79 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  80 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  81 | Tensor<[1, 1, 5, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 5                                     | Unknown  | Fallback   | True  |
|  82 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
|  83 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  84 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
|  85 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                     | None     | Fallback   | True  |
|  86 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                      | Unknown  | Done       | True  |
|  87 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
|  88 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
|  89 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
|  90 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Unknown    | N/A   |
|  91 | Tensor<[1, 100, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
|  92 | Tensor<[1, 102, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                   | Done     | Unknown    | N/A   |
|  93 | Tensor<[1, 102, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 38                                  | Done     | Unknown    | N/A   |
|  94 | Tensor<[1, 102, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 38,<br>Optional[int] end = 102                                 | Done     | Unknown    | N/A   |
|  95 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                               | Unknown  | Done       | True  |
|  96 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                             | Unknown  | Done       | True  |
|  97 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 768                             | Unknown  | Done       | True  |
|  98 | Tensor<[1, 1024, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 1024                            | Unknown  | Done       | True  |
|  99 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 384                                 | Done     | Done       | True  |
| 100 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 384,<br>Optional[int] end = 640                               | Done     | Done       | True  |
| 101 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 640,<br>Optional[int] end = 1024                              | Done     | Done       | True  |
| 102 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 640,<br>Optional[int] end = 896                               | Done     | Done       | True  |
| 103 | Tensor<[1, 1024, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 896,<br>Optional[int] end = 1024                              | Done     | Done       | True  |
| 104 | Tensor<[1, 1024, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512                                 | Done     | Done       | True  |
| 105 | Tensor<[1, 1024, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 1024                              | Done     | Done       | True  |
| 106 | Tensor<[1, 1072, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                   | Done     | Done       | True  |
| 107 | Tensor<[1, 1072, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 432                                 | Done     | Done       | True  |
| 108 | Tensor<[1, 1072, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 432,<br>Optional[int] end = 1072                                | Done     | Done       | True  |
| 109 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512                                 | Done     | Done       | True  |
| 110 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 704                               | Done     | Done       | True  |
| 111 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 704,<br>Optional[int] end = 896                               | Done     | Done       | True  |
| 112 | Tensor<[1, 1088, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 896,<br>Optional[int] end = 1088                              | Done     | Done       | True  |
| 113 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 114 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 115 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 116 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 56                                   | Done     | Done       | True  |
| 117 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 56,<br>Optional[int] end = 112                                 | Done     | Done       | True  |
| 118 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 119 | Tensor<[1, 112, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 120 | Tensor<[1, 118, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 121 | Tensor<[1, 118, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 118                                 | Done     | Done       | True  |
| 122 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 123 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 124 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 125 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 126 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 127 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 128 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 129 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 130 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 131 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 132 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 133 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   |
| 134 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 135 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 136 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   |
| 137 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 138 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 139 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 140 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 60                                   | Done     | Done       | True  |
| 141 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 60,<br>Optional[int] end = 120                                 | Done     | Done       | True  |
| 142 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 143 | Tensor<[1, 120, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 144 | Tensor<[1, 122, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Done       | True  |
| 145 | Tensor<[1, 122, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Done       | True  |
| 146 | Tensor<[1, 122, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 122                                 | Done     | Done       | True  |
| 147 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                   | Done     | Unknown    | N/A   |
| 148 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 28                                  | Done     | Unknown    | N/A   |
| 149 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 28,<br>Optional[int] end = 42                                  | Done     | Unknown    | N/A   |
| 150 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 42,<br>Optional[int] end = 56                                  | Done     | Unknown    | N/A   |
| 151 | Tensor<[1, 124, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 56,<br>Optional[int] end = 124                                 | Done     | Unknown    | N/A   |
| 152 | Tensor<[1, 128, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                 | Done     | Done       | True  |
| 153 | Tensor<[1, 128, 128, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 128                               | Done     | Done       | True  |
| 154 | Tensor<[1, 128, 224, 224]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                 | Done     | Done       | True  |
| 155 | Tensor<[1, 128, 224, 224]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 128                               | Done     | Done       | True  |
| 156 | Tensor<[1, 128, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                   | Done     | Done       | True  |
| 157 | Tensor<[1, 128, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 128                                 | Done     | Done       | True  |
| 158 | Tensor<[1, 1280, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 512                                   | Done     | Done       | True  |
| 159 | Tensor<[1, 1280, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1024,<br>Optional[int] end = 1280                               | Done     | Done       | True  |
| 160 | Tensor<[1, 1280, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 1024                                | Done     | Done       | True  |
| 161 | Tensor<[1, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
| 162 | Tensor<[1, 1280]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
| 163 | Tensor<[1, 12]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 164 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 165 | Tensor<[1, 14, 14, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 166 | Tensor<[1, 14, 14, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 167 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 168 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 169 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 170 | Tensor<[1, 14, 14, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 171 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 172 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 173 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 174 | Tensor<[1, 14, 14, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 175 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 176 | Tensor<[1, 14, 28, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 177 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 178 | Tensor<[1, 14, 28, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 179 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                   | Done     | Unknown    | N/A   |
| 180 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 38                                  | Done     | Unknown    | N/A   |
| 181 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 38,<br>Optional[int] end = 78                                  | Done     | Unknown    | N/A   |
| 182 | Tensor<[1, 142, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 78,<br>Optional[int] end = 142                                 | Done     | Unknown    | N/A   |
| 183 | Tensor<[1, 144, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 184 | Tensor<[1, 144, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 144                                 | Done     | Unknown    | N/A   |
| 185 | Tensor<[1, 144, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 186 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 768                                   | Done     | Done       | True  |
| 187 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1216,<br>Optional[int] end = 1440                               | Done     | Done       | True  |
| 188 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 992                                 | Done     | Done       | True  |
| 189 | Tensor<[1, 1440, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 992,<br>Optional[int] end = 1216                                | Done     | Done       | True  |
| 190 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 191 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = 9223372036854775807                 | Done     | Done       | True  |
| 192 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 193 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807                     | Done     | Done       | True  |
| 194 | Tensor<[1, 152, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 195 | Tensor<[1, 152, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Done       | True  |
| 196 | Tensor<[1, 152, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 152                                 | Done     | Done       | True  |
| 197 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 192                                   | Done     | Done       | True  |
| 198 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                   | Done     | Done       | True  |
| 199 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1280,<br>Optional[int] end = 1536                               | Done     | Done       | True  |
| 200 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 512                                 | Done     | Done       | True  |
| 201 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 768                                 | Done     | Done       | True  |
| 202 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 1536                                | Done     | Done       | True  |
| 203 | Tensor<[1, 1536, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 768,<br>Optional[int] end = 1280                                | Done     | Done       | True  |
| 204 | Tensor<[1, 156, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 205 | Tensor<[1, 156, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 156                                 | Done     | Done       | True  |
| 206 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 207 | Tensor<[1, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 208 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 209 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 210 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 211 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 212 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                                   | Done     | Done       | True  |
| 213 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 8,<br>Optional[int] end = 16                                  | Done     | Done       | True  |
| 214 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 215 | Tensor<[1, 16, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 216 | Tensor<[1, 16, 16, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 217 | Tensor<[1, 16, 16, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 218 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 219 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 220 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 221 | Tensor<[1, 16, 16, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 222 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 223 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 224 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 225 | Tensor<[1, 16, 16, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 226 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 227 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 228 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 229 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 230 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 231 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 232 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 233 | Tensor<[1, 16, 32, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 234 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 235 | Tensor<[1, 16, 32, 256]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 236 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 237 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 238 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   |
| 239 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 240 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 241 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   |
| 242 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 243 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 80                                     | Done     | Done       | True  |
| 244 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 160                                   | Done     | Done       | True  |
| 245 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 246 | Tensor<[1, 160, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 247 | Tensor<[1, 160, 73, 73]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                   | Done     | Done       | True  |
| 248 | Tensor<[1, 160, 73, 73]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 160                                 | Done     | Done       | True  |
| 249 | Tensor<[1, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 250 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 251 | Tensor<[1, 172, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Unknown    | N/A   |
| 252 | Tensor<[1, 172, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Unknown    | N/A   |
| 253 | Tensor<[1, 172, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 172                                 | Done     | Unknown    | N/A   |
| 254 | Tensor<[1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 255 | Tensor<[1, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 256 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 257 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 92                                   | Done     | Done       | True  |
| 258 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 92,<br>Optional[int] end = 184                                 | Done     | Done       | True  |
| 259 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 260 | Tensor<[1, 184, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 261 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 262 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = -57,<br>Optional[int] end = 9223372036854775807                | Done     | Done       | True  |
| 263 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Done     | Done       | True  |
| 264 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 147                                | Done     | Done       | True  |
| 265 | Tensor<[1, 185, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 147,<br>Optional[int] end = 185                                | Done     | Done       | True  |
| 266 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 267 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                      | Unknown  | Done       | True  |
| 268 | Tensor<[1, 1876, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int]<s0> end = ?                                  | Unknown  | Failed     | N/A   |
| 269 | Tensor<[1, 192, 71, 71]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 96                                   | Done     | Done       | True  |
| 270 | Tensor<[1, 192, 71, 71]> self = ?,<br>int dim = 1,<br>Optional[int] start = 96,<br>Optional[int] end = 192                                 | Done     | Done       | True  |
| 271 | Tensor<[1, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 272 | Tensor<[1, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 273 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 274 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 275 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 276 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                      | Done     | Done       | True  |
| 277 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                                    | Done     | Done       | True  |
| 278 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807                    | Done     | Done       | True  |
| 279 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 280 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                       | Done     | Done       | True  |
| 281 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                                     | Done     | Done       | True  |
| 282 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807                     | Done     | Done       | True  |
| 283 | Tensor<[1, 19]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 284 | Tensor<[1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 285 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 286 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 287 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 288 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 289 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 290 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 100                                  | Done     | Done       | True  |
| 291 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 100,<br>Optional[int] end = 200                                | Done     | Done       | True  |
| 292 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 293 | Tensor<[1, 200, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 294 | Tensor<[1, 201, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 295 | Tensor<[1, 201]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 296 | Tensor<[1, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Removed  | Fallback   | True  |
| 297 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Done       | True  |
| 298 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Done       | True  |
| 299 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 90                                  | Done     | Done       | True  |
| 300 | Tensor<[1, 218, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 90,<br>Optional[int] end = 218                                 | Done     | Done       | True  |
| 301 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 302 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 303 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 304 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 305 | Tensor<[1, 23, 40, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 306 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 307 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Done     | Done       | True  |
| 308 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 309 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                      | Done     | Done       | True  |
| 310 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 311 | Tensor<[1, 236, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 312 | Tensor<[1, 236, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 236                                 | Done     | Done       | True  |
| 313 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 314 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 12                                    | Done     | Done       | True  |
| 315 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 12,<br>Optional[int] end = 24                                   | Done     | Done       | True  |
| 316 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 317 | Tensor<[1, 24, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 318 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 319 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 120                                  | Done     | Done       | True  |
| 320 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 120,<br>Optional[int] end = 240                                | Done     | Done       | True  |
| 321 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 322 | Tensor<[1, 240, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 323 | Tensor<[1, 24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 324 | Tensor<[1, 24]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 325 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 326 | Tensor<[1, 256, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                | Done     | Done       | True  |
| 327 | Tensor<[1, 256, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                              | Done     | Done       | True  |
| 328 | Tensor<[1, 256, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Done     | Done       | True  |
| 329 | Tensor<[1, 256, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                                | Done     | Done       | True  |
| 330 | Tensor<[1, 256, 64, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Done     | Done       | True  |
| 331 | Tensor<[1, 256, 64, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                                | Done     | Done       | True  |
| 332 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 333 | Tensor<[1, 25]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 334 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Done       | True  |
| 335 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 112,<br>Optional[int] end = 128                                | Done     | Done       | True  |
| 336 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 262                                | Done     | Done       | True  |
| 337 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 32                                  | Done     | Done       | True  |
| 338 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 32,<br>Optional[int] end = 48                                  | Done     | Done       | True  |
| 339 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 48,<br>Optional[int] end = 64                                  | Done     | Done       | True  |
| 340 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 80                                  | Done     | Done       | True  |
| 341 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 96                                  | Done     | Done       | True  |
| 342 | Tensor<[1, 262, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 96,<br>Optional[int] end = 112                                 | Done     | Done       | True  |
| 343 | Tensor<[1, 276, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 344 | Tensor<[1, 276, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 276                                 | Done     | Done       | True  |
| 345 | Tensor<[1, 28, 28, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 346 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 347 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 348 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 349 | Tensor<[1, 28, 28, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 350 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 351 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 352 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 353 | Tensor<[1, 28, 28, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 354 | Tensor<[1, 28, 28, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 355 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 356 | Tensor<[1, 28, 56, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 357 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 358 | Tensor<[1, 28, 56, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 359 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                   | Done     | Done       | True  |
| 360 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 44                                  | Done     | Done       | True  |
| 361 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 168,<br>Optional[int] end = 296                                | Done     | Done       | True  |
| 362 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 44,<br>Optional[int] end = 90                                  | Done     | Done       | True  |
| 363 | Tensor<[1, 296, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 90,<br>Optional[int] end = 168                                 | Done     | Done       | True  |
| 364 | Tensor<[1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 365 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 366 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 367 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 368 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 369 | Tensor<[1, 304, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 370 | Tensor<[1, 304, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 304                                | Done     | Done       | True  |
| 371 | Tensor<[1, 304, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Done       | True  |
| 372 | Tensor<[1, 310, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 373 | Tensor<[1, 310, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Done       | True  |
| 374 | Tensor<[1, 310, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 310                                 | Done     | Done       | True  |
| 375 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 376 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 377 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 378 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 379 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 380 | Tensor<[1, 32, 32, 192]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 381 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 382 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 383 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 384 | Tensor<[1, 32, 32, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 385 | Tensor<[1, 32, 32, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 386 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 387 | Tensor<[1, 32, 64, 128]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 388 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 389 | Tensor<[1, 32, 64, 96]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 390 | Tensor<[1, 320]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 391 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                          | Done     | Done       | True  |
| 392 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 393 | Tensor<[1, 320]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 9223372036854775807                        | Done     | Done       | True  |
| 394 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 395 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 100,<br>Optional[int] end = 120                                | Done     | Done       | True  |
| 396 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 120,<br>Optional[int] end = 140                                | Done     | Done       | True  |
| 397 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 140,<br>Optional[int] end = 160                                | Done     | Done       | True  |
| 398 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 328                                | Done     | Done       | True  |
| 399 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 40                                  | Done     | Done       | True  |
| 400 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 60                                  | Done     | Done       | True  |
| 401 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 60,<br>Optional[int] end = 80                                  | Done     | Done       | True  |
| 402 | Tensor<[1, 328, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 100                                 | Done     | Done       | True  |
| 403 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 404 | Tensor<[1, 360, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 405 | Tensor<[1, 360, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 360                                 | Done     | Done       | True  |
| 406 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 407 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 112,<br>Optional[int] end = 368                                | Done     | Done       | True  |
| 408 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Done       | True  |
| 409 | Tensor<[1, 368, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 112                                 | Done     | Done       | True  |
| 410 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 192                                  | Done     | Done       | True  |
| 411 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 96                                   | Done     | Done       | True  |
| 412 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 288                                | Done     | Done       | True  |
| 413 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 384                                | Done     | Done       | True  |
| 414 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 288,<br>Optional[int] end = 384                                | Done     | Done       | True  |
| 415 | Tensor<[1, 384, 35, 35]> self = ?,<br>int dim = 1,<br>Optional[int] start = 96,<br>Optional[int] end = 192                                 | Done     | Done       | True  |
| 416 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 417 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 418 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                    | Done     | Done       | True  |
| 419 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 420 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 421 | Tensor<[1, 40, 28, 28]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 422 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 423 | Tensor<[1, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                                             | Done     | Done       | True  |
| 424 | Tensor<[1, 4150, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 425 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 426 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = 9223372036854775807                 | Done     | Done       | True  |
| 427 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = -100                                   | Done     | Done       | True  |
| 428 | Tensor<[1, 428, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 429 | Tensor<[1, 428, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 428                                | Done     | Done       | True  |
| 430 | Tensor<[1, 428, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Done       | True  |
| 431 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 128                                  | Done     | Done       | True  |
| 432 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 128,<br>Optional[int] end = 256                                | Done     | Done       | True  |
| 433 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 320                                | Done     | Done       | True  |
| 434 | Tensor<[1, 448, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 448                                | Done     | Done       | True  |
| 435 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 64                                   | Done     | Done       | True  |
| 436 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 192,<br>Optional[int] end = 320                                | Done     | Done       | True  |
| 437 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 448                                | Done     | Done       | True  |
| 438 | Tensor<[1, 448, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 64,<br>Optional[int] end = 192                                 | Done     | Done       | True  |
| 439 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 440 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                   | Done     | Done       | True  |
| 441 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 112,<br>Optional[int] end = 210                                | Done     | Done       | True  |
| 442 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 54                                  | Done     | Done       | True  |
| 443 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 210,<br>Optional[int] end = 466                                | Done     | Done       | True  |
| 444 | Tensor<[1, 466, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 54,<br>Optional[int] end = 112                                 | Done     | Done       | True  |
| 445 | Tensor<[1, 46]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 446 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | True  |
| 447 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 448 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                                  | Done     | Done       | True  |
| 449 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 1,<br>Optional[int] start = 24,<br>Optional[int] end = 48                                 | Done     | Done       | True  |
| 450 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 451 | Tensor<[1, 48, 112, 112]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Removed  | Fallback   | True  |
| 452 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 453 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 240                                  | Done     | Done       | True  |
| 454 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 240,<br>Optional[int] end = 480                                | Done     | Done       | True  |
| 455 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 456 | Tensor<[1, 480, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 457 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 458 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 459 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 460 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 461 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
| 462 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2   | Unknown  | Fallback   | True  |
| 463 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 464 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 465 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 466 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                     | Unknown  | Done       | True  |
| 467 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 468 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
| 469 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                        | Unknown  | Fallback   | True  |
| 470 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Removed  | Fallback   | True  |
| 471 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
| 472 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                        | Done     | Done       | True  |
| 473 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 50                                       | Done     | Done       | True  |
| 474 | Tensor<[1, 512, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Done       | True  |
| 475 | Tensor<[1, 512, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Done       | True  |
| 476 | Tensor<[1, 512, 32, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Done       | True  |
| 477 | Tensor<[1, 512, 32, 32]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Done       | True  |
| 478 | Tensor<[1, 512, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Done       | True  |
| 479 | Tensor<[1, 512, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Done       | True  |
| 480 | Tensor<[1, 512, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                    | Done     | Done       | True  |
| 481 | Tensor<[1, 512, 8, 8]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                  | Done     | Done       | True  |
| 482 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 483 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 12                                           | Done     | Done       | True  |
| 484 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                           | Done     | Done       | True  |
| 485 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                           | Done     | Done       | True  |
| 486 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 25                                           | None     | Fallback   | True  |
| 487 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                          | Done     | Done       | True  |
| 488 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                                            | Done     | Done       | True  |
| 489 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9                                            | None     | Fallback   | True  |
| 490 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 491 | Tensor<[1, 514]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 10                                           | Done     | Done       | True  |
| 492 | Tensor<[1, 54, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                    | Done     | Unknown    | N/A   |
| 493 | Tensor<[1, 54, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 54                                   | Done     | Unknown    | N/A   |
| 494 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 495 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 224                                | Done     | Done       | True  |
| 496 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 224,<br>Optional[int] end = 544                                | Done     | Done       | True  |
| 497 | Tensor<[1, 544, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Done       | True  |
| 498 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 499 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 500 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 501 | Tensor<[1, 56, 56, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 502 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 503 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 504 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 505 | Tensor<[1, 56, 56, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 506 | Tensor<[1, 59]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 507 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 508 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 509 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 510 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 511 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 512 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
| 513 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 514 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 515 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 516 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 517 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 518 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 519 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 520 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 521 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Done       | True  |
| 522 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 523 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 524 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 525 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 526 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 527 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 528 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 529 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 530 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 531 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 532 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Fallback   | True  |
| 533 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 534 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                                      | Done     | Done       | True  |
| 535 | Tensor<[1, 60]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Fallback   | True  |
| 536 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>Optional[int] start = 59,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Done       | True  |
| 537 | Tensor<[1, 62, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                    | Done     | Done       | True  |
| 538 | Tensor<[1, 62, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 62                                   | Done     | Done       | True  |
| 539 | Tensor<[1, 64, 256, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                  | Done     | Done       | True  |
| 540 | Tensor<[1, 64, 256, 256]> self = ?,<br>int dim = 1,<br>Optional[int] start = 32,<br>Optional[int] end = 64                                 | Done     | Done       | True  |
| 541 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 542 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 543 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2 | None     | Fallback   | True  |
| 544 | Tensor<[1, 64, 64, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 545 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 546 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 547 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 548 | Tensor<[1, 64, 64, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 549 | Tensor<[1, 640]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 550 | Tensor<[1, 640]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 551 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 552 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 553 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 120,<br>Optional[int] end = 160                                | Done     | Done       | True  |
| 554 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 200                                | Done     | Done       | True  |
| 555 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 200,<br>Optional[int] end = 240                                | Done     | Done       | True  |
| 556 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 240,<br>Optional[int] end = 280                                | Done     | Done       | True  |
| 557 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 280,<br>Optional[int] end = 320                                | Done     | Done       | True  |
| 558 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 654                                | Done     | Done       | True  |
| 559 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 80                                  | Done     | Done       | True  |
| 560 | Tensor<[1, 654, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 80,<br>Optional[int] end = 120                                 | Done     | Done       | True  |
| 561 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 562 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 336                                  | Done     | Done       | True  |
| 563 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 336,<br>Optional[int] end = 672                                | Done     | Done       | True  |
| 564 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 565 | Tensor<[1, 672, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Removed  | Fallback   | True  |
| 566 | Tensor<[1, 6]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 567 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 5,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Done       | True  |
| 568 | Tensor<[1, 7, 14, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 569 | Tensor<[1, 7, 14, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 570 | Tensor<[1, 7, 14, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 571 | Tensor<[1, 7, 14, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 572 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 573 | Tensor<[1, 7, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 574 | Tensor<[1, 7, 7, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 575 | Tensor<[1, 7, 7, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 576 | Tensor<[1, 7, 7, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 577 | Tensor<[1, 7, 7, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 578 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 579 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                                     | Done     | Done       | True  |
| 580 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 581 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                                     | Unknown  | Done       | True  |
| 582 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | True  |
| 583 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 584 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 36                                    | Done     | Done       | True  |
| 585 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 36,<br>Optional[int] end = 72                                   | Done     | Done       | True  |
| 586 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 587 | Tensor<[1, 72, 56, 56]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 588 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Done       | True  |
| 589 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 416                                | Done     | Done       | True  |
| 590 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 416,<br>Optional[int] end = 576                                | Done     | Done       | True  |
| 591 | Tensor<[1, 736, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 576,<br>Optional[int] end = 736                                | Done     | Done       | True  |
| 592 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                   | Done     | Done       | True  |
| 593 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 108,<br>Optional[int] end = 224                                | Done     | Done       | True  |
| 594 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 224,<br>Optional[int] end = 420                                | Done     | Done       | True  |
| 595 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 108                                 | Done     | Done       | True  |
| 596 | Tensor<[1, 740, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 420,<br>Optional[int] end = 740                                | Done     | Done       | True  |
| 597 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Removed  | Fallback   | True  |
| 598 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Removed  | Fallback   | True  |
| 599 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                             | Done     | Done       | True  |
| 600 | Tensor<[1, 78, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 20                                    | Done     | Done       | True  |
| 601 | Tensor<[1, 78, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 20,<br>Optional[int] end = 78                                   | Done     | Done       | True  |
| 602 | Tensor<[1, 78, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 14                                    | Done     | Unknown    | N/A   |
| 603 | Tensor<[1, 78, 56, 56]> self = ?,<br>int dim = 1,<br>Optional[int] start = 14,<br>Optional[int] end = 78                                   | Done     | Unknown    | N/A   |
| 604 | Tensor<[1, 782, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                    | Done     | Done       | True  |
| 605 | Tensor<[1, 782, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 320                                  | Done     | Done       | True  |
| 606 | Tensor<[1, 782, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 320,<br>Optional[int] end = 782                                  | Done     | Done       | True  |
| 607 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 608 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 609 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 610 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
| 611 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 612 | Tensor<[1, 8, 16, 384]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 613 | Tensor<[1, 8, 16, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 614 | Tensor<[1, 8, 16, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2  | None     | Fallback   | True  |
| 615 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 616 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 617 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Done       | True  |
| 618 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 619 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 620 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Done       | True  |
| 621 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 622 | Tensor<[1, 8, 8, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 623 | Tensor<[1, 8, 8, 384]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 624 | Tensor<[1, 8, 8, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 625 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 626 | Tensor<[1, 8, 8, 768]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | Fallback   | True  |
| 627 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 628 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 629 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 630 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 631 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   |
| 632 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   |
| 633 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 634 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 40                                    | Done     | Done       | True  |
| 635 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 40,<br>Optional[int] end = 80                                   | Done     | Done       | True  |
| 636 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 637 | Tensor<[1, 80, 14, 14]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Removed  | Fallback   | True  |
| 638 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 639 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 640 | Tensor<[1, 800, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 160                                    | Done     | Done       | True  |
| 641 | Tensor<[1, 800, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 160,<br>Optional[int] end = 800                                  | Done     | Done       | True  |
| 642 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                                  | Done     | Done       | True  |
| 643 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 256,<br>Optional[int] end = 512                                | Done     | Done       | True  |
| 644 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 512,<br>Optional[int] end = 640                                | Done     | Done       | True  |
| 645 | Tensor<[1, 896, 14, 14]> self = ?,<br>int dim = 1,<br>Optional[int] start = 640,<br>Optional[int] end = 896                                | Done     | Done       | True  |
| 646 | Tensor<[1, 8]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Removed  | Fallback   | True  |
| 647 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Removed  | Fallback   | True  |
| 648 | Tensor<[1, 94, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                                    | Done     | Done       | True  |
| 649 | Tensor<[1, 94, 28, 28]> self = ?,<br>int dim = 1,<br>Optional[int] start = 16,<br>Optional[int] end = 94                                   | Done     | Done       | True  |
| 650 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 651 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 480                                    | Done     | Done       | True  |
| 652 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 1,<br>Optional[int] start = 480,<br>Optional[int] end = 960                                  | Done     | Done       | True  |
| 653 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 654 | Tensor<[1, 960, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Removed  | Fallback   | True  |
| 655 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Unknown    | N/A   |
| 656 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Unknown    | N/A   |
| 657 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                           | Unknown  | Unknown    | N/A   |
| 658 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |
| 659 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                       | Unknown  | Unknown    | N/A   |
| 660 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Unknown    | N/A   |
| 661 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Unknown    | N/A   |
| 662 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s10> start = ?,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
| 663 | Tensor<[10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 664 | Tensor<[15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 665 | Tensor<[17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 666 | Tensor<[192, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Fallback   | True  |
| 667 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
| 668 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Removed  | Fallback   | True  |
| 669 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Removed  | Fallback   | True  |
| 670 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                                          | Done     | Done       | True  |
| 671 | Tensor<[24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 672 | Tensor<[25]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                              | Unknown  | Fallback   | True  |
| 673 | Tensor<[2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
| 674 | Tensor<[3234, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
| 675 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                                           | Done     | Done       | True  |
| 676 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 677 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 678 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 679 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 680 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807                         | Done     | Done       | True  |
| 681 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 682 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 683 | Tensor<[3234]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 684 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                               | Unknown  | Fallback   | True  |
| 685 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1                                          | Done     | Done       | True  |
| 686 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 4                                          | Unknown  | Done       | True  |
| 687 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 4,<br>Optional[int] end = 5                                          | Unknown  | Done       | True  |
| 688 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ?                              | Unknown  | Failed     | N/A   |
| 689 | Tensor<[8732, 4]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                         | Unknown  | Fallback   | True  |
| 690 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                                           | Done     | Done       | True  |
| 691 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 692 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 693 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 2        | Unknown  | Fallback   | True  |
| 694 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 695 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807                         | Done     | Done       | True  |
| 696 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 2,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 697 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 3,<br>Optional[int] end = 9223372036854775807,<br>int step = 4        | Unknown  | Fallback   | True  |
| 698 | Tensor<[8732]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                            | Unknown  | Fallback   | True  |
| 699 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   |

