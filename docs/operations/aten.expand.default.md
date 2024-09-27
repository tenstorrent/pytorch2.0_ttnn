### aten.expand.default
|     | ATen Input Variations                                                                           | Status   |
|----:|:------------------------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int]<> size = [1, 1, 1, 16, 2]                       | Unknown  |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int]<> size = [1, 12, 16, 16]                           | Done     |
|   2 | Tensor<[1, 1, 1, 19]> self = ?,<br>List[int]<> size = [1, 1, 19, 19]                            | Done     |
|   3 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int]<> size = [1, 1, 1, 24]                             | Unknown  |
|   4 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int]<> size = [1, 1, 24, 24]                            | Done     |
|   5 | Tensor<[1, 1, 1, 32]> self = ?,<br>List[int]<> size = [1, 1, 32, 32]                            | Done     |
|   6 | Tensor<[1, 1, 1, 45]> self = ?,<br>List[int]<> size = [1, 1, 45, 45]                            | Unknown  |
|   7 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int]<> size = [1, 1, 1, 46]                             | Unknown  |
|   8 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int]<> size = [1, 1, 59, 59]                            | Done     |
|   9 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int]<> size = [1, 1, 1, 60]                             | Unknown  |
|  10 | Tensor<[1, 1, 1, 920]> self = ?,<br>List[int]<> size = [-1, 8, -1, -1]                          | Unknown  |
|  11 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int]<> size = [1, 1, 1, 'torch.Size(s10 + 1)']     | Unknown  |
|  12 | Tensor<[1, 1, 1024]> self = ?,<br>List[int]<> size = [1, -1, -1]                                | Unknown  |
|  13 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int]<> size = [1, 1, -1, -1, -1]                    | Unknown  |
|  14 | Tensor<[1, 1, 1280]> self = ?,<br>List[int]<> size = [1, -1, -1]                                | Unknown  |
|  15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int]<> size = [1, 1, 16384, 256]                   | Unknown  |
|  16 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int]<> size = [1, 1, 16384, 32]                     | Unknown  |
|  17 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int]<> size = [1, 1, 19, 19]                           | Unknown  |
|  18 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int]<> size = [1, 1, 19200, 300]                   | Unknown  |
|  19 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int]<> size = [1, 1, 19200, 64]                     | Unknown  |
|  20 | Tensor<[1, 1, 192]> self = ?,<br>List[int]<> size = [1, -1, -1]                                 | Removed  |
|  21 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int]<> size = [1, 1, 256, 32]                         | Unknown  |
|  22 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int]<> size = [1, 1, 300, 64]                         | Unknown  |
|  23 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int]<> size = [1, 1, 32, 256]                         | Unknown  |
|  24 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int]<> size = [1, 1, 32, 32]                           | Removed  |
|  25 | Tensor<[1, 1, 38, 38]> self = ?,<br>List[int]<> size = [1, 512, 38, 38]                         | Done     |
|  26 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int]<> size = [1, 1, 45, 45]                           | Unknown  |
|  27 | Tensor<[1, 1, 45]> self = ?,<br>List[int]<> size = [1, 1, 45]                                   | Unknown  |
|  28 | Tensor<[1, 1, 512]> self = ?,<br>List[int]<> size = [-1, 'torch.Size(s0)', -1]                  | Unknown  |
|  29 | Tensor<[1, 1, 512]> self = ?,<br>List[int]<> size = [-1, 1, -1]                                 | Unknown  |
|  30 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int]<> size = [1, 1, 59, 59]                           | Unknown  |
|  31 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int]<> size = [1, 1, 64, 300]                         | Unknown  |
|  32 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int]<> size = [1, 71, 64, 7]                            | Unknown  |
|  33 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int]<> size = [1, 71, 7, 64]                            | Unknown  |
|  34 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int]<> size = [2, 1, 7, 7]                               | Done     |
|  35 | Tensor<[1, 1, 768]> self = ?,<br>List[int]<> size = [1, -1, -1]                                 | Removed  |
|  36 | Tensor<[1, 100, 192]> self = ?,<br>List[int]<> size = [1, -1, -1]                               | Removed  |
|  37 | Tensor<[1, 10]> self = ?,<br>List[int]<> size = [1, 10]                                         | Unknown  |
|  38 | Tensor<[1, 10]> self = ?,<br>List[int]<> size = [10, 10]                                        | Done     |
|  39 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int]<> size = [1, 12, 1, 10]                           | Unknown  |
|  40 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int]<> size = [1, 12, 1, 1]                             | Unknown  |
|  41 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int]<> size = [1, 12, 1, 2]                             | Unknown  |
|  42 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int]<> size = [1, 12, 1, 46]                           | Unknown  |
|  43 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int]<> size = [1, 12, 1, 64]                           | Unknown  |
|  44 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int]<> size = [1, 12, 1, 'torch.Size(s0 + 1)']     | Unknown  |
|  45 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int]<> size = [1, 12, 1, 'torch.Size(s10 + 1)']   | Unknown  |
|  46 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int]<> size = [1, 12, 10, 10]                         | Unknown  |
|  47 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int]<> size = [1, 12, 10, 64]                         | Unknown  |
|  48 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int]<> size = [1, 12, 12, 12]                         | Unknown  |
|  49 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int]<> size = [1, 12, 12, 64]                         | Unknown  |
|  50 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int]<> size = [1, 12, 14, 14]                         | Unknown  |
|  51 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int]<> size = [1, 12, 14, 64]                         | Unknown  |
|  52 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int]<> size = [1, 12, 16, 16]                         | Unknown  |
|  53 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int]<> size = [1, 12, 16, 64]                         | Unknown  |
|  54 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int]<> size = [1, 12, 197, 197]                     | Removed  |
|  55 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int]<> size = [1, 12, 197, 64]                       | Removed  |
|  56 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int]<> size = [1, 12, 2, 64]                           | Unknown  |
|  57 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int]<> size = [1, 12, 201, 201]                     | Unknown  |
|  58 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int]<> size = [1, 12, 201, 64]                       | Unknown  |
|  59 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int]<> size = [1, 12, 25, 25]                         | Unknown  |
|  60 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int]<> size = [1, 12, 25, 64]                         | Unknown  |
|  61 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int]<> size = [1, 12, 45, 45]                         | Unknown  |
|  62 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int]<> size = [1, 12, 45, 64]                         | Unknown  |
|  63 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int]<> size = [1, 12, 46, 64]                         | Unknown  |
|  64 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int]<> size = [1, 12, 64, 10]                         | Unknown  |
|  65 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int]<> size = [1, 12, 64, 12]                         | Unknown  |
|  66 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int]<> size = [1, 12, 64, 14]                         | Unknown  |
|  67 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int]<> size = [1, 12, 64, 16]                         | Unknown  |
|  68 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int]<> size = [1, 12, 64, 197]                       | Removed  |
|  69 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int]<> size = [1, 12, 64, 1]                           | Unknown  |
|  70 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int]<> size = [1, 12, 64, 201]                       | Unknown  |
|  71 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int]<> size = [1, 12, 64, 25]                         | Unknown  |
|  72 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int]<> size = [1, 12, 64, 2]                           | Unknown  |
|  73 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int]<> size = [1, 12, 64, 45]                         | Unknown  |
|  74 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int]<> size = [1, 12, 64, 46]                         | Unknown  |
|  75 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int]<> size = [1, 12, 64, 7]                           | Unknown  |
|  76 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int]<> size = [1, 12, 64, 8]                           | Unknown  |
|  77 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int]<> size = [1, 12, 64, 9]                           | Unknown  |
|  78 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int]<> size = [1, 12, 64, 'torch.Size(s0 + 1)']   | Unknown  |
|  79 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int]<> size = [1, 12, 64, 'torch.Size(s10 + 1)'] | Unknown  |
|  80 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int]<> size = [1, 12, 7, 64]                           | Unknown  |
|  81 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int]<> size = [1, 12, 7, 7]                             | Unknown  |
|  82 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int]<> size = [1, 12, 8, 64]                           | Unknown  |
|  83 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int]<> size = [1, 12, 8, 8]                             | Unknown  |
|  84 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int]<> size = [1, 12, 9, 64]                           | Unknown  |
|  85 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int]<> size = [1, 12, 9, 9]                             | Unknown  |
|  86 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int]<> size = [1, 12, 'torch.Size(s0 + 1)', 64]   | Unknown  |
|  87 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int]<> size = [1, 12, 'torch.Size(s10 + 1)', 64] | Unknown  |
|  88 | Tensor<[1, 136]> self = ?,<br>List[int]<> size = [100, 136]                                     | Unknown  |
|  89 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int]<> size = [1, 16, 1, 10]                           | Unknown  |
|  90 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int]<> size = [1, 16, 1, 1]                             | Unknown  |
|  91 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int]<> size = [1, 16, 1, 2]                             | Unknown  |
|  92 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int]<> size = [1, 16, 1, 64]                           | Unknown  |
|  93 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int]<> size = [1, 16, 1, 6]                             | Unknown  |
|  94 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int]<> size = [1, 16, 1, 'torch.Size(s0 + 1)']     | Unknown  |
|  95 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int]<> size = [1, 16, 1, 'torch.Size(s10 + 1)']   | Unknown  |
|  96 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int]<> size = [1, 16, 10, 10]                         | Unknown  |
|  97 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int]<> size = [1, 16, 10, 64]                         | Unknown  |
|  98 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int]<> size = [1, 16, 128, 9]                         | Unknown  |
|  99 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int]<> size = [1, 16, 197, 197]                     | Unknown  |
| 100 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int]<> size = [1, 16, 197, 64]                       | Unknown  |
| 101 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int]<> size = [1, 16, 2, 64]                           | Unknown  |
| 102 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int]<> size = [1, 16, 256, 256]                     | Removed  |
| 103 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int]<> size = [1, 16, 256, 64]                       | Removed  |
| 104 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int]<> size = [1, 16, 5, 5]                             | Unknown  |
| 105 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int]<> size = [1, 16, 5, 64]                           | Unknown  |
| 106 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int]<> size = [1, 16, 6, 64]                           | Unknown  |
| 107 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int]<> size = [1, 16, 64, 10]                         | Unknown  |
| 108 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int]<> size = [1, 16, 64, 197]                       | Unknown  |
| 109 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int]<> size = [1, 16, 64, 1]                           | Unknown  |
| 110 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int]<> size = [1, 16, 64, 256]                       | Removed  |
| 111 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int]<> size = [1, 16, 64, 2]                           | Unknown  |
| 112 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int]<> size = [1, 16, 64, 5]                           | Unknown  |
| 113 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int]<> size = [1, 16, 64, 6]                           | Unknown  |
| 114 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int]<> size = [1, 16, 64, 9]                           | Unknown  |
| 115 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int]<> size = [1, 16, 64, 'torch.Size(s0 + 1)']   | Unknown  |
| 116 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int]<> size = [1, 16, 64, 'torch.Size(s10 + 1)'] | Unknown  |
| 117 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int]<> size = [1, 16, 9, 128]                         | Unknown  |
| 118 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int]<> size = [1, 16, 9, 64]                           | Unknown  |
| 119 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int]<> size = [1, 16, 9, 9]                             | Unknown  |
| 120 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int]<> size = [1, 16, 'torch.Size(s0 + 1)', 64]   | Unknown  |
| 121 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int]<> size = [1, 16, 'torch.Size(s10 + 1)', 64] | Unknown  |
| 122 | Tensor<[1, 16]> self = ?,<br>List[int]<> size = [12, 16]                                        | Unknown  |
| 123 | Tensor<[1, 17]> self = ?,<br>List[int]<> size = [13, 17]                                        | Unknown  |
| 124 | Tensor<[1, 19]> self = ?,<br>List[int]<> size = [19, 19]                                        | Done     |
| 125 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [1, 1]                                           | None     |
| 126 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [1, 512]                                         | Unknown  |
| 127 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int]<> size = [1, 2, 256, 32]                         | Unknown  |
| 128 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int]<> size = [1, 2, 300, 64]                         | Unknown  |
| 129 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int]<> size = [1, 2, 32, 256]                         | Unknown  |
| 130 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int]<> size = [1, 2, 4096, 256]                     | Unknown  |
| 131 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int]<> size = [1, 2, 4096, 32]                       | Unknown  |
| 132 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int]<> size = [1, 2, 4800, 300]                     | Unknown  |
| 133 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int]<> size = [1, 2, 4800, 64]                       | Unknown  |
| 134 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int]<> size = [1, 2, 64, 300]                         | Unknown  |
| 135 | Tensor<[1, 20]> self = ?,<br>List[int]<> size = [20, 20]                                        | Done     |
| 136 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int]<> size = [1, 24, 32, 49]                         | Unknown  |
| 137 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int]<> size = [1, 24, 32, 64]                         | Unknown  |
| 138 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int]<> size = [1, 24, 49, 32]                         | Unknown  |
| 139 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int]<> size = [1, 24, 49, 49]                         | Unknown  |
| 140 | Tensor<[1, 24, 64, 1]> self = ?,<br>List[int]<> size = [1, 24, 64, 32]                          | None     |
| 141 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int]<> size = [1, 24, 64, 32]                         | Unknown  |
| 142 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int]<> size = [1, 24, 64, 64]                         | Unknown  |
| 143 | Tensor<[1, 25]> self = ?,<br>List[int]<> size = [1, 25]                                         | Unknown  |
| 144 | Tensor<[1, 2]> self = ?,<br>List[int]<> size = [2, 2]                                           | Done     |
| 145 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int]<> size = [1, 3, 1445, 1445]                   | Removed  |
| 146 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int]<> size = [1, 3, 1445, 64]                       | Removed  |
| 147 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int]<> size = [1, 3, 64, 1445]                       | Removed  |
| 148 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int]<> size = [1, 32, 32, 49]                         | Unknown  |
| 149 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int]<> size = [1, 32, 32, 64]                         | Unknown  |
| 150 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int]<> size = [1, 32, 49, 32]                         | Unknown  |
| 151 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int]<> size = [1, 32, 49, 49]                         | Unknown  |
| 152 | Tensor<[1, 32, 64, 1]> self = ?,<br>List[int]<> size = [1, 32, 64, 32]                          | None     |
| 153 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int]<> size = [1, 32, 64, 32]                         | Unknown  |
| 154 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int]<> size = [1, 32, 64, 64]                         | Unknown  |
| 155 | Tensor<[1, 34]> self = ?,<br>List[int]<> size = [25, 34]                                        | Unknown  |
| 156 | Tensor<[1, 38]> self = ?,<br>List[int]<> size = [38, 38]                                        | Done     |
| 157 | Tensor<[1, 3]> self = ?,<br>List[int]<> size = [3, 3]                                           | Done     |
| 158 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int]<> size = [1, 5, 1, 16, 2]                       | Unknown  |
| 159 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int]<> size = [1, 5, 1024, 256]                     | Unknown  |
| 160 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int]<> size = [1, 5, 1024, 32]                       | Unknown  |
| 161 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int]<> size = [1, 5, 1200, 300]                     | Unknown  |
| 162 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int]<> size = [1, 5, 1200, 64]                       | Unknown  |
| 163 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int]<> size = [1, 5, 256, 32]                         | Unknown  |
| 164 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int]<> size = [1, 5, 300, 64]                         | Unknown  |
| 165 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int]<> size = [1, 5, 32, 256]                         | Unknown  |
| 166 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int]<> size = [1, 5, 64, 300]                         | Unknown  |
| 167 | Tensor<[1, 5]> self = ?,<br>List[int]<> size = [5, 5]                                           | Done     |
| 168 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int]<> size = [1, 6, 1, 15]                             | Unknown  |
| 169 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int]<> size = [1, 6, 1, 17]                             | Unknown  |
| 170 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int]<> size = [1, 6, 1, 1]                               | Unknown  |
| 171 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int]<> size = [1, 6, 1, 2]                               | Unknown  |
| 172 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int]<> size = [1, 6, 1, 64]                             | Unknown  |
| 173 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int]<> size = [1, 6, 1, 'torch.Size(s0 + 1)']       | Unknown  |
| 174 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int]<> size = [1, 6, 15, 15]                           | Unknown  |
| 175 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int]<> size = [1, 6, 15, 64]                           | Unknown  |
| 176 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int]<> size = [1, 6, 17, 64]                           | Unknown  |
| 177 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int]<> size = [1, 6, 2, 64]                             | Unknown  |
| 178 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int]<> size = [1, 6, 64, 15]                           | Unknown  |
| 179 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int]<> size = [1, 6, 64, 17]                           | Unknown  |
| 180 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int]<> size = [1, 6, 64, 1]                             | Unknown  |
| 181 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int]<> size = [1, 6, 64, 2]                             | Unknown  |
| 182 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int]<> size = [1, 6, 64, 'torch.Size(s0 + 1)']     | Unknown  |
| 183 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int]<> size = [1, 6, 'torch.Size(s0 + 1)', 64]     | Unknown  |
| 184 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int]<> size = [1, 64, 64, 9]                           | Unknown  |
| 185 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int]<> size = [1, 64, 9, 64]                           | Unknown  |
| 186 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int]<> size = [1, 64, 9, 9]                             | Unknown  |
| 187 | Tensor<[1, 68]> self = ?,<br>List[int]<> size = [50, 68]                                        | Unknown  |
| 188 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int]<> size = [1, 71, 7, 64]                           | Unknown  |
| 189 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int]<> size = [1, 71, 7, 7]                             | Unknown  |
| 190 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int]<> size = [1, 8, 1, 10]                             | Unknown  |
| 191 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int]<> size = [1, 8, 1, 1]                               | Unknown  |
| 192 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int]<> size = [1, 8, 1, 2]                               | Unknown  |
| 193 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int]<> size = [1, 8, 1, 64]                             | Unknown  |
| 194 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int]<> size = [1, 8, 1, 'torch.Size(s0 + 1)']       | Unknown  |
| 195 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int]<> size = [1, 8, 10, 10]                           | Unknown  |
| 196 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int]<> size = [1, 8, 10, 64]                           | Unknown  |
| 197 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int]<> size = [1, 8, 2, 64]                             | Unknown  |
| 198 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int]<> size = [1, 8, 2048, 160]                     | Unknown  |
| 199 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int]<> size = [1, 8, 2048, 256]                     | Unknown  |
| 200 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int]<> size = [1, 8, 2048, 32]                       | Unknown  |
| 201 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int]<> size = [1, 8, 256, 160]                       | Unknown  |
| 202 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int]<> size = [1, 8, 256, 2048]                     | Unknown  |
| 203 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int]<> size = [1, 8, 256, 256]                       | Unknown  |
| 204 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int]<> size = [1, 8, 256, 32]                         | Unknown  |
| 205 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int]<> size = [1, 8, 256, 96]                         | Unknown  |
| 206 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int]<> size = [1, 8, 300, 300]                       | Unknown  |
| 207 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int]<> size = [1, 8, 300, 64]                         | Unknown  |
| 208 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int]<> size = [1, 8, 32, 2048]                       | Unknown  |
| 209 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int]<> size = [1, 8, 32, 256]                         | Unknown  |
| 210 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int]<> size = [1, 8, 64, 10]                           | Unknown  |
| 211 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int]<> size = [1, 8, 64, 1]                             | Unknown  |
| 212 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int]<> size = [1, 8, 64, 2]                             | Unknown  |
| 213 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int]<> size = [1, 8, 64, 300]                         | Unknown  |
| 214 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int]<> size = [1, 8, 64, 'torch.Size(s0 + 1)']     | Unknown  |
| 215 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int]<> size = [1, 8, 'torch.Size(s0 + 1)', 64]     | Unknown  |
| 216 | Tensor<[1, 9]> self = ?,<br>List[int]<> size = [7, 9]                                           | Unknown  |
| 217 | Tensor<[10, 1]> self = ?,<br>List[int]<> size = [10, 10]                                        | None     |
| 218 | Tensor<[100, 1]> self = ?,<br>List[int]<> size = [100, 136]                                     | Unknown  |
| 219 | Tensor<[12, 1]> self = ?,<br>List[int]<> size = [12, 16]                                        | Unknown  |
| 220 | Tensor<[13, 1]> self = ?,<br>List[int]<> size = [13, 17]                                        | Unknown  |
| 221 | Tensor<[16, 6, 32, 49]> self = ?,<br>List[int]<> size = [16, 6, 32, 49]                         | Unknown  |
| 222 | Tensor<[16, 6, 32, 64]> self = ?,<br>List[int]<> size = [16, 6, 32, 64]                         | Unknown  |
| 223 | Tensor<[16, 6, 49, 32]> self = ?,<br>List[int]<> size = [16, 6, 49, 32]                         | Unknown  |
| 224 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int]<> size = [16, 6, 49, 49]                         | Unknown  |
| 225 | Tensor<[16, 6, 64, 1]> self = ?,<br>List[int]<> size = [16, 6, 64, 32]                          | None     |
| 226 | Tensor<[16, 6, 64, 32]> self = ?,<br>List[int]<> size = [16, 6, 64, 32]                         | Unknown  |
| 227 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int]<> size = [16, 6, 64, 64]                         | Unknown  |
| 228 | Tensor<[16, 8, 32, 49]> self = ?,<br>List[int]<> size = [16, 8, 32, 49]                         | Unknown  |
| 229 | Tensor<[16, 8, 32, 64]> self = ?,<br>List[int]<> size = [16, 8, 32, 64]                         | Unknown  |
| 230 | Tensor<[16, 8, 49, 32]> self = ?,<br>List[int]<> size = [16, 8, 49, 32]                         | Unknown  |
| 231 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int]<> size = [16, 8, 49, 49]                         | Unknown  |
| 232 | Tensor<[16, 8, 64, 1]> self = ?,<br>List[int]<> size = [16, 8, 64, 32]                          | None     |
| 233 | Tensor<[16, 8, 64, 32]> self = ?,<br>List[int]<> size = [16, 8, 64, 32]                         | Unknown  |
| 234 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int]<> size = [16, 8, 64, 64]                         | Unknown  |
| 235 | Tensor<[19, 1]> self = ?,<br>List[int]<> size = [19, 19]                                        | None     |
| 236 | Tensor<[1]> self = ?,<br>List[int]<> size = [1]                                                 | None     |
| 237 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int]<> size = [2, 1, 7, 7]                               | Done     |
| 238 | Tensor<[2, 1]> self = ?,<br>List[int]<> size = [2, 2]                                           | None     |
| 239 | Tensor<[20, 1]> self = ?,<br>List[int]<> size = [20, 20]                                        | None     |
| 240 | Tensor<[2048, 768]> self = ?,<br>List[int]<> size = [1, -1, -1]                                 | Unknown  |
| 241 | Tensor<[24, 12, 64]> self = ?,<br>List[int]<> size = [24, 12, 64]                               | Unknown  |
| 242 | Tensor<[24, 64, 24]> self = ?,<br>List[int]<> size = [24, 64, 24]                               | Unknown  |
| 243 | Tensor<[25, 1]> self = ?,<br>List[int]<> size = [25, 34]                                        | Unknown  |
| 244 | Tensor<[256, 1280]> self = ?,<br>List[int]<> size = [1, -1, -1]                                 | Unknown  |
| 245 | Tensor<[3, 1]> self = ?,<br>List[int]<> size = [3, 3]                                           | None     |
| 246 | Tensor<[38, 1]> self = ?,<br>List[int]<> size = [38, 38]                                        | None     |
| 247 | Tensor<[4, 12, 32, 49]> self = ?,<br>List[int]<> size = [4, 12, 32, 49]                         | Unknown  |
| 248 | Tensor<[4, 12, 32, 64]> self = ?,<br>List[int]<> size = [4, 12, 32, 64]                         | Unknown  |
| 249 | Tensor<[4, 12, 49, 32]> self = ?,<br>List[int]<> size = [4, 12, 49, 32]                         | Unknown  |
| 250 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int]<> size = [4, 12, 49, 49]                         | Unknown  |
| 251 | Tensor<[4, 12, 64, 1]> self = ?,<br>List[int]<> size = [4, 12, 64, 32]                          | None     |
| 252 | Tensor<[4, 12, 64, 32]> self = ?,<br>List[int]<> size = [4, 12, 64, 32]                         | Unknown  |
| 253 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int]<> size = [4, 12, 64, 64]                         | Unknown  |
| 254 | Tensor<[4, 16, 32, 49]> self = ?,<br>List[int]<> size = [4, 16, 32, 49]                         | Unknown  |
| 255 | Tensor<[4, 16, 32, 64]> self = ?,<br>List[int]<> size = [4, 16, 32, 64]                         | Unknown  |
| 256 | Tensor<[4, 16, 49, 32]> self = ?,<br>List[int]<> size = [4, 16, 49, 32]                         | Unknown  |
| 257 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int]<> size = [4, 16, 49, 49]                         | Unknown  |
| 258 | Tensor<[4, 16, 64, 1]> self = ?,<br>List[int]<> size = [4, 16, 64, 32]                          | None     |
| 259 | Tensor<[4, 16, 64, 32]> self = ?,<br>List[int]<> size = [4, 16, 64, 32]                         | Unknown  |
| 260 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int]<> size = [4, 16, 64, 64]                         | Unknown  |
| 261 | Tensor<[5, 1]> self = ?,<br>List[int]<> size = [5, 5]                                           | None     |
| 262 | Tensor<[50, 1]> self = ?,<br>List[int]<> size = [50, 68]                                        | Unknown  |
| 263 | Tensor<[64, 3, 32, 49]> self = ?,<br>List[int]<> size = [64, 3, 32, 49]                         | Unknown  |
| 264 | Tensor<[64, 3, 32, 64]> self = ?,<br>List[int]<> size = [64, 3, 32, 64]                         | Unknown  |
| 265 | Tensor<[64, 3, 49, 32]> self = ?,<br>List[int]<> size = [64, 3, 49, 32]                         | Unknown  |
| 266 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int]<> size = [64, 3, 49, 49]                         | Unknown  |
| 267 | Tensor<[64, 3, 64, 1]> self = ?,<br>List[int]<> size = [64, 3, 64, 32]                          | None     |
| 268 | Tensor<[64, 3, 64, 32]> self = ?,<br>List[int]<> size = [64, 3, 64, 32]                         | Unknown  |
| 269 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int]<> size = [64, 3, 64, 64]                         | Unknown  |
| 270 | Tensor<[64, 4, 32, 49]> self = ?,<br>List[int]<> size = [64, 4, 32, 49]                         | Unknown  |
| 271 | Tensor<[64, 4, 32, 64]> self = ?,<br>List[int]<> size = [64, 4, 32, 64]                         | Unknown  |
| 272 | Tensor<[64, 4, 49, 32]> self = ?,<br>List[int]<> size = [64, 4, 49, 32]                         | Unknown  |
| 273 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int]<> size = [64, 4, 49, 49]                         | Unknown  |
| 274 | Tensor<[64, 4, 64, 1]> self = ?,<br>List[int]<> size = [64, 4, 64, 32]                          | None     |
| 275 | Tensor<[64, 4, 64, 32]> self = ?,<br>List[int]<> size = [64, 4, 64, 32]                         | Unknown  |
| 276 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int]<> size = [64, 4, 64, 64]                         | Unknown  |
| 277 | Tensor<[7, 1]> self = ?,<br>List[int]<> size = [7, 9]                                           | Unknown  |
| 278 | Tensor<[768]> self = ?,<br>List[int]<> size = [1, 1, -1]                                        | Done     |

