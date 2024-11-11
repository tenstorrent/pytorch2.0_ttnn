### aten.view.default
|      | ATen Input Variations                                                          | Status   | Isolated   | PCC   |
|-----:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|
|    0 | Tensor<[0, 1, 4]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Fallback   | True  |
|    1 | Tensor<[0, 2, 2]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Fallback   | True  |
|    2 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]           | Unknown  | Done       | True  |
|    3 | Tensor<[1, 1, 1, 4, 4]> self = ?,<br>List[int] size = [1, -1, 4]               | Fallback | Done       | True  |
|    4 | Tensor<[1, 1, 1, 4, 91]> self = ?,<br>List[int] size = [1, -1, 91]             | Fallback | Done       | True  |
|    5 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]               | Fallback | Done       | True  |
|    6 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]             | Fallback | Done       | True  |
|    7 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]      | Done     | Done       | True  |
|    8 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 49, 768]        | Done     | Done       | True  |
|    9 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]      | None     | Fallback   | True  |
|   10 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]        | None     | Fallback   | True  |
|   11 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]                  | Unknown  | Done       | True  |
|   12 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]             | Unknown  | Done       | True  |
|   13 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                | Unknown  | Done       | True  |
|   14 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 16, 64]              | Unknown  | Done       | True  |
|   15 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                   | Unknown  | Done       | True  |
|   16 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1024]                      | Fallback | Done       | True  |
|   17 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]              | Unknown  | Done       | True  |
|   18 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]               | Done     | Done       | True  |
|   19 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]         | Unknown  | Done       | True  |
|   20 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]             | Unknown  | Unknown    | N/A   |
|   21 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]              | Unknown  | Done       | True  |
|   22 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | Done       | True  |
|   23 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | True  |
|   24 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300]       | Done     | Done       | True  |
|   25 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Done       | True  |
|   26 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]                   | Unknown  | Done       | True  |
|   27 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | True  |
|   28 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [256]                        | Unknown  | Done       | True  |
|   29 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Done     | Done       | True  |
|   30 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]               | Unknown  | Done       | True  |
|   31 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                   | Done     | Done       | True  |
|   32 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]             | Done     | Done       | True  |
|   33 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                    | Done     | Unknown    | N/A   |
|   34 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]               | Unknown  | Done       | True  |
|   35 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                     | Unknown  | Done       | True  |
|   36 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [384]                        | Fallback | Done       | True  |
|   37 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]          | Unknown  | Fallback   | True  |
|   38 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                   | Unknown  | Done       | True  |
|   39 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                       | Fallback | Done       | True  |
|   40 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]               | Unknown  | Done       | True  |
|   41 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                     | Unknown  | Done       | True  |
|   42 | Tensor<[1, 1, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]               | Unknown  | Done       | True  |
|   43 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]             | Done     | Done       | True  |
|   44 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]    | Done     | Done       | True  |
|   45 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]      | Done     | Done       | True  |
|   46 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]              | Fallback | Done       | True  |
|   47 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [-1, 1, 768]                 | Unknown  | Done       | True  |
|   48 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]              | Done     | Done       | True  |
|   49 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]               | Done     | Done       | True  |
|   50 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                     | Done     | Done       | True  |
|   51 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]                        | Fallback | Done       | True  |
|   52 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]    | Done     | Done       | True  |
|   53 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]      | Done     | Done       | True  |
|   54 | Tensor<[1, 1, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]               | Unknown  | Done       | True  |
|   55 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Done     | Done       | True  |
|   56 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [10, 1024]                 | Done     | Done       | True  |
|   57 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]             | Done     | Done       | True  |
|   58 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, 10, 768]             | Done     | Done       | True  |
|   59 | Tensor<[1, 10, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]            | Done     | Done       | True  |
|   60 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]                 | Done     | Done       | True  |
|   61 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]                 | Done     | Done       | True  |
|   62 | Tensor<[1, 10, 4096]> self = ?,<br>List[int] size = [10, 4096]                 | Done     | Unknown    | N/A   |
|   63 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]              | Done     | Done       | True  |
|   64 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]                   | Done     | Done       | True  |
|   65 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | True  |
|   66 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, 10, 12, 64]             | Done     | Done       | True  |
|   67 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                   | Done     | Done       | True  |
|   68 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]              | Done     | Done       | True  |
|   69 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]                 | Done     | Done       | True  |
|   70 | Tensor<[1, 1000, 1, 1]> self = ?,<br>List[int] size = [1, 1000]                | Fallback | Done       | True  |
|   71 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1, 1000, 1, 1]                | Fallback | Done       | True  |
|   72 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                         | Fallback | Done       | True  |
|   73 | Tensor<[1, 1008, 1, 1]> self = ?,<br>List[int] size = [1, 1008]                | Done     | Done       | True  |
|   74 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, -1]                  | Done     | Done       | True  |
|   75 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]                | Done     | Done       | True  |
|   76 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196]         | None     | Fallback   | True  |
|   77 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]         | None     | Fallback   | True  |
|   78 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]          | Done     | Done       | True  |
|   79 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]           | Done     | Done       | True  |
|   80 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]               | Done     | Done       | True  |
|   81 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] size = [1, 1024, 14, 14]         | Fallback | Done       | True  |
|   82 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]         | Fallback | Done       | True  |
|   83 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1024, 256]               | Unknown  | Done       | True  |
|   84 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]          | Done     | Done       | True  |
|   85 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]               | Done     | Done       | True  |
|   86 | Tensor<[1, 1024, 7, 7]> self = ?,<br>List[int] size = [1, 1024, 49]            | Fallback | Done       | True  |
|   87 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  | Done       | True  |
|   88 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1024, 1, 1]                | None     | Fallback   | True  |
|   89 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                         | Fallback | Done       | True  |
|   90 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                         | None     | Fallback   | True  |
|   91 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10]                             | Fallback | Done       | True  |
|   92 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]               | Unknown  | Done       | True  |
|   93 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]                 | Unknown  | Done       | True  |
|   94 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]                 | Unknown  | Done       | True  |
|   95 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]               | Unknown  | Done       | True  |
|   96 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]               | Unknown  | Done       | True  |
|   97 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   |
|   98 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
|   99 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]             | Done     | Done       | True  |
|  100 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]             | Done     | Done       | True  |
|  101 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12]             | Done     | Done       | True  |
|  102 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64]             | Done     | Done       | True  |
|  103 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]                   | Done     | Done       | True  |
|  104 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [12, 14, 14]             | Done     | Done       | True  |
|  105 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [12, 14, 64]             | Done     | Done       | True  |
|  106 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16]             | Done     | Done       | True  |
|  107 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64]             | Done     | Done       | True  |
|  108 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197]         | None     | Fallback   | True  |
|  109 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]           | None     | Fallback   | True  |
|  110 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]               | Unknown  | Done       | True  |
|  111 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]             | Done     | Done       | True  |
|  112 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]             | Done     | Done       | True  |
|  113 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25]             | Done     | Done       | True  |
|  114 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64]             | Done     | Done       | True  |
|  115 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]                 | Done     | Done       | True  |
|  116 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]             | Unknown  | Done       | True  |
|  117 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]             | Unknown  | Done       | True  |
|  118 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]             | Unknown  | Done       | True  |
|  119 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64]             | None     | Fallback   | True  |
|  120 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, 50, 64]             | Done     | Done       | True  |
|  121 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]             | Done     | Done       | True  |
|  122 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12]             | Done     | Done       | True  |
|  123 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [12, 64, 14]             | Done     | Done       | True  |
|  124 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16]             | Done     | Done       | True  |
|  125 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]           | None     | Fallback   | True  |
|  126 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]               | Unknown  | Done       | True  |
|  127 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25]             | Done     | Done       | True  |
|  128 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]               | Unknown  | Done       | True  |
|  129 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]             | Unknown  | Done       | True  |
|  130 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]             | Unknown  | Done       | True  |
|  131 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7]               | Unknown  | Done       | True  |
|  132 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9]               | Done     | Done       | True  |
|  133 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   |
|  134 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   |
|  135 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64]               | Unknown  | Done       | True  |
|  136 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]                 | Unknown  | Done       | True  |
|  137 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Done     | Done       | True  |
|  138 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]                   | Done     | Done       | True  |
|  139 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64]               | Done     | Done       | True  |
|  140 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]                 | Done     | Done       | True  |
|  141 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   |
|  142 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   |
|  143 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]             | Done     | Done       | True  |
|  144 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]          | Done     | Done       | True  |
|  145 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]           | Done     | Done       | True  |
|  146 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]               | Done     | Done       | True  |
|  147 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]          | Done     | Done       | True  |
|  148 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384]       | Done     | Done       | True  |
|  149 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Unknown  | Done       | True  |
|  150 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]           | Done     | Done       | True  |
|  151 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128]       | Fallback | Done       | True  |
|  152 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]          | Fallback | Done       | True  |
|  153 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]          | None     | Fallback   | True  |
|  154 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280]                | Done     | Done       | True  |
|  155 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]        | Fallback | Done       | True  |
|  156 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]        | Done     | Done       | True  |
|  157 | Tensor<[1, 1280, 37, 37]> self = ?,<br>List[int] size = [1, 1280, 1369]        | Fallback | Done       | True  |
|  158 | Tensor<[1, 1280]> self = ?,<br>List[int] size = [1, 1280, 1, 1]                | None     | Fallback   | True  |
|  159 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]                           | Fallback | Done       | True  |
|  160 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Fallback | Done       | True  |
|  161 | Tensor<[1, 12]> self = ?,<br>List[int] size = [12]                             | Fallback | Done       | True  |
|  162 | Tensor<[1, 1370, 1280]> self = ?,<br>List[int] size = [1370, 1280]             | Done     | Done       | True  |
|  163 | Tensor<[1, 1370, 5120]> self = ?,<br>List[int] size = [1370, 5120]             | Done     | Done       | True  |
|  164 | Tensor<[1, 14, 128]> self = ?,<br>List[int] size = [14, 128]                   | Done     | Done       | True  |
|  165 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int] size = [196, 1024]            | Done     | Done       | True  |
|  166 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int] size = [196, 1536]            | Done     | Done       | True  |
|  167 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int] size = [196, 2048]            | Done     | Done       | True  |
|  168 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 384]    | Fallback | Done       | True  |
|  169 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [196, 384]              | Done     | Done       | True  |
|  170 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 512]    | Fallback | Done       | True  |
|  171 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [196, 512]              | Done     | Done       | True  |
|  172 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int] size = [196, 768]              | Done     | Done       | True  |
|  173 | Tensor<[1, 14, 3072]> self = ?,<br>List[int] size = [14, 3072]                 | Done     | Done       | True  |
|  174 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [1, 14, 12, 64]             | Done     | Done       | True  |
|  175 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [14, 768]                   | Done     | Done       | True  |
|  176 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1, 1445, 3, 64]          | Done     | Done       | True  |
|  177 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]               | Done     | Done       | True  |
|  178 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] size = [1, 1445, 192]          | Done     | Done       | True  |
|  179 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]               | Done     | Done       | True  |
|  180 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]                 | Done     | Done       | True  |
|  181 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]                 | Fallback | Done       | True  |
|  182 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int] size = [-1, 16]                 | Fallback | Done       | True  |
|  183 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]                 | Fallback | Done       | True  |
|  184 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]                  | Done     | Done       | True  |
|  185 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int] size = [-1, 32]                 | Fallback | Done       | True  |
|  186 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                   | Fallback | Done       | True  |
|  187 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int] size = [-1, 4]                   | Fallback | Done       | True  |
|  188 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]              | Done     | Done       | True  |
|  189 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                   | Fallback | Done       | True  |
|  190 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int] size = [-1, 8]                   | Fallback | Done       | True  |
|  191 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]              | Done     | Done       | True  |
|  192 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [15, 384]                   | Done     | Done       | True  |
|  193 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]                   | Done     | Done       | True  |
|  194 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]              | Done     | Done       | True  |
|  195 | Tensor<[1, 1500, 12, 64]> self = ?,<br>List[int] size = [1, 1500, 768]         | Done     | Done       | True  |
|  196 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]             | Done     | Done       | True  |
|  197 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]           | Done     | Done       | True  |
|  198 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, 1500, 12, 64]         | Done     | Done       | True  |
|  199 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]               | Done     | Done       | True  |
|  200 | Tensor<[1, 1512, 1, 1]> self = ?,<br>List[int] size = [1, 1512]                | Done     | Done       | True  |
|  201 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536]                | Done     | Done       | True  |
|  202 | Tensor<[1, 1536]> self = ?,<br>List[int] size = [1, 1536, 1, 1]                | None     | Fallback   | True  |
|  203 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                         | Fallback | Done       | True  |
|  204 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [16, 1, 10]               | Unknown  | Unknown    | N/A   |
|  205 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]           | Fallback | Done       | True  |
|  206 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [16, 1, 1]                 | Unknown  | Unknown    | N/A   |
|  207 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [16, 1, 2]                 | Unknown  | Unknown    | N/A   |
|  208 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int] size = [16, 1, 60]               | Unknown  | Done       | True  |
|  209 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]              | Unknown  | Done       | True  |
|  210 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]               | Unknown  | Done       | True  |
|  211 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                 | Unknown  | Done       | True  |
|  212 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   |
|  213 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
|  214 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [16, 10, 10]             | Done     | Done       | True  |
|  215 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [16, 10, 64]             | Done     | Done       | True  |
|  216 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]             | Done     | Done       | True  |
|  217 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [16, 128, 9]             | Done     | Done       | True  |
|  218 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int] size = [256, 1024]            | None     | Fallback   | True  |
|  219 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]            | Done     | Done       | True  |
|  220 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int] size = [256, 2048]            | Done     | Done       | True  |
|  221 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Unknown  | Fallback   | True  |
|  222 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384]    | Fallback | Done       | True  |
|  223 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [256, 384]              | Done     | Done       | True  |
|  224 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 512]    | Fallback | Done       | True  |
|  225 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [256, 512]              | Done     | Done       | True  |
|  226 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]              | None     | Fallback   | True  |
|  227 | Tensor<[1, 16, 19, 19]> self = ?,<br>List[int] size = [16, 19, 19]             | Done     | Done       | True  |
|  228 | Tensor<[1, 16, 19, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Done     | Done       | True  |
|  229 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197]         | None     | Fallback   | True  |
|  230 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]           | None     | Fallback   | True  |
|  231 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [16, 2, 64]               | Unknown  | Unknown    | N/A   |
|  232 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256]         | Done     | Done       | True  |
|  233 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]           | Done     | Done       | True  |
|  234 | Tensor<[1, 16, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]           | Fallback | Done       | True  |
|  235 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]                 | Done     | Done       | True  |
|  236 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]             | Done     | Done       | True  |
|  237 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]             | Fallback | Done       | True  |
|  238 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]                  | Done     | Done       | True  |
|  239 | Tensor<[1, 16, 38, 38]> self = ?,<br>List[int] size = [1, -1, 4, 38, 38]       | Fallback | Done       | True  |
|  240 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                 | Unknown  | Done       | True  |
|  241 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]               | Unknown  | Done       | True  |
|  242 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int] size = [16, 59, 59]             | Done     | Done       | True  |
|  243 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Done     | Done       | True  |
|  244 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int] size = [-1, 6, 49, 49]       | Done     | Done       | True  |
|  245 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]       | Done     | Done       | True  |
|  246 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]               | Unknown  | Done       | True  |
|  247 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Unknown  | Done       | True  |
|  248 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [16, 64, 10]             | Done     | Done       | True  |
|  249 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]           | None     | Fallback   | True  |
|  250 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [16, 64, 1]               | Unknown  | Unknown    | N/A   |
|  251 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]           | Done     | Done       | True  |
|  252 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [16, 64, 2]               | Unknown  | Unknown    | N/A   |
|  253 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]               | Unknown  | Done       | True  |
|  254 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]               | Unknown  | Done       | True  |
|  255 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]               | Done     | Unknown    | N/A   |
|  256 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   |
|  257 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   |
|  258 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | True  |
|  259 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]                   | Done     | Done       | True  |
|  260 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int] size = [-1, 8, 49, 49]       | Done     | Done       | True  |
|  261 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int] size = [-1, 8, 64, 64]       | Done     | Done       | True  |
|  262 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [16, 9, 128]             | Done     | Done       | True  |
|  263 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]               | Done     | Unknown    | N/A   |
|  264 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]                 | Done     | Done       | True  |
|  265 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]             | Fallback | Done       | True  |
|  266 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   |
|  267 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]        | Unknown  | Unknown    | N/A   |
|  268 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   |
|  269 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]          | Fallback | Done       | True  |
|  270 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]           | None     | Fallback   | True  |
|  271 | Tensor<[1, 160, 256]> self = ?,<br>List[int] size = [1, 160, 16, 16]           | Unknown  | Done       | True  |
|  272 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]          | Done     | Done       | True  |
|  273 | Tensor<[1, 160]> self = ?,<br>List[int] size = [160]                           | Unknown  | Done       | True  |
|  274 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | None     | Fallback   | True  |
|  275 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]             | Done     | Done       | True  |
|  276 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]       | Done     | Done       | True  |
|  277 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [16384, 256]             | Unknown  | Done       | True  |
|  278 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]         | Done     | Done       | True  |
|  279 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]         | Done     | Done       | True  |
|  280 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]         | Done     | Done       | True  |
|  281 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]               | Done     | Done       | True  |
|  282 | Tensor<[1, 1664, 1, 1]> self = ?,<br>List[int] size = [1, 1664]                | Done     | Done       | True  |
|  283 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]                    | Done     | Done       | True  |
|  284 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Done     | Done       | True  |
|  285 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, 19, 16, 64]            | Done     | Done       | True  |
|  286 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [19, 1024]                 | Done     | Done       | True  |
|  287 | Tensor<[1, 19, 256008]> self = ?,<br>List[int] size = [-1, 256008]             | Fallback | Done       | True  |
|  288 | Tensor<[1, 19, 4096]> self = ?,<br>List[int] size = [19, 4096]                 | Done     | Done       | True  |
|  289 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]          | Done     | Done       | True  |
|  290 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]          | Fallback | Done       | True  |
|  291 | Tensor<[1, 1920, 1, 1]> self = ?,<br>List[int] size = [1, 1920]                | Done     | Done       | True  |
|  292 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | None     | Fallback   | True  |
|  293 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]             | Done     | Done       | True  |
|  294 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]       | Fallback | Done       | True  |
|  295 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]         | Done     | Done       | True  |
|  296 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]         | Done     | Done       | True  |
|  297 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]         | Done     | Done       | True  |
|  298 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]               | Done     | Done       | True  |
|  299 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]               | Done     | Done       | True  |
|  300 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]                 | Done     | Done       | True  |
|  301 | Tensor<[1, 196]> self = ?,<br>List[int] size = [196]                           | Fallback | Done       | True  |
|  302 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [1, 197, 16, 64]          | None     | Fallback   | True  |
|  303 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]               | None     | Fallback   | True  |
|  304 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]           | None     | Fallback   | True  |
|  305 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]          | None     | Fallback   | True  |
|  306 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]               | None     | Fallback   | True  |
|  307 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]               | None     | Fallback   | True  |
|  308 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]           | None     | Fallback   | True  |
|  309 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]                 | None     | Fallback   | True  |
|  310 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1, 19]                         | Fallback | Done       | True  |
|  311 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1]                             | Fallback | Done       | True  |
|  312 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                           | None     | Fallback   | True  |
|  313 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                              | Fallback | Done       | True  |
|  314 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                               | Fallback | Done       | True  |
|  315 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]             | Done     | Done       | True  |
|  316 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]             | Done     | Done       | True  |
|  317 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]             | Done     | Done       | True  |
|  318 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]         | Done     | Done       | True  |
|  319 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]           | Done     | Done       | True  |
|  320 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]         | Done     | Done       | True  |
|  321 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]           | Done     | Done       | True  |
|  322 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]             | Done     | Done       | True  |
|  323 | Tensor<[1, 2016, 1, 1]> self = ?,<br>List[int] size = [1, 2016]                | Done     | Done       | True  |
|  324 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048]                | Done     | Done       | True  |
|  325 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160]        | Done     | Done       | True  |
|  326 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]         | Done     | Done       | True  |
|  327 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]          | Done     | Done       | True  |
|  328 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]         | Fallback | Done       | True  |
|  329 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [-1, 768]                 | Done     | Unknown    | N/A   |
|  330 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]               | Done     | Done       | True  |
|  331 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]          | Done     | Done       | True  |
|  332 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]                   | Unknown  | Done       | True  |
|  333 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 2048, 1, 1]                | None     | Fallback   | True  |
|  334 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [2048]                         | Fallback | Done       | True  |
|  335 | Tensor<[1, 21843]> self = ?,<br>List[int] size = [21843]                       | Fallback | Done       | True  |
|  336 | Tensor<[1, 2208, 1, 1]> self = ?,<br>List[int] size = [1, 2208]                | Done     | Done       | True  |
|  337 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128]      | Fallback | Done       | True  |
|  338 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                     | Done     | Done       | True  |
|  339 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]           | Fallback | Done       | True  |
|  340 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]       | Fallback | Done       | True  |
|  341 | Tensor<[1, 24, 19, 19]> self = ?,<br>List[int] size = [1, -1, 4, 19, 19]       | Fallback | Done       | True  |
|  342 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]           | Fallback | Done       | True  |
|  343 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]       | Fallback | Done       | True  |
|  344 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]           | Fallback | Done       | True  |
|  345 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]                 | Done     | Done       | True  |
|  346 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [24, 32, 49]             | Done     | Done       | True  |
|  347 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]             | Done     | Done       | True  |
|  348 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [24, 49, 32]             | Done     | Done       | True  |
|  349 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [24, 49, 49]             | Done     | Done       | True  |
|  350 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]           | Fallback | Done       | True  |
|  351 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]             | Done     | Done       | True  |
|  352 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]             | Done     | Done       | True  |
|  353 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | True  |
|  354 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, 24, 12, 64]             | Done     | Done       | True  |
|  355 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]                   | Done     | Done       | True  |
|  356 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] size = [1, 25, 768]             | Done     | Done       | True  |
|  357 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]                 | Done     | Done       | True  |
|  358 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [1, 25, 12, 64]             | Done     | Done       | True  |
|  359 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]                   | Done     | Done       | True  |
|  360 | Tensor<[1, 2520, 1, 1]> self = ?,<br>List[int] size = [1, 2520]                | Done     | Done       | True  |
|  361 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Unknown  | Fallback   | True  |
|  362 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 16, 64]          | Done     | Done       | True  |
|  363 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]          | Fallback | Done       | True  |
|  364 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]               | Done     | Done       | True  |
|  365 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200]       | Done     | Done       | True  |
|  366 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16384]       | Unknown  | Done       | True  |
|  367 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 256, 8, 160]          | Done     | Done       | True  |
|  368 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]               | Done     | Done       | True  |
|  369 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]           | None     | Fallback   | True  |
|  370 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] size = [1, 256, 1024]          | Done     | Done       | True  |
|  371 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]            | Done     | Done       | True  |
|  372 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]                 | Done     | Done       | True  |
|  373 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128]       | Fallback | Done       | True  |
|  374 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160]       | Fallback | Done       | True  |
|  375 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]             | Unknown  | Done       | True  |
|  376 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]           | Done     | Done       | True  |
|  377 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]            | Done     | Done       | True  |
|  378 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]           | Fallback | Done       | True  |
|  379 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]            | Done     | Done       | True  |
|  380 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                 | Done     | Done       | True  |
|  381 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[int] size = [1, 256, 1024]          | Unknown  | Done       | True  |
|  382 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]             | Unknown  | Done       | True  |
|  383 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]             | Done     | Done       | True  |
|  384 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]                   | Done     | Done       | True  |
|  385 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]          | Fallback | Done       | True  |
|  386 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]               | Done     | Done       | True  |
|  387 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]            | Unknown  | Done       | True  |
|  388 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                 | Done     | Done       | True  |
|  389 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]          | Done     | Done       | True  |
|  390 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]             | Done     | Done       | True  |
|  391 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]                   | Done     | Done       | True  |
|  392 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 16, 16, 16, 16, 3]     | Unknown  | Fallback   | True  |
|  393 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]            | Done     | Done       | True  |
|  394 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                 | Done     | Done       | True  |
|  395 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]          | Done     | Done       | True  |
|  396 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]            | Done     | Done       | True  |
|  397 | Tensor<[1, 256]> self = ?,<br>List[int] size = [256]                           | Unknown  | Done       | True  |
|  398 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                          | Fallback | Done       | True  |
|  399 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int] size = [784, 1024]            | Done     | Done       | True  |
|  400 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 192]    | Fallback | Done       | True  |
|  401 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [784, 192]              | Done     | Done       | True  |
|  402 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 256]    | Fallback | Done       | True  |
|  403 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [784, 256]              | Done     | Done       | True  |
|  404 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int] size = [784, 384]              | Done     | Done       | True  |
|  405 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int] size = [784, 512]              | Done     | Done       | True  |
|  406 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int] size = [784, 768]              | Done     | Done       | True  |
|  407 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445]       | Done     | Done       | True  |
|  408 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]           | Done     | Done       | True  |
|  409 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16]  | None     | Fallback   | True  |
|  410 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]           | Done     | Done       | True  |
|  411 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]            | Done     | Done       | True  |
|  412 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]                 | Done     | Done       | True  |
|  413 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]               | Done     | Done       | True  |
|  414 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]            | Done     | Done       | True  |
|  415 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]                 | Done     | Done       | True  |
|  416 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]            | Done     | Done       | True  |
|  417 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]            | Done     | Done       | True  |
|  418 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]                 | Done     | Done       | True  |
|  419 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]             | Done     | Done       | True  |
|  420 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]                   | Done     | Done       | True  |
|  421 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]            | Done     | Done       | True  |
|  422 | Tensor<[1, 3024, 1, 1]> self = ?,<br>List[int] size = [1, 3024]                | Done     | Done       | True  |
|  423 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                   | Done     | Done       | True  |
|  424 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]                         | Fallback | Done       | True  |
|  425 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]         | Done     | Done       | True  |
|  426 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]                 | Done     | Done       | True  |
|  427 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]             | None     | Fallback   | True  |
|  428 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]         | Fallback | Done       | True  |
|  429 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]             | Unknown  | Done       | True  |
|  430 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 16, 16]             | Unknown  | Done       | True  |
|  431 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int] size = [1024, 1024]           | Done     | Done       | True  |
|  432 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] size = [1, 1024, 160]          | Unknown  | Done       | True  |
|  433 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192]    | Fallback | Done       | True  |
|  434 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1024, 192]             | Done     | Done       | True  |
|  435 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 256]    | Fallback | Done       | True  |
|  436 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1024, 256]             | Done     | Done       | True  |
|  437 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]             | Done     | Done       | True  |
|  438 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [32, 32, 49]             | Done     | Done       | True  |
|  439 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int] size = [1024, 512]             | Done     | Done       | True  |
|  440 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [32, 32, 64]             | Done     | Done       | True  |
|  441 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]             | Done     | Done       | True  |
|  442 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96]         | None     | Fallback   | True  |
|  443 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [32, 49, 32]             | Done     | Done       | True  |
|  444 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [32, 49, 49]             | Done     | Done       | True  |
|  445 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]                 | Done     | Done       | True  |
|  446 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [32, 64, 32]             | Done     | Done       | True  |
|  447 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [32, 64, 64]             | Done     | Done       | True  |
|  448 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]          | Fallback | Done       | True  |
|  449 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]           | Done     | Done       | True  |
|  450 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]          | Done     | Done       | True  |
|  451 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]                 | Unknown  | Done       | True  |
|  452 | Tensor<[1, 32]> self = ?,<br>List[int] size = [32]                             | Unknown  | Done       | True  |
|  453 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]   | Fallback | Done       | True  |
|  454 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]       | Fallback | Done       | True  |
|  455 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]       | Fallback | Done       | True  |
|  456 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]       | Fallback | Done       | True  |
|  457 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]           | Fallback | Done       | True  |
|  458 | Tensor<[1, 364, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]         | Fallback | Done       | True  |
|  459 | Tensor<[1, 364, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]         | Fallback | Done       | True  |
|  460 | Tensor<[1, 364, 38, 38]> self = ?,<br>List[int] size = [1, -1, 91, 38, 38]     | Fallback | Done       | True  |
|  461 | Tensor<[1, 3712, 1, 1]> self = ?,<br>List[int] size = [1, 3712]                | Done     | Done       | True  |
|  462 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                     | Unknown  | Done       | True  |
|  463 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3]                               | Fallback | Done       | True  |
|  464 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int] size = [-1, 12, 49, 49]      | Done     | Done       | True  |
|  465 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]      | Done     | Done       | True  |
|  466 | Tensor<[1, 4, 12, 64]> self = ?,<br>List[int] size = [1, 4, 768]               | Unknown  | Done       | True  |
|  467 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int] size = [-1, 16, 49, 49]      | Done     | Done       | True  |
|  468 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int] size = [-1, 16, 64, 64]      | Done     | Done       | True  |
|  469 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]                   | Unknown  | Done       | True  |
|  470 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]              | Unknown  | Done       | True  |
|  471 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, 4, 12, 64]               | Unknown  | Done       | True  |
|  472 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]                     | Unknown  | Done       | True  |
|  473 | Tensor<[1, 400, 1, 1]> self = ?,<br>List[int] size = [1, 400]                  | Done     | Done       | True  |
|  474 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]             | Unknown  | Done       | True  |
|  475 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | Done       | True  |
|  476 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]               | Done     | Done       | True  |
|  477 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]            | Unknown  | Done       | True  |
|  478 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]          | Unknown  | Done       | True  |
|  479 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]               | Unknown  | Done       | True  |
|  480 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]           | Done     | Done       | True  |
|  481 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]            | Done     | Done       | True  |
|  482 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]                 | Done     | Done       | True  |
|  483 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]            | Unknown  | Done       | True  |
|  484 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                   | Unknown  | Done       | True  |
|  485 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [4096]                         | Fallback | Done       | True  |
|  486 | Tensor<[1, 440, 1, 1]> self = ?,<br>List[int] size = [1, 440]                  | Done     | Done       | True  |
|  487 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] size = [1, 45, 768]             | Unknown  | Done       | True  |
|  488 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                 | Unknown  | Done       | True  |
|  489 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [-1, 45, 768]               | Unknown  | Done       | True  |
|  490 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [1, 45, 12, 64]             | Unknown  | Done       | True  |
|  491 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                   | Unknown  | Done       | True  |
|  492 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                         | Unknown  | Done       | True  |
|  493 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]          | Done     | Done       | True  |
|  494 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]           | Done     | Done       | True  |
|  495 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]               | Done     | Done       | True  |
|  496 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]          | Done     | Done       | True  |
|  497 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]               | Done     | Done       | True  |
|  498 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 1024]      | Fallback | Done       | True  |
|  499 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [49, 1024]                 | Done     | Done       | True  |
|  500 | Tensor<[1, 49, 2304]> self = ?,<br>List[int] size = [1, 49, 3, 24, 32]         | None     | Fallback   | True  |
|  501 | Tensor<[1, 49, 3072]> self = ?,<br>List[int] size = [1, 49, 3, 32, 32]         | None     | Fallback   | True  |
|  502 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 768]        | Fallback | Done       | True  |
|  503 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [49, 768]                   | Done     | Done       | True  |
|  504 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                           | Unknown  | Done       | True  |
|  505 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]           | Unknown  | Done       | True  |
|  506 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]         | Done     | Done       | True  |
|  507 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]           | Done     | Done       | True  |
|  508 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                | Unknown  | Done       | True  |
|  509 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                   | Unknown  | Done       | True  |
|  510 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]         | Done     | Done       | True  |
|  511 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]           | Done     | Done       | True  |
|  512 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]         | Unknown  | Done       | True  |
|  513 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]              | Unknown  | Done       | True  |
|  514 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]             | Done     | Done       | True  |
|  515 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]             | Done     | Done       | True  |
|  516 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]               | Unknown  | Done       | True  |
|  517 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]             | Done     | Done       | True  |
|  518 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]          | Unknown  | Fallback   | True  |
|  519 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                   | Unknown  | Done       | True  |
|  520 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]             | Done     | Done       | True  |
|  521 | Tensor<[1, 50, 1024]> self = ?,<br>List[int] size = [50, 1024]                 | Done     | Done       | True  |
|  522 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768]             | Fallback | Done       | True  |
|  523 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]                 | None     | Fallback   | True  |
|  524 | Tensor<[1, 50, 4096]> self = ?,<br>List[int] size = [50, 4096]                 | Done     | Done       | True  |
|  525 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | None     | Fallback   | True  |
|  526 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64]             | None     | Fallback   | True  |
|  527 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]                   | None     | Fallback   | True  |
|  528 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                 | Unknown  | Done       | True  |
|  529 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]                 | Unknown  | Done       | True  |
|  530 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512]                  | Done     | Done       | True  |
|  531 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]           | Done     | Done       | True  |
|  532 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]          | Fallback | Done       | True  |
|  533 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]          | None     | Fallback   | True  |
|  534 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] size = [1, 25088]                | Fallback | Done       | True  |
|  535 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                 | Unknown  | Done       | True  |
|  536 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                     | Unknown  | Done       | True  |
|  537 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512, 1, 1]                  | None     | Fallback   | True  |
|  538 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]                           | Fallback | Done       | True  |
|  539 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]                 | Fallback | Done       | True  |
|  540 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]         | Fallback | Done       | True  |
|  541 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10]     | Fallback | Done       | True  |
|  542 | Tensor<[1, 546, 19, 19]> self = ?,<br>List[int] size = [1, -1, 91, 19, 19]     | Fallback | Done       | True  |
|  543 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]         | Fallback | Done       | True  |
|  544 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20]     | Fallback | Done       | True  |
|  545 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]         | Fallback | Done       | True  |
|  546 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]         | Fallback | Done       | True  |
|  547 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 128]    | Fallback | Done       | True  |
|  548 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [3136, 128]             | Done     | Done       | True  |
|  549 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int] size = [3136, 384]             | Done     | Done       | True  |
|  550 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int] size = [3136, 512]             | Done     | Done       | True  |
|  551 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 96]      | Fallback | Done       | True  |
|  552 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [3136, 96]               | Done     | Done       | True  |
|  553 | Tensor<[1, 576, 1, 1]> self = ?,<br>List[int] size = [1, 576]                  | Done     | Done       | True  |
|  554 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]                 | Done     | Done       | True  |
|  555 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Done     | Done       | True  |
|  556 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, 59, 16, 64]            | Done     | Done       | True  |
|  557 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]                 | Done     | Done       | True  |
|  558 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]                   | Done     | Done       | True  |
|  559 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]                         | Fallback | Done       | True  |
|  560 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                           | Unknown  | Done       | True  |
|  561 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | True  |
|  562 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]                 | Unknown  | Done       | True  |
|  563 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]                 | Unknown  | Done       | True  |
|  564 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]                   | Unknown  | Done       | True  |
|  565 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]                   | Unknown  | Done       | True  |
|  566 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]                 | Unknown  | Done       | True  |
|  567 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   |
|  568 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]               | Done     | Done       | True  |
|  569 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]               | Done     | Done       | True  |
|  570 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]               | Unknown  | Done       | True  |
|  571 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]                 | Unknown  | Done       | True  |
|  572 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]               | Done     | Done       | True  |
|  573 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]               | Unknown  | Done       | True  |
|  574 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]                 | Unknown  | Done       | True  |
|  575 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]                 | Unknown  | Done       | True  |
|  576 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   |
|  577 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   |
|  578 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 1024]      | Fallback | Done       | True  |
|  579 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [64, 1024]                 | Done     | Done       | True  |
|  580 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]                | Done     | Done       | True  |
|  581 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]         | Done     | Done       | True  |
|  582 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]             | Done     | Done       | True  |
|  583 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]             | None     | Fallback   | True  |
|  584 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]         | Fallback | Done       | True  |
|  585 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                    | Done     | Unknown    | N/A   |
|  586 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]         | None     | Fallback   | True  |
|  587 | Tensor<[1, 64, 256]> self = ?,<br>List[int] size = [1, 64, 16, 16]             | Unknown  | Done       | True  |
|  588 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int] size = [-1, 3, 49, 49]       | Done     | Done       | True  |
|  589 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]       | Done     | Done       | True  |
|  590 | Tensor<[1, 64, 3072]> self = ?,<br>List[int] size = [1, 64, 3, 32, 32]         | None     | Fallback   | True  |
|  591 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]                  | Done     | Unknown    | N/A   |
|  592 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int] size = [-1, 4, 49, 49]       | Done     | Done       | True  |
|  593 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int] size = [-1, 4, 64, 64]       | Done     | Done       | True  |
|  594 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]            | Fallback | Done       | True  |
|  595 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]    | Fallback | Done       | True  |
|  596 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]             | Done     | Done       | True  |
|  597 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]          | Unknown  | Done       | True  |
|  598 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]             | Done     | Done       | True  |
|  599 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int] size = [4096, 512]             | Done     | Done       | True  |
|  600 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 4096, 64]            | Unknown  | Done       | True  |
|  601 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]            | Done     | Done       | True  |
|  602 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]      | Fallback | Done       | True  |
|  603 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Done     | Done       | True  |
|  604 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [64, 64, 9]               | Done     | Done       | True  |
|  605 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 768]        | Fallback | Done       | True  |
|  606 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                   | Done     | Done       | True  |
|  607 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [64, 9, 64]               | Done     | Done       | True  |
|  608 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [64, 9, 9]                 | Done     | Done       | True  |
|  609 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]          | Fallback | Done       | True  |
|  610 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]          | Done     | Done       | True  |
|  611 | Tensor<[1, 640]> self = ?,<br>List[int] size = [640]                           | Unknown  | Done       | True  |
|  612 | Tensor<[1, 64]> self = ?,<br>List[int] size = [64]                             | Fallback | Done       | True  |
|  613 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672]                  | Done     | Done       | True  |
|  614 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | True  |
|  615 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768]               | Unknown  | Done       | True  |
|  616 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]                 | Done     | Done       | True  |
|  617 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]                  | Unknown  | Done       | True  |
|  618 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]                   | Done     | Done       | True  |
|  619 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]              | Fallback | Done       | True  |
|  620 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 1024]    | Fallback | Done       | True  |
|  621 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [49, 1024]               | Done     | Done       | True  |
|  622 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int] size = [49, 1536]               | Done     | Done       | True  |
|  623 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int] size = [49, 2048]               | Done     | Done       | True  |
|  624 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int] size = [49, 3072]               | Done     | Done       | True  |
|  625 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int] size = [49, 4096]               | Done     | Done       | True  |
|  626 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 768]      | Fallback | Done       | True  |
|  627 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [49, 768]                 | Done     | Done       | True  |
|  628 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 7, 768]                 | Unknown  | Done       | True  |
|  629 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]                    | Unknown  | Done       | True  |
|  630 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 12, 64]               | Unknown  | Done       | True  |
|  631 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [7, 768]                     | Unknown  | Done       | True  |
|  632 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]               | Done     | Done       | True  |
|  633 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]            | Done     | Done       | True  |
|  634 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [71, 7, 64]               | Done     | Done       | True  |
|  635 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]                 | Done     | Done       | True  |
|  636 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int] size = [1, 7392]                | Done     | Done       | True  |
|  637 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]                  | Done     | Done       | True  |
|  638 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192]           | None     | Fallback   | True  |
|  639 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]           | None     | Fallback   | True  |
|  640 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12]           | Fallback | Done       | True  |
|  641 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14]           | Fallback | Done       | True  |
|  642 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]                 | Done     | Done       | True  |
|  643 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]                 | Done     | Done       | True  |
|  644 | Tensor<[1, 768, 49]> self = ?,<br>List[int] size = [1, 768, 7, 7]              | Fallback | Done       | True  |
|  645 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]              | None     | Fallback   | True  |
|  646 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                     | Done     | Done       | True  |
|  647 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                           | Fallback | Done       | True  |
|  648 | Tensor<[1, 784, 1, 1]> self = ?,<br>List[int] size = [1, 784]                  | Done     | Done       | True  |
|  649 | Tensor<[1, 784]> self = ?,<br>List[int] size = [784]                           | Fallback | Done       | True  |
|  650 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]                           | Unknown  | Done       | True  |
|  651 | Tensor<[1, 7]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | True  |
|  652 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]                 | Unknown  | Done       | True  |
|  653 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]                   | Unknown  | Done       | True  |
|  654 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]                   | Unknown  | Done       | True  |
|  655 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]                 | Unknown  | Done       | True  |
|  656 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]               | Done     | Done       | True  |
|  657 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   |
|  658 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]               | Done     | Done       | True  |
|  659 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]               | Done     | Done       | True  |
|  660 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]                 | Unknown  | Done       | True  |
|  661 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]         | Done     | Done       | True  |
|  662 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]         | Done     | Done       | True  |
|  663 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]           | Done     | Done       | True  |
|  664 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]           | Done     | Done       | True  |
|  665 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]         | Done     | Done       | True  |
|  666 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]           | Done     | Done       | True  |
|  667 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]             | Done     | Done       | True  |
|  668 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]             | Done     | Done       | True  |
|  669 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]           | Done     | Done       | True  |
|  670 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]             | Done     | Done       | True  |
|  671 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]           | Done     | Done       | True  |
|  672 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]             | Done     | Done       | True  |
|  673 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]               | Done     | Done       | True  |
|  674 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]                 | Unknown  | Done       | True  |
|  675 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]                 | Unknown  | Done       | True  |
|  676 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]             | Done     | Done       | True  |
|  677 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   |
|  678 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 1024]    | Fallback | Done       | True  |
|  679 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [64, 1024]               | Done     | Done       | True  |
|  680 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]               | None     | Fallback   | True  |
|  681 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int] size = [64, 2048]               | None     | Fallback   | True  |
|  682 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]               | Done     | Done       | True  |
|  683 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int] size = [64, 4096]               | Done     | Done       | True  |
|  684 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]      | Fallback | Done       | True  |
|  685 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [64, 768]                 | Done     | Done       | True  |
|  686 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   |
|  687 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136] | Fallback | Done       | True  |
|  688 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]     | Fallback | Done       | True  |
|  689 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]     | Fallback | Done       | True  |
|  690 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]     | Fallback | Done       | True  |
|  691 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]         | Fallback | Done       | True  |
|  692 | Tensor<[1, 888, 1, 1]> self = ?,<br>List[int] size = [1, 888]                  | Done     | Done       | True  |
|  693 | Tensor<[1, 8]> self = ?,<br>List[int] size = [-1, 2]                           | Fallback | Done       | True  |
|  694 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [1, 9, 16, 64]              | Done     | Unknown    | N/A   |
|  695 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]                   | Done     | Unknown    | N/A   |
|  696 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]             | Unknown  | Done       | True  |
|  697 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]                     | Done     | Done       | True  |
|  698 | Tensor<[1, 9, 16384]> self = ?,<br>List[int] size = [9, 16384]                 | Done     | Done       | True  |
|  699 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [1, 9, 16, 128]             | Done     | Done       | True  |
|  700 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [9, 2048]                   | Done     | Done       | True  |
|  701 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]                   | Done     | Done       | True  |
|  702 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]               | Unknown  | Done       | True  |
|  703 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [1, 9, 64, 64]              | Done     | Done       | True  |
|  704 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]                   | Done     | Done       | True  |
|  705 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]               | Unknown  | Done       | True  |
|  706 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [1, 9, 12, 64]               | Done     | Done       | True  |
|  707 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                     | Done     | Done       | True  |
|  708 | Tensor<[1, 9, 8192]> self = ?,<br>List[int] size = [9, 8192]                   | Done     | Done       | True  |
|  709 | Tensor<[1, 912, 1, 1]> self = ?,<br>List[int] size = [1, 912]                  | Done     | Done       | True  |
|  710 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]                  | Done     | Done       | True  |
|  711 | Tensor<[1, 9216]> self = ?,<br>List[int] size = [1, 64, 12, 12]                | Fallback | Done       | True  |
|  712 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960]                  | Done     | Done       | True  |
|  713 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]         | Unknown  | Unknown    | N/A   |
|  714 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 1280]   | Unknown  | Unknown    | N/A   |
|  715 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [<s0*s1>, 1280]         | Unknown  | Unknown    | N/A   |
|  716 | Tensor<[1, s0*s1, 2560]> self = ?,<br>List[int] size = [<s0*s1>, 2560]         | Unknown  | Unknown    | N/A   |
|  717 | Tensor<[1, s0*s1, 5120]> self = ?,<br>List[int] size = [<s0*s1>, 5120]         | Unknown  | Unknown    | N/A   |
|  718 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]           | Unknown  | Unknown    | N/A   |
|  719 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 640]     | Unknown  | Unknown    | N/A   |
|  720 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [<s0*s1>, 640]           | Unknown  | Unknown    | N/A   |
|  721 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]         | Unknown  | Unknown    | N/A   |
|  722 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]           | Unknown  | Unknown    | N/A   |
|  723 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]     | Unknown  | Unknown    | N/A   |
|  724 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]       | Unknown  | Unknown    | N/A   |
|  725 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]         | Unknown  | Unknown    | N/A   |
|  726 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 1280]   | Unknown  | Unknown    | N/A   |
|  727 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [<s1*s2>, 1280]         | Unknown  | Unknown    | N/A   |
|  728 | Tensor<[1, s1*s2, 2560]> self = ?,<br>List[int] size = [<s1*s2>, 2560]         | Unknown  | Unknown    | N/A   |
|  729 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]           | Unknown  | Unknown    | N/A   |
|  730 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 320]     | Unknown  | Unknown    | N/A   |
|  731 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [<s1*s2>, 320]           | Unknown  | Unknown    | N/A   |
|  732 | Tensor<[1, s1*s2, 5120]> self = ?,<br>List[int] size = [<s1*s2>, 5120]         | Unknown  | Unknown    | N/A   |
|  733 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]           | Unknown  | Unknown    | N/A   |
|  734 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 640]     | Unknown  | Unknown    | N/A   |
|  735 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [<s1*s2>, 640]           | Unknown  | Unknown    | N/A   |
|  736 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]         | Unknown  | Unknown    | N/A   |
|  737 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]           | Unknown  | Unknown    | N/A   |
|  738 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]           | Unknown  | Unknown    | N/A   |
|  739 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]     | Unknown  | Unknown    | N/A   |
|  740 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]       | Unknown  | Unknown    | N/A   |
|  741 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]       | Unknown  | Unknown    | N/A   |
|  742 | Tensor<[1, s10 + 1]> self = ?,<br>List[int] size = [1, -1]                     | Unknown  | Unknown    | N/A   |
|  743 | Tensor<[10, 1024]> self = ?,<br>List[int] size = [1, 10, 1024]                 | Done     | Done       | True  |
|  744 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]                 | Done     | Done       | True  |
|  745 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002]             | Fallback | Done       | True  |
|  746 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]                 | Done     | Done       | True  |
|  747 | Tensor<[10, 4096]> self = ?,<br>List[int] size = [1, 10, 4096]                 | Done     | Unknown    | N/A   |
|  748 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]                   | Done     | Done       | True  |
|  749 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                   | Done     | Done       | True  |
|  750 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]               | Done     | Done       | True  |
|  751 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]                 | Done     | Done       | True  |
|  752 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 8, 32]               | Done     | Done       | True  |
|  753 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Fallback | Done       | True  |
|  754 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]                 | Done     | Done       | True  |
|  755 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]               | Done     | Done       | True  |
|  756 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]                 | Done     | Done       | True  |
|  757 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]                     | Done     | Done       | True  |
|  758 | Tensor<[100, 8, 32]> self = ?,<br>List[int] size = [100, 256]                  | Done     | Done       | True  |
|  759 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]                   | Fallback | Done       | True  |
|  760 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                            | Fallback | Done       | True  |
|  761 | Tensor<[1024, 1024]> self = ?,<br>List[int] size = [1, 32, 32, 1024]           | Done     | Done       | True  |
|  762 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]               | Done     | Done       | True  |
|  763 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]             | Done     | Done       | True  |
|  764 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [16, 64, 192]                | Done     | Done       | True  |
|  765 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]               | Done     | Done       | True  |
|  766 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256]             | Done     | Done       | True  |
|  767 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [16, 64, 256]                | Done     | Done       | True  |
|  768 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]                | Fallback | Done       | True  |
|  769 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]               | Done     | Done       | True  |
|  770 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]             | Done     | Done       | True  |
|  771 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [16, 64, 768]                | Fallback | Done       | True  |
|  772 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Done     | Done       | True  |
|  773 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
|  774 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | True  |
|  775 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]               | Unknown  | Done       | True  |
|  776 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                 | Unknown  | Done       | True  |
|  777 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                 | Unknown  | Done       | True  |
|  778 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | True  |
|  779 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | True  |
|  780 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   |
|  781 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
|  782 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]             | Done     | Done       | True  |
|  783 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]             | Done     | Done       | True  |
|  784 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]             | Done     | Done       | True  |
|  785 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Done     | Done       | True  |
|  786 | Tensor<[12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]             | Done     | Done       | True  |
|  787 | Tensor<[12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]             | Done     | Done       | True  |
|  788 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]             | Fallback | Done       | True  |
|  789 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]             | Done     | Done       | True  |
|  790 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]         | None     | Fallback   | True  |
|  791 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]           | None     | Fallback   | True  |
|  792 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [1, 12, 24, 24]             | Done     | Done       | True  |
|  793 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]                | Done     | Done       | True  |
|  794 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]             | Done     | Done       | True  |
|  795 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]                | Done     | Done       | True  |
|  796 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]             | Fallback | Done       | True  |
|  797 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]             | Done     | Done       | True  |
|  798 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]                       | Fallback | Done       | True  |
|  799 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]                 | Done     | Done       | True  |
|  800 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | True  |
|  801 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | True  |
|  802 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]             | None     | Fallback   | True  |
|  803 | Tensor<[12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]           | Fallback | Done       | True  |
|  804 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]               | Unknown  | Done       | True  |
|  805 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                 | Unknown  | Done       | True  |
|  806 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]                   | Done     | Done       | True  |
|  807 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]               | Done     | Done       | True  |
|  808 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                 | Fallback | Done       | True  |
|  809 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]             | Done     | Done       | True  |
|  810 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]               | Done     | Done       | True  |
|  811 | Tensor<[128, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]            | Done     | Done       | True  |
|  812 | Tensor<[128, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]            | Done     | Done       | True  |
|  813 | Tensor<[128, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]            | Done     | Done       | True  |
|  814 | Tensor<[128, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]            | Fallback | Done       | True  |
|  815 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       | True  |
|  816 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
|  817 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                    | Done     | Done       | True  |
|  818 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                    | Fallback | Done       | True  |
|  819 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                            | Done     | Done       | True  |
|  820 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 1280]             | Done     | Done       | True  |
|  821 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 16, 80]           | Done     | Done       | True  |
|  822 | Tensor<[1370, 1, 16, 80]> self = ?,<br>List[int] size = [1370, 1280]           | Done     | Done       | True  |
|  823 | Tensor<[1370, 1, 3840]> self = ?,<br>List[int] size = [1370, 1, 3, 1280]       | Done     | Done       | True  |
|  824 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1, 1370, 1280]             | Done     | Done       | True  |
|  825 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1370, 1, 1280]             | Done     | Done       | True  |
|  826 | Tensor<[1370, 3840]> self = ?,<br>List[int] size = [1370, 1, 3840]             | Done     | Done       | True  |
|  827 | Tensor<[1370, 5120]> self = ?,<br>List[int] size = [1, 1370, 5120]             | Done     | Done       | True  |
|  828 | Tensor<[13]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
|  829 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                    | Fallback | Done       | True  |
|  830 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]                  | None     | Fallback   | True  |
|  831 | Tensor<[14, 2]> self = ?,<br>List[int] size = [1, 14, 2]                       | Done     | Done       | True  |
|  832 | Tensor<[14, 3072]> self = ?,<br>List[int] size = [1, 14, 3072]                 | Done     | Done       | True  |
|  833 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]                    | None     | Fallback   | True  |
|  834 | Tensor<[14, 768]> self = ?,<br>List[int] size = [1, 14, 768]                   | Done     | Done       | True  |
|  835 | Tensor<[1444, 8]> self = ?,<br>List[int] size = [-1, 2]                        | Fallback | Done       | True  |
|  836 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]               | Done     | Done       | True  |
|  837 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]               | Done     | Done       | True  |
|  838 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]                 | Done     | Done       | True  |
|  839 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]                   | Done     | Done       | True  |
|  840 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]                   | Done     | Done       | True  |
|  841 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]             | Done     | Done       | True  |
|  842 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]               | Done     | Done       | True  |
|  843 | Tensor<[16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]               | Unknown  | Unknown    | N/A   |
|  844 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                 | Unknown  | Unknown    | N/A   |
|  845 | Tensor<[16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                 | Unknown  | Unknown    | N/A   |
|  846 | Tensor<[16, 1, 60]> self = ?,<br>List[int] size = [1, 16, 1, 60]               | Unknown  | Done       | True  |
|  847 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Done       | True  |
|  848 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Done       | True  |
|  849 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   |
|  850 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
|  851 | Tensor<[16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]             | Done     | Done       | True  |
|  852 | Tensor<[16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]             | Done     | Done       | True  |
|  853 | Tensor<[16, 1370, 80]> self = ?,<br>List[int] size = [1, 16, 1370, 80]         | Fallback | Done       | True  |
|  854 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                    | Done     | Done       | True  |
|  855 | Tensor<[16, 19, 19]> self = ?,<br>List[int] size = [1, 16, 19, 19]             | Done     | Done       | True  |
|  856 | Tensor<[16, 19, 64]> self = ?,<br>List[int] size = [1, 16, 19, 64]             | Done     | Done       | True  |
|  857 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]         | None     | Fallback   | True  |
|  858 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]           | None     | Fallback   | True  |
|  859 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]         | Done     | Done       | True  |
|  860 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]           | Done     | Done       | True  |
|  861 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]                 | Done     | Done       | True  |
|  862 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]             | Done     | Done       | True  |
|  863 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]             | Done     | Done       | True  |
|  864 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 192]       | Fallback | Done       | True  |
|  865 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [784, 192]                 | Done     | Done       | True  |
|  866 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 256]       | Fallback | Done       | True  |
|  867 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [784, 256]                 | Done     | Done       | True  |
|  868 | Tensor<[16, 49, 576]> self = ?,<br>List[int] size = [16, 49, 3, 6, 32]         | None     | Fallback   | True  |
|  869 | Tensor<[16, 49, 768]> self = ?,<br>List[int] size = [16, 49, 3, 8, 32]         | None     | Fallback   | True  |
|  870 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Done       | True  |
|  871 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Done       | True  |
|  872 | Tensor<[16, 50, 64]> self = ?,<br>List[int] size = [1, 16, 50, 64]             | Fallback | Done       | True  |
|  873 | Tensor<[16, 59, 59]> self = ?,<br>List[int] size = [1, 16, 59, 59]             | Done     | Done       | True  |
|  874 | Tensor<[16, 59, 64]> self = ?,<br>List[int] size = [1, 16, 59, 64]             | Done     | Done       | True  |
|  875 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [1, 16, 6, 49, 49]       | Done     | Done       | True  |
|  876 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [96, 49, 49]             | Done     | Done       | True  |
|  877 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64, 64]       | Done     | Done       | True  |
|  878 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]             | Done     | Done       | True  |
|  879 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 192]       | Fallback | Done       | True  |
|  880 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]                | Done     | Done       | True  |
|  881 | Tensor<[16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]           | Fallback | Done       | True  |
|  882 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 256]       | Fallback | Done       | True  |
|  883 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1024, 256]                | Done     | Done       | True  |
|  884 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]         | None     | Fallback   | True  |
|  885 | Tensor<[16, 64, 768]> self = ?,<br>List[int] size = [16, 64, 3, 8, 32]         | None     | Fallback   | True  |
|  886 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]                | None     | Fallback   | True  |
|  887 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]                  | None     | Fallback   | True  |
|  888 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]                   | Done     | Done       | True  |
|  889 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [1, 16, 8, 49, 49]       | Done     | Done       | True  |
|  890 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [128, 49, 49]            | Done     | Done       | True  |
|  891 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [1, 16, 8, 64, 64]       | Done     | Done       | True  |
|  892 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [128, 64, 64]            | Done     | Done       | True  |
|  893 | Tensor<[16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]             | Done     | Done       | True  |
|  894 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]               | Done     | Unknown    | N/A   |
|  895 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                 | Fallback | Done       | True  |
|  896 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]             | Done     | Done       | True  |
|  897 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]             | Done     | Done       | True  |
|  898 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]               | Done     | Done       | True  |
|  899 | Tensor<[16]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | True  |
|  900 | Tensor<[17]> self = ?,<br>List[int] size = [1, -1]                             | Fallback | Done       | True  |
|  901 | Tensor<[19, 1024]> self = ?,<br>List[int] size = [1, 19, 1024]                 | Done     | Done       | True  |
|  902 | Tensor<[19, 256008]> self = ?,<br>List[int] size = [1, 19, 256008]             | Fallback | Done       | True  |
|  903 | Tensor<[19, 4096]> self = ?,<br>List[int] size = [1, 19, 4096]                 | Done     | Done       | True  |
|  904 | Tensor<[192, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]            | Done     | Done       | True  |
|  905 | Tensor<[192, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]            | Done     | Done       | True  |
|  906 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]            | Done     | Done       | True  |
|  907 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]            | Fallback | Done       | True  |
|  908 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]             | Done     | Done       | True  |
|  909 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]               | Done     | Done       | True  |
|  910 | Tensor<[192]> self = ?,<br>List[int] size = [1, 192, 1, 1]                     | Fallback | Done       | True  |
|  911 | Tensor<[196, 1152]> self = ?,<br>List[int] size = [4, 49, 1152]                | Fallback | Done       | True  |
|  912 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [1, 14, 14, 1536]            | Done     | Done       | True  |
|  913 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [4, 49, 1536]                | Fallback | Done       | True  |
|  914 | Tensor<[196, 2048]> self = ?,<br>List[int] size = [1, 14, 14, 2048]            | Done     | Done       | True  |
|  915 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]               | Done     | Done       | True  |
|  916 | Tensor<[196, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]              | Done     | Done       | True  |
|  917 | Tensor<[196, 384]> self = ?,<br>List[int] size = [4, 49, 384]                  | Done     | Done       | True  |
|  918 | Tensor<[196, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]              | Done     | Done       | True  |
|  919 | Tensor<[196, 512]> self = ?,<br>List[int] size = [4, 49, 512]                  | Done     | Done       | True  |
|  920 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]                 | Done     | Done       | True  |
|  921 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 1024]               | Done     | Done       | True  |
|  922 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 16, 64]             | Done     | Done       | True  |
|  923 | Tensor<[197, 1, 12, 64]> self = ?,<br>List[int] size = [197, 768]              | Done     | Done       | True  |
|  924 | Tensor<[197, 1, 16, 64]> self = ?,<br>List[int] size = [197, 1024]             | Done     | Done       | True  |
|  925 | Tensor<[197, 1, 2304]> self = ?,<br>List[int] size = [197, 1, 3, 768]          | Done     | Done       | True  |
|  926 | Tensor<[197, 1, 3072]> self = ?,<br>List[int] size = [197, 1, 3, 1024]         | Done     | Done       | True  |
|  927 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 12, 64]              | Done     | Done       | True  |
|  928 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 768]                 | Done     | Done       | True  |
|  929 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]               | None     | Fallback   | True  |
|  930 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [197, 1, 1024]               | Done     | Done       | True  |
|  931 | Tensor<[197, 197, 12]> self = ?,<br>List[int] size = [38809, 12]               | Fallback | Done       | True  |
|  932 | Tensor<[197, 197, 16]> self = ?,<br>List[int] size = [38809, 16]               | Fallback | Done       | True  |
|  933 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                          | None     | Fallback   | True  |
|  934 | Tensor<[197, 2304]> self = ?,<br>List[int] size = [197, 1, 2304]               | Done     | Done       | True  |
|  935 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]               | None     | Fallback   | True  |
|  936 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [197, 1, 3072]               | Done     | Done       | True  |
|  937 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]               | None     | Fallback   | True  |
|  938 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]                 | None     | Fallback   | True  |
|  939 | Tensor<[197, 768]> self = ?,<br>List[int] size = [197, 1, 768]                 | Done     | Done       | True  |
|  940 | Tensor<[19]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
|  941 | Tensor<[19]> self = ?,<br>List[int] size = [1, -1]                             | Fallback | Done       | True  |
|  942 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                              | Done     | Done       | True  |
|  943 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       | True  |
|  944 | Tensor<[1]> self = ?,<br>List[int] size = [1, 1, 1, 1]                         | Fallback | Done       | True  |
|  945 | Tensor<[2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]             | Unknown  | Done       | True  |
|  946 | Tensor<[2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]             | Unknown  | Done       | True  |
|  947 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]         | Done     | Done       | True  |
|  948 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]           | Done     | Done       | True  |
|  949 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]         | Fallback | Done       | True  |
|  950 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]           | Done     | Done       | True  |
|  951 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]                  | None     | Fallback   | True  |
|  952 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]                    | None     | Fallback   | True  |
|  953 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]               | None     | Fallback   | True  |
|  954 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]                | None     | Fallback   | True  |
|  955 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]                | Done     | Done       | True  |
|  956 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]                           | None     | Fallback   | True  |
|  957 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]               | None     | Fallback   | True  |
|  958 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]                  | None     | Fallback   | True  |
|  959 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]             | Done     | Done       | True  |
|  960 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]               | Done     | Done       | True  |
|  961 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]               | Fallback | Unknown    | N/A   |
|  962 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, 2048, 768]               | Done     | Done       | True  |
|  963 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Done     | Done       | True  |
|  964 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
|  965 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | True  |
|  966 | Tensor<[221, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Done     | Done       | True  |
|  967 | Tensor<[221, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Fallback | Done       | True  |
|  968 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]                | Done     | Done       | True  |
|  969 | Tensor<[225, 16]> self = ?,<br>List[int] size = [1, 15, 15, 16]                | Done     | Done       | True  |
|  970 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]                | Done     | Done       | True  |
|  971 | Tensor<[225, 32]> self = ?,<br>List[int] size = [1, 15, 15, 32]                | Done     | Done       | True  |
|  972 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]                  | Done     | Done       | True  |
|  973 | Tensor<[225, 4]> self = ?,<br>List[int] size = [1, 15, 15, 4]                  | Done     | Done       | True  |
|  974 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]              | Done     | Done       | True  |
|  975 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]                  | Done     | Done       | True  |
|  976 | Tensor<[225, 8]> self = ?,<br>List[int] size = [1, 15, 15, 8]                  | Done     | Done       | True  |
|  977 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]                | Done     | Done       | True  |
|  978 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                | Done     | Done       | True  |
|  979 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]                 | Done     | Done       | True  |
|  980 | Tensor<[24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]             | Done     | Done       | True  |
|  981 | Tensor<[24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]             | Done     | Done       | True  |
|  982 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                | Done     | Done       | True  |
|  983 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]             | Done     | Done       | True  |
|  984 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]             | Done     | Done       | True  |
|  985 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]                   | Done     | Done       | True  |
|  986 | Tensor<[2401, 12]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Done       | True  |
|  987 | Tensor<[2401, 16]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Done       | True  |
|  988 | Tensor<[2401, 24]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Done       | True  |
|  989 | Tensor<[2401, 32]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Done       | True  |
|  990 | Tensor<[2401, 3]> self = ?,<br>List[int] size = [49, 49, -1]                   | Fallback | Done       | True  |
|  991 | Tensor<[2401, 4]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | True  |
|  992 | Tensor<[2401, 6]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | True  |
|  993 | Tensor<[2401, 8]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | True  |
|  994 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                         | Fallback | Done       | True  |
|  995 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]                       | Done     | Done       | True  |
|  996 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]                 | Done     | Done       | True  |
|  997 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]                   | Done     | Done       | True  |
|  998 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]               | Done     | Done       | True  |
|  999 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]                | Fallback | Done       | True  |
| 1000 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]               | Done     | Done       | True  |
| 1001 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]            | Done     | Done       | True  |
| 1002 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [4, 64, 1536]                | Fallback | Done       | True  |
| 1003 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]                 | Done     | Done       | True  |
| 1004 | Tensor<[256, 2048]> self = ?,<br>List[int] size = [1, 16, 16, 2048]            | Done     | Done       | True  |
| 1005 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                 | Done     | Done       | True  |
| 1006 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]                     | Done     | Done       | True  |
| 1007 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]                   | Done     | Done       | True  |
| 1008 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]              | Done     | Done       | True  |
| 1009 | Tensor<[256, 384]> self = ?,<br>List[int] size = [4, 64, 384]                  | Done     | Done       | True  |
| 1010 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]               | Done     | Done       | True  |
| 1011 | Tensor<[256, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]            | Done     | Done       | True  |
| 1012 | Tensor<[256, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]            | Done     | Done       | True  |
| 1013 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512]              | Done     | Done       | True  |
| 1014 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                 | Done     | Done       | True  |
| 1015 | Tensor<[256, 512]> self = ?,<br>List[int] size = [4, 64, 512]                  | Done     | Done       | True  |
| 1016 | Tensor<[256, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]            | Done     | Done       | True  |
| 1017 | Tensor<[256, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]            | Fallback | Done       | True  |
| 1018 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]                   | Done     | Done       | True  |
| 1019 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]                 | Done     | Done       | True  |
| 1020 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       | True  |
| 1021 | Tensor<[25]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
| 1022 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                    | Fallback | Done       | True  |
| 1023 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                              | Fallback | Done       | True  |
| 1024 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       | True  |
| 1025 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]       | Fallback | Done       | True  |
| 1026 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]           | Done     | Done       | True  |
| 1027 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]                 | Done     | Done       | True  |
| 1028 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]               | Done     | Done       | True  |
| 1029 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]                 | Done     | Done       | True  |
| 1030 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]                 | Done     | Done       | True  |
| 1031 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]                   | Done     | Done       | True  |
| 1032 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128]             | Done     | Done       | True  |
| 1033 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [64, 49, 128]                | Done     | Done       | True  |
| 1034 | Tensor<[3136, 288]> self = ?,<br>List[int] size = [64, 49, 288]                | Fallback | Done       | True  |
| 1035 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [1, 56, 56, 384]             | Done     | Done       | True  |
| 1036 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [64, 49, 384]                | Fallback | Done       | True  |
| 1037 | Tensor<[3136, 512]> self = ?,<br>List[int] size = [1, 56, 56, 512]             | Done     | Done       | True  |
| 1038 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]               | Done     | Done       | True  |
| 1039 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [64, 49, 96]                  | Done     | Done       | True  |
| 1040 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]                 | Done     | Done       | True  |
| 1041 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]             | Fallback | Done       | True  |
| 1042 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                    | Done     | Done       | True  |
| 1043 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]                 | Fallback | Done       | True  |
| 1044 | Tensor<[32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]             | Done     | Done       | True  |
| 1045 | Tensor<[32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]             | Done     | Done       | True  |
| 1046 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]                 | Done     | Done       | True  |
| 1047 | Tensor<[32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]             | Done     | Done       | True  |
| 1048 | Tensor<[32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]             | Done     | Done       | True  |
| 1049 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]                   | Unknown  | Done       | True  |
| 1050 | Tensor<[3234, 2, 2]> self = ?,<br>List[int] size = [3234, 4]                   | Unknown  | Done       | True  |
| 1051 | Tensor<[32]> self = ?,<br>List[int] size = [1, 1, 32, 1]                       | Done     | Done       | True  |
| 1052 | Tensor<[3400, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                     | Done     | Done       | True  |
| 1053 | Tensor<[3400, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                     | Fallback | Done       | True  |
| 1054 | Tensor<[34]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | True  |
| 1055 | Tensor<[361, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Fallback | Done       | True  |
| 1056 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]               | None     | Fallback   | True  |
| 1057 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]               | None     | Fallback   | True  |
| 1058 | Tensor<[38]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
| 1059 | Tensor<[38]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | True  |
| 1060 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                              | Fallback | Done       | True  |
| 1061 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                              | Fallback | Done       | True  |
| 1062 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [1, 4, 12, 49, 49]       | Done     | Done       | True  |
| 1063 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [48, 49, 49]             | Done     | Done       | True  |
| 1064 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [1, 4, 12, 64, 64]       | Done     | Done       | True  |
| 1065 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]             | Done     | Done       | True  |
| 1066 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Fallback | Done       | True  |
| 1067 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [1, 4, 16, 49, 49]       | Done     | Done       | True  |
| 1068 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [64, 49, 49]             | Done     | Done       | True  |
| 1069 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [1, 4, 16, 64, 64]       | Done     | Done       | True  |
| 1070 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [64, 64, 64]             | Done     | Done       | True  |
| 1071 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]                   | Unknown  | Done       | True  |
| 1072 | Tensor<[4, 49, 1152]> self = ?,<br>List[int] size = [4, 49, 3, 12, 32]         | None     | Fallback   | True  |
| 1073 | Tensor<[4, 49, 1536]> self = ?,<br>List[int] size = [4, 49, 3, 16, 32]         | None     | Fallback   | True  |
| 1074 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 384]        | Fallback | Done       | True  |
| 1075 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [196, 384]                  | Done     | Done       | True  |
| 1076 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 512]        | Fallback | Done       | True  |
| 1077 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [196, 512]                  | Done     | Done       | True  |
| 1078 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]                 | Unknown  | Done       | True  |
| 1079 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]         | None     | Fallback   | True  |
| 1080 | Tensor<[4, 64, 1536]> self = ?,<br>List[int] size = [4, 64, 3, 16, 32]         | None     | Fallback   | True  |
| 1081 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 384]        | Fallback | Done       | True  |
| 1082 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]                  | Done     | Done       | True  |
| 1083 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 512]        | Fallback | Done       | True  |
| 1084 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [256, 512]                  | Done     | Done       | True  |
| 1085 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]                     | Unknown  | Done       | True  |
| 1086 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Fallback | Done       | True  |
| 1087 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [1, 64, 64, 128]             | Done     | Done       | True  |
| 1088 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [64, 64, 128]                | Done     | Done       | True  |
| 1089 | Tensor<[4096, 12]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | True  |
| 1090 | Tensor<[4096, 16]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | True  |
| 1091 | Tensor<[4096, 24]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | True  |
| 1092 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]             | Unknown  | Done       | True  |
| 1093 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]               | Done     | Done       | True  |
| 1094 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]                | Fallback | Done       | True  |
| 1095 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]               | Unknown  | Done       | True  |
| 1096 | Tensor<[4096, 32]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | True  |
| 1097 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]             | Done     | Done       | True  |
| 1098 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [64, 64, 384]                | Fallback | Done       | True  |
| 1099 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                   | Fallback | Done       | True  |
| 1100 | Tensor<[4096, 4]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | True  |
| 1101 | Tensor<[4096, 512]> self = ?,<br>List[int] size = [1, 64, 64, 512]             | Done     | Done       | True  |
| 1102 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]                 | Done     | Done       | True  |
| 1103 | Tensor<[4096, 6]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | True  |
| 1104 | Tensor<[4096, 8]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | True  |
| 1105 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]               | Done     | Done       | True  |
| 1106 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]                  | Done     | Done       | True  |
| 1107 | Tensor<[42]> self = ?,<br>List[int] size = [1, 1, 1, 42]                       | Done     | Done       | True  |
| 1108 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                 | Unknown  | Done       | True  |
| 1109 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]               | Unknown  | Done       | True  |
| 1110 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                   | Unknown  | Done       | True  |
| 1111 | Tensor<[45]> self = ?,<br>List[int] size = [45, 1]                             | Fallback | Unknown    | N/A   |
| 1112 | Tensor<[48, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]             | Done     | Done       | True  |
| 1113 | Tensor<[48, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]             | Done     | Done       | True  |
| 1114 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]             | Done     | Done       | True  |
| 1115 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]             | Fallback | Done       | True  |
| 1116 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]               | Done     | Done       | True  |
| 1117 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]               | Done     | Done       | True  |
| 1118 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]                 | Done     | Done       | True  |
| 1119 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]               | Done     | Done       | True  |
| 1120 | Tensor<[49, 2304]> self = ?,<br>List[int] size = [1, 49, 2304]                 | Fallback | Done       | True  |
| 1121 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 49, 3072]                 | Fallback | Done       | True  |
| 1122 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 7, 7, 3072]               | Done     | Done       | True  |
| 1123 | Tensor<[49, 4096]> self = ?,<br>List[int] size = [1, 7, 7, 4096]               | Done     | Done       | True  |
| 1124 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 49, 768]                   | Done     | Done       | True  |
| 1125 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]                 | Done     | Done       | True  |
| 1126 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]         | Done     | Done       | True  |
| 1127 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]           | Done     | Done       | True  |
| 1128 | Tensor<[5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  | Done       | True  |
| 1129 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]         | Fallback | Done       | True  |
| 1130 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]           | Done     | Done       | True  |
| 1131 | Tensor<[5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]             | Unknown  | Done       | True  |
| 1132 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                   | Unknown  | Done       | True  |
| 1133 | Tensor<[5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]             | Unknown  | Done       | True  |
| 1134 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                   | Unknown  | Done       | True  |
| 1135 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                 | Unknown  | Done       | True  |
| 1136 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 1024]                 | Done     | Done       | True  |
| 1137 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 16, 64]               | Done     | Done       | True  |
| 1138 | Tensor<[50, 1, 12, 64]> self = ?,<br>List[int] size = [50, 768]                | Done     | Done       | True  |
| 1139 | Tensor<[50, 1, 16, 64]> self = ?,<br>List[int] size = [50, 1024]               | Done     | Done       | True  |
| 1140 | Tensor<[50, 1, 2304]> self = ?,<br>List[int] size = [50, 1, 3, 768]            | Done     | Done       | True  |
| 1141 | Tensor<[50, 1, 3072]> self = ?,<br>List[int] size = [50, 1, 3, 1024]           | Done     | Done       | True  |
| 1142 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 12, 64]                | Done     | Done       | True  |
| 1143 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 768]                   | Done     | Done       | True  |
| 1144 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [1, 50, 1024]                 | Done     | Done       | True  |
| 1145 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [50, 1, 1024]                 | Done     | Done       | True  |
| 1146 | Tensor<[50, 2304]> self = ?,<br>List[int] size = [50, 1, 2304]                 | Done     | Done       | True  |
| 1147 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]                 | None     | Fallback   | True  |
| 1148 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [50, 1, 3072]                 | Done     | Done       | True  |
| 1149 | Tensor<[50, 4096]> self = ?,<br>List[int] size = [1, 50, 4096]                 | Done     | Done       | True  |
| 1150 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]                   | None     | Fallback   | True  |
| 1151 | Tensor<[50, 768]> self = ?,<br>List[int] size = [50, 1, 768]                   | Done     | Done       | True  |
| 1152 | Tensor<[50]> self = ?,<br>List[int] size = [-1, 1]                             | Fallback | Done       | True  |
| 1153 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       | True  |
| 1154 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                    | Fallback | Done       | True  |
| 1155 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]                 | Done     | Done       | True  |
| 1156 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272]               | Fallback | Done       | True  |
| 1157 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]                   | Done     | Done       | True  |
| 1158 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                              | Fallback | Done       | True  |
| 1159 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                              | Fallback | Done       | True  |
| 1160 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]              | Done     | Done       | True  |
| 1161 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                 | Unknown  | Done       | True  |
| 1162 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                 | Unknown  | Done       | True  |
| 1163 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                   | Unknown  | Done       | True  |
| 1164 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                   | Unknown  | Done       | True  |
| 1165 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                 | Unknown  | Done       | True  |
| 1166 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   |
| 1167 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]               | Done     | Done       | True  |
| 1168 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]               | Done     | Done       | True  |
| 1169 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]              | Done     | Done       | True  |
| 1170 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]                  | Done     | Done       | True  |
| 1171 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]                | Fallback | Done       | True  |
| 1172 | Tensor<[63, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                       | Done     | Done       | True  |
| 1173 | Tensor<[63, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                       | Fallback | Done       | True  |
| 1174 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]                 | Done     | Done       | True  |
| 1175 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]               | Done     | Done       | True  |
| 1176 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]                 | Fallback | Done       | True  |
| 1177 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [1, 64, 3, 49, 49]       | Done     | Done       | True  |
| 1178 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [192, 49, 49]            | Done     | Done       | True  |
| 1179 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [1, 64, 3, 64, 64]       | Done     | Done       | True  |
| 1180 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]            | Done     | Done       | True  |
| 1181 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 64, 3072]                 | Fallback | Done       | True  |
| 1182 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]               | Done     | Done       | True  |
| 1183 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [1, 64, 4, 49, 49]       | Done     | Done       | True  |
| 1184 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [256, 49, 49]            | Done     | Done       | True  |
| 1185 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4, 64, 64]       | Done     | Done       | True  |
| 1186 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [256, 64, 64]            | Done     | Done       | True  |
| 1187 | Tensor<[64, 4096]> self = ?,<br>List[int] size = [1, 8, 8, 4096]               | Done     | Done       | True  |
| 1188 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 128]       | Fallback | Done       | True  |
| 1189 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [3136, 128]                | Done     | Done       | True  |
| 1190 | Tensor<[64, 49, 288]> self = ?,<br>List[int] size = [64, 49, 3, 3, 32]         | None     | Fallback   | True  |
| 1191 | Tensor<[64, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]             | Done     | Done       | True  |
| 1192 | Tensor<[64, 49, 384]> self = ?,<br>List[int] size = [64, 49, 3, 4, 32]         | None     | Fallback   | True  |
| 1193 | Tensor<[64, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]             | Done     | Done       | True  |
| 1194 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 96]         | Fallback | Done       | True  |
| 1195 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [3136, 96]                  | Done     | Done       | True  |
| 1196 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]       | Fallback | Done       | True  |
| 1197 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]                | Done     | Done       | True  |
| 1198 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]         | None     | Fallback   | True  |
| 1199 | Tensor<[64, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]             | Done     | Done       | True  |
| 1200 | Tensor<[64, 64, 384]> self = ?,<br>List[int] size = [64, 64, 3, 4, 32]         | None     | Fallback   | True  |
| 1201 | Tensor<[64, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]             | Fallback | Done       | True  |
| 1202 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]         | Fallback | Done       | True  |
| 1203 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]                  | Done     | Done       | True  |
| 1204 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                    | Done     | Done       | True  |
| 1205 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 64, 768]                   | Done     | Done       | True  |
| 1206 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]                 | Done     | Done       | True  |
| 1207 | Tensor<[64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]               | Done     | Done       | True  |
| 1208 | Tensor<[64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                 | Fallback | Done       | True  |
| 1209 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                       | Done     | Done       | True  |
| 1210 | Tensor<[68]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | True  |
| 1211 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]                 | Done     | Done       | True  |
| 1212 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]                   | Unknown  | Done       | True  |
| 1213 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]                         | Unknown  | Done       | True  |
| 1214 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]                   | Unknown  | Done       | True  |
| 1215 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]                   | Done     | Done       | True  |
| 1216 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]                   | Done     | Done       | True  |
| 1217 | Tensor<[7, 768]> self = ?,<br>List[int] size = [1, 7, 768]                     | Unknown  | Done       | True  |
| 1218 | Tensor<[71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]               | Done     | Done       | True  |
| 1219 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]                 | Done     | Done       | True  |
| 1220 | Tensor<[768, 196]> self = ?,<br>List[int] size = [1, 768, 196]                 | Done     | Done       | True  |
| 1221 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]                 | Done     | Done       | True  |
| 1222 | Tensor<[784, 1024]> self = ?,<br>List[int] size = [1, 28, 28, 1024]            | Done     | Done       | True  |
| 1223 | Tensor<[784, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]              | Done     | Done       | True  |
| 1224 | Tensor<[784, 192]> self = ?,<br>List[int] size = [16, 49, 192]                 | Done     | Done       | True  |
| 1225 | Tensor<[784, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]              | Done     | Done       | True  |
| 1226 | Tensor<[784, 256]> self = ?,<br>List[int] size = [16, 49, 256]                 | Done     | Done       | True  |
| 1227 | Tensor<[784, 576]> self = ?,<br>List[int] size = [16, 49, 576]                 | Fallback | Done       | True  |
| 1228 | Tensor<[784, 768]> self = ?,<br>List[int] size = [1, 28, 28, 768]              | Done     | Done       | True  |
| 1229 | Tensor<[784, 768]> self = ?,<br>List[int] size = [16, 49, 768]                 | Fallback | Done       | True  |
| 1230 | Tensor<[7]> self = ?,<br>List[int] size = [-1, 1]                              | Fallback | Done       | True  |
| 1231 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                 | Unknown  | Done       | True  |
| 1232 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                   | Unknown  | Done       | True  |
| 1233 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                   | Unknown  | Done       | True  |
| 1234 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                 | Unknown  | Done       | True  |
| 1235 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   |
| 1236 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]               | Done     | Done       | True  |
| 1237 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]               | Done     | Done       | True  |
| 1238 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]         | Done     | Done       | True  |
| 1239 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]           | Done     | Done       | True  |
| 1240 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]           | Done     | Done       | True  |
| 1241 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]         | Done     | Done       | True  |
| 1242 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]           | Done     | Done       | True  |
| 1243 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]             | Done     | Done       | True  |
| 1244 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]           | Fallback | Done       | True  |
| 1245 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]             | Done     | Done       | True  |
| 1246 | Tensor<[8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]             | Unknown  | Done       | True  |
| 1247 | Tensor<[850, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Done     | Done       | True  |
| 1248 | Tensor<[850, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Fallback | Done       | True  |
| 1249 | Tensor<[8732, 1, 4]> self = ?,<br>List[int] size = [8732, 4]                   | Unknown  | Done       | True  |
| 1250 | Tensor<[8732, 2, 2]> self = ?,<br>List[int] size = [8732, 4]                   | Unknown  | Done       | True  |
| 1251 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]                   | Done     | Done       | True  |
| 1252 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]                   | Unknown  | Done       | True  |
| 1253 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]                     | Done     | Done       | True  |
| 1254 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Fallback | Done       | True  |
| 1255 | Tensor<[9, 16384]> self = ?,<br>List[int] size = [1, 9, 16384]                 | Done     | Done       | True  |
| 1256 | Tensor<[9, 2048]> self = ?,<br>List[int] size = [1, 9, 2048]                   | Done     | Done       | True  |
| 1257 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]                 | Fallback | Done       | True  |
| 1258 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]                   | Done     | Done       | True  |
| 1259 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]                     | Unknown  | Done       | True  |
| 1260 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]                   | Done     | Done       | True  |
| 1261 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                        | Done     | Done       | True  |
| 1262 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]                     | Unknown  | Done       | True  |
| 1263 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]                     | Done     | Done       | True  |
| 1264 | Tensor<[9, 8192]> self = ?,<br>List[int] size = [1, 9, 8192]                   | Done     | Done       | True  |
| 1265 | Tensor<[9, 8]> self = ?,<br>List[int] size = [-1, 2]                           | Fallback | Done       | True  |
| 1266 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]               | Done     | Done       | True  |
| 1267 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]                 | Done     | Done       | True  |
| 1268 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 8, 32]               | Done     | Done       | True  |
| 1269 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]               | Done     | Done       | True  |
| 1270 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]                 | Done     | Done       | True  |
| 1271 | Tensor<[920, 8, 32]> self = ?,<br>List[int] size = [920, 256]                  | Done     | Done       | True  |
| 1272 | Tensor<[96, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]             | Done     | Done       | True  |
| 1273 | Tensor<[96, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]             | Done     | Done       | True  |
| 1274 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]             | Done     | Done       | True  |
| 1275 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]             | Fallback | Done       | True  |
| 1276 | Tensor<[9]> self = ?,<br>List[int] size = [1, -1]                              | Fallback | Done       | True  |
| 1277 | Tensor<[s0*s1, 10240]> self = ?,<br>List[int] size = [1, <s0*s1>, 10240]       | Unknown  | Unknown    | N/A   |
| 1278 | Tensor<[s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]         | Unknown  | Unknown    | N/A   |
| 1279 | Tensor<[s0*s1, 5120]> self = ?,<br>List[int] size = [1, <s0*s1>, 5120]         | Unknown  | Unknown    | N/A   |
| 1280 | Tensor<[s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]           | Unknown  | Unknown    | N/A   |
| 1281 | Tensor<[s1*s2, 10240]> self = ?,<br>List[int] size = [1, <s1*s2>, 10240]       | Unknown  | Unknown    | N/A   |
| 1282 | Tensor<[s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]         | Unknown  | Unknown    | N/A   |
| 1283 | Tensor<[s1*s2, 2560]> self = ?,<br>List[int] size = [1, <s1*s2>, 2560]         | Unknown  | Unknown    | N/A   |
| 1284 | Tensor<[s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]           | Unknown  | Unknown    | N/A   |
| 1285 | Tensor<[s1*s2, 5120]> self = ?,<br>List[int] size = [1, <s1*s2>, 5120]         | Unknown  | Unknown    | N/A   |
| 1286 | Tensor<[s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]           | Unknown  | Unknown    | N/A   |

