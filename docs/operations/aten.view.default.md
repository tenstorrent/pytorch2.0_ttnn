### aten.view.default
|      | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|-----:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|    0 | Tensor<[0, 1, 4]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Fallback   | 1.0   | -1     |
|    1 | Tensor<[0, 2, 2]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  | Fallback   | 1.0   | -1     |
|    2 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]           | Unknown  | Done       | 1.0   | -1     |
|    3 | Tensor<[1, 1, 1, 4, 4]> self = ?,<br>List[int] size = [1, -1, 4]               | Unknown  | Done       | 1.0   | -1     |
|    4 | Tensor<[1, 1, 1, 4, 91]> self = ?,<br>List[int] size = [1, -1, 91]             | Unknown  | Done       | 1.0   | -1     |
|    5 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]               | Unknown  | Done       | 1.0   | -1     |
|    6 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]             | Unknown  | Done       | 1.0   | -1     |
|    7 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]      | Done     | Unknown    | N/A   | N/A    |
|    8 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 49, 768]        | Done     | Done       | 1.0   | -1     |
|    9 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]      | Done     | Done       | 1.0   | -1     |
|   10 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]        | Done     | Done       | 1.0   | -1     |
|   11 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]                  | Unknown  | Done       | 1.0   | -1     |
|   12 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]             | Unknown  | Done       | 1.0   | -1     |
|   13 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                | Unknown  | Done       | 1.0   | -1     |
|   14 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 16, 64]              | Unknown  | Done       | 1.0   | -1     |
|   15 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                   | Unknown  | Done       | 1.0   | -1     |
|   16 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1024]                      | Done     | Done       | 1.0   | -1     |
|   17 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]              | Unknown  | Done       | 1.0   | -1     |
|   18 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]               | Unknown  | Done       | 1.0   | -1     |
|   19 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]         | Unknown  | Done       | 1.0   | -1     |
|   20 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]             | Unknown  | Done       | 1.0   | -1     |
|   21 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]              | Unknown  | Done       | 1.0   | -1     |
|   22 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | Done       | 1.0   | -1     |
|   23 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | -1     |
|   24 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300]       | Done     | Done       | 1.0   | -1     |
|   25 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Done       | 1.0   | -1     |
|   26 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]                   | Unknown  | Done       | 1.0   | -1     |
|   27 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | 1.0   | -1     |
|   28 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [256]                        | Done     | Done       | 1.0   | -1     |
|   29 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Done     | Done       | 1.0   | -1     |
|   30 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]               | Unknown  | Done       | 1.0   | -1     |
|   31 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                   | Unknown  | Done       | 1.0   | -1     |
|   32 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]             | Done     | Done       | 1.0   | -1     |
|   33 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                    | Done     | Done       | 1.0   | -1     |
|   34 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]               | Unknown  | Done       | 1.0   | -1     |
|   35 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                     | Unknown  | Done       | 1.0   | -1     |
|   36 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [384]                        | Done     | Done       | 1.0   | -1     |
|   37 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]          | Unknown  | Done       | 1.0   | -1     |
|   38 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                   | Unknown  | Done       | 1.0   | -1     |
|   39 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                       | Unknown  | Done       | 1.0   | -1     |
|   40 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]               | Unknown  | Done       | 1.0   | -1     |
|   41 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                     | Unknown  | Done       | 1.0   | -1     |
|   42 | Tensor<[1, 1, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]               | Unknown  | Done       | 1.0   | -1     |
|   43 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]             | Done     | Done       | 1.0   | -1     |
|   44 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]    | Done     | Unknown    | N/A   | N/A    |
|   45 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]      | Done     | Done       | 1.0   | -1     |
|   46 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [-1, 1, 768]                 | Unknown  | Done       | 1.0   | -1     |
|   47 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]              | Unknown  | Done       | 1.0   | -1     |
|   48 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]               | Unknown  | Done       | 1.0   | -1     |
|   49 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                     | Unknown  | Done       | 1.0   | -1     |
|   50 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]                        | Done     | Done       | 1.0   | -1     |
|   51 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]    | Done     | Done       | 1.0   | -1     |
|   52 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]      | Done     | Done       | 1.0   | -1     |
|   53 | Tensor<[1, 1, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]               | Unknown  | Done       | 1.0   | -1     |
|   54 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Unknown  | Done       | 1.0   | -1     |
|   55 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [10, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|   56 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]             | Unknown  | Done       | 1.0   | -1     |
|   57 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, 10, 768]             | Done     | Done       | 1.0   | -1     |
|   58 | Tensor<[1, 10, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]            | Unknown  | Done       | 1.0   | -1     |
|   59 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]                 | Unknown  | Done       | 1.0   | -1     |
|   60 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]                 | Done     | Done       | 1.0   | -1     |
|   61 | Tensor<[1, 10, 4096]> self = ?,<br>List[int] size = [10, 4096]                 | Unknown  | Done       | 1.0   | -1     |
|   62 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]              | Unknown  | Done       | 1.0   | -1     |
|   63 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]                   | Unknown  | Done       | 1.0   | -1     |
|   64 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Unknown  | Done       | 1.0   | -1     |
|   65 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, 10, 12, 64]             | Done     | Done       | 1.0   | -1     |
|   66 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                   | Done     | Done       | 1.0   | -1     |
|   67 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]              | Unknown  | Done       | 1.0   | -1     |
|   68 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]                 | Done     | Done       | 1.0   | -1     |
|   69 | Tensor<[1, 1000, 1, 1]> self = ?,<br>List[int] size = [1, 1000]                | Done     | Done       | 1.0   | -1     |
|   70 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1, 1000, 1, 1]                | Done     | Done       | 1.0   | -1     |
|   71 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                         | Done     | Done       | 1.0   | -1     |
|   72 | Tensor<[1, 1008, 1, 1]> self = ?,<br>List[int] size = [1, 1008]                | Done     | Done       | 1.0   | -1     |
|   73 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, -1]                  | Done     | Done       | 1.0   | -1     |
|   74 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]                | Done     | Done       | 1.0   | -1     |
|   75 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196]         | Done     | Done       | 1.0   | -1     |
|   76 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]         | Done     | Done       | 1.0   | -1     |
|   77 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]          | Done     | Done       | 1.0   | -1     |
|   78 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]           | Done     | Done       | 1.0   | -1     |
|   79 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]               | Done     | Done       | 1.0   | -1     |
|   80 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] size = [1, 1024, 14, 14]         | Done     | Done       | 1.0   | -1     |
|   81 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]         | Done     | Done       | 1.0   | -1     |
|   82 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1024, 256]               | Done     | Done       | 1.0   | -1     |
|   83 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]          | Done     | Done       | 1.0   | -1     |
|   84 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]               | Done     | Done       | 1.0   | -1     |
|   85 | Tensor<[1, 1024, 7, 7]> self = ?,<br>List[int] size = [1, 1024, 49]            | Done     | Done       | 1.0   | -1     |
|   86 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  | Done       | 1.0   | -1     |
|   87 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1024, 1, 1]                | Done     | Done       | 1.0   | -1     |
|   88 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                         | Done     | Done       | 1.0   | -1     |
|   89 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                         | Unknown  | Done       | 1.0   | -1     |
|   90 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10]                             | Done     | Done       | 1.0   | -1     |
|   91 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]               | Unknown  | Done       | 1.0   | -1     |
|   92 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]                 | Unknown  | Done       | 1.0   | -1     |
|   93 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]                 | Unknown  | Done       | 1.0   | -1     |
|   94 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]               | Unknown  | Done       | 1.0   | -1     |
|   95 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|   96 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|   97 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|   98 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]             | Done     | Done       | 1.0   | -1     |
|   99 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]             | Done     | Done       | 1.0   | -1     |
|  100 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12]             | Done     | Done       | 1.0   | -1     |
|  101 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  102 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]                   | Done     | Done       | 1.0   | -1     |
|  103 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [12, 14, 14]             | Done     | Done       | 1.0   | -1     |
|  104 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [12, 14, 64]             | Done     | Done       | 1.0   | -1     |
|  105 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16]             | Done     | Done       | 1.0   | -1     |
|  106 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64]             | Done     | Done       | 1.0   | -1     |
|  107 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197]         | Done     | Done       | 1.0   | -1     |
|  108 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]           | Done     | Done       | 1.0   | -1     |
|  109 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]               | Unknown  | Done       | 1.0   | -1     |
|  110 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]             | Done     | Done       | 1.0   | -1     |
|  111 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]             | Done     | Done       | 1.0   | -1     |
|  112 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25]             | Done     | Done       | 1.0   | -1     |
|  113 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64]             | Done     | Done       | 1.0   | -1     |
|  114 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]                 | Done     | Done       | 1.0   | -1     |
|  115 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]             | Unknown  | Done       | 1.0   | -1     |
|  116 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]             | Unknown  | Done       | 1.0   | -1     |
|  117 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]             | Unknown  | Done       | 1.0   | -1     |
|  118 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64]             | Done     | Done       | 1.0   | -1     |
|  119 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, 50, 64]             | Unknown  | Done       | 1.0   | -1     |
|  120 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]             | Done     | Done       | 1.0   | -1     |
|  121 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12]             | Done     | Done       | 1.0   | -1     |
|  122 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [12, 64, 14]             | Done     | Done       | 1.0   | -1     |
|  123 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16]             | Done     | Done       | 1.0   | -1     |
|  124 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]           | Done     | Done       | 1.0   | -1     |
|  125 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]               | Unknown  | Done       | 1.0   | -1     |
|  126 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25]             | Done     | Done       | 1.0   | -1     |
|  127 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]               | Unknown  | Done       | 1.0   | -1     |
|  128 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]             | Unknown  | Done       | 1.0   | -1     |
|  129 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]             | Unknown  | Done       | 1.0   | -1     |
|  130 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7]               | Done     | Done       | 1.0   | -1     |
|  131 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9]               | Done     | Done       | 1.0   | -1     |
|  132 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  133 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  134 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64]               | Done     | Done       | 1.0   | -1     |
|  135 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]                 | Done     | Done       | 1.0   | -1     |
|  136 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  137 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]                   | Done     | Done       | 1.0   | -1     |
|  138 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64]               | Done     | Done       | 1.0   | -1     |
|  139 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]                 | Done     | Done       | 1.0   | -1     |
|  140 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  141 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  142 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]             | Done     | Done       | 1.0   | -1     |
|  143 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]          | Done     | Done       | 1.0   | -1     |
|  144 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]           | Done     | Done       | 1.0   | -1     |
|  145 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]               | Done     | Done       | 1.0   | -1     |
|  146 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]          | Done     | Done       | 1.0   | -1     |
|  147 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384]       | Done     | Done       | 1.0   | -1     |
|  148 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | -1     |
|  149 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]           | Done     | Done       | 1.0   | -1     |
|  150 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128]       | Done     | Done       | 1.0   | -1     |
|  151 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]          | Done     | Done       | 1.0   | -1     |
|  152 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]          | Done     | Done       | 1.0   | -1     |
|  153 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280]                | Done     | Done       | 1.0   | -1     |
|  154 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]        | Done     | Done       | 1.0   | -1     |
|  155 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]        | Done     | Done       | 1.0   | -1     |
|  156 | Tensor<[1, 1280, 37, 37]> self = ?,<br>List[int] size = [1, 1280, 1369]        | Done     | Done       | 1.0   | -1     |
|  157 | Tensor<[1, 1280]> self = ?,<br>List[int] size = [1, 1280, 1, 1]                | Done     | Done       | 1.0   | -1     |
|  158 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]                           | Done     | Done       | 1.0   | -1     |
|  159 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Unknown  | Done       | 1.0   | -1     |
|  160 | Tensor<[1, 12]> self = ?,<br>List[int] size = [12]                             | Done     | Done       | 1.0   | -1     |
|  161 | Tensor<[1, 1370, 1280]> self = ?,<br>List[int] size = [1370, 1280]             | Done     | Done       | 1.0   | -1     |
|  162 | Tensor<[1, 1370, 5120]> self = ?,<br>List[int] size = [1370, 5120]             | Done     | Done       | 1.0   | -1     |
|  163 | Tensor<[1, 14, 128]> self = ?,<br>List[int] size = [14, 128]                   | Done     | Done       | 1.0   | -1     |
|  164 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int] size = [196, 1024]            | Done     | Unknown    | N/A   | N/A    |
|  165 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int] size = [196, 1536]            | Done     | Done       | 1.0   | -1     |
|  166 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int] size = [196, 2048]            | Done     | Unknown    | N/A   | N/A    |
|  167 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 384]    | Done     | Done       | 1.0   | -1     |
|  168 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [196, 384]              | Done     | Done       | 1.0   | -1     |
|  169 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 512]    | Done     | Unknown    | N/A   | N/A    |
|  170 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [196, 512]              | Done     | Unknown    | N/A   | N/A    |
|  171 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int] size = [196, 768]              | Done     | Done       | 1.0   | -1     |
|  172 | Tensor<[1, 14, 3072]> self = ?,<br>List[int] size = [14, 3072]                 | Done     | Done       | 1.0   | -1     |
|  173 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [1, 14, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  174 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [14, 768]                   | Done     | Done       | 1.0   | -1     |
|  175 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1, 1445, 3, 64]          | Done     | Done       | 1.0   | -1     |
|  176 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]               | Done     | Done       | 1.0   | -1     |
|  177 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] size = [1, 1445, 192]          | Done     | Done       | 1.0   | -1     |
|  178 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]               | Done     | Done       | 1.0   | -1     |
|  179 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  180 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]                 | Done     | Done       | 1.0   | -1     |
|  181 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int] size = [-1, 16]                 | Done     | Done       | 1.0   | -1     |
|  182 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]                 | Done     | Done       | 1.0   | -1     |
|  183 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]                  | Done     | Done       | 1.0   | -1     |
|  184 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int] size = [-1, 32]                 | Done     | Done       | 1.0   | -1     |
|  185 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                   | Done     | Done       | 1.0   | -1     |
|  186 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int] size = [-1, 4]                   | Done     | Done       | 1.0   | -1     |
|  187 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]              | Done     | Done       | 1.0   | -1     |
|  188 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                   | Done     | Done       | 1.0   | -1     |
|  189 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int] size = [-1, 8]                   | Done     | Done       | 1.0   | -1     |
|  190 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]              | Unknown  | Done       | 1.0   | -1     |
|  191 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [15, 384]                   | Unknown  | Done       | 1.0   | -1     |
|  192 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]                   | Unknown  | Done       | 1.0   | -1     |
|  193 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]              | Unknown  | Done       | 1.0   | -1     |
|  194 | Tensor<[1, 1500, 12, 64]> self = ?,<br>List[int] size = [1, 1500, 768]         | Unknown  | Done       | 1.0   | -1     |
|  195 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]             | Unknown  | Done       | 1.0   | -1     |
|  196 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]           | Unknown  | Done       | 1.0   | -1     |
|  197 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, 1500, 12, 64]         | Unknown  | Done       | 1.0   | -1     |
|  198 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]               | Unknown  | Done       | 1.0   | -1     |
|  199 | Tensor<[1, 1512, 1, 1]> self = ?,<br>List[int] size = [1, 1512]                | Done     | Done       | 1.0   | -1     |
|  200 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536]                | Done     | Done       | 1.0   | -1     |
|  201 | Tensor<[1, 1536]> self = ?,<br>List[int] size = [1, 1536, 1, 1]                | Done     | Done       | 1.0   | -1     |
|  202 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                         | Unknown  | Done       | 1.0   | -1     |
|  203 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [16, 1, 10]               | Unknown  | Done       | 1.0   | -1     |
|  204 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]           | Unknown  | Done       | 1.0   | -1     |
|  205 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [16, 1, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  206 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [16, 1, 2]                 | Unknown  | Unknown    | N/A   | N/A    |
|  207 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int] size = [16, 1, 60]               | Unknown  | Done       | 1.0   | -1     |
|  208 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]              | Unknown  | Done       | 1.0   | -1     |
|  209 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  210 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                 | Unknown  | Done       | 1.0   | -1     |
|  211 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  212 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  213 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [16, 10, 10]             | Unknown  | Done       | 1.0   | -1     |
|  214 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [16, 10, 64]             | Unknown  | Done       | 1.0   | -1     |
|  215 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]             | Done     | Done       | 1.0   | -1     |
|  216 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [16, 128, 9]             | Done     | Done       | 1.0   | -1     |
|  217 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int] size = [256, 1024]            | Done     | Done       | 1.0   | -1     |
|  218 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]            | Done     | Done       | 1.0   | -1     |
|  219 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int] size = [256, 2048]            | Done     | Done       | 1.0   | -1     |
|  220 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Done       | 1.0   | -1     |
|  221 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384]    | Done     | Done       | 1.0   | -1     |
|  222 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [256, 384]              | Done     | Done       | 1.0   | -1     |
|  223 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 512]    | Done     | Done       | 1.0   | -1     |
|  224 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [256, 512]              | Done     | Done       | 1.0   | -1     |
|  225 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]              | Done     | Done       | 1.0   | -1     |
|  226 | Tensor<[1, 16, 19, 19]> self = ?,<br>List[int] size = [16, 19, 19]             | Done     | Done       | 1.0   | -1     |
|  227 | Tensor<[1, 16, 19, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Done     | Done       | 1.0   | -1     |
|  228 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197]         | Done     | Done       | 1.0   | -1     |
|  229 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]           | Done     | Done       | 1.0   | -1     |
|  230 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [16, 2, 64]               | Unknown  | Unknown    | N/A   | N/A    |
|  231 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256]         | Done     | Done       | 1.0   | -1     |
|  232 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]           | Done     | Done       | 1.0   | -1     |
|  233 | Tensor<[1, 16, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]           | Unknown  | Done       | 1.0   | -1     |
|  234 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]                 | Done     | Done       | 1.0   | -1     |
|  235 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]             | Done     | Done       | 1.0   | -1     |
|  236 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]             | Done     | Done       | 1.0   | -1     |
|  237 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]                  | Done     | Done       | 1.0   | -1     |
|  238 | Tensor<[1, 16, 38, 38]> self = ?,<br>List[int] size = [1, -1, 4, 38, 38]       | Unknown  | Done       | 1.0   | -1     |
|  239 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                 | Unknown  | Done       | 1.0   | -1     |
|  240 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]               | Unknown  | Done       | 1.0   | -1     |
|  241 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int] size = [16, 59, 59]             | Unknown  | Done       | 1.0   | -1     |
|  242 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  243 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int] size = [-1, 6, 49, 49]       | Done     | Done       | 1.0   | -1     |
|  244 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]       | Done     | Done       | 1.0   | -1     |
|  245 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]               | Unknown  | Done       | 1.0   | -1     |
|  246 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  247 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [16, 64, 10]             | Unknown  | Done       | 1.0   | -1     |
|  248 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]           | Done     | Done       | 1.0   | -1     |
|  249 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [16, 64, 1]               | Unknown  | Done       | 1.0   | -1     |
|  250 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]           | Done     | Done       | 1.0   | -1     |
|  251 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [16, 64, 2]               | Unknown  | Unknown    | N/A   | N/A    |
|  252 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]               | Unknown  | Done       | 1.0   | -1     |
|  253 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]               | Unknown  | Done       | 1.0   | -1     |
|  254 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]               | Done     | Done       | 1.0   | -1     |
|  255 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  256 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  257 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  258 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]                   | Done     | Done       | 1.0   | -1     |
|  259 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int] size = [-1, 8, 49, 49]       | Done     | Unknown    | N/A   | N/A    |
|  260 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int] size = [-1, 8, 64, 64]       | Done     | Done       | 1.0   | -1     |
|  261 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [16, 9, 128]             | Done     | Done       | 1.0   | -1     |
|  262 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]               | Done     | Done       | 1.0   | -1     |
|  263 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]                 | Done     | Done       | 1.0   | -1     |
|  264 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]             | Done     | Done       | 1.0   | -1     |
|  265 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  266 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]        | Unknown  | Unknown    | N/A   | N/A    |
|  267 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  268 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]          | Done     | Done       | 1.0   | -1     |
|  269 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]           | Done     | Done       | 1.0   | -1     |
|  270 | Tensor<[1, 160, 256]> self = ?,<br>List[int] size = [1, 160, 16, 16]           | Done     | Done       | 1.0   | -1     |
|  271 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]          | Done     | Done       | 1.0   | -1     |
|  272 | Tensor<[1, 160]> self = ?,<br>List[int] size = [160]                           | Done     | Done       | 1.0   | -1     |
|  273 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | -1     |
|  274 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]             | Done     | Done       | 1.0   | -1     |
|  275 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]       | Done     | Done       | 1.0   | -1     |
|  276 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [16384, 256]             | Done     | Done       | 1.0   | -1     |
|  277 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]         | Done     | Done       | 1.0   | -1     |
|  278 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]         | Done     | Done       | 1.0   | -1     |
|  279 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]         | Done     | Done       | 1.0   | -1     |
|  280 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]               | Done     | Done       | 1.0   | -1     |
|  281 | Tensor<[1, 1664, 1, 1]> self = ?,<br>List[int] size = [1, 1664]                | Done     | Done       | 1.0   | -1     |
|  282 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]                    | Done     | Done       | 1.0   | -1     |
|  283 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Done     | Done       | 1.0   | -1     |
|  284 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, 19, 16, 64]            | Done     | Done       | 1.0   | -1     |
|  285 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [19, 1024]                 | Done     | Done       | 1.0   | -1     |
|  286 | Tensor<[1, 19, 256008]> self = ?,<br>List[int] size = [-1, 256008]             | Done     | Done       | 1.0   | -1     |
|  287 | Tensor<[1, 19, 4096]> self = ?,<br>List[int] size = [19, 4096]                 | Done     | Done       | 1.0   | -1     |
|  288 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]          | Done     | Done       | 1.0   | -1     |
|  289 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]          | Done     | Done       | 1.0   | -1     |
|  290 | Tensor<[1, 1920, 1, 1]> self = ?,<br>List[int] size = [1, 1920]                | Done     | Done       | 1.0   | -1     |
|  291 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Done       | 1.0   | -1     |
|  292 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]             | Done     | Done       | 1.0   | -1     |
|  293 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]       | Done     | Done       | 1.0   | -1     |
|  294 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]         | Done     | Done       | 1.0   | -1     |
|  295 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]         | Done     | Done       | 1.0   | -1     |
|  296 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]         | Done     | Done       | 1.0   | -1     |
|  297 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]               | Done     | Done       | 1.0   | -1     |
|  298 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]               | Done     | Done       | 1.0   | -1     |
|  299 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]                 | Done     | Done       | 1.0   | -1     |
|  300 | Tensor<[1, 196]> self = ?,<br>List[int] size = [196]                           | Done     | Done       | 1.0   | -1     |
|  301 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [1, 197, 16, 64]          | Done     | Done       | 1.0   | -1     |
|  302 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]               | Done     | Done       | 1.0   | -1     |
|  303 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]           | Done     | Done       | 1.0   | -1     |
|  304 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]          | Done     | Done       | 1.0   | -1     |
|  305 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]               | Done     | Done       | 1.0   | -1     |
|  306 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]               | Done     | Done       | 1.0   | -1     |
|  307 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]           | Done     | Done       | 1.0   | -1     |
|  308 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]                 | Done     | Done       | 1.0   | -1     |
|  309 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1, 19]                         | Done     | Done       | 1.0   | -1     |
|  310 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1]                             | Done     | Done       | 1.0   | -1     |
|  311 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                           | Unknown  | Done       | 1.0   | -1     |
|  312 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                              | Unknown  | Done       | 1.0   | -1     |
|  313 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                               | Done     | Done       | 1.0   | -1     |
|  314 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]             | Done     | Done       | 1.0   | -1     |
|  315 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]             | Done     | Done       | 1.0   | -1     |
|  316 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  317 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]         | Done     | Done       | 1.0   | -1     |
|  318 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]           | Done     | Done       | 1.0   | -1     |
|  319 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]         | Done     | Done       | 1.0   | -1     |
|  320 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]           | Done     | Done       | 1.0   | -1     |
|  321 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]             | Done     | Done       | 1.0   | -1     |
|  322 | Tensor<[1, 2016, 1, 1]> self = ?,<br>List[int] size = [1, 2016]                | Done     | Done       | 1.0   | -1     |
|  323 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048]                | Done     | Done       | 1.0   | -1     |
|  324 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160]        | Done     | Done       | 1.0   | -1     |
|  325 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]         | Done     | Done       | 1.0   | -1     |
|  326 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]          | Done     | Done       | 1.0   | -1     |
|  327 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]         | Done     | Done       | 1.0   | -1     |
|  328 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [-1, 768]                 | Done     | Unknown    | N/A   | N/A    |
|  329 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]               | Done     | Done       | 1.0   | -1     |
|  330 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]          | Done     | Unknown    | N/A   | N/A    |
|  331 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]                   | Unknown  | Done       | 1.0   | -1     |
|  332 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 2048, 1, 1]                | Done     | Done       | 1.0   | -1     |
|  333 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [2048]                         | Unknown  | Done       | 1.0   | -1     |
|  334 | Tensor<[1, 21843]> self = ?,<br>List[int] size = [21843]                       | Done     | Done       | 1.0   | -1     |
|  335 | Tensor<[1, 2208, 1, 1]> self = ?,<br>List[int] size = [1, 2208]                | Done     | Done       | 1.0   | -1     |
|  336 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128]      | Done     | Done       | 1.0   | -1     |
|  337 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                     | Done     | Done       | 1.0   | -1     |
|  338 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]           | Unknown  | Done       | 1.0   | -1     |
|  339 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]       | Unknown  | Done       | 1.0   | -1     |
|  340 | Tensor<[1, 24, 19, 19]> self = ?,<br>List[int] size = [1, -1, 4, 19, 19]       | Unknown  | Done       | 1.0   | -1     |
|  341 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]           | Unknown  | Done       | 1.0   | -1     |
|  342 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]       | Unknown  | Done       | 1.0   | -1     |
|  343 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]           | Unknown  | Done       | 1.0   | -1     |
|  344 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]                 | Done     | Done       | 1.0   | -1     |
|  345 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [24, 32, 49]             | Done     | Done       | 1.0   | -1     |
|  346 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]             | Done     | Done       | 1.0   | -1     |
|  347 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [24, 49, 32]             | Done     | Done       | 1.0   | -1     |
|  348 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [24, 49, 49]             | Done     | Done       | 1.0   | -1     |
|  349 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]           | Unknown  | Done       | 1.0   | -1     |
|  350 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]             | Done     | Done       | 1.0   | -1     |
|  351 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]             | Done     | Done       | 1.0   | -1     |
|  352 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  353 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, 24, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  354 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]                   | Done     | Done       | 1.0   | -1     |
|  355 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] size = [1, 25, 768]             | Done     | Done       | 1.0   | -1     |
|  356 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]                 | Done     | Done       | 1.0   | -1     |
|  357 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [1, 25, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  358 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]                   | Done     | Done       | 1.0   | -1     |
|  359 | Tensor<[1, 2520, 1, 1]> self = ?,<br>List[int] size = [1, 2520]                | Done     | Done       | 1.0   | -1     |
|  360 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | 1.0   | -1     |
|  361 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 16, 64]          | Done     | Done       | 1.0   | -1     |
|  362 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]          | Done     | Done       | 1.0   | -1     |
|  363 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]               | Done     | Done       | 1.0   | -1     |
|  364 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200]       | Done     | Done       | 1.0   | -1     |
|  365 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16384]       | Done     | Done       | 1.0   | -1     |
|  366 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 256, 8, 160]          | Done     | Done       | 1.0   | -1     |
|  367 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]               | Done     | Done       | 1.0   | -1     |
|  368 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Done       | 1.0   | -1     |
|  369 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] size = [1, 256, 1024]          | Done     | Done       | 1.0   | -1     |
|  370 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]            | Done     | Done       | 1.0   | -1     |
|  371 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]                 | Done     | Done       | 1.0   | -1     |
|  372 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128]       | Done     | Done       | 1.0   | -1     |
|  373 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160]       | Done     | Done       | 1.0   | -1     |
|  374 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]             | Done     | Done       | 1.0   | -1     |
|  375 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]           | Done     | Done       | 1.0   | -1     |
|  376 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]            | Done     | Done       | 1.0   | -1     |
|  377 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]           | Done     | Done       | 1.0   | -1     |
|  378 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]            | Done     | Done       | 1.0   | -1     |
|  379 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                 | Done     | Done       | 1.0   | -1     |
|  380 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[int] size = [1, 256, 1024]          | Done     | Done       | 1.0   | -1     |
|  381 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]             | Done     | Done       | 1.0   | -1     |
|  382 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]             | Done     | Done       | 1.0   | -1     |
|  383 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]                   | Done     | Done       | 1.0   | -1     |
|  384 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]          | Done     | Done       | 1.0   | -1     |
|  385 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]               | Done     | Done       | 1.0   | -1     |
|  386 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]            | Done     | Done       | 1.0   | -1     |
|  387 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                 | Done     | Done       | 1.0   | -1     |
|  388 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]          | Done     | Done       | 1.0   | -1     |
|  389 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]             | Done     | Done       | 1.0   | -1     |
|  390 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]                   | Done     | Done       | 1.0   | -1     |
|  391 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 16, 16, 16, 16, 3]     | Done     | Done       | 1.0   | -1     |
|  392 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]            | Done     | Done       | 1.0   | -1     |
|  393 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                 | Done     | Done       | 1.0   | -1     |
|  394 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]          | Done     | Done       | 1.0   | -1     |
|  395 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]            | Done     | Done       | 1.0   | -1     |
|  396 | Tensor<[1, 256]> self = ?,<br>List[int] size = [256]                           | Done     | Done       | 1.0   | -1     |
|  397 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                          | Done     | Done       | 1.0   | -1     |
|  398 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int] size = [784, 1024]            | Done     | Unknown    | N/A   | N/A    |
|  399 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 192]    | Done     | Done       | 1.0   | -1     |
|  400 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [784, 192]              | Done     | Done       | 1.0   | -1     |
|  401 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 256]    | Done     | Done       | 1.0   | -1     |
|  402 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [784, 256]              | Done     | Unknown    | N/A   | N/A    |
|  403 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int] size = [784, 384]              | Done     | Done       | 1.0   | -1     |
|  404 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int] size = [784, 512]              | Done     | Done       | 1.0   | -1     |
|  405 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int] size = [784, 768]              | Done     | Done       | 1.0   | -1     |
|  406 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445]       | Done     | Done       | 1.0   | -1     |
|  407 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]           | Done     | Done       | 1.0   | -1     |
|  408 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16]  | Done     | Done       | 1.0   | -1     |
|  409 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]           | Done     | Done       | 1.0   | -1     |
|  410 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]            | Done     | Done       | 1.0   | -1     |
|  411 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]                 | Done     | Done       | 1.0   | -1     |
|  412 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]               | Done     | Done       | 1.0   | -1     |
|  413 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]            | Done     | Done       | 1.0   | -1     |
|  414 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]                 | Done     | Done       | 1.0   | -1     |
|  415 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]            | Done     | Done       | 1.0   | -1     |
|  416 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]            | Done     | Done       | 1.0   | -1     |
|  417 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]                 | Done     | Done       | 1.0   | -1     |
|  418 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]             | Done     | Done       | 1.0   | -1     |
|  419 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]                   | Done     | Done       | 1.0   | -1     |
|  420 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]            | Done     | Done       | 1.0   | -1     |
|  421 | Tensor<[1, 3024, 1, 1]> self = ?,<br>List[int] size = [1, 3024]                | Done     | Done       | 1.0   | -1     |
|  422 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                   | Unknown  | Done       | 1.0   | -1     |
|  423 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]                         | Done     | Done       | 1.0   | -1     |
|  424 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]         | Done     | Done       | 1.0   | -1     |
|  425 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]                 | Done     | Done       | 1.0   | -1     |
|  426 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  427 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]         | Done     | Done       | 1.0   | -1     |
|  428 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  429 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 16, 16]             | Done     | Done       | 1.0   | -1     |
|  430 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int] size = [1024, 1024]           | Done     | Done       | 1.0   | -1     |
|  431 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] size = [1, 1024, 160]          | Done     | Done       | 1.0   | -1     |
|  432 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192]    | Done     | Done       | 1.0   | -1     |
|  433 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1024, 192]             | Done     | Done       | 1.0   | -1     |
|  434 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 256]    | Done     | Done       | 1.0   | -1     |
|  435 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1024, 256]             | Done     | Done       | 1.0   | -1     |
|  436 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]             | Done     | Done       | 1.0   | -1     |
|  437 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [32, 32, 49]             | Done     | Unknown    | N/A   | N/A    |
|  438 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int] size = [1024, 512]             | Done     | Done       | 1.0   | -1     |
|  439 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [32, 32, 64]             | Done     | Done       | 1.0   | -1     |
|  440 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]             | Done     | Done       | 1.0   | -1     |
|  441 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96]         | Done     | Done       | 1.0   | -1     |
|  442 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [32, 49, 32]             | Done     | Unknown    | N/A   | N/A    |
|  443 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [32, 49, 49]             | Done     | Unknown    | N/A   | N/A    |
|  444 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]                 | Done     | Done       | 1.0   | -1     |
|  445 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [32, 64, 32]             | Done     | Done       | 1.0   | -1     |
|  446 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [32, 64, 64]             | Done     | Done       | 1.0   | -1     |
|  447 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]          | Done     | Done       | 1.0   | -1     |
|  448 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]           | Done     | Done       | 1.0   | -1     |
|  449 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]          | Done     | Done       | 1.0   | -1     |
|  450 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]                 | Unknown  | Done       | 1.0   | -1     |
|  451 | Tensor<[1, 32]> self = ?,<br>List[int] size = [32]                             | Done     | Done       | 1.0   | -1     |
|  452 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]   | Unknown  | Unknown    | N/A   | N/A    |
|  453 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]       | Unknown  | Done       | 1.0   | -1     |
|  454 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]       | Unknown  | Unknown    | N/A   | N/A    |
|  455 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]       | Unknown  | Unknown    | N/A   | N/A    |
|  456 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]           | Unknown  | Done       | 1.0   | -1     |
|  457 | Tensor<[1, 364, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]         | Unknown  | Done       | 1.0   | -1     |
|  458 | Tensor<[1, 364, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]         | Unknown  | Done       | 1.0   | -1     |
|  459 | Tensor<[1, 364, 38, 38]> self = ?,<br>List[int] size = [1, -1, 91, 38, 38]     | Unknown  | Done       | 1.0   | -1     |
|  460 | Tensor<[1, 3712, 1, 1]> self = ?,<br>List[int] size = [1, 3712]                | Done     | Done       | 1.0   | -1     |
|  461 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                     | Unknown  | Done       | 1.0   | -1     |
|  462 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3]                               | Done     | Done       | 1.0   | -1     |
|  463 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int] size = [-1, 12, 49, 49]      | Done     | Done       | 1.0   | -1     |
|  464 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]      | Done     | Done       | 1.0   | -1     |
|  465 | Tensor<[1, 4, 12, 64]> self = ?,<br>List[int] size = [1, 4, 768]               | Unknown  | Done       | 1.0   | -1     |
|  466 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int] size = [-1, 16, 49, 49]      | Done     | Unknown    | N/A   | N/A    |
|  467 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int] size = [-1, 16, 64, 64]      | Done     | Done       | 1.0   | -1     |
|  468 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]                   | Unknown  | Done       | 1.0   | -1     |
|  469 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]              | Unknown  | Done       | 1.0   | -1     |
|  470 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, 4, 12, 64]               | Unknown  | Done       | 1.0   | -1     |
|  471 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]                     | Unknown  | Done       | 1.0   | -1     |
|  472 | Tensor<[1, 400, 1, 1]> self = ?,<br>List[int] size = [1, 400]                  | Done     | Done       | 1.0   | -1     |
|  473 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]             | Unknown  | Done       | 1.0   | -1     |
|  474 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | Done       | 1.0   | -1     |
|  475 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]               | Done     | Done       | 1.0   | -1     |
|  476 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]            | Unknown  | Done       | 1.0   | -1     |
|  477 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]          | Unknown  | Done       | 1.0   | -1     |
|  478 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]               | Unknown  | Done       | 1.0   | -1     |
|  479 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]           | Done     | Done       | 1.0   | -1     |
|  480 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]            | Done     | Done       | 1.0   | -1     |
|  481 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]                 | Done     | Done       | 1.0   | -1     |
|  482 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]            | Unknown  | Done       | 1.0   | -1     |
|  483 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                   | Unknown  | Done       | 1.0   | -1     |
|  484 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [4096]                         | Done     | Done       | 1.0   | -1     |
|  485 | Tensor<[1, 440, 1, 1]> self = ?,<br>List[int] size = [1, 440]                  | Done     | Done       | 1.0   | -1     |
|  486 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] size = [1, 45, 768]             | Unknown  | Done       | 1.0   | -1     |
|  487 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                 | Unknown  | Done       | 1.0   | -1     |
|  488 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [-1, 45, 768]               | Unknown  | Done       | 1.0   | -1     |
|  489 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [1, 45, 12, 64]             | Unknown  | Done       | 1.0   | -1     |
|  490 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                   | Unknown  | Done       | 1.0   | -1     |
|  491 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                         | Unknown  | Done       | 1.0   | -1     |
|  492 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]          | Done     | Done       | 1.0   | -1     |
|  493 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]           | Done     | Done       | 1.0   | -1     |
|  494 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]               | Done     | Done       | 1.0   | -1     |
|  495 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]          | Done     | Done       | 1.0   | -1     |
|  496 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]               | Done     | Done       | 1.0   | -1     |
|  497 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 1024]      | Done     | Unknown    | N/A   | N/A    |
|  498 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [49, 1024]                 | Done     | Unknown    | N/A   | N/A    |
|  499 | Tensor<[1, 49, 2304]> self = ?,<br>List[int] size = [1, 49, 3, 24, 32]         | Done     | Done       | 1.0   | -1     |
|  500 | Tensor<[1, 49, 3072]> self = ?,<br>List[int] size = [1, 49, 3, 32, 32]         | Done     | Unknown    | N/A   | N/A    |
|  501 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 768]        | Done     | Done       | 1.0   | -1     |
|  502 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [49, 768]                   | Done     | Done       | 1.0   | -1     |
|  503 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                           | Unknown  | Done       | 1.0   | -1     |
|  504 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]           | Unknown  | Done       | 1.0   | -1     |
|  505 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]         | Done     | Done       | 1.0   | -1     |
|  506 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]           | Done     | Done       | 1.0   | -1     |
|  507 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                | Unknown  | Done       | 1.0   | -1     |
|  508 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                   | Unknown  | Done       | 1.0   | -1     |
|  509 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]         | Done     | Done       | 1.0   | -1     |
|  510 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]           | Done     | Done       | 1.0   | -1     |
|  511 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]         | Unknown  | Done       | 1.0   | -1     |
|  512 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]              | Unknown  | Done       | 1.0   | -1     |
|  513 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]             | Done     | Done       | 1.0   | -1     |
|  514 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]             | Done     | Done       | 1.0   | -1     |
|  515 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]               | Unknown  | Done       | 1.0   | -1     |
|  516 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  517 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]          | Unknown  | Done       | 1.0   | -1     |
|  518 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                   | Unknown  | Done       | 1.0   | -1     |
|  519 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]             | Done     | Done       | 1.0   | -1     |
|  520 | Tensor<[1, 50, 1024]> self = ?,<br>List[int] size = [50, 1024]                 | Done     | Done       | 1.0   | -1     |
|  521 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768]             | Unknown  | Done       | 1.0   | -1     |
|  522 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]                 | Done     | Done       | 1.0   | -1     |
|  523 | Tensor<[1, 50, 4096]> self = ?,<br>List[int] size = [50, 4096]                 | Done     | Done       | 1.0   | -1     |
|  524 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  525 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  526 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]                   | Done     | Done       | 1.0   | -1     |
|  527 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                 | Unknown  | Done       | 1.0   | -1     |
|  528 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]                 | Unknown  | Done       | 1.0   | -1     |
|  529 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512]                  | Done     | Done       | 1.0   | -1     |
|  530 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]           | Done     | Done       | 1.0   | -1     |
|  531 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]          | Done     | Done       | 1.0   | -1     |
|  532 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]          | Done     | Done       | 1.0   | -1     |
|  533 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] size = [1, 25088]                | Done     | Done       | 1.0   | -1     |
|  534 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                 | Unknown  | Done       | 1.0   | -1     |
|  535 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                     | Unknown  | Done       | 1.0   | -1     |
|  536 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512, 1, 1]                  | Done     | Done       | 1.0   | -1     |
|  537 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]                           | Done     | Done       | 1.0   | -1     |
|  538 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]                 | Unknown  | Done       | 1.0   | -1     |
|  539 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]         | Unknown  | Done       | 1.0   | -1     |
|  540 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10]     | Unknown  | Done       | 1.0   | -1     |
|  541 | Tensor<[1, 546, 19, 19]> self = ?,<br>List[int] size = [1, -1, 91, 19, 19]     | Unknown  | Done       | 1.0   | -1     |
|  542 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]         | Unknown  | Done       | 1.0   | -1     |
|  543 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20]     | Unknown  | Done       | 1.0   | -1     |
|  544 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]         | Unknown  | Done       | 1.0   | -1     |
|  545 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]         | Unknown  | Done       | 1.0   | -1     |
|  546 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 128]    | Done     | Done       | 1.0   | -1     |
|  547 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [3136, 128]             | Done     | Done       | 1.0   | -1     |
|  548 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int] size = [3136, 384]             | Done     | Done       | 1.0   | -1     |
|  549 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int] size = [3136, 512]             | Done     | Done       | 1.0   | -1     |
|  550 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 96]      | Done     | Done       | 1.0   | -1     |
|  551 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [3136, 96]               | Done     | Done       | 1.0   | -1     |
|  552 | Tensor<[1, 576, 1, 1]> self = ?,<br>List[int] size = [1, 576]                  | Done     | Done       | 1.0   | -1     |
|  553 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  554 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Unknown  | Done       | 1.0   | -1     |
|  555 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, 59, 16, 64]            | Unknown  | Done       | 1.0   | -1     |
|  556 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  557 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]                   | Unknown  | Done       | 1.0   | -1     |
|  558 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]                         | Unknown  | Done       | 1.0   | -1     |
|  559 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                           | Unknown  | Done       | 1.0   | -1     |
|  560 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | 1.0   | -1     |
|  561 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]                 | Unknown  | Done       | 1.0   | -1     |
|  562 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]                 | Unknown  | Done       | 1.0   | -1     |
|  563 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]                   | Unknown  | Done       | 1.0   | -1     |
|  564 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]                   | Unknown  | Done       | 1.0   | -1     |
|  565 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]                 | Unknown  | Done       | 1.0   | -1     |
|  566 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
|  567 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]               | Unknown  | Done       | 1.0   | -1     |
|  568 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]               | Unknown  | Done       | 1.0   | -1     |
|  569 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]               | Unknown  | Done       | 1.0   | -1     |
|  570 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]                 | Unknown  | Done       | 1.0   | -1     |
|  571 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]               | Unknown  | Done       | 1.0   | -1     |
|  572 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]               | Unknown  | Done       | 1.0   | -1     |
|  573 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  574 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]                 | Unknown  | Done       | 1.0   | -1     |
|  575 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  576 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
|  577 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 1024]      | Done     | Done       | 1.0   | -1     |
|  578 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [64, 1024]                 | Done     | Done       | 1.0   | -1     |
|  579 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]                | Done     | Done       | 1.0   | -1     |
|  580 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]         | Done     | Done       | 1.0   | -1     |
|  581 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]             | Done     | Done       | 1.0   | -1     |
|  582 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]             | Done     | Done       | 1.0   | -1     |
|  583 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]         | Done     | Done       | 1.0   | -1     |
|  584 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                    | Done     | Done       | 1.0   | -1     |
|  585 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]         | Done     | Done       | 1.0   | -1     |
|  586 | Tensor<[1, 64, 256]> self = ?,<br>List[int] size = [1, 64, 16, 16]             | Done     | Done       | 1.0   | -1     |
|  587 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int] size = [-1, 3, 49, 49]       | Done     | Done       | 1.0   | -1     |
|  588 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]       | Done     | Done       | 1.0   | -1     |
|  589 | Tensor<[1, 64, 3072]> self = ?,<br>List[int] size = [1, 64, 3, 32, 32]         | Done     | Done       | 1.0   | -1     |
|  590 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]                  | Done     | Done       | 1.0   | -1     |
|  591 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int] size = [-1, 4, 49, 49]       | Done     | Done       | 1.0   | -1     |
|  592 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int] size = [-1, 4, 64, 64]       | Done     | Done       | 1.0   | -1     |
|  593 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]            | Done     | Done       | 1.0   | -1     |
|  594 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]    | Done     | Done       | 1.0   | -1     |
|  595 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]             | Done     | Done       | 1.0   | -1     |
|  596 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]          | Unknown  | Done       | 1.0   | -1     |
|  597 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]             | Done     | Done       | 1.0   | -1     |
|  598 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int] size = [4096, 512]             | Done     | Done       | 1.0   | -1     |
|  599 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 4096, 64]            | Done     | Done       | 1.0   | -1     |
|  600 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]            | Done     | Done       | 1.0   | -1     |
|  601 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]      | Done     | Done       | 1.0   | -1     |
|  602 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Done     | Done       | 1.0   | -1     |
|  603 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [64, 64, 9]               | Done     | Done       | 1.0   | -1     |
|  604 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 768]        | Done     | Done       | 1.0   | -1     |
|  605 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                   | Done     | Done       | 1.0   | -1     |
|  606 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [64, 9, 64]               | Done     | Done       | 1.0   | -1     |
|  607 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [64, 9, 9]                 | Done     | Done       | 1.0   | -1     |
|  608 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]          | Done     | Done       | 1.0   | -1     |
|  609 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]          | Done     | Done       | 1.0   | -1     |
|  610 | Tensor<[1, 640]> self = ?,<br>List[int] size = [640]                           | Done     | Done       | 1.0   | -1     |
|  611 | Tensor<[1, 64]> self = ?,<br>List[int] size = [64]                             | Done     | Done       | 1.0   | -1     |
|  612 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672]                  | Done     | Done       | 1.0   | -1     |
|  613 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | 1.0   | -1     |
|  614 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768]               | Done     | Done       | 1.0   | -1     |
|  615 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]                  | Done     | Done       | 1.0   | -1     |
|  616 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 1024]    | Done     | Unknown    | N/A   | N/A    |
|  617 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [49, 1024]               | Done     | Unknown    | N/A   | N/A    |
|  618 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int] size = [49, 1536]               | Done     | Done       | 1.0   | -1     |
|  619 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int] size = [49, 2048]               | Done     | Unknown    | N/A   | N/A    |
|  620 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int] size = [49, 3072]               | Done     | Done       | 1.0   | -1     |
|  621 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int] size = [49, 4096]               | Done     | Unknown    | N/A   | N/A    |
|  622 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 768]      | Done     | Done       | 1.0   | -1     |
|  623 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [49, 768]                 | Done     | Done       | 1.0   | -1     |
|  624 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 7, 768]                 | Done     | Done       | 1.0   | -1     |
|  625 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]                    | Done     | Done       | 1.0   | -1     |
|  626 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 12, 64]               | Done     | Done       | 1.0   | -1     |
|  627 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [7, 768]                     | Done     | Done       | 1.0   | -1     |
|  628 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int] size = [1, 7392]                | Done     | Done       | 1.0   | -1     |
|  629 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]                  | Done     | Done       | 1.0   | -1     |
|  630 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192]           | Done     | Done       | 1.0   | -1     |
|  631 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]           | Done     | Done       | 1.0   | -1     |
|  632 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12]           | Done     | Done       | 1.0   | -1     |
|  633 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14]           | Done     | Done       | 1.0   | -1     |
|  634 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]                 | Done     | Done       | 1.0   | -1     |
|  635 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]                 | Done     | Done       | 1.0   | -1     |
|  636 | Tensor<[1, 768, 49]> self = ?,<br>List[int] size = [1, 768, 7, 7]              | Unknown  | Done       | 1.0   | -1     |
|  637 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]              | Done     | Done       | 1.0   | -1     |
|  638 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                     | Unknown  | Done       | 1.0   | -1     |
|  639 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                           | Done     | Done       | 1.0   | -1     |
|  640 | Tensor<[1, 784, 1, 1]> self = ?,<br>List[int] size = [1, 784]                  | Done     | Done       | 1.0   | -1     |
|  641 | Tensor<[1, 784]> self = ?,<br>List[int] size = [784]                           | Done     | Done       | 1.0   | -1     |
|  642 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]                           | Done     | Done       | 1.0   | -1     |
|  643 | Tensor<[1, 7]> self = ?,<br>List[int] size = [1, -1]                           | Done     | Done       | 1.0   | -1     |
|  644 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]                 | Unknown  | Done       | 1.0   | -1     |
|  645 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]                   | Unknown  | Done       | 1.0   | -1     |
|  646 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]                   | Unknown  | Done       | 1.0   | -1     |
|  647 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]                 | Unknown  | Done       | 1.0   | -1     |
|  648 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]               | Done     | Done       | 1.0   | -1     |
|  649 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
|  650 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]               | Unknown  | Done       | 1.0   | -1     |
|  651 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]               | Unknown  | Done       | 1.0   | -1     |
|  652 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]                 | Unknown  | Done       | 1.0   | -1     |
|  653 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]         | Done     | Done       | 1.0   | -1     |
|  654 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]         | Done     | Done       | 1.0   | -1     |
|  655 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]           | Done     | Done       | 1.0   | -1     |
|  656 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]           | Done     | Done       | 1.0   | -1     |
|  657 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]         | Done     | Done       | 1.0   | -1     |
|  658 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]           | Done     | Done       | 1.0   | -1     |
|  659 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]             | Done     | Done       | 1.0   | -1     |
|  660 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]             | Done     | Unknown    | N/A   | N/A    |
|  661 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]           | Done     | Done       | 1.0   | -1     |
|  662 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]             | Done     | Done       | 1.0   | -1     |
|  663 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]           | Done     | Done       | 1.0   | -1     |
|  664 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  665 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]               | Unknown  | Done       | 1.0   | -1     |
|  666 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  667 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]                 | Unknown  | Done       | 1.0   | -1     |
|  668 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]             | Done     | Done       | 1.0   | -1     |
|  669 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  670 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 1024]    | Done     | Done       | 1.0   | -1     |
|  671 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [64, 1024]               | Done     | Done       | 1.0   | -1     |
|  672 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]               | Done     | Done       | 1.0   | -1     |
|  673 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int] size = [64, 2048]               | Done     | Done       | 1.0   | -1     |
|  674 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]               | Done     | Done       | 1.0   | -1     |
|  675 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int] size = [64, 4096]               | Done     | Done       | 1.0   | -1     |
|  676 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]      | Done     | Done       | 1.0   | -1     |
|  677 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [64, 768]                 | Done     | Done       | 1.0   | -1     |
|  678 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
|  679 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136] | Unknown  | Unknown    | N/A   | N/A    |
|  680 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]     | Unknown  | Unknown    | N/A   | N/A    |
|  681 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]     | Unknown  | Unknown    | N/A   | N/A    |
|  682 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]     | Unknown  | Unknown    | N/A   | N/A    |
|  683 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]         | Unknown  | Unknown    | N/A   | N/A    |
|  684 | Tensor<[1, 888, 1, 1]> self = ?,<br>List[int] size = [1, 888]                  | Done     | Done       | 1.0   | -1     |
|  685 | Tensor<[1, 8]> self = ?,<br>List[int] size = [-1, 2]                           | Unknown  | Done       | 1.0   | -1     |
|  686 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [1, 9, 16, 64]              | Done     | Done       | 1.0   | -1     |
|  687 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]                   | Done     | Done       | 1.0   | -1     |
|  688 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]             | Unknown  | Done       | 1.0   | -1     |
|  689 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]                     | Done     | Done       | 1.0   | -1     |
|  690 | Tensor<[1, 9, 16384]> self = ?,<br>List[int] size = [9, 16384]                 | Done     | Done       | 1.0   | -1     |
|  691 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [1, 9, 16, 128]             | Done     | Done       | 1.0   | -1     |
|  692 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [9, 2048]                   | Done     | Done       | 1.0   | -1     |
|  693 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]                   | Done     | Done       | 1.0   | -1     |
|  694 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]               | Unknown  | Done       | 1.0   | -1     |
|  695 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [1, 9, 64, 64]              | Done     | Done       | 1.0   | -1     |
|  696 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]                   | Done     | Done       | 1.0   | -1     |
|  697 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]               | Unknown  | Done       | 1.0   | -1     |
|  698 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [1, 9, 12, 64]               | Done     | Done       | 1.0   | -1     |
|  699 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                     | Done     | Done       | 1.0   | -1     |
|  700 | Tensor<[1, 9, 8192]> self = ?,<br>List[int] size = [9, 8192]                   | Done     | Done       | 1.0   | -1     |
|  701 | Tensor<[1, 912, 1, 1]> self = ?,<br>List[int] size = [1, 912]                  | Done     | Done       | 1.0   | -1     |
|  702 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]                  | Done     | Done       | 1.0   | -1     |
|  703 | Tensor<[1, 9216]> self = ?,<br>List[int] size = [1, 64, 12, 12]                | Done     | Done       | 1.0   | -1     |
|  704 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960]                  | Done     | Done       | 1.0   | -1     |
|  705 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]         | Unknown  | Unknown    | N/A   | N/A    |
|  706 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 1280]   | Unknown  | Unknown    | N/A   | N/A    |
|  707 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [<s0*s1>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  708 | Tensor<[1, s0*s1, 2560]> self = ?,<br>List[int] size = [<s0*s1>, 2560]         | Unknown  | Unknown    | N/A   | N/A    |
|  709 | Tensor<[1, s0*s1, 5120]> self = ?,<br>List[int] size = [<s0*s1>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
|  710 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]           | Unknown  | Unknown    | N/A   | N/A    |
|  711 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 640]     | Unknown  | Unknown    | N/A   | N/A    |
|  712 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [<s0*s1>, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  713 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  714 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  715 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]     | Unknown  | Unknown    | N/A   | N/A    |
|  716 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]       | Unknown  | Unknown    | N/A   | N/A    |
|  717 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]         | Unknown  | Unknown    | N/A   | N/A    |
|  718 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 1280]   | Unknown  | Unknown    | N/A   | N/A    |
|  719 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [<s1*s2>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  720 | Tensor<[1, s1*s2, 2560]> self = ?,<br>List[int] size = [<s1*s2>, 2560]         | Unknown  | Unknown    | N/A   | N/A    |
|  721 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]           | Unknown  | Unknown    | N/A   | N/A    |
|  722 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 320]     | Unknown  | Unknown    | N/A   | N/A    |
|  723 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [<s1*s2>, 320]           | Unknown  | Unknown    | N/A   | N/A    |
|  724 | Tensor<[1, s1*s2, 5120]> self = ?,<br>List[int] size = [<s1*s2>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
|  725 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]           | Unknown  | Unknown    | N/A   | N/A    |
|  726 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 640]     | Unknown  | Unknown    | N/A   | N/A    |
|  727 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [<s1*s2>, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  728 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  729 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]           | Unknown  | Unknown    | N/A   | N/A    |
|  730 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  731 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]     | Unknown  | Unknown    | N/A   | N/A    |
|  732 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]       | Unknown  | Unknown    | N/A   | N/A    |
|  733 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]       | Unknown  | Unknown    | N/A   | N/A    |
|  734 | Tensor<[1, s10 + 1]> self = ?,<br>List[int] size = [1, -1]                     | Unknown  | Unknown    | N/A   | N/A    |
|  735 | Tensor<[10, 1024]> self = ?,<br>List[int] size = [1, 10, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  736 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]                 | Unknown  | Done       | 1.0   | -1     |
|  737 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002]             | Done     | Done       | 1.0   | -1     |
|  738 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]                 | Done     | Done       | 1.0   | -1     |
|  739 | Tensor<[10, 4096]> self = ?,<br>List[int] size = [1, 10, 4096]                 | Unknown  | Done       | 1.0   | -1     |
|  740 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]                   | Unknown  | Done       | 1.0   | -1     |
|  741 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                   | Done     | Done       | 1.0   | -1     |
|  742 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]               | Done     | Done       | 1.0   | -1     |
|  743 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]                 | Done     | Done       | 1.0   | -1     |
|  744 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 8, 32]               | Done     | Done       | 1.0   | -1     |
|  745 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Unknown  | Done       | 1.0   | -1     |
|  746 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]                 | Done     | Done       | 1.0   | -1     |
|  747 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]               | Done     | Done       | 1.0   | -1     |
|  748 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]                 | Done     | Done       | 1.0   | -1     |
|  749 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]                     | Done     | Done       | 1.0   | -1     |
|  750 | Tensor<[100, 8, 32]> self = ?,<br>List[int] size = [100, 256]                  | Done     | Done       | 1.0   | -1     |
|  751 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]                   | Done     | Done       | 1.0   | -1     |
|  752 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                            | Unknown  | Done       | 1.0   | -1     |
|  753 | Tensor<[1024, 1024]> self = ?,<br>List[int] size = [1, 32, 32, 1024]           | Done     | Done       | 1.0   | -1     |
|  754 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]               | Done     | Done       | 1.0   | -1     |
|  755 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]             | Done     | Done       | 1.0   | -1     |
|  756 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [16, 64, 192]                | Done     | Done       | 1.0   | -1     |
|  757 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]               | Done     | Done       | 1.0   | -1     |
|  758 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  759 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [16, 64, 256]                | Done     | Done       | 1.0   | -1     |
|  760 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]                | Done     | Done       | 1.0   | -1     |
|  761 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]               | Done     | Done       | 1.0   | -1     |
|  762 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]             | Done     | Done       | 1.0   | -1     |
|  763 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [16, 64, 768]                | Done     | Done       | 1.0   | -1     |
|  764 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Done     | Done       | 1.0   | -1     |
|  765 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
|  766 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
|  767 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]               | Unknown  | Done       | 1.0   | -1     |
|  768 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  769 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                 | Unknown  | Done       | 1.0   | -1     |
|  770 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | 1.0   | -1     |
|  771 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  772 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  773 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  774 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]             | Done     | Done       | 1.0   | -1     |
|  775 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]             | Done     | Done       | 1.0   | -1     |
|  776 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]             | Done     | Done       | 1.0   | -1     |
|  777 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Done     | Done       | 1.0   | -1     |
|  778 | Tensor<[12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]             | Done     | Done       | 1.0   | -1     |
|  779 | Tensor<[12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]             | Done     | Done       | 1.0   | -1     |
|  780 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]             | Done     | Done       | 1.0   | -1     |
|  781 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]             | Done     | Done       | 1.0   | -1     |
|  782 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]         | Done     | Done       | 1.0   | -1     |
|  783 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]           | Done     | Done       | 1.0   | -1     |
|  784 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [1, 12, 24, 24]             | Done     | Done       | 1.0   | -1     |
|  785 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]                | Done     | Done       | 1.0   | -1     |
|  786 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]             | Done     | Done       | 1.0   | -1     |
|  787 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]                | Done     | Done       | 1.0   | -1     |
|  788 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]             | Done     | Done       | 1.0   | -1     |
|  789 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]             | Done     | Done       | 1.0   | -1     |
|  790 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]                       | Done     | Done       | 1.0   | -1     |
|  791 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]                 | Done     | Done       | 1.0   | -1     |
|  792 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | 1.0   | -1     |
|  793 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | 1.0   | -1     |
|  794 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]             | Done     | Done       | 1.0   | -1     |
|  795 | Tensor<[12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]           | Done     | Done       | 1.0   | -1     |
|  796 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]               | Done     | Done       | 1.0   | -1     |
|  797 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                 | Done     | Done       | 1.0   | -1     |
|  798 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]                   | Done     | Done       | 1.0   | -1     |
|  799 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]               | Done     | Done       | 1.0   | -1     |
|  800 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                 | Done     | Done       | 1.0   | -1     |
|  801 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]             | Done     | Done       | 1.0   | -1     |
|  802 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]               | Done     | Done       | 1.0   | -1     |
|  803 | Tensor<[128, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]            | Done     | Unknown    | N/A   | N/A    |
|  804 | Tensor<[128, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]            | Done     | Unknown    | N/A   | N/A    |
|  805 | Tensor<[128, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]            | Done     | Done       | 1.0   | -1     |
|  806 | Tensor<[128, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]            | Done     | Done       | 1.0   | -1     |
|  807 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       | 1.0   | -1     |
|  808 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       | 1.0   | -1     |
|  809 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                    | Unknown  | Done       | 1.0   | -1     |
|  810 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                    | Unknown  | Done       | 1.0   | -1     |
|  811 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                            | Unknown  | Done       | 1.0   | -1     |
|  812 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 1280]             | Done     | Done       | 1.0   | -1     |
|  813 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 16, 80]           | Done     | Done       | 1.0   | -1     |
|  814 | Tensor<[1370, 1, 16, 80]> self = ?,<br>List[int] size = [1370, 1280]           | Done     | Done       | 1.0   | -1     |
|  815 | Tensor<[1370, 1, 3840]> self = ?,<br>List[int] size = [1370, 1, 3, 1280]       | Done     | Done       | 1.0   | -1     |
|  816 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1, 1370, 1280]             | Done     | Done       | 1.0   | -1     |
|  817 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1370, 1, 1280]             | Done     | Done       | 1.0   | -1     |
|  818 | Tensor<[1370, 3840]> self = ?,<br>List[int] size = [1370, 1, 3840]             | Done     | Done       | 1.0   | -1     |
|  819 | Tensor<[1370, 5120]> self = ?,<br>List[int] size = [1, 1370, 5120]             | Done     | Done       | 1.0   | -1     |
|  820 | Tensor<[13]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
|  821 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                    | Done     | Done       | 1.0   | -1     |
|  822 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]                  | Done     | Done       | 1.0   | -1     |
|  823 | Tensor<[14, 2]> self = ?,<br>List[int] size = [1, 14, 2]                       | Done     | Done       | 1.0   | -1     |
|  824 | Tensor<[14, 3072]> self = ?,<br>List[int] size = [1, 14, 3072]                 | Done     | Done       | 1.0   | -1     |
|  825 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]                    | Done     | Done       | 1.0   | -1     |
|  826 | Tensor<[14, 768]> self = ?,<br>List[int] size = [1, 14, 768]                   | Done     | Done       | 1.0   | -1     |
|  827 | Tensor<[1444, 8]> self = ?,<br>List[int] size = [-1, 2]                        | Unknown  | Done       | 1.0   | -1     |
|  828 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]               | Done     | Done       | 1.0   | -1     |
|  829 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]               | Done     | Done       | 1.0   | -1     |
|  830 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  831 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]                   | Unknown  | Done       | 1.0   | -1     |
|  832 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]                   | Unknown  | Done       | 1.0   | -1     |
|  833 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]             | Unknown  | Done       | 1.0   | -1     |
|  834 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]               | Unknown  | Done       | 1.0   | -1     |
|  835 | Tensor<[16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]               | Unknown  | Done       | 1.0   | -1     |
|  836 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                 | Unknown  | Done       | 1.0   | -1     |
|  837 | Tensor<[16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                 | Unknown  | Unknown    | N/A   | N/A    |
|  838 | Tensor<[16, 1, 60]> self = ?,<br>List[int] size = [1, 16, 1, 60]               | Unknown  | Done       | 1.0   | -1     |
|  839 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  840 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Done       | 1.0   | -1     |
|  841 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  842 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  843 | Tensor<[16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]             | Unknown  | Done       | 1.0   | -1     |
|  844 | Tensor<[16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]             | Unknown  | Done       | 1.0   | -1     |
|  845 | Tensor<[16, 1370, 80]> self = ?,<br>List[int] size = [1, 16, 1370, 80]         | Done     | Done       | 1.0   | -1     |
|  846 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                    | Done     | Done       | 1.0   | -1     |
|  847 | Tensor<[16, 19, 19]> self = ?,<br>List[int] size = [1, 16, 19, 19]             | Done     | Done       | 1.0   | -1     |
|  848 | Tensor<[16, 19, 64]> self = ?,<br>List[int] size = [1, 16, 19, 64]             | Done     | Done       | 1.0   | -1     |
|  849 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197]         | Done     | Done       | 1.0   | -1     |
|  850 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]           | Done     | Done       | 1.0   | -1     |
|  851 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256]         | Done     | Done       | 1.0   | -1     |
|  852 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]           | Done     | Done       | 1.0   | -1     |
|  853 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]                 | Done     | Done       | 1.0   | -1     |
|  854 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]             | Done     | Done       | 1.0   | -1     |
|  855 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]             | Done     | Done       | 1.0   | -1     |
|  856 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 192]       | Done     | Done       | 1.0   | -1     |
|  857 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [784, 192]                 | Done     | Done       | 1.0   | -1     |
|  858 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 256]       | Done     | Unknown    | N/A   | N/A    |
|  859 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [784, 256]                 | Done     | Unknown    | N/A   | N/A    |
|  860 | Tensor<[16, 49, 576]> self = ?,<br>List[int] size = [16, 49, 3, 6, 32]         | Done     | Done       | 1.0   | -1     |
|  861 | Tensor<[16, 49, 768]> self = ?,<br>List[int] size = [16, 49, 3, 8, 32]         | Done     | Unknown    | N/A   | N/A    |
|  862 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Done       | 1.0   | -1     |
|  863 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Done       | 1.0   | -1     |
|  864 | Tensor<[16, 50, 64]> self = ?,<br>List[int] size = [1, 16, 50, 64]             | Done     | Done       | 1.0   | -1     |
|  865 | Tensor<[16, 59, 59]> self = ?,<br>List[int] size = [1, 16, 59, 59]             | Unknown  | Done       | 1.0   | -1     |
|  866 | Tensor<[16, 59, 64]> self = ?,<br>List[int] size = [1, 16, 59, 64]             | Unknown  | Done       | 1.0   | -1     |
|  867 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [1, 16, 6, 49, 49]       | Done     | Done       | 1.0   | -1     |
|  868 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [96, 49, 49]             | Done     | Done       | 1.0   | -1     |
|  869 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64, 64]       | Done     | Done       | 1.0   | -1     |
|  870 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]             | Done     | Done       | 1.0   | -1     |
|  871 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 192]       | Done     | Done       | 1.0   | -1     |
|  872 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]                | Done     | Done       | 1.0   | -1     |
|  873 | Tensor<[16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]           | Done     | Done       | 1.0   | -1     |
|  874 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 256]       | Done     | Done       | 1.0   | -1     |
|  875 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1024, 256]                | Done     | Done       | 1.0   | -1     |
|  876 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]         | Done     | Done       | 1.0   | -1     |
|  877 | Tensor<[16, 64, 768]> self = ?,<br>List[int] size = [16, 64, 3, 8, 32]         | Done     | Done       | 1.0   | -1     |
|  878 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]                | Done     | Done       | 1.0   | -1     |
|  879 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]                  | Done     | Done       | 1.0   | -1     |
|  880 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]                   | Done     | Done       | 1.0   | -1     |
|  881 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [1, 16, 8, 49, 49]       | Done     | Unknown    | N/A   | N/A    |
|  882 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [128, 49, 49]            | Done     | Unknown    | N/A   | N/A    |
|  883 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [1, 16, 8, 64, 64]       | Done     | Done       | 1.0   | -1     |
|  884 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [128, 64, 64]            | Done     | Done       | 1.0   | -1     |
|  885 | Tensor<[16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]             | Done     | Done       | 1.0   | -1     |
|  886 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]               | Done     | Done       | 1.0   | -1     |
|  887 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                 | Done     | Done       | 1.0   | -1     |
|  888 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]             | Done     | Done       | 1.0   | -1     |
|  889 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]             | Done     | Done       | 1.0   | -1     |
|  890 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]               | Done     | Done       | 1.0   | -1     |
|  891 | Tensor<[17]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
|  892 | Tensor<[19, 1024]> self = ?,<br>List[int] size = [1, 19, 1024]                 | Done     | Done       | 1.0   | -1     |
|  893 | Tensor<[19, 256008]> self = ?,<br>List[int] size = [1, 19, 256008]             | Done     | Done       | 1.0   | -1     |
|  894 | Tensor<[19, 4096]> self = ?,<br>List[int] size = [1, 19, 4096]                 | Done     | Done       | 1.0   | -1     |
|  895 | Tensor<[192, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]            | Done     | Done       | 1.0   | -1     |
|  896 | Tensor<[192, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]            | Done     | Done       | 1.0   | -1     |
|  897 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]            | Done     | Done       | 1.0   | -1     |
|  898 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]            | Done     | Done       | 1.0   | -1     |
|  899 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]             | Done     | Done       | 1.0   | -1     |
|  900 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]               | Done     | Done       | 1.0   | -1     |
|  901 | Tensor<[196, 1152]> self = ?,<br>List[int] size = [4, 49, 1152]                | Done     | Done       | 1.0   | -1     |
|  902 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [1, 14, 14, 1536]            | Done     | Done       | 1.0   | -1     |
|  903 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [4, 49, 1536]                | Done     | Unknown    | N/A   | N/A    |
|  904 | Tensor<[196, 2048]> self = ?,<br>List[int] size = [1, 14, 14, 2048]            | Done     | Unknown    | N/A   | N/A    |
|  905 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]               | Done     | Done       | 1.0   | -1     |
|  906 | Tensor<[196, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]              | Done     | Done       | 1.0   | -1     |
|  907 | Tensor<[196, 384]> self = ?,<br>List[int] size = [4, 49, 384]                  | Done     | Done       | 1.0   | -1     |
|  908 | Tensor<[196, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]              | Done     | Unknown    | N/A   | N/A    |
|  909 | Tensor<[196, 512]> self = ?,<br>List[int] size = [4, 49, 512]                  | Done     | Unknown    | N/A   | N/A    |
|  910 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]                 | Done     | Done       | 1.0   | -1     |
|  911 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 1024]               | Done     | Done       | 1.0   | -1     |
|  912 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 16, 64]             | Done     | Done       | 1.0   | -1     |
|  913 | Tensor<[197, 1, 12, 64]> self = ?,<br>List[int] size = [197, 768]              | Done     | Done       | 1.0   | -1     |
|  914 | Tensor<[197, 1, 16, 64]> self = ?,<br>List[int] size = [197, 1024]             | Done     | Done       | 1.0   | -1     |
|  915 | Tensor<[197, 1, 2304]> self = ?,<br>List[int] size = [197, 1, 3, 768]          | Done     | Done       | 1.0   | -1     |
|  916 | Tensor<[197, 1, 3072]> self = ?,<br>List[int] size = [197, 1, 3, 1024]         | Done     | Done       | 1.0   | -1     |
|  917 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 12, 64]              | Done     | Done       | 1.0   | -1     |
|  918 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 768]                 | Done     | Done       | 1.0   | -1     |
|  919 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]               | Done     | Done       | 1.0   | -1     |
|  920 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [197, 1, 1024]               | Done     | Done       | 1.0   | -1     |
|  921 | Tensor<[197, 197, 12]> self = ?,<br>List[int] size = [38809, 12]               | Done     | Done       | 1.0   | -1     |
|  922 | Tensor<[197, 197, 16]> self = ?,<br>List[int] size = [38809, 16]               | Done     | Done       | 1.0   | -1     |
|  923 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                          | None     | Fallback   | 1.0   | -1     |
|  924 | Tensor<[197, 2304]> self = ?,<br>List[int] size = [197, 1, 2304]               | Done     | Done       | 1.0   | -1     |
|  925 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]               | Done     | Done       | 1.0   | -1     |
|  926 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [197, 1, 3072]               | Done     | Done       | 1.0   | -1     |
|  927 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]               | Done     | Done       | 1.0   | -1     |
|  928 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]                 | Done     | Done       | 1.0   | -1     |
|  929 | Tensor<[197, 768]> self = ?,<br>List[int] size = [197, 1, 768]                 | Done     | Done       | 1.0   | -1     |
|  930 | Tensor<[19]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
|  931 | Tensor<[19]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
|  932 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Done       | 1.0   | -1     |
|  933 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Done       | 1.0   | -1     |
|  934 | Tensor<[2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]             | Done     | Done       | 1.0   | -1     |
|  935 | Tensor<[2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]             | Done     | Done       | 1.0   | -1     |
|  936 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]         | Done     | Done       | 1.0   | -1     |
|  937 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]           | Done     | Done       | 1.0   | -1     |
|  938 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]         | Done     | Done       | 1.0   | -1     |
|  939 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]           | Done     | Done       | 1.0   | -1     |
|  940 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]                  | Done     | Done       | 1.0   | -1     |
|  941 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]                    | Done     | Done       | 1.0   | -1     |
|  942 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]               | Done     | Done       | 1.0   | -1     |
|  943 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]                | Done     | Done       | 1.0   | -1     |
|  944 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]                | Unknown  | Done       | 1.0   | -1     |
|  945 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]                           | Done     | Done       | 1.0   | -1     |
|  946 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]               | Done     | Done       | 1.0   | -1     |
|  947 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]                  | Done     | Done       | 1.0   | -1     |
|  948 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]             | Done     | Done       | 1.0   | -1     |
|  949 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]               | Done     | Done       | 1.0   | -1     |
|  950 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]               | Done     | Unknown    | N/A   | N/A    |
|  951 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, 2048, 768]               | Done     | Unknown    | N/A   | N/A    |
|  952 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Done     | Done       | 1.0   | -1     |
|  953 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
|  954 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
|  955 | Tensor<[221, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Unknown  | Done       | 1.0   | -1     |
|  956 | Tensor<[221, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Unknown  | Done       | 1.0   | -1     |
|  957 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]                | Done     | Done       | 1.0   | -1     |
|  958 | Tensor<[225, 16]> self = ?,<br>List[int] size = [1, 15, 15, 16]                | Done     | Done       | 1.0   | -1     |
|  959 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]                | Done     | Done       | 1.0   | -1     |
|  960 | Tensor<[225, 32]> self = ?,<br>List[int] size = [1, 15, 15, 32]                | Done     | Done       | 1.0   | -1     |
|  961 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]                  | Done     | Done       | 1.0   | -1     |
|  962 | Tensor<[225, 4]> self = ?,<br>List[int] size = [1, 15, 15, 4]                  | Done     | Done       | 1.0   | -1     |
|  963 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]              | Done     | Done       | 1.0   | -1     |
|  964 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]                  | Done     | Done       | 1.0   | -1     |
|  965 | Tensor<[225, 8]> self = ?,<br>List[int] size = [1, 15, 15, 8]                  | Done     | Done       | 1.0   | -1     |
|  966 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]                | Done     | Done       | 1.0   | -1     |
|  967 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                | Done     | Done       | 1.0   | -1     |
|  968 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]                 | Done     | Done       | 1.0   | -1     |
|  969 | Tensor<[24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]             | Done     | Done       | 1.0   | -1     |
|  970 | Tensor<[24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]             | Done     | Done       | 1.0   | -1     |
|  971 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                | Done     | Done       | 1.0   | -1     |
|  972 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]             | Done     | Done       | 1.0   | -1     |
|  973 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]             | Done     | Done       | 1.0   | -1     |
|  974 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]                   | Done     | Done       | 1.0   | -1     |
|  975 | Tensor<[2401, 12]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Done       | 1.0   | -1     |
|  976 | Tensor<[2401, 16]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Unknown    | N/A   | N/A    |
|  977 | Tensor<[2401, 24]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Done       | 1.0   | -1     |
|  978 | Tensor<[2401, 32]> self = ?,<br>List[int] size = [49, 49, -1]                  | Done     | Unknown    | N/A   | N/A    |
|  979 | Tensor<[2401, 3]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | 1.0   | -1     |
|  980 | Tensor<[2401, 4]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | 1.0   | -1     |
|  981 | Tensor<[2401, 6]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | 1.0   | -1     |
|  982 | Tensor<[2401, 8]> self = ?,<br>List[int] size = [49, 49, -1]                   | Done     | Done       | 1.0   | -1     |
|  983 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                         | Unknown  | Done       | 1.0   | -1     |
|  984 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]                       | Done     | Done       | 1.0   | -1     |
|  985 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]                 | Done     | Done       | 1.0   | -1     |
|  986 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]                   | Done     | Done       | 1.0   | -1     |
|  987 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]               | Done     | Done       | 1.0   | -1     |
|  988 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]                | Done     | Done       | 1.0   | -1     |
|  989 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]               | Done     | Done       | 1.0   | -1     |
|  990 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]            | Done     | Done       | 1.0   | -1     |
|  991 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [4, 64, 1536]                | Done     | Done       | 1.0   | -1     |
|  992 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]                 | Done     | Done       | 1.0   | -1     |
|  993 | Tensor<[256, 2048]> self = ?,<br>List[int] size = [1, 16, 16, 2048]            | Done     | Done       | 1.0   | -1     |
|  994 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                 | Done     | Done       | 1.0   | -1     |
|  995 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]                     | Done     | Done       | 1.0   | -1     |
|  996 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]                   | Done     | Done       | 1.0   | -1     |
|  997 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]              | Done     | Done       | 1.0   | -1     |
|  998 | Tensor<[256, 384]> self = ?,<br>List[int] size = [4, 64, 384]                  | Done     | Done       | 1.0   | -1     |
|  999 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]               | Done     | Done       | 1.0   | -1     |
| 1000 | Tensor<[256, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]            | Done     | Done       | 1.0   | -1     |
| 1001 | Tensor<[256, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]            | Done     | Done       | 1.0   | -1     |
| 1002 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512]              | Done     | Done       | 1.0   | -1     |
| 1003 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                 | Done     | Done       | 1.0   | -1     |
| 1004 | Tensor<[256, 512]> self = ?,<br>List[int] size = [4, 64, 512]                  | Done     | Done       | 1.0   | -1     |
| 1005 | Tensor<[256, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]            | Done     | Done       | 1.0   | -1     |
| 1006 | Tensor<[256, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]            | Done     | Done       | 1.0   | -1     |
| 1007 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]                   | Done     | Done       | 1.0   | -1     |
| 1008 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]                 | Done     | Done       | 1.0   | -1     |
| 1009 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       | 1.0   | -1     |
| 1010 | Tensor<[25]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
| 1011 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                    | Done     | Done       | 1.0   | -1     |
| 1012 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Done       | 1.0   | -1     |
| 1013 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Done       | 1.0   | -1     |
| 1014 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]       | Done     | Done       | 1.0   | -1     |
| 1015 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]           | Done     | Done       | 1.0   | -1     |
| 1016 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]                 | Done     | Done       | 1.0   | -1     |
| 1017 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]               | Done     | Done       | 1.0   | -1     |
| 1018 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]                 | Done     | Done       | 1.0   | -1     |
| 1019 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]                 | Done     | Done       | 1.0   | -1     |
| 1020 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]                   | Done     | Done       | 1.0   | -1     |
| 1021 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128]             | Done     | Done       | 1.0   | -1     |
| 1022 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [64, 49, 128]                | Done     | Done       | 1.0   | -1     |
| 1023 | Tensor<[3136, 288]> self = ?,<br>List[int] size = [64, 49, 288]                | Done     | Done       | 1.0   | -1     |
| 1024 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [1, 56, 56, 384]             | Done     | Done       | 1.0   | -1     |
| 1025 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [64, 49, 384]                | Done     | Done       | 1.0   | -1     |
| 1026 | Tensor<[3136, 512]> self = ?,<br>List[int] size = [1, 56, 56, 512]             | Done     | Done       | 1.0   | -1     |
| 1027 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]               | Done     | Done       | 1.0   | -1     |
| 1028 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [64, 49, 96]                  | Done     | Done       | 1.0   | -1     |
| 1029 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]                 | Done     | Done       | 1.0   | -1     |
| 1030 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]             | Done     | Done       | 1.0   | -1     |
| 1031 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                    | Done     | Done       | 1.0   | -1     |
| 1032 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]                 | Done     | Done       | 1.0   | -1     |
| 1033 | Tensor<[32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]             | Done     | Unknown    | N/A   | N/A    |
| 1034 | Tensor<[32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]             | Done     | Unknown    | N/A   | N/A    |
| 1035 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]                 | Done     | Done       | 1.0   | -1     |
| 1036 | Tensor<[32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]             | Done     | Done       | 1.0   | -1     |
| 1037 | Tensor<[32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]             | Done     | Done       | 1.0   | -1     |
| 1038 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]                   | Unknown  | Done       | 1.0   | -1     |
| 1039 | Tensor<[3234, 2, 2]> self = ?,<br>List[int] size = [3234, 4]                   | Unknown  | Done       | 1.0   | -1     |
| 1040 | Tensor<[3400, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                     | Unknown  | Done       | 1.0   | -1     |
| 1041 | Tensor<[3400, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                     | Unknown  | Done       | 1.0   | -1     |
| 1042 | Tensor<[34]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
| 1043 | Tensor<[361, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Unknown  | Done       | 1.0   | -1     |
| 1044 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]               | Done     | Done       | 1.0   | -1     |
| 1045 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]               | Done     | Done       | 1.0   | -1     |
| 1046 | Tensor<[38]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
| 1047 | Tensor<[38]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
| 1048 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Done       | 1.0   | -1     |
| 1049 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Done       | 1.0   | -1     |
| 1050 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [1, 4, 12, 49, 49]       | Done     | Done       | 1.0   | -1     |
| 1051 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [48, 49, 49]             | Done     | Done       | 1.0   | -1     |
| 1052 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [1, 4, 12, 64, 64]       | Done     | Done       | 1.0   | -1     |
| 1053 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]             | Done     | Done       | 1.0   | -1     |
| 1054 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Unknown  | Done       | 1.0   | -1     |
| 1055 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [1, 4, 16, 49, 49]       | Done     | Unknown    | N/A   | N/A    |
| 1056 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [64, 49, 49]             | Done     | Unknown    | N/A   | N/A    |
| 1057 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [1, 4, 16, 64, 64]       | Done     | Done       | 1.0   | -1     |
| 1058 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [64, 64, 64]             | Done     | Done       | 1.0   | -1     |
| 1059 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]                   | Unknown  | Done       | 1.0   | -1     |
| 1060 | Tensor<[4, 49, 1152]> self = ?,<br>List[int] size = [4, 49, 3, 12, 32]         | Done     | Done       | 1.0   | -1     |
| 1061 | Tensor<[4, 49, 1536]> self = ?,<br>List[int] size = [4, 49, 3, 16, 32]         | Done     | Unknown    | N/A   | N/A    |
| 1062 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 384]        | Done     | Done       | 1.0   | -1     |
| 1063 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [196, 384]                  | Done     | Done       | 1.0   | -1     |
| 1064 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 512]        | Done     | Unknown    | N/A   | N/A    |
| 1065 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [196, 512]                  | Done     | Unknown    | N/A   | N/A    |
| 1066 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]                 | Unknown  | Done       | 1.0   | -1     |
| 1067 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]         | Done     | Done       | 1.0   | -1     |
| 1068 | Tensor<[4, 64, 1536]> self = ?,<br>List[int] size = [4, 64, 3, 16, 32]         | Done     | Done       | 1.0   | -1     |
| 1069 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 384]        | Done     | Done       | 1.0   | -1     |
| 1070 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]                  | Done     | Done       | 1.0   | -1     |
| 1071 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 512]        | Done     | Done       | 1.0   | -1     |
| 1072 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [256, 512]                  | Done     | Done       | 1.0   | -1     |
| 1073 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]                     | Unknown  | Done       | 1.0   | -1     |
| 1074 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Unknown  | Done       | 1.0   | -1     |
| 1075 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [1, 64, 64, 128]             | Done     | Done       | 1.0   | -1     |
| 1076 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [64, 64, 128]                | Done     | Done       | 1.0   | -1     |
| 1077 | Tensor<[4096, 12]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | 1.0   | -1     |
| 1078 | Tensor<[4096, 16]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | 1.0   | -1     |
| 1079 | Tensor<[4096, 24]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | 1.0   | -1     |
| 1080 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]             | Unknown  | Done       | 1.0   | -1     |
| 1081 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]               | Done     | Done       | 1.0   | -1     |
| 1082 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]                | Done     | Done       | 1.0   | -1     |
| 1083 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]               | Unknown  | Done       | 1.0   | -1     |
| 1084 | Tensor<[4096, 32]> self = ?,<br>List[int] size = [64, 64, -1]                  | Done     | Done       | 1.0   | -1     |
| 1085 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]             | Done     | Done       | 1.0   | -1     |
| 1086 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [64, 64, 384]                | Done     | Done       | 1.0   | -1     |
| 1087 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | 1.0   | -1     |
| 1088 | Tensor<[4096, 4]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | 1.0   | -1     |
| 1089 | Tensor<[4096, 512]> self = ?,<br>List[int] size = [1, 64, 64, 512]             | Done     | Done       | 1.0   | -1     |
| 1090 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]                 | Done     | Done       | 1.0   | -1     |
| 1091 | Tensor<[4096, 6]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | 1.0   | -1     |
| 1092 | Tensor<[4096, 8]> self = ?,<br>List[int] size = [64, 64, -1]                   | Done     | Done       | 1.0   | -1     |
| 1093 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]               | Done     | Done       | 1.0   | -1     |
| 1094 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]                  | Done     | Done       | 1.0   | -1     |
| 1095 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                 | Unknown  | Done       | 1.0   | -1     |
| 1096 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]               | Unknown  | Done       | 1.0   | -1     |
| 1097 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                   | Unknown  | Done       | 1.0   | -1     |
| 1098 | Tensor<[48, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]             | Done     | Done       | 1.0   | -1     |
| 1099 | Tensor<[48, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]             | Done     | Done       | 1.0   | -1     |
| 1100 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]             | Done     | Done       | 1.0   | -1     |
| 1101 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]             | Done     | Done       | 1.0   | -1     |
| 1102 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]               | Done     | Done       | 1.0   | -1     |
| 1103 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]               | Done     | Done       | 1.0   | -1     |
| 1104 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]                 | Done     | Unknown    | N/A   | N/A    |
| 1105 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]               | Done     | Unknown    | N/A   | N/A    |
| 1106 | Tensor<[49, 2304]> self = ?,<br>List[int] size = [1, 49, 2304]                 | Done     | Done       | 1.0   | -1     |
| 1107 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 49, 3072]                 | Done     | Unknown    | N/A   | N/A    |
| 1108 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 7, 7, 3072]               | Done     | Done       | 1.0   | -1     |
| 1109 | Tensor<[49, 4096]> self = ?,<br>List[int] size = [1, 7, 7, 4096]               | Done     | Unknown    | N/A   | N/A    |
| 1110 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 49, 768]                   | Done     | Done       | 1.0   | -1     |
| 1111 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]                 | Done     | Done       | 1.0   | -1     |
| 1112 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]         | Done     | Done       | 1.0   | -1     |
| 1113 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]           | Done     | Done       | 1.0   | -1     |
| 1114 | Tensor<[5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  | Done       | 1.0   | -1     |
| 1115 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]         | Done     | Done       | 1.0   | -1     |
| 1116 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]           | Done     | Done       | 1.0   | -1     |
| 1117 | Tensor<[5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]             | Done     | Done       | 1.0   | -1     |
| 1118 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                   | Unknown  | Done       | 1.0   | -1     |
| 1119 | Tensor<[5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]             | Done     | Done       | 1.0   | -1     |
| 1120 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                   | Unknown  | Done       | 1.0   | -1     |
| 1121 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                 | Unknown  | Done       | 1.0   | -1     |
| 1122 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 1024]                 | Done     | Done       | 1.0   | -1     |
| 1123 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 16, 64]               | Done     | Done       | 1.0   | -1     |
| 1124 | Tensor<[50, 1, 12, 64]> self = ?,<br>List[int] size = [50, 768]                | Done     | Done       | 1.0   | -1     |
| 1125 | Tensor<[50, 1, 16, 64]> self = ?,<br>List[int] size = [50, 1024]               | Done     | Done       | 1.0   | -1     |
| 1126 | Tensor<[50, 1, 2304]> self = ?,<br>List[int] size = [50, 1, 3, 768]            | Done     | Done       | 1.0   | -1     |
| 1127 | Tensor<[50, 1, 3072]> self = ?,<br>List[int] size = [50, 1, 3, 1024]           | Done     | Done       | 1.0   | -1     |
| 1128 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 12, 64]                | Done     | Done       | 1.0   | -1     |
| 1129 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 768]                   | Done     | Done       | 1.0   | -1     |
| 1130 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [1, 50, 1024]                 | Done     | Done       | 1.0   | -1     |
| 1131 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [50, 1, 1024]                 | Done     | Done       | 1.0   | -1     |
| 1132 | Tensor<[50, 2304]> self = ?,<br>List[int] size = [50, 1, 2304]                 | Done     | Done       | 1.0   | -1     |
| 1133 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]                 | Done     | Done       | 1.0   | -1     |
| 1134 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [50, 1, 3072]                 | Done     | Done       | 1.0   | -1     |
| 1135 | Tensor<[50, 4096]> self = ?,<br>List[int] size = [1, 50, 4096]                 | Done     | Done       | 1.0   | -1     |
| 1136 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]                   | Done     | Done       | 1.0   | -1     |
| 1137 | Tensor<[50, 768]> self = ?,<br>List[int] size = [50, 1, 768]                   | Done     | Done       | 1.0   | -1     |
| 1138 | Tensor<[50]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  | Done       | 1.0   | -1     |
| 1139 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Done     | Done       | 1.0   | -1     |
| 1140 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                    | Done     | Done       | 1.0   | -1     |
| 1141 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]                 | Unknown  | Done       | 1.0   | -1     |
| 1142 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272]               | Unknown  | Done       | 1.0   | -1     |
| 1143 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]                   | Unknown  | Done       | 1.0   | -1     |
| 1144 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Done       | 1.0   | -1     |
| 1145 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Done       | 1.0   | -1     |
| 1146 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]              | Done     | Done       | 1.0   | -1     |
| 1147 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                 | Unknown  | Done       | 1.0   | -1     |
| 1148 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                 | Unknown  | Done       | 1.0   | -1     |
| 1149 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                   | Unknown  | Done       | 1.0   | -1     |
| 1150 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                   | Unknown  | Done       | 1.0   | -1     |
| 1151 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                 | Unknown  | Done       | 1.0   | -1     |
| 1152 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 1153 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]               | Unknown  | Done       | 1.0   | -1     |
| 1154 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]               | Unknown  | Done       | 1.0   | -1     |
| 1155 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]              | Done     | Done       | 1.0   | -1     |
| 1156 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]                  | Done     | Done       | 1.0   | -1     |
| 1157 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]                | Done     | Done       | 1.0   | -1     |
| 1158 | Tensor<[63, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                       | Unknown  | Done       | 1.0   | -1     |
| 1159 | Tensor<[63, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                       | Unknown  | Done       | 1.0   | -1     |
| 1160 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]                 | Done     | Done       | 1.0   | -1     |
| 1161 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]               | Done     | Done       | 1.0   | -1     |
| 1162 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]                 | Done     | Done       | 1.0   | -1     |
| 1163 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [1, 64, 3, 49, 49]       | Done     | Done       | 1.0   | -1     |
| 1164 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [192, 49, 49]            | Done     | Done       | 1.0   | -1     |
| 1165 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [1, 64, 3, 64, 64]       | Done     | Done       | 1.0   | -1     |
| 1166 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]            | Done     | Done       | 1.0   | -1     |
| 1167 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 64, 3072]                 | Done     | Done       | 1.0   | -1     |
| 1168 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]               | Done     | Done       | 1.0   | -1     |
| 1169 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [1, 64, 4, 49, 49]       | Done     | Done       | 1.0   | -1     |
| 1170 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [256, 49, 49]            | Done     | Done       | 1.0   | -1     |
| 1171 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4, 64, 64]       | Done     | Done       | 1.0   | -1     |
| 1172 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [256, 64, 64]            | Done     | Done       | 1.0   | -1     |
| 1173 | Tensor<[64, 4096]> self = ?,<br>List[int] size = [1, 8, 8, 4096]               | Done     | Done       | 1.0   | -1     |
| 1174 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 128]       | Done     | Done       | 1.0   | -1     |
| 1175 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [3136, 128]                | Done     | Done       | 1.0   | -1     |
| 1176 | Tensor<[64, 49, 288]> self = ?,<br>List[int] size = [64, 49, 3, 3, 32]         | Done     | Done       | 1.0   | -1     |
| 1177 | Tensor<[64, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]             | Done     | Unknown    | N/A   | N/A    |
| 1178 | Tensor<[64, 49, 384]> self = ?,<br>List[int] size = [64, 49, 3, 4, 32]         | Done     | Done       | 1.0   | -1     |
| 1179 | Tensor<[64, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]             | Done     | Unknown    | N/A   | N/A    |
| 1180 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 96]         | Done     | Done       | 1.0   | -1     |
| 1181 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [3136, 96]                  | Done     | Done       | 1.0   | -1     |
| 1182 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]       | Done     | Done       | 1.0   | -1     |
| 1183 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]                | Done     | Done       | 1.0   | -1     |
| 1184 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]         | Done     | Done       | 1.0   | -1     |
| 1185 | Tensor<[64, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]             | Done     | Done       | 1.0   | -1     |
| 1186 | Tensor<[64, 64, 384]> self = ?,<br>List[int] size = [64, 64, 3, 4, 32]         | Done     | Done       | 1.0   | -1     |
| 1187 | Tensor<[64, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]             | Done     | Done       | 1.0   | -1     |
| 1188 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]         | Done     | Done       | 1.0   | -1     |
| 1189 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]                  | Done     | Done       | 1.0   | -1     |
| 1190 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                    | Done     | Done       | 1.0   | -1     |
| 1191 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 64, 768]                   | Done     | Done       | 1.0   | -1     |
| 1192 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]                 | Done     | Done       | 1.0   | -1     |
| 1193 | Tensor<[64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]               | Done     | Done       | 1.0   | -1     |
| 1194 | Tensor<[64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                 | Done     | Done       | 1.0   | -1     |
| 1195 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                       | Done     | Done       | 1.0   | -1     |
| 1196 | Tensor<[68]> self = ?,<br>List[int] size = [1, -1]                             | Unknown  | Done       | 1.0   | -1     |
| 1197 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]                   | Done     | Done       | 1.0   | -1     |
| 1198 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]                         | Done     | Done       | 1.0   | -1     |
| 1199 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]                   | Done     | Done       | 1.0   | -1     |
| 1200 | Tensor<[7, 768]> self = ?,<br>List[int] size = [1, 7, 768]                     | Done     | Done       | 1.0   | -1     |
| 1201 | Tensor<[768, 196]> self = ?,<br>List[int] size = [1, 768, 196]                 | Done     | Done       | 1.0   | -1     |
| 1202 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]                 | Done     | Done       | 1.0   | -1     |
| 1203 | Tensor<[784, 1024]> self = ?,<br>List[int] size = [1, 28, 28, 1024]            | Done     | Unknown    | N/A   | N/A    |
| 1204 | Tensor<[784, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]              | Done     | Done       | 1.0   | -1     |
| 1205 | Tensor<[784, 192]> self = ?,<br>List[int] size = [16, 49, 192]                 | Done     | Done       | 1.0   | -1     |
| 1206 | Tensor<[784, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]              | Done     | Done       | 1.0   | -1     |
| 1207 | Tensor<[784, 256]> self = ?,<br>List[int] size = [16, 49, 256]                 | Done     | Unknown    | N/A   | N/A    |
| 1208 | Tensor<[784, 576]> self = ?,<br>List[int] size = [16, 49, 576]                 | Done     | Done       | 1.0   | -1     |
| 1209 | Tensor<[784, 768]> self = ?,<br>List[int] size = [1, 28, 28, 768]              | Done     | Done       | 1.0   | -1     |
| 1210 | Tensor<[784, 768]> self = ?,<br>List[int] size = [16, 49, 768]                 | Done     | Unknown    | N/A   | N/A    |
| 1211 | Tensor<[7]> self = ?,<br>List[int] size = [-1, 1]                              | Unknown  | Done       | 1.0   | -1     |
| 1212 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                 | Unknown  | Done       | 1.0   | -1     |
| 1213 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                   | Unknown  | Done       | 1.0   | -1     |
| 1214 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                   | Unknown  | Done       | 1.0   | -1     |
| 1215 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                 | Unknown  | Done       | 1.0   | -1     |
| 1216 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 1217 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]               | Unknown  | Done       | 1.0   | -1     |
| 1218 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]               | Unknown  | Done       | 1.0   | -1     |
| 1219 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]         | Done     | Done       | 1.0   | -1     |
| 1220 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]           | Done     | Unknown    | N/A   | N/A    |
| 1221 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]           | Done     | Done       | 1.0   | -1     |
| 1222 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]         | Done     | Done       | 1.0   | -1     |
| 1223 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]           | Done     | Done       | 1.0   | -1     |
| 1224 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]             | Done     | Done       | 1.0   | -1     |
| 1225 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]           | Done     | Done       | 1.0   | -1     |
| 1226 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]             | Done     | Done       | 1.0   | -1     |
| 1227 | Tensor<[8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]             | Done     | Done       | 1.0   | -1     |
| 1228 | Tensor<[850, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                      | Unknown  | Done       | 1.0   | -1     |
| 1229 | Tensor<[850, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                      | Unknown  | Done       | 1.0   | -1     |
| 1230 | Tensor<[8732, 1, 4]> self = ?,<br>List[int] size = [8732, 4]                   | Unknown  | Done       | 1.0   | -1     |
| 1231 | Tensor<[8732, 2, 2]> self = ?,<br>List[int] size = [8732, 4]                   | Unknown  | Done       | 1.0   | -1     |
| 1232 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]                   | Done     | Done       | 1.0   | -1     |
| 1233 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]                   | Unknown  | Done       | 1.0   | -1     |
| 1234 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]                     | Done     | Done       | 1.0   | -1     |
| 1235 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Unknown  | Done       | 1.0   | -1     |
| 1236 | Tensor<[9, 16384]> self = ?,<br>List[int] size = [1, 9, 16384]                 | Done     | Done       | 1.0   | -1     |
| 1237 | Tensor<[9, 2048]> self = ?,<br>List[int] size = [1, 9, 2048]                   | Done     | Done       | 1.0   | -1     |
| 1238 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]                 | Done     | Done       | 1.0   | -1     |
| 1239 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]                   | Done     | Done       | 1.0   | -1     |
| 1240 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]                     | Unknown  | Done       | 1.0   | -1     |
| 1241 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]                   | Done     | Done       | 1.0   | -1     |
| 1242 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                        | Unknown  | Done       | 1.0   | -1     |
| 1243 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]                     | Unknown  | Done       | 1.0   | -1     |
| 1244 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]                     | Done     | Done       | 1.0   | -1     |
| 1245 | Tensor<[9, 8192]> self = ?,<br>List[int] size = [1, 9, 8192]                   | Done     | Done       | 1.0   | -1     |
| 1246 | Tensor<[9, 8]> self = ?,<br>List[int] size = [-1, 2]                           | Unknown  | Done       | 1.0   | -1     |
| 1247 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]               | Done     | Done       | 1.0   | -1     |
| 1248 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]                 | Done     | Done       | 1.0   | -1     |
| 1249 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 8, 32]               | Done     | Done       | 1.0   | -1     |
| 1250 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]               | Done     | Done       | 1.0   | -1     |
| 1251 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]                 | Done     | Done       | 1.0   | -1     |
| 1252 | Tensor<[920, 8, 32]> self = ?,<br>List[int] size = [920, 256]                  | Done     | Done       | 1.0   | -1     |
| 1253 | Tensor<[96, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]             | Done     | Done       | 1.0   | -1     |
| 1254 | Tensor<[96, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]             | Done     | Done       | 1.0   | -1     |
| 1255 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]             | Done     | Done       | 1.0   | -1     |
| 1256 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]             | Done     | Done       | 1.0   | -1     |
| 1257 | Tensor<[9]> self = ?,<br>List[int] size = [1, -1]                              | Unknown  | Done       | 1.0   | -1     |
| 1258 | Tensor<[s0*s1, 10240]> self = ?,<br>List[int] size = [1, <s0*s1>, 10240]       | Unknown  | Unknown    | N/A   | N/A    |
| 1259 | Tensor<[s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
| 1260 | Tensor<[s0*s1, 5120]> self = ?,<br>List[int] size = [1, <s0*s1>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
| 1261 | Tensor<[s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]           | Unknown  | Unknown    | N/A   | N/A    |
| 1262 | Tensor<[s1*s2, 10240]> self = ?,<br>List[int] size = [1, <s1*s2>, 10240]       | Unknown  | Unknown    | N/A   | N/A    |
| 1263 | Tensor<[s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
| 1264 | Tensor<[s1*s2, 2560]> self = ?,<br>List[int] size = [1, <s1*s2>, 2560]         | Unknown  | Unknown    | N/A   | N/A    |
| 1265 | Tensor<[s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]           | Unknown  | Unknown    | N/A   | N/A    |
| 1266 | Tensor<[s1*s2, 5120]> self = ?,<br>List[int] size = [1, <s1*s2>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
| 1267 | Tensor<[s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]           | Unknown  | Unknown    | N/A   | N/A    |

