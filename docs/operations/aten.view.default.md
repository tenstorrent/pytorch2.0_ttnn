### aten.view.default
|      | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|-----:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|    0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]           | Unknown  | Done       | 1.0   | 0      |
|    1 | Tensor<[1, 1, 1, 4, 4]> self = ?,<br>List[int] size = [1, -1, 4]               | Done     | Done       | 1.0   | 0      |
|    2 | Tensor<[1, 1, 1, 4, 91]> self = ?,<br>List[int] size = [1, -1, 91]             | Done     | Done       | 1.0   | 0      |
|    3 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]               | Done     | Done       | 1.0   | 0      |
|    4 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]             | Done     | Done       | 1.0   | 0      |
|    5 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]      | Done     | Done       | 1.0   | 0      |
|    6 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 49, 768]        | Done     | Done       | 1.0   | 0      |
|    7 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]      | Done     | Done       | 1.0   | 0      |
|    8 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 64, 768]        | Done     | Done       | 1.0   | 0      |
|    9 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]                  | Unknown  | Done       | 1.0   | 0      |
|   10 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]             | Unknown  | Done       | 1.0   | 0      |
|   11 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                | Unknown  | Done       | 1.0   | 0      |
|   12 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 16, 64]              | Unknown  | Done       | 1.0   | 0      |
|   13 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                   | Unknown  | Done       | 1.0   | 0      |
|   14 | Tensor<[1, 1, 12, 16, 2]> self = ?,<br>List[int] size = [1, 192, 2]            | Unknown  | Unknown    | N/A   | N/A    |
|   15 | Tensor<[1, 1, 12, 16]> self = ?,<br>List[int] size = [1, 192]                  | Unknown  | Unknown    | N/A   | N/A    |
|   16 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]              | Unknown  | Done       | 1.0   | 0      |
|   17 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]               | Unknown  | Done       | 1.0   | 0      |
|   18 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, 1280]                   | Unknown  | Unknown    | N/A   | N/A    |
|   19 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]         | Unknown  | Done       | 1.0   | 0      |
|   20 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]             | Unknown  | Done       | 1.0   | 0      |
|   21 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]              | Unknown  | Done       | 1.0   | 0      |
|   22 | Tensor<[1, 1, 16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]       | Done     | Done       | 1.0   | 0      |
|   23 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | 0      |
|   24 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300]       | Done     | Done       | 1.0   | 0      |
|   25 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Done       | 1.0   | 0      |
|   26 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]                   | Unknown  | Done       | 1.0   | 0      |
|   27 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | 1.0   | 0      |
|   28 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [1, 256]                     | Unknown  | Unknown    | N/A   | N/A    |
|   29 | Tensor<[1, 1, 256]> self = ?,<br>List[int] size = [256]                        | Done     | Done       | 1.0   | 0      |
|   30 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Done     | Done       | 1.0   | 0      |
|   31 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]               | Unknown  | Done       | 1.0   | 0      |
|   32 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                   | Unknown  | Done       | 1.0   | 0      |
|   33 | Tensor<[1, 1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 256]             | Done     | Done       | 1.0   | 0      |
|   34 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                    | Unknown  | Done       | 1.0   | 0      |
|   35 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]               | Unknown  | Done       | 1.0   | 0      |
|   36 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                     | Unknown  | Done       | 1.0   | 0      |
|   37 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [384]                        | Done     | Done       | 1.0   | 0      |
|   38 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]          | Unknown  | Done       | 1.0   | 0      |
|   39 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                   | Unknown  | Done       | 1.0   | 0      |
|   40 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                       | Unknown  | Done       | 1.0   | 0      |
|   41 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]               | Unknown  | Done       | 1.0   | 0      |
|   42 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                     | Unknown  | Done       | 1.0   | 0      |
|   43 | Tensor<[1, 1, 51865]> self = ?,<br>List[int] size = [1, 51865]                 | Unknown  | Unknown    | N/A   | N/A    |
|   44 | Tensor<[1, 1, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]               | Unknown  | Done       | 1.0   | 0      |
|   45 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]             | Done     | Done       | 1.0   | 0      |
|   46 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]    | Done     | Done       | 1.0   | 0      |
|   47 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]      | Done     | Done       | 1.0   | 0      |
|   48 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]              | Unknown  | Unknown    | N/A   | N/A    |
|   49 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [-1, 1, 768]                 | Unknown  | Done       | 1.0   | 0      |
|   50 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]              | Unknown  | Done       | 1.0   | 0      |
|   51 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]               | Unknown  | Done       | 1.0   | 0      |
|   52 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                     | Unknown  | Done       | 1.0   | 0      |
|   53 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]                        | Done     | Done       | 1.0   | 0      |
|   54 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]    | Done     | Done       | 1.0   | 0      |
|   55 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]      | Done     | Unknown    | N/A   | N/A    |
|   56 | Tensor<[1, 1, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]               | Unknown  | Done       | 1.0   | 0      |
|   57 | Tensor<[1, 1, 80]> self = ?,<br>List[int] size = [1, 80]                       | Unknown  | Unknown    | N/A   | N/A    |
|   58 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Unknown  | Done       | 1.0   | 0      |
|   59 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [10, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|   60 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]             | Unknown  | Done       | 1.0   | 0      |
|   61 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, 10, 768]             | Removed  | Done       | 1.0   | 0      |
|   62 | Tensor<[1, 10, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]            | Unknown  | Done       | 1.0   | 0      |
|   63 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]                 | Unknown  | Done       | 1.0   | 0      |
|   64 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]                 | Done     | Done       | 1.0   | 0      |
|   65 | Tensor<[1, 10, 4096]> self = ?,<br>List[int] size = [10, 4096]                 | Unknown  | Done       | 1.0   | 0      |
|   66 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]              | Unknown  | Done       | 1.0   | 0      |
|   67 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]                   | Unknown  | Done       | 1.0   | 0      |
|   68 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Unknown  | Done       | 1.0   | 0      |
|   69 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, 10, 12, 64]             | Removed  | Done       | 1.0   | 0      |
|   70 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                   | Done     | Done       | 1.0   | 0      |
|   71 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]              | Unknown  | Done       | 1.0   | 0      |
|   72 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]                 | Done     | Done       | 1.0   | 0      |
|   73 | Tensor<[1, 1000, 1, 1]> self = ?,<br>List[int] size = [1, 1000]                | Done     | Done       | 1.0   | 0      |
|   74 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1, 1000, 1, 1]                | Done     | Done       | 1.0   | 0      |
|   75 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                         | Done     | Done       | 1.0   | 0      |
|   76 | Tensor<[1, 1008, 1, 1]> self = ?,<br>List[int] size = [1, 1008]                | Done     | Done       | 1.0   | 0      |
|   77 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, -1]                  | Done     | Done       | 1.0   | 0      |
|   78 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024]                | Done     | Done       | 1.0   | 0      |
|   79 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196]         | Done     | Done       | 1.0   | 0      |
|   80 | Tensor<[1, 1024, 16, 16]> self = ?,<br>List[int] size = [1, 1024, 256]         | Done     | Done       | 1.0   | 0      |
|   81 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 1024, 5, 32]          | Done     | Done       | 1.0   | 0      |
|   82 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1, 32, 32, -1]           | Done     | Done       | 1.0   | 0      |
|   83 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] size = [1024, 160]               | Done     | Done       | 1.0   | 0      |
|   84 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1, 1024, 16, 16]         | Done     | Done       | 1.0   | 0      |
|   85 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] size = [1024, 256]               | Done     | Done       | 1.0   | 0      |
|   86 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] size = [1, 1024, 160]          | Done     | Done       | 1.0   | 0      |
|   87 | Tensor<[1, 1024, 640]> self = ?,<br>List[int] size = [1024, 640]               | Done     | Done       | 1.0   | 0      |
|   88 | Tensor<[1, 1024, 7, 7]> self = ?,<br>List[int] size = [1, 1024, 49]            | Done     | Unknown    | N/A   | N/A    |
|   89 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  | Done       | 1.0   | 0      |
|   90 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1024, 1, 1]                | Done     | Done       | 1.0   | 0      |
|   91 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1024]                         | Done     | Done       | 1.0   | 0      |
|   92 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                         | Unknown  | Done       | 1.0   | 0      |
|   93 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10]                             | Done     | Done       | 1.0   | 0      |
|   94 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]               | Unknown  | Done       | 1.0   | 0      |
|   95 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]                 | Unknown  | Done       | 1.0   | 0      |
|   96 | Tensor<[1, 12, 1, 24]> self = ?,<br>List[int] size = [12, 1, 24]               | Unknown  | Unknown    | N/A   | N/A    |
|   97 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]                 | Unknown  | Done       | 1.0   | 0      |
|   98 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]               | Unknown  | Done       | 1.0   | 0      |
|   99 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]              | Unknown  | Unknown    | N/A   | N/A    |
|  100 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]               | Unknown  | Done       | 1.0   | 0      |
|  101 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  102 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  103 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]             | Removed  | Done       | 1.0   | 0      |
|  104 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]             | Removed  | Done       | 1.0   | 0      |
|  105 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12]             | Done     | Done       | 1.0   | 0      |
|  106 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  107 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]                   | Done     | Done       | 1.0   | 0      |
|  108 | Tensor<[1, 12, 14, 14]> self = ?,<br>List[int] size = [12, 14, 14]             | Done     | Done       | 1.0   | 0      |
|  109 | Tensor<[1, 12, 14, 64]> self = ?,<br>List[int] size = [12, 14, 64]             | Done     | Done       | 1.0   | 0      |
|  110 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16]             | Done     | Done       | 1.0   | 0      |
|  111 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64]             | Done     | Done       | 1.0   | 0      |
|  112 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197]         | Done     | Done       | 1.0   | 0      |
|  113 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]           | Done     | Done       | 1.0   | 0      |
|  114 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, -1, 64]              | Unknown  | Unknown    | N/A   | N/A    |
|  115 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]               | Unknown  | Done       | 1.0   | 0      |
|  116 | Tensor<[1, 12, 201, 201]> self = ?,<br>List[int] size = [12, 201, 201]         | Unknown  | Unknown    | N/A   | N/A    |
|  117 | Tensor<[1, 12, 201, 64]> self = ?,<br>List[int] size = [12, 201, 64]           | Unknown  | Unknown    | N/A   | N/A    |
|  118 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]             | Unknown  | Done       | 1.0   | 0      |
|  119 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]             | Unknown  | Done       | 1.0   | 0      |
|  120 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25]             | Removed  | Done       | 1.0   | 0      |
|  121 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64]             | Removed  | Done       | 1.0   | 0      |
|  122 | Tensor<[1, 12, 257, 257]> self = ?,<br>List[int] size = [12, 257, 257]         | Done     | Unknown    | N/A   | N/A    |
|  123 | Tensor<[1, 12, 257, 64]> self = ?,<br>List[int] size = [12, 257, 64]           | Done     | Unknown    | N/A   | N/A    |
|  124 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]                 | Done     | Done       | 1.0   | 0      |
|  125 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]             | Unknown  | Done       | 1.0   | 0      |
|  126 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]             | Unknown  | Done       | 1.0   | 0      |
|  127 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]             | Unknown  | Done       | 1.0   | 0      |
|  128 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64]             | Done     | Done       | 1.0   | 0      |
|  129 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, 50, 64]             | Done     | Done       | 1.0   | 0      |
|  130 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]             | Removed  | Done       | 1.0   | 0      |
|  131 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12]             | Done     | Done       | 1.0   | 0      |
|  132 | Tensor<[1, 12, 64, 14]> self = ?,<br>List[int] size = [12, 64, 14]             | Done     | Done       | 1.0   | 0      |
|  133 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16]             | Done     | Done       | 1.0   | 0      |
|  134 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]           | Done     | Done       | 1.0   | 0      |
|  135 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]               | Unknown  | Done       | 1.0   | 0      |
|  136 | Tensor<[1, 12, 64, 201]> self = ?,<br>List[int] size = [12, 64, 201]           | Unknown  | Unknown    | N/A   | N/A    |
|  137 | Tensor<[1, 12, 64, 257]> self = ?,<br>List[int] size = [12, 64, 257]           | Done     | Unknown    | N/A   | N/A    |
|  138 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25]             | Removed  | Done       | 1.0   | 0      |
|  139 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]               | Unknown  | Done       | 1.0   | 0      |
|  140 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]             | Unknown  | Done       | 1.0   | 0      |
|  141 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]             | Unknown  | Done       | 1.0   | 0      |
|  142 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7]               | Done     | Done       | 1.0   | 0      |
|  143 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9]               | Done     | Done       | 1.0   | 0      |
|  144 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  145 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  146 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64]               | Done     | Done       | 1.0   | 0      |
|  147 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]                 | Done     | Done       | 1.0   | 0      |
|  148 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  149 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]                   | Done     | Done       | 1.0   | 0      |
|  150 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64]               | Done     | Done       | 1.0   | 0      |
|  151 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]                 | Done     | Done       | 1.0   | 0      |
|  152 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  | Unknown    | N/A   | N/A    |
|  153 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  154 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]        | Unknown  | Unknown    | N/A   | N/A    |
|  155 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  156 | Tensor<[1, 12, s2 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  | Unknown    | N/A   | N/A    |
|  157 | Tensor<[1, 12, s4 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  | Unknown    | N/A   | N/A    |
|  158 | Tensor<[1, 12, s6 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  | Unknown    | N/A   | N/A    |
|  159 | Tensor<[1, 12, s8 + 1, 64]> self = ?,<br>List[int] size = [12, -1, 64]         | Unknown  | Unknown    | N/A   | N/A    |
|  160 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]             | Done     | Done       | 1.0   | 0      |
|  161 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]          | Done     | Done       | 1.0   | 0      |
|  162 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]           | Done     | Done       | 1.0   | 0      |
|  163 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]               | Done     | Done       | 1.0   | 0      |
|  164 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]          | Done     | Done       | 1.0   | 0      |
|  165 | Tensor<[1, 128, 128, 128]> self = ?,<br>List[int] size = [1, 128, 16384]       | Done     | Done       | 1.0   | 0      |
|  166 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | 0      |
|  167 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]           | Done     | Done       | 1.0   | 0      |
|  168 | Tensor<[1, 128, 16384]> self = ?,<br>List[int] size = [1, 128, 128, 128]       | Done     | Done       | 1.0   | 0      |
|  169 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]          | Done     | Done       | 1.0   | 0      |
|  170 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]          | Done     | Done       | 1.0   | 0      |
|  171 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280]                | Done     | Done       | 1.0   | 0      |
|  172 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]        | Done     | Done       | 1.0   | 0      |
|  173 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]        | Done     | Done       | 1.0   | 0      |
|  174 | Tensor<[1, 1280, 37, 37]> self = ?,<br>List[int] size = [1, 1280, 1369]        | Done     | Done       | 1.0   | 0      |
|  175 | Tensor<[1, 1280]> self = ?,<br>List[int] size = [1, 1280, 1, 1]                | Done     | Done       | 1.0   | 0      |
|  176 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]                           | Done     | Done       | 1.0   | 0      |
|  177 | Tensor<[1, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Done     | Done       | 1.0   | 0      |
|  178 | Tensor<[1, 12]> self = ?,<br>List[int] size = [12]                             | Done     | Done       | 1.0   | 0      |
|  179 | Tensor<[1, 1369, 768]> self = ?,<br>List[int] size = [1, 37, 37, 768]          | Removed  | Unknown    | N/A   | N/A    |
|  180 | Tensor<[1, 1370, 1280]> self = ?,<br>List[int] size = [1370, 1280]             | Done     | Done       | 1.0   | 0      |
|  181 | Tensor<[1, 1370, 5120]> self = ?,<br>List[int] size = [1370, 5120]             | Done     | Done       | 1.0   | 0      |
|  182 | Tensor<[1, 14, 128]> self = ?,<br>List[int] size = [14, 128]                   | Done     | Done       | 1.0   | 0      |
|  183 | Tensor<[1, 14, 14, 1024]> self = ?,<br>List[int] size = [196, 1024]            | Done     | Done       | 1.0   | 0      |
|  184 | Tensor<[1, 14, 14, 1536]> self = ?,<br>List[int] size = [196, 1536]            | Done     | Done       | 1.0   | 0      |
|  185 | Tensor<[1, 14, 14, 2048]> self = ?,<br>List[int] size = [196, 2048]            | Done     | Done       | 1.0   | 0      |
|  186 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 384]    | Done     | Done       | 1.0   | 0      |
|  187 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] size = [196, 384]              | Done     | Done       | 1.0   | 0      |
|  188 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [1, 2, 7, 2, 7, 512]    | Done     | Done       | 1.0   | 0      |
|  189 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] size = [196, 512]              | Done     | Done       | 1.0   | 0      |
|  190 | Tensor<[1, 14, 14, 768]> self = ?,<br>List[int] size = [196, 768]              | Done     | Done       | 1.0   | 0      |
|  191 | Tensor<[1, 14, 3072]> self = ?,<br>List[int] size = [14, 3072]                 | Done     | Done       | 1.0   | 0      |
|  192 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [1, 14, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  193 | Tensor<[1, 14, 768]> self = ?,<br>List[int] size = [14, 768]                   | Done     | Done       | 1.0   | 0      |
|  194 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1, 1445, 3, 64]          | Done     | Done       | 1.0   | 0      |
|  195 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]               | Done     | Done       | 1.0   | 0      |
|  196 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] size = [1, 1445, 192]          | Done     | Done       | 1.0   | 0      |
|  197 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]               | Done     | Done       | 1.0   | 0      |
|  198 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  199 | Tensor<[1, 15, 15, 12]> self = ?,<br>List[int] size = [-1, 12]                 | Removed  | Done       | 1.0   | 0      |
|  200 | Tensor<[1, 15, 15, 16]> self = ?,<br>List[int] size = [-1, 16]                 | Removed  | Done       | 1.0   | 0      |
|  201 | Tensor<[1, 15, 15, 24]> self = ?,<br>List[int] size = [-1, 24]                 | Removed  | Done       | 1.0   | 0      |
|  202 | Tensor<[1, 15, 15, 2]> self = ?,<br>List[int] size = [225, 2]                  | Removed  | Done       | 1.0   | 0      |
|  203 | Tensor<[1, 15, 15, 32]> self = ?,<br>List[int] size = [-1, 32]                 | Removed  | Done       | 1.0   | 0      |
|  204 | Tensor<[1, 15, 15, 3]> self = ?,<br>List[int] size = [-1, 3]                   | Removed  | Done       | 1.0   | 0      |
|  205 | Tensor<[1, 15, 15, 4]> self = ?,<br>List[int] size = [-1, 4]                   | Removed  | Done       | 1.0   | 0      |
|  206 | Tensor<[1, 15, 15, 512]> self = ?,<br>List[int] size = [225, 512]              | Removed  | Done       | 1.0   | 0      |
|  207 | Tensor<[1, 15, 15, 6]> self = ?,<br>List[int] size = [-1, 6]                   | Removed  | Done       | 1.0   | 0      |
|  208 | Tensor<[1, 15, 15, 8]> self = ?,<br>List[int] size = [-1, 8]                   | Removed  | Done       | 1.0   | 0      |
|  209 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]              | Unknown  | Done       | 1.0   | 0      |
|  210 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [15, 384]                   | Unknown  | Done       | 1.0   | 0      |
|  211 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]                   | Unknown  | Done       | 1.0   | 0      |
|  212 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]              | Unknown  | Done       | 1.0   | 0      |
|  213 | Tensor<[1, 1500, 12, 64]> self = ?,<br>List[int] size = [1, 1500, 768]         | Unknown  | Done       | 1.0   | 0      |
|  214 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072]             | Unknown  | Done       | 1.0   | 0      |
|  215 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]           | Unknown  | Done       | 1.0   | 0      |
|  216 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1, 1500, 12, 64]         | Unknown  | Done       | 1.0   | 0      |
|  217 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]               | Unknown  | Done       | 1.0   | 0      |
|  218 | Tensor<[1, 1512, 1, 1]> self = ?,<br>List[int] size = [1, 1512]                | Done     | Done       | 1.0   | 0      |
|  219 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536]                | Done     | Done       | 1.0   | 0      |
|  220 | Tensor<[1, 1536]> self = ?,<br>List[int] size = [1, 1536, 1, 1]                | Done     | Done       | 1.0   | 0      |
|  221 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                         | Unknown  | Done       | 1.0   | 0      |
|  222 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [16, 1, 10]               | Unknown  | Done       | 1.0   | 0      |
|  223 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]           | Done     | Done       | 1.0   | 0      |
|  224 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [16, 1, 1]                 | Unknown  | Done       | 1.0   | 0      |
|  225 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [16, 1, 2]                 | Unknown  | Done       | 1.0   | 0      |
|  226 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int] size = [16, 1, 60]               | Unknown  | Done       | 1.0   | 0      |
|  227 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]              | Unknown  | Done       | 1.0   | 0      |
|  228 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]               | Unknown  | Done       | 1.0   | 0      |
|  229 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                 | Unknown  | Done       | 1.0   | 0      |
|  230 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  231 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  232 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [16, 10, 10]             | Unknown  | Done       | 1.0   | 0      |
|  233 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [16, 10, 64]             | Unknown  | Done       | 1.0   | 0      |
|  234 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]             | Done     | Done       | 1.0   | 0      |
|  235 | Tensor<[1, 16, 128, 9]> self = ?,<br>List[int] size = [16, 128, 9]             | Done     | Done       | 1.0   | 0      |
|  236 | Tensor<[1, 16, 16, 1024]> self = ?,<br>List[int] size = [256, 1024]            | Done     | Done       | 1.0   | 0      |
|  237 | Tensor<[1, 16, 16, 1536]> self = ?,<br>List[int] size = [256, 1536]            | Done     | Done       | 1.0   | 0      |
|  238 | Tensor<[1, 16, 16, 2048]> self = ?,<br>List[int] size = [256, 2048]            | Done     | Done       | 1.0   | 0      |
|  239 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Done       | 1.0   | 0      |
|  240 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 384]    | Done     | Done       | 1.0   | 0      |
|  241 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] size = [256, 384]              | Done     | Done       | 1.0   | 0      |
|  242 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [1, 2, 8, 2, 8, 512]    | Done     | Done       | 1.0   | 0      |
|  243 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] size = [256, 512]              | Done     | Done       | 1.0   | 0      |
|  244 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [1, -1, 768]            | Done     | Unknown    | N/A   | N/A    |
|  245 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [256, 768]              | Done     | Done       | 1.0   | 0      |
|  246 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [16, 2, 64]               | Unknown  | Done       | 1.0   | 0      |
|  247 | Tensor<[1, 16, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]           | Done     | Done       | 1.0   | 0      |
|  248 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]                 | Done     | Done       | 1.0   | 0      |
|  249 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]             | Done     | Done       | 1.0   | 0      |
|  250 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]             | Done     | Done       | 1.0   | 0      |
|  251 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]                  | Done     | Done       | 1.0   | 0      |
|  252 | Tensor<[1, 16, 38, 38]> self = ?,<br>List[int] size = [1, -1, 4, 38, 38]       | Done     | Done       | 1.0   | 0      |
|  253 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                 | Unknown  | Done       | 1.0   | 0      |
|  254 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]               | Unknown  | Done       | 1.0   | 0      |
|  255 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int] size = [16, 59, 59]             | Unknown  | Done       | 1.0   | 0      |
|  256 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Unknown  | Done       | 1.0   | 0      |
|  257 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>List[int] size = [-1, 6, 49, 49]       | Done     | Done       | 1.0   | 0      |
|  258 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>List[int] size = [-1, 6, 64, 64]       | Done     | Done       | 1.0   | 0      |
|  259 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]               | Unknown  | Done       | 1.0   | 0      |
|  260 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int] size = [16, -1, 64]             | Unknown  | Done       | 1.0   | 0      |
|  261 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [16, 64, 10]             | Unknown  | Done       | 1.0   | 0      |
|  262 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [16, 64, 1]               | Unknown  | Done       | 1.0   | 0      |
|  263 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [16, 64, 2]               | Unknown  | Done       | 1.0   | 0      |
|  264 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]               | Unknown  | Done       | 1.0   | 0      |
|  265 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]               | Unknown  | Done       | 1.0   | 0      |
|  266 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]               | Done     | Done       | 1.0   | 0      |
|  267 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  268 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  269 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  270 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]                   | Done     | Done       | 1.0   | 0      |
|  271 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>List[int] size = [-1, 8, 49, 49]       | Done     | Done       | 1.0   | 0      |
|  272 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>List[int] size = [-1, 8, 64, 64]       | Done     | Done       | 1.0   | 0      |
|  273 | Tensor<[1, 16, 9, 128]> self = ?,<br>List[int] size = [16, 9, 128]             | Done     | Done       | 1.0   | 0      |
|  274 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]               | Done     | Done       | 1.0   | 0      |
|  275 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]                 | Done     | Done       | 1.0   | 0      |
|  276 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]             | Done     | Done       | 1.0   | 0      |
|  277 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, <s0 + 1>, 64]   | Unknown  | Unknown    | N/A   | N/A    |
|  278 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]        | Unknown  | Unknown    | N/A   | N/A    |
|  279 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
|  280 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] size = [1, 160, 32, 32]          | Done     | Done       | 1.0   | 0      |
|  281 | Tensor<[1, 160, 16, 16]> self = ?,<br>List[int] size = [1, 160, 256]           | Done     | Done       | 1.0   | 0      |
|  282 | Tensor<[1, 160, 256]> self = ?,<br>List[int] size = [1, 160, 16, 16]           | Done     | Done       | 1.0   | 0      |
|  283 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] size = [1, 160, 1024]          | Done     | Done       | 1.0   | 0      |
|  284 | Tensor<[1, 160]> self = ?,<br>List[int] size = [160]                           | Done     | Done       | 1.0   | 0      |
|  285 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] size = [1, 16384, 32]         | Done     | Done       | 1.0   | 0      |
|  286 | Tensor<[1, 16384, 128]> self = ?,<br>List[int] size = [16384, 128]             | Done     | Done       | 1.0   | 0      |
|  287 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [1, 1, 16384, 256]       | Done     | Done       | 1.0   | 0      |
|  288 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] size = [16384, 256]             | Done     | Done       | 1.0   | 0      |
|  289 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 1, 16384, 32]         | Done     | Done       | 1.0   | 0      |
|  290 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 128, 128, -1]         | Done     | Done       | 1.0   | 0      |
|  291 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [1, 16384, 1, 32]         | Done     | Done       | 1.0   | 0      |
|  292 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] size = [16384, 32]               | Done     | Done       | 1.0   | 0      |
|  293 | Tensor<[1, 1664, 1, 1]> self = ?,<br>List[int] size = [1, 1664]                | Done     | Done       | 1.0   | 0      |
|  294 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]                    | Done     | Done       | 1.0   | 0      |
|  295 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]          | Done     | Done       | 1.0   | 0      |
|  296 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]          | Removed  | Done       | 1.0   | 0      |
|  297 | Tensor<[1, 1920, 1, 1]> self = ?,<br>List[int] size = [1, 1920]                | Done     | Done       | 1.0   | 0      |
|  298 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Done       | 1.0   | 0      |
|  299 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]             | Done     | Done       | 1.0   | 0      |
|  300 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300]       | Done     | Done       | 1.0   | 0      |
|  301 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]         | Done     | Done       | 1.0   | 0      |
|  302 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]         | Done     | Done       | 1.0   | 0      |
|  303 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]         | Done     | Done       | 1.0   | 0      |
|  304 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]               | Done     | Done       | 1.0   | 0      |
|  305 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]               | Done     | Done       | 1.0   | 0      |
|  306 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]                 | Done     | Done       | 1.0   | 0      |
|  307 | Tensor<[1, 196]> self = ?,<br>List[int] size = [196]                           | Done     | Done       | 1.0   | 0      |
|  308 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]               | Done     | Done       | 1.0   | 0      |
|  309 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]           | Done     | Done       | 1.0   | 0      |
|  310 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]               | Done     | Done       | 1.0   | 0      |
|  311 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]               | Done     | Done       | 1.0   | 0      |
|  312 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]           | Done     | Done       | 1.0   | 0      |
|  313 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]                 | Done     | Done       | 1.0   | 0      |
|  314 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                           | Unknown  | Done       | 1.0   | 0      |
|  315 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                              | Done     | Done       | 1.0   | 0      |
|  316 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                               | Done     | Done       | 1.0   | 0      |
|  317 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] size = [2, 256, 32]             | Done     | Done       | 1.0   | 0      |
|  318 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]             | Done     | Done       | 1.0   | 0      |
|  319 | Tensor<[1, 2, 32, 256]> self = ?,<br>List[int] size = [2, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  320 | Tensor<[1, 2, 4096, 256]> self = ?,<br>List[int] size = [2, 4096, 256]         | Done     | Done       | 1.0   | 0      |
|  321 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] size = [2, 4096, 32]           | Done     | Done       | 1.0   | 0      |
|  322 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]         | Done     | Done       | 1.0   | 0      |
|  323 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]           | Done     | Done       | 1.0   | 0      |
|  324 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]             | Done     | Done       | 1.0   | 0      |
|  325 | Tensor<[1, 201, 12, 64]> self = ?,<br>List[int] size = [1, 201, 768]           | Unknown  | Unknown    | N/A   | N/A    |
|  326 | Tensor<[1, 201, 3072]> self = ?,<br>List[int] size = [201, 3072]               | Unknown  | Unknown    | N/A   | N/A    |
|  327 | Tensor<[1, 201, 768]> self = ?,<br>List[int] size = [1, 201, 12, 64]           | Unknown  | Unknown    | N/A   | N/A    |
|  328 | Tensor<[1, 201, 768]> self = ?,<br>List[int] size = [201, 768]                 | Unknown  | Unknown    | N/A   | N/A    |
|  329 | Tensor<[1, 2016, 1, 1]> self = ?,<br>List[int] size = [1, 2016]                | Done     | Done       | 1.0   | 0      |
|  330 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048]                | Done     | Done       | 1.0   | 0      |
|  331 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160]        | Done     | Done       | 1.0   | 0      |
|  332 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]         | Done     | Done       | 1.0   | 0      |
|  333 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]          | Done     | Done       | 1.0   | 0      |
|  334 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]         | Done     | Done       | 1.0   | 0      |
|  335 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [-1, 768]                 | Done     | Done       | 1.0   | 0      |
|  336 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]               | Done     | Done       | 1.0   | 0      |
|  337 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]          | Done     | Done       | 1.0   | 0      |
|  338 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]                   | Unknown  | Done       | 1.0   | 0      |
|  339 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 2048, 1, 1]                | Done     | Done       | 1.0   | 0      |
|  340 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [2048]                         | Done     | Done       | 1.0   | 0      |
|  341 | Tensor<[1, 21843]> self = ?,<br>List[int] size = [21843]                       | Done     | Done       | 1.0   | 0      |
|  342 | Tensor<[1, 2208, 1, 1]> self = ?,<br>List[int] size = [1, 2208]                | Done     | Done       | 1.0   | 0      |
|  343 | Tensor<[1, 23, 40, 64, 2]> self = ?,<br>List[int] size = [1, 23, 40, 128]      | Done     | Done       | 1.0   | 0      |
|  344 | Tensor<[1, 23, 40]> self = ?,<br>List[int] size = [1, 920]                     | Done     | Unknown    | N/A   | N/A    |
|  345 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]           | Done     | Done       | 1.0   | 0      |
|  346 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]       | Done     | Done       | 1.0   | 0      |
|  347 | Tensor<[1, 24, 19, 19]> self = ?,<br>List[int] size = [1, -1, 4, 19, 19]       | Done     | Done       | 1.0   | 0      |
|  348 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]           | Done     | Done       | 1.0   | 0      |
|  349 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]       | Done     | Done       | 1.0   | 0      |
|  350 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]           | Done     | Done       | 1.0   | 0      |
|  351 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]                 | Unknown  | Done       | 1.0   | 0      |
|  352 | Tensor<[1, 24, 32, 49]> self = ?,<br>List[int] size = [24, 32, 49]             | Done     | Done       | 1.0   | 0      |
|  353 | Tensor<[1, 24, 32, 64]> self = ?,<br>List[int] size = [24, 32, 64]             | Done     | Unknown    | N/A   | N/A    |
|  354 | Tensor<[1, 24, 49, 32]> self = ?,<br>List[int] size = [24, 49, 32]             | Done     | Done       | 1.0   | 0      |
|  355 | Tensor<[1, 24, 49, 49]> self = ?,<br>List[int] size = [24, 49, 49]             | Done     | Done       | 1.0   | 0      |
|  356 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]           | Done     | Done       | 1.0   | 0      |
|  357 | Tensor<[1, 24, 64, 32]> self = ?,<br>List[int] size = [24, 64, 32]             | Done     | Unknown    | N/A   | N/A    |
|  358 | Tensor<[1, 24, 64, 64]> self = ?,<br>List[int] size = [24, 64, 64]             | Done     | Unknown    | N/A   | N/A    |
|  359 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Unknown  | Done       | 1.0   | 0      |
|  360 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, 24, 12, 64]             | Unknown  | Done       | 1.0   | 0      |
|  361 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]                   | Unknown  | Done       | 1.0   | 0      |
|  362 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] size = [1, 25, 768]             | Removed  | Done       | 1.0   | 0      |
|  363 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]                 | Done     | Done       | 1.0   | 0      |
|  364 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [1, 25, 12, 64]             | Removed  | Done       | 1.0   | 0      |
|  365 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]                   | Done     | Done       | 1.0   | 0      |
|  366 | Tensor<[1, 2520, 1, 1]> self = ?,<br>List[int] size = [1, 2520]                | Done     | Done       | 1.0   | 0      |
|  367 | Tensor<[1, 255, 16, 16]> self = ?,<br>List[int] size = [1, 3, 85, 16, 16]      | Unknown  | Unknown    | N/A   | N/A    |
|  368 | Tensor<[1, 255, 32, 32]> self = ?,<br>List[int] size = [1, 3, 85, 32, 32]      | Unknown  | Unknown    | N/A   | N/A    |
|  369 | Tensor<[1, 255, 64, 64]> self = ?,<br>List[int] size = [1, 3, 85, 64, 64]      | Unknown  | Unknown    | N/A   | N/A    |
|  370 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] size = [1, 256, 32]             | Done     | Done       | 1.0   | 0      |
|  371 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 32, 32]          | Done     | Done       | 1.0   | 0      |
|  372 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]               | Done     | Done       | 1.0   | 0      |
|  373 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200]       | Done     | Done       | 1.0   | 0      |
|  374 | Tensor<[1, 256, 128, 128]> self = ?,<br>List[int] size = [1, 256, 16384]       | Done     | Done       | 1.0   | 0      |
|  375 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 256, 8, 160]          | Done     | Done       | 1.0   | 0      |
|  376 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]               | Done     | Done       | 1.0   | 0      |
|  377 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] size = [1, 256, 256]           | Done     | Done       | 1.0   | 0      |
|  378 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [1, 256, 5, 32]            | Done     | Done       | 1.0   | 0      |
|  379 | Tensor<[1, 256, 160]> self = ?,<br>List[int] size = [256, 160]                 | Done     | Done       | 1.0   | 0      |
|  380 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] size = [1, 256, 128, 128]       | Done     | Done       | 1.0   | 0      |
|  381 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160]       | Done     | Done       | 1.0   | 0      |
|  382 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] size = [1, 256, 64]             | Done     | Done       | 1.0   | 0      |
|  383 | Tensor<[1, 256, 23, 40]> self = ?,<br>List[int] size = [1, 256, 920]           | Done     | Done       | 1.0   | 0      |
|  384 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 16, 16, -1]            | Done     | Done       | 1.0   | 0      |
|  385 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 16, 16]           | Done     | Done       | 1.0   | 0      |
|  386 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]            | Done     | Done       | 1.0   | 0      |
|  387 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                 | Done     | Done       | 1.0   | 0      |
|  388 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[int] size = [1, 256, 1024]          | Done     | Done       | 1.0   | 0      |
|  389 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 1, 256, 32]             | Done     | Done       | 1.0   | 0      |
|  390 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [1, 256, 1, 32]             | Done     | Done       | 1.0   | 0      |
|  391 | Tensor<[1, 256, 32]> self = ?,<br>List[int] size = [256, 32]                   | Done     | Done       | 1.0   | 0      |
|  392 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [1, 256, 64, 64]          | Done     | Done       | 1.0   | 0      |
|  393 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] size = [1, 256, 160]            | Done     | Done       | 1.0   | 0      |
|  394 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                 | Done     | Done       | 1.0   | 0      |
|  395 | Tensor<[1, 256, 64, 64]> self = ?,<br>List[int] size = [1, 256, 4096]          | Done     | Done       | 1.0   | 0      |
|  396 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [1, 256, 2, 32]             | Done     | Done       | 1.0   | 0      |
|  397 | Tensor<[1, 256, 64]> self = ?,<br>List[int] size = [256, 64]                   | Done     | Done       | 1.0   | 0      |
|  398 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 16, 16, 16, 16, 3]     | Done     | Done       | 1.0   | 0      |
|  399 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]            | Done     | Done       | 1.0   | 0      |
|  400 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                 | Done     | Done       | 1.0   | 0      |
|  401 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]          | Done     | Done       | 1.0   | 0      |
|  402 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] size = [1, 256, 256]            | Done     | Done       | 1.0   | 0      |
|  403 | Tensor<[1, 256]> self = ?,<br>List[int] size = [1, 1, 256]                     | Unknown  | Unknown    | N/A   | N/A    |
|  404 | Tensor<[1, 256]> self = ?,<br>List[int] size = [256]                           | Done     | Done       | 1.0   | 0      |
|  405 | Tensor<[1, 257, 12, 64]> self = ?,<br>List[int] size = [1, 257, 768]           | Done     | Unknown    | N/A   | N/A    |
|  406 | Tensor<[1, 257, 3072]> self = ?,<br>List[int] size = [257, 3072]               | Done     | Unknown    | N/A   | N/A    |
|  407 | Tensor<[1, 257, 768]> self = ?,<br>List[int] size = [1, 257, 12, 64]           | Done     | Unknown    | N/A   | N/A    |
|  408 | Tensor<[1, 257, 768]> self = ?,<br>List[int] size = [257, 768]                 | Done     | Unknown    | N/A   | N/A    |
|  409 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                          | Done     | Done       | 1.0   | 0      |
|  410 | Tensor<[1, 28, 28, 1024]> self = ?,<br>List[int] size = [784, 1024]            | Done     | Done       | 1.0   | 0      |
|  411 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 192]    | Done     | Done       | 1.0   | 0      |
|  412 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] size = [784, 192]              | Done     | Done       | 1.0   | 0      |
|  413 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [1, 4, 7, 4, 7, 256]    | Done     | Done       | 1.0   | 0      |
|  414 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] size = [784, 256]              | Done     | Done       | 1.0   | 0      |
|  415 | Tensor<[1, 28, 28, 384]> self = ?,<br>List[int] size = [784, 384]              | Done     | Done       | 1.0   | 0      |
|  416 | Tensor<[1, 28, 28, 512]> self = ?,<br>List[int] size = [784, 512]              | Done     | Done       | 1.0   | 0      |
|  417 | Tensor<[1, 28, 28, 768]> self = ?,<br>List[int] size = [784, 768]              | Done     | Done       | 1.0   | 0      |
|  418 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445]       | Done     | Done       | 1.0   | 0      |
|  419 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]           | Done     | Done       | 1.0   | 0      |
|  420 | Tensor<[1, 3, 16, 16, 85]> self = ?,<br>List[int] size = [1, 768, 85]          | Unknown  | Unknown    | N/A   | N/A    |
|  421 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16]  | Done     | Done       | 1.0   | 0      |
|  422 | Tensor<[1, 3, 32, 32, 85]> self = ?,<br>List[int] size = [1, 3072, 85]         | Unknown  | Unknown    | N/A   | N/A    |
|  423 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]           | Done     | Done       | 1.0   | 0      |
|  424 | Tensor<[1, 3, 64, 64, 85]> self = ?,<br>List[int] size = [1, 12288, 85]        | Unknown  | Unknown    | N/A   | N/A    |
|  425 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]            | Done     | Done       | 1.0   | 0      |
|  426 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]                 | Done     | Done       | 1.0   | 0      |
|  427 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]               | Done     | Done       | 1.0   | 0      |
|  428 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]            | Done     | Done       | 1.0   | 0      |
|  429 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]                 | Done     | Done       | 1.0   | 0      |
|  430 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]            | Done     | Done       | 1.0   | 0      |
|  431 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]            | Done     | Done       | 1.0   | 0      |
|  432 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]                 | Done     | Done       | 1.0   | 0      |
|  433 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]             | Done     | Done       | 1.0   | 0      |
|  434 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]                   | Done     | Done       | 1.0   | 0      |
|  435 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]            | Done     | Done       | 1.0   | 0      |
|  436 | Tensor<[1, 3024, 1, 1]> self = ?,<br>List[int] size = [1, 3024]                | Done     | Done       | 1.0   | 0      |
|  437 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                   | Unknown  | Done       | 1.0   | 0      |
|  438 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]                         | Done     | Done       | 1.0   | 0      |
|  439 | Tensor<[1, 32, 11008]> self = ?,<br>List[int] size = [32, 11008]               | Unknown  | Unknown    | N/A   | N/A    |
|  440 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] size = [1, 32, 16384]         | Done     | Done       | 1.0   | 0      |
|  441 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [32, 128, 32]           | Unknown  | Unknown    | N/A   | N/A    |
|  442 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]                 | Done     | Done       | 1.0   | 0      |
|  443 | Tensor<[1, 32, 16, 16]> self = ?,<br>List[int] size = [1, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  444 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] size = [1, 32, 128, 128]         | Done     | Done       | 1.0   | 0      |
|  445 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 1, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  446 | Tensor<[1, 32, 256]> self = ?,<br>List[int] size = [1, 32, 16, 16]             | Done     | Done       | 1.0   | 0      |
|  447 | Tensor<[1, 32, 32, 1024]> self = ?,<br>List[int] size = [1024, 1024]           | Done     | Done       | 1.0   | 0      |
|  448 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 4096]           | Unknown  | Unknown    | N/A   | N/A    |
|  449 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [32, 32, 128]           | Unknown  | Unknown    | N/A   | N/A    |
|  450 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] size = [1, 1024, 160]          | Done     | Done       | 1.0   | 0      |
|  451 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 192]    | Done     | Done       | 1.0   | 0      |
|  452 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] size = [1024, 192]             | Done     | Done       | 1.0   | 0      |
|  453 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1, 4, 8, 4, 8, 256]    | Done     | Done       | 1.0   | 0      |
|  454 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] size = [1024, 256]             | Done     | Done       | 1.0   | 0      |
|  455 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [32, 32, 32]             | Unknown  | Unknown    | N/A   | N/A    |
|  456 | Tensor<[1, 32, 32, 384]> self = ?,<br>List[int] size = [1024, 384]             | Done     | Done       | 1.0   | 0      |
|  457 | Tensor<[1, 32, 32, 49]> self = ?,<br>List[int] size = [32, 32, 49]             | Done     | Done       | 1.0   | 0      |
|  458 | Tensor<[1, 32, 32, 512]> self = ?,<br>List[int] size = [1024, 512]             | Done     | Done       | 1.0   | 0      |
|  459 | Tensor<[1, 32, 32, 64]> self = ?,<br>List[int] size = [32, 32, 64]             | Done     | Done       | 1.0   | 0      |
|  460 | Tensor<[1, 32, 32, 768]> self = ?,<br>List[int] size = [1024, 768]             | Done     | Done       | 1.0   | 0      |
|  461 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [1, 32, 32, 128]           | Unknown  | Unknown    | N/A   | N/A    |
|  462 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [32, 4096]                 | Unknown  | Unknown    | N/A   | N/A    |
|  463 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96]         | Done     | Done       | 1.0   | 0      |
|  464 | Tensor<[1, 32, 49, 32]> self = ?,<br>List[int] size = [32, 49, 32]             | Done     | Done       | 1.0   | 0      |
|  465 | Tensor<[1, 32, 49, 49]> self = ?,<br>List[int] size = [32, 49, 49]             | Done     | Done       | 1.0   | 0      |
|  466 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]                 | Done     | Done       | 1.0   | 0      |
|  467 | Tensor<[1, 32, 64, 32]> self = ?,<br>List[int] size = [32, 64, 32]             | Done     | Done       | 1.0   | 0      |
|  468 | Tensor<[1, 32, 64, 64]> self = ?,<br>List[int] size = [32, 64, 64]             | Done     | Done       | 1.0   | 0      |
|  469 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]          | Done     | Done       | 1.0   | 0      |
|  470 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]           | Done     | Done       | 1.0   | 0      |
|  471 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]          | Done     | Done       | 1.0   | 0      |
|  472 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]                 | Unknown  | Done       | 1.0   | 0      |
|  473 | Tensor<[1, 32]> self = ?,<br>List[int] size = [32]                             | Done     | Done       | 1.0   | 0      |
|  474 | Tensor<[1, 364, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]         | Done     | Done       | 1.0   | 0      |
|  475 | Tensor<[1, 364, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]         | Done     | Done       | 1.0   | 0      |
|  476 | Tensor<[1, 364, 38, 38]> self = ?,<br>List[int] size = [1, -1, 91, 38, 38]     | Done     | Done       | 1.0   | 0      |
|  477 | Tensor<[1, 3712, 1, 1]> self = ?,<br>List[int] size = [1, 3712]                | Done     | Done       | 1.0   | 0      |
|  478 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                     | Unknown  | Done       | 1.0   | 0      |
|  479 | Tensor<[1, 3]> self = ?,<br>List[int] size = [3]                               | Done     | Done       | 1.0   | 0      |
|  480 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>List[int] size = [-1, 12, 49, 49]      | Done     | Done       | 1.0   | 0      |
|  481 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>List[int] size = [-1, 12, 64, 64]      | Done     | Done       | 1.0   | 0      |
|  482 | Tensor<[1, 4, 12, 64]> self = ?,<br>List[int] size = [1, 4, 768]               | Unknown  | Done       | 1.0   | 0      |
|  483 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>List[int] size = [-1, 16, 49, 49]      | Done     | Done       | 1.0   | 0      |
|  484 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>List[int] size = [-1, 16, 64, 64]      | Done     | Done       | 1.0   | 0      |
|  485 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]                   | Unknown  | Done       | 1.0   | 0      |
|  486 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]              | Unknown  | Done       | 1.0   | 0      |
|  487 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [1, 4, 12, 64]               | Unknown  | Done       | 1.0   | 0      |
|  488 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]                     | Unknown  | Done       | 1.0   | 0      |
|  489 | Tensor<[1, 400, 1, 1]> self = ?,<br>List[int] size = [1, 400]                  | Done     | Done       | 1.0   | 0      |
|  490 | Tensor<[1, 4096, 1280]> self = ?,<br>List[int] size = [4096, 1280]             | Unknown  | Done       | 1.0   | 0      |
|  491 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] size = [1, 4096, 64]           | Done     | Done       | 1.0   | 0      |
|  492 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] size = [4096, 256]               | Done     | Done       | 1.0   | 0      |
|  493 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]            | Unknown  | Done       | 1.0   | 0      |
|  494 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [1, 64, 64, 320]          | Unknown  | Done       | 1.0   | 0      |
|  495 | Tensor<[1, 4096, 320]> self = ?,<br>List[int] size = [4096, 320]               | Unknown  | Done       | 1.0   | 0      |
|  496 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 4096, 2, 32]           | Done     | Done       | 1.0   | 0      |
|  497 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [1, 64, 64, -1]            | Done     | Done       | 1.0   | 0      |
|  498 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] size = [4096, 64]                 | Done     | Done       | 1.0   | 0      |
|  499 | Tensor<[1, 4096, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]            | Unknown  | Done       | 1.0   | 0      |
|  500 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                   | Unknown  | Done       | 1.0   | 0      |
|  501 | Tensor<[1, 440, 1, 1]> self = ?,<br>List[int] size = [1, 440]                  | Done     | Done       | 1.0   | 0      |
|  502 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] size = [1, 45, 768]             | Unknown  | Done       | 1.0   | 0      |
|  503 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                 | Unknown  | Done       | 1.0   | 0      |
|  504 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [-1, 45, 768]               | Unknown  | Done       | 1.0   | 0      |
|  505 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [1, 45, 12, 64]             | Unknown  | Done       | 1.0   | 0      |
|  506 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                   | Unknown  | Done       | 1.0   | 0      |
|  507 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                         | Unknown  | Done       | 1.0   | 0      |
|  508 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]          | Done     | Done       | 1.0   | 0      |
|  509 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]           | Done     | Done       | 1.0   | 0      |
|  510 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]               | Done     | Done       | 1.0   | 0      |
|  511 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]          | Done     | Done       | 1.0   | 0      |
|  512 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]               | Done     | Done       | 1.0   | 0      |
|  513 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 1024]      | Done     | Done       | 1.0   | 0      |
|  514 | Tensor<[1, 49, 1024]> self = ?,<br>List[int] size = [49, 1024]                 | Done     | Done       | 1.0   | 0      |
|  515 | Tensor<[1, 49, 2304]> self = ?,<br>List[int] size = [1, 49, 3, 24, 32]         | Done     | Done       | 1.0   | 0      |
|  516 | Tensor<[1, 49, 3072]> self = ?,<br>List[int] size = [1, 49, 3, 32, 32]         | Done     | Done       | 1.0   | 0      |
|  517 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [1, 1, 1, 7, 7, 768]        | Done     | Done       | 1.0   | 0      |
|  518 | Tensor<[1, 49, 768]> self = ?,<br>List[int] size = [49, 768]                   | Done     | Done       | 1.0   | 0      |
|  519 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]                           | Unknown  | Done       | 1.0   | 0      |
|  520 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]           | Unknown  | Done       | 1.0   | 0      |
|  521 | Tensor<[1, 5, 1024, 256]> self = ?,<br>List[int] size = [5, 1024, 256]         | Done     | Done       | 1.0   | 0      |
|  522 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] size = [5, 1024, 32]           | Done     | Done       | 1.0   | 0      |
|  523 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                | Unknown  | Done       | 1.0   | 0      |
|  524 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                   | Unknown  | Done       | 1.0   | 0      |
|  525 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]         | Done     | Done       | 1.0   | 0      |
|  526 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]           | Done     | Done       | 1.0   | 0      |
|  527 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]         | Unknown  | Done       | 1.0   | 0      |
|  528 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]              | Unknown  | Done       | 1.0   | 0      |
|  529 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] size = [5, 256, 32]             | Done     | Done       | 1.0   | 0      |
|  530 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]             | Done     | Done       | 1.0   | 0      |
|  531 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]               | Unknown  | Done       | 1.0   | 0      |
|  532 | Tensor<[1, 5, 32, 256]> self = ?,<br>List[int] size = [5, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  533 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]          | Unknown  | Done       | 1.0   | 0      |
|  534 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                   | Unknown  | Done       | 1.0   | 0      |
|  535 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]             | Done     | Done       | 1.0   | 0      |
|  536 | Tensor<[1, 50, 1024]> self = ?,<br>List[int] size = [50, 1024]                 | Done     | Done       | 1.0   | 0      |
|  537 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768]             | Done     | Done       | 1.0   | 0      |
|  538 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]                 | Done     | Done       | 1.0   | 0      |
|  539 | Tensor<[1, 50, 4096]> self = ?,<br>List[int] size = [50, 4096]                 | Done     | Done       | 1.0   | 0      |
|  540 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  541 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  542 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]                   | Done     | Done       | 1.0   | 0      |
|  543 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                 | Unknown  | Done       | 1.0   | 0      |
|  544 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]                 | Unknown  | Done       | 1.0   | 0      |
|  545 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512]                  | Done     | Done       | 1.0   | 0      |
|  546 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]           | Done     | Done       | 1.0   | 0      |
|  547 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]          | Done     | Done       | 1.0   | 0      |
|  548 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]          | Done     | Done       | 1.0   | 0      |
|  549 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] size = [1, 25088]                | Done     | Done       | 1.0   | 0      |
|  550 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                 | Unknown  | Done       | 1.0   | 0      |
|  551 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                     | Unknown  | Done       | 1.0   | 0      |
|  552 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512, 1, 1]                  | Done     | Done       | 1.0   | 0      |
|  553 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]                           | Done     | Done       | 1.0   | 0      |
|  554 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]                 | Unknown  | Done       | 1.0   | 0      |
|  555 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]         | Done     | Done       | 1.0   | 0      |
|  556 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10]     | Done     | Done       | 1.0   | 0      |
|  557 | Tensor<[1, 546, 19, 19]> self = ?,<br>List[int] size = [1, -1, 91, 19, 19]     | Done     | Done       | 1.0   | 0      |
|  558 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]         | Done     | Done       | 1.0   | 0      |
|  559 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20]     | Done     | Done       | 1.0   | 0      |
|  560 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]         | Done     | Done       | 1.0   | 0      |
|  561 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]         | Done     | Done       | 1.0   | 0      |
|  562 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 128]    | Done     | Done       | 1.0   | 0      |
|  563 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] size = [3136, 128]             | Done     | Done       | 1.0   | 0      |
|  564 | Tensor<[1, 56, 56, 384]> self = ?,<br>List[int] size = [3136, 384]             | Done     | Done       | 1.0   | 0      |
|  565 | Tensor<[1, 56, 56, 512]> self = ?,<br>List[int] size = [3136, 512]             | Done     | Done       | 1.0   | 0      |
|  566 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [1, 8, 7, 8, 7, 96]      | Done     | Done       | 1.0   | 0      |
|  567 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] size = [3136, 96]               | Done     | Done       | 1.0   | 0      |
|  568 | Tensor<[1, 576, 1, 1]> self = ?,<br>List[int] size = [1, 576]                  | Done     | Done       | 1.0   | 0      |
|  569 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  570 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]            | Unknown  | Done       | 1.0   | 0      |
|  571 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, 59, 16, 64]            | Unknown  | Done       | 1.0   | 0      |
|  572 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  573 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]                   | Unknown  | Done       | 1.0   | 0      |
|  574 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]                         | Unknown  | Done       | 1.0   | 0      |
|  575 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                           | Unknown  | Done       | 1.0   | 0      |
|  576 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | 1.0   | 0      |
|  577 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]                 | Unknown  | Done       | 1.0   | 0      |
|  578 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]                 | Unknown  | Done       | 1.0   | 0      |
|  579 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]                   | Unknown  | Done       | 1.0   | 0      |
|  580 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]                   | Unknown  | Done       | 1.0   | 0      |
|  581 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]                 | Unknown  | Done       | 1.0   | 0      |
|  582 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
|  583 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]               | Unknown  | Done       | 1.0   | 0      |
|  584 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]               | Unknown  | Done       | 1.0   | 0      |
|  585 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]               | Unknown  | Done       | 1.0   | 0      |
|  586 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]                 | Unknown  | Done       | 1.0   | 0      |
|  587 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]               | Unknown  | Done       | 1.0   | 0      |
|  588 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]               | Unknown  | Done       | 1.0   | 0      |
|  589 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]                 | Unknown  | Done       | 1.0   | 0      |
|  590 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]                 | Unknown  | Done       | 1.0   | 0      |
|  591 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  592 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
|  593 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 1024]      | Done     | Done       | 1.0   | 0      |
|  594 | Tensor<[1, 64, 1024]> self = ?,<br>List[int] size = [64, 1024]                 | Done     | Done       | 1.0   | 0      |
|  595 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216]                | Done     | Done       | 1.0   | 0      |
|  596 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]         | Done     | Done       | 1.0   | 0      |
|  597 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]             | Done     | Done       | 1.0   | 0      |
|  598 | Tensor<[1, 64, 16, 16]> self = ?,<br>List[int] size = [1, 64, 256]             | Done     | Done       | 1.0   | 0      |
|  599 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]         | Done     | Done       | 1.0   | 0      |
|  600 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                    | Unknown  | Done       | 1.0   | 0      |
|  601 | Tensor<[1, 64, 2304]> self = ?,<br>List[int] size = [1, 64, 3, 24, 32]         | Done     | Unknown    | N/A   | N/A    |
|  602 | Tensor<[1, 64, 256]> self = ?,<br>List[int] size = [1, 64, 16, 16]             | Done     | Done       | 1.0   | 0      |
|  603 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>List[int] size = [-1, 3, 49, 49]       | Done     | Done       | 1.0   | 0      |
|  604 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>List[int] size = [-1, 3, 64, 64]       | Done     | Done       | 1.0   | 0      |
|  605 | Tensor<[1, 64, 3072]> self = ?,<br>List[int] size = [1, 64, 3, 32, 32]         | Done     | Done       | 1.0   | 0      |
|  606 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]                  | Unknown  | Done       | 1.0   | 0      |
|  607 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>List[int] size = [-1, 4, 49, 49]       | Done     | Done       | 1.0   | 0      |
|  608 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>List[int] size = [-1, 4, 64, 64]       | Done     | Done       | 1.0   | 0      |
|  609 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] size = [1, 64, 64, 64]            | Done     | Done       | 1.0   | 0      |
|  610 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]    | Done     | Done       | 1.0   | 0      |
|  611 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]             | Done     | Done       | 1.0   | 0      |
|  612 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] size = [1, 4096, 320]          | Unknown  | Done       | 1.0   | 0      |
|  613 | Tensor<[1, 64, 64, 384]> self = ?,<br>List[int] size = [4096, 384]             | Done     | Done       | 1.0   | 0      |
|  614 | Tensor<[1, 64, 64, 512]> self = ?,<br>List[int] size = [4096, 512]             | Done     | Done       | 1.0   | 0      |
|  615 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 4096, 64]            | Done     | Done       | 1.0   | 0      |
|  616 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4096]            | Done     | Done       | 1.0   | 0      |
|  617 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]      | Done     | Done       | 1.0   | 0      |
|  618 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]               | Done     | Done       | 1.0   | 0      |
|  619 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int] size = [64, 64, 9]               | Done     | Done       | 1.0   | 0      |
|  620 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [1, 1, 1, 8, 8, 768]        | Done     | Unknown    | N/A   | N/A    |
|  621 | Tensor<[1, 64, 768]> self = ?,<br>List[int] size = [64, 768]                   | Done     | Done       | 1.0   | 0      |
|  622 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int] size = [64, 9, 64]               | Done     | Done       | 1.0   | 0      |
|  623 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int] size = [64, 9, 9]                 | Done     | Done       | 1.0   | 0      |
|  624 | Tensor<[1, 640, 1024]> self = ?,<br>List[int] size = [1, 640, 32, 32]          | Done     | Done       | 1.0   | 0      |
|  625 | Tensor<[1, 640, 32, 32]> self = ?,<br>List[int] size = [1, 640, 1024]          | Done     | Done       | 1.0   | 0      |
|  626 | Tensor<[1, 640]> self = ?,<br>List[int] size = [640]                           | Done     | Done       | 1.0   | 0      |
|  627 | Tensor<[1, 64]> self = ?,<br>List[int] size = [64]                             | Done     | Done       | 1.0   | 0      |
|  628 | Tensor<[1, 672, 1, 1]> self = ?,<br>List[int] size = [1, 672]                  | Done     | Done       | 1.0   | 0      |
|  629 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                           | Unknown  | Done       | 1.0   | 0      |
|  630 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768]               | Done     | Done       | 1.0   | 0      |
|  631 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]                 | Unknown  | Unknown    | N/A   | N/A    |
|  632 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]                  | Done     | Done       | 1.0   | 0      |
|  633 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]                   | Unknown  | Unknown    | N/A   | N/A    |
|  634 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]              | Unknown  | Unknown    | N/A   | N/A    |
|  635 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 1024]    | Done     | Done       | 1.0   | 0      |
|  636 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] size = [49, 1024]               | Done     | Done       | 1.0   | 0      |
|  637 | Tensor<[1, 7, 7, 1536]> self = ?,<br>List[int] size = [49, 1536]               | Done     | Done       | 1.0   | 0      |
|  638 | Tensor<[1, 7, 7, 2048]> self = ?,<br>List[int] size = [49, 2048]               | Done     | Done       | 1.0   | 0      |
|  639 | Tensor<[1, 7, 7, 3072]> self = ?,<br>List[int] size = [49, 3072]               | Done     | Done       | 1.0   | 0      |
|  640 | Tensor<[1, 7, 7, 4096]> self = ?,<br>List[int] size = [49, 4096]               | Done     | Done       | 1.0   | 0      |
|  641 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [1, 1, 7, 1, 7, 768]      | Done     | Done       | 1.0   | 0      |
|  642 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] size = [49, 768]                 | Done     | Done       | 1.0   | 0      |
|  643 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 7, 768]                 | Done     | Done       | 1.0   | 0      |
|  644 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]                    | Done     | Done       | 1.0   | 0      |
|  645 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 12, 64]               | Done     | Done       | 1.0   | 0      |
|  646 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [7, 768]                     | Done     | Done       | 1.0   | 0      |
|  647 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]               | Unknown  | Unknown    | N/A   | N/A    |
|  648 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]            | Unknown  | Unknown    | N/A   | N/A    |
|  649 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [71, 7, 64]               | Unknown  | Unknown    | N/A   | N/A    |
|  650 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]                 | Unknown  | Unknown    | N/A   | N/A    |
|  651 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int] size = [1, 7392]                | Done     | Done       | 1.0   | 0      |
|  652 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768]                  | Done     | Done       | 1.0   | 0      |
|  653 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192]           | Unknown  | Done       | 1.0   | 0      |
|  654 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]           | Done     | Done       | 1.0   | 0      |
|  655 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12]           | Unknown  | Done       | 1.0   | 0      |
|  656 | Tensor<[1, 768, 16, 16]> self = ?,<br>List[int] size = [1, 768, 256]           | Done     | Unknown    | N/A   | N/A    |
|  657 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14]           | Done     | Done       | 1.0   | 0      |
|  658 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]                 | Done     | Done       | 1.0   | 0      |
|  659 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]                 | Done     | Done       | 1.0   | 0      |
|  660 | Tensor<[1, 768, 49]> self = ?,<br>List[int] size = [1, 768, 7, 7]              | Done     | Done       | 1.0   | 0      |
|  661 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]              | Done     | Done       | 1.0   | 0      |
|  662 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                     | Unknown  | Done       | 1.0   | 0      |
|  663 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                           | Done     | Done       | 1.0   | 0      |
|  664 | Tensor<[1, 784, 1, 1]> self = ?,<br>List[int] size = [1, 784]                  | Done     | Done       | 1.0   | 0      |
|  665 | Tensor<[1, 784]> self = ?,<br>List[int] size = [784]                           | Done     | Done       | 1.0   | 0      |
|  666 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]                           | Done     | Done       | 1.0   | 0      |
|  667 | Tensor<[1, 7]> self = ?,<br>List[int] size = [1, -1]                           | Done     | Done       | 1.0   | 0      |
|  668 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]                 | Unknown  | Done       | 1.0   | 0      |
|  669 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]                   | Unknown  | Done       | 1.0   | 0      |
|  670 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]                   | Unknown  | Done       | 1.0   | 0      |
|  671 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]                 | Unknown  | Done       | 1.0   | 0      |
|  672 | Tensor<[1, 8, 1, 920]> self = ?,<br>List[int] size = [8, 1, 920]               | Done     | Done       | 1.0   | 0      |
|  673 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
|  674 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]               | Unknown  | Done       | 1.0   | 0      |
|  675 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]               | Unknown  | Done       | 1.0   | 0      |
|  676 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]                 | Unknown  | Done       | 1.0   | 0      |
|  677 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]         | Done     | Done       | 1.0   | 0      |
|  678 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]         | Done     | Done       | 1.0   | 0      |
|  679 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]           | Removed  | Done       | 1.0   | 0      |
|  680 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]           | Done     | Done       | 1.0   | 0      |
|  681 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]         | Done     | Done       | 1.0   | 0      |
|  682 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]           | Done     | Done       | 1.0   | 0      |
|  683 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]             | Done     | Done       | 1.0   | 0      |
|  684 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]             | Done     | Done       | 1.0   | 0      |
|  685 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]           | Done     | Done       | 1.0   | 0      |
|  686 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]             | Done     | Done       | 1.0   | 0      |
|  687 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]           | Done     | Done       | 1.0   | 0      |
|  688 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  689 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]               | Unknown  | Done       | 1.0   | 0      |
|  690 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]                 | Unknown  | Done       | 1.0   | 0      |
|  691 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]                 | Unknown  | Done       | 1.0   | 0      |
|  692 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]             | Done     | Done       | 1.0   | 0      |
|  693 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  694 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 1024]    | Done     | Done       | 1.0   | 0      |
|  695 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] size = [64, 1024]               | Done     | Done       | 1.0   | 0      |
|  696 | Tensor<[1, 8, 8, 1536]> self = ?,<br>List[int] size = [64, 1536]               | Done     | Done       | 1.0   | 0      |
|  697 | Tensor<[1, 8, 8, 2048]> self = ?,<br>List[int] size = [64, 2048]               | Done     | Done       | 1.0   | 0      |
|  698 | Tensor<[1, 8, 8, 3072]> self = ?,<br>List[int] size = [64, 3072]               | Done     | Unknown    | N/A   | N/A    |
|  699 | Tensor<[1, 8, 8, 4096]> self = ?,<br>List[int] size = [64, 4096]               | Done     | Done       | 1.0   | 0      |
|  700 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [1, 1, 8, 1, 8, 768]      | Done     | Done       | 1.0   | 0      |
|  701 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] size = [64, 768]                 | Done     | Unknown    | N/A   | N/A    |
|  702 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, <s0 + 1>, 64]     | Unknown  | Unknown    | N/A   | N/A    |
|  703 | Tensor<[1, 888, 1, 1]> self = ?,<br>List[int] size = [1, 888]                  | Done     | Done       | 1.0   | 0      |
|  704 | Tensor<[1, 8]> self = ?,<br>List[int] size = [-1, 2]                           | Done     | Done       | 1.0   | 0      |
|  705 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [1, 9, 16, 64]              | Done     | Done       | 1.0   | 0      |
|  706 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]                   | Done     | Done       | 1.0   | 0      |
|  707 | Tensor<[1, 9, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]             | Unknown  | Done       | 1.0   | 0      |
|  708 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]                     | Done     | Done       | 1.0   | 0      |
|  709 | Tensor<[1, 9, 16384]> self = ?,<br>List[int] size = [9, 16384]                 | Done     | Done       | 1.0   | 0      |
|  710 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [1, 9, 16, 128]             | Done     | Done       | 1.0   | 0      |
|  711 | Tensor<[1, 9, 2048]> self = ?,<br>List[int] size = [9, 2048]                   | Done     | Done       | 1.0   | 0      |
|  712 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]                   | Done     | Done       | 1.0   | 0      |
|  713 | Tensor<[1, 9, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]               | Unknown  | Done       | 1.0   | 0      |
|  714 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [1, 9, 64, 64]              | Done     | Done       | 1.0   | 0      |
|  715 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]                   | Done     | Done       | 1.0   | 0      |
|  716 | Tensor<[1, 9, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]               | Unknown  | Done       | 1.0   | 0      |
|  717 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [1, 9, 12, 64]               | Done     | Done       | 1.0   | 0      |
|  718 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]                     | Done     | Done       | 1.0   | 0      |
|  719 | Tensor<[1, 9, 8192]> self = ?,<br>List[int] size = [9, 8192]                   | Done     | Done       | 1.0   | 0      |
|  720 | Tensor<[1, 912, 1, 1]> self = ?,<br>List[int] size = [1, 912]                  | Done     | Done       | 1.0   | 0      |
|  721 | Tensor<[1, 920]> self = ?,<br>List[int] size = [1, 1, 1, 920]                  | Done     | Done       | 1.0   | 0      |
|  722 | Tensor<[1, 9216]> self = ?,<br>List[int] size = [1, 64, 12, 12]                | Done     | Done       | 1.0   | 0      |
|  723 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960]                  | Done     | Done       | 1.0   | 0      |
|  724 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]         | Unknown  | Unknown    | N/A   | N/A    |
|  725 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 1280]   | Unknown  | Unknown    | N/A   | N/A    |
|  726 | Tensor<[1, s0*s1, 1280]> self = ?,<br>List[int] size = [<s0*s1>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  727 | Tensor<[1, s0*s1, 2560]> self = ?,<br>List[int] size = [<s0*s1>, 2560]         | Unknown  | Unknown    | N/A   | N/A    |
|  728 | Tensor<[1, s0*s1, 5120]> self = ?,<br>List[int] size = [<s0*s1>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
|  729 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]           | Unknown  | Unknown    | N/A   | N/A    |
|  730 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0>, <s1>, 640]     | Unknown  | Unknown    | N/A   | N/A    |
|  731 | Tensor<[1, s0*s1, 640]> self = ?,<br>List[int] size = [<s0*s1>, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  732 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  733 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  734 | Tensor<[1, s0, 1280]> self = ?,<br>List[int] size = [<s0>, 1280]               | Unknown  | Unknown    | N/A   | N/A    |
|  735 | Tensor<[1, s0, 256]> self = ?,<br>List[int] size = [<s0>, 256]                 | Unknown  | Unknown    | N/A   | N/A    |
|  736 | Tensor<[1, s0, 80]> self = ?,<br>List[int] size = [<s0>, 80]                   | Unknown  | Unknown    | N/A   | N/A    |
|  737 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]     | Unknown  | Unknown    | N/A   | N/A    |
|  738 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]       | Unknown  | Unknown    | N/A   | N/A    |
|  739 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, -1, 8, 160]         | Unknown  | Unknown    | N/A   | N/A    |
|  740 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 1280]   | Unknown  | Unknown    | N/A   | N/A    |
|  741 | Tensor<[1, s1*s2, 1280]> self = ?,<br>List[int] size = [<s1*s2>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  742 | Tensor<[1, s1*s2, 2560]> self = ?,<br>List[int] size = [<s1*s2>, 2560]         | Unknown  | Unknown    | N/A   | N/A    |
|  743 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, -1, 8, 40]           | Unknown  | Unknown    | N/A   | N/A    |
|  744 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 320]     | Unknown  | Unknown    | N/A   | N/A    |
|  745 | Tensor<[1, s1*s2, 320]> self = ?,<br>List[int] size = [<s1*s2>, 320]           | Unknown  | Unknown    | N/A   | N/A    |
|  746 | Tensor<[1, s1*s2, 5120]> self = ?,<br>List[int] size = [<s1*s2>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
|  747 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, -1, 8, 80]           | Unknown  | Unknown    | N/A   | N/A    |
|  748 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1>, <s2>, 640]     | Unknown  | Unknown    | N/A   | N/A    |
|  749 | Tensor<[1, s1*s2, 640]> self = ?,<br>List[int] size = [<s1*s2>, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  750 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>List[int] size = [1, -1, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
|  751 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>List[int] size = [1, -1, 320]           | Unknown  | Unknown    | N/A   | N/A    |
|  752 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>List[int] size = [1, -1, 640]           | Unknown  | Unknown    | N/A   | N/A    |
|  753 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]     | Unknown  | Unknown    | N/A   | N/A    |
|  754 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]       | Unknown  | Unknown    | N/A   | N/A    |
|  755 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]       | Unknown  | Unknown    | N/A   | N/A    |
|  756 | Tensor<[1, s10 + 1]> self = ?,<br>List[int] size = [1, -1]                     | Unknown  | Unknown    | N/A   | N/A    |
|  757 | Tensor<[10, 1024]> self = ?,<br>List[int] size = [1, 10, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  758 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]                 | Unknown  | Done       | 1.0   | 0      |
|  759 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002]             | Done     | Done       | 1.0   | 0      |
|  760 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]                 | Removed  | Done       | 1.0   | 0      |
|  761 | Tensor<[10, 4096]> self = ?,<br>List[int] size = [1, 10, 4096]                 | Unknown  | Done       | 1.0   | 0      |
|  762 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]                   | Unknown  | Done       | 1.0   | 0      |
|  763 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                   | Done     | Done       | 1.0   | 0      |
|  764 | Tensor<[100, 1, 2048]> self = ?,<br>List[int] size = [100, 2048]               | Done     | Done       | 1.0   | 0      |
|  765 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 256]                 | Done     | Done       | 1.0   | 0      |
|  766 | Tensor<[100, 1, 256]> self = ?,<br>List[int] size = [100, 8, 32]               | Done     | Done       | 1.0   | 0      |
|  767 | Tensor<[100, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Done     | Done       | 1.0   | 0      |
|  768 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]                 | Removed  | Done       | 1.0   | 0      |
|  769 | Tensor<[100, 2048]> self = ?,<br>List[int] size = [100, 1, 2048]               | Done     | Done       | 1.0   | 0      |
|  770 | Tensor<[100, 256]> self = ?,<br>List[int] size = [100, 1, 256]                 | Done     | Done       | 1.0   | 0      |
|  771 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]                     | Done     | Done       | 1.0   | 0      |
|  772 | Tensor<[100, 8, 32]> self = ?,<br>List[int] size = [100, 256]                  | Done     | Done       | 1.0   | 0      |
|  773 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]                   | Done     | Done       | 1.0   | 0      |
|  774 | Tensor<[1024, 1024]> self = ?,<br>List[int] size = [1, 32, 32, 1024]           | Removed  | Done       | 1.0   | 0      |
|  775 | Tensor<[1024, 160]> self = ?,<br>List[int] size = [1, 1024, 160]               | Done     | Done       | 1.0   | 0      |
|  776 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [1, 32, 32, 192]             | Done     | Done       | 1.0   | 0      |
|  777 | Tensor<[1024, 192]> self = ?,<br>List[int] size = [16, 64, 192]                | Done     | Done       | 1.0   | 0      |
|  778 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 1024, 256]               | Done     | Done       | 1.0   | 0      |
|  779 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [1, 32, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  780 | Tensor<[1024, 256]> self = ?,<br>List[int] size = [16, 64, 256]                | Done     | Done       | 1.0   | 0      |
|  781 | Tensor<[1024, 576]> self = ?,<br>List[int] size = [16, 64, 576]                | Done     | Done       | 1.0   | 0      |
|  782 | Tensor<[1024, 640]> self = ?,<br>List[int] size = [1, 1024, 640]               | Done     | Done       | 1.0   | 0      |
|  783 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [1, 32, 32, 768]             | Removed  | Done       | 1.0   | 0      |
|  784 | Tensor<[1024, 768]> self = ?,<br>List[int] size = [16, 64, 768]                | Done     | Done       | 1.0   | 0      |
|  785 | Tensor<[1024]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Removed  | Done       | 1.0   | 0      |
|  786 | Tensor<[10]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       | 1.0   | 0      |
|  787 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | 1.0   | 0      |
|  788 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]               | Unknown  | Done       | 1.0   | 0      |
|  789 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]                 | Unknown  | Done       | 1.0   | 0      |
|  790 | Tensor<[12, 1, 24]> self = ?,<br>List[int] size = [1, 12, 1, 24]               | Unknown  | Unknown    | N/A   | N/A    |
|  791 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]                 | Unknown  | Done       | 1.0   | 0      |
|  792 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | 1.0   | 0      |
|  793 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | 1.0   | 0      |
|  794 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  795 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  796 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]             | Removed  | Done       | 1.0   | 0      |
|  797 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]             | Removed  | Done       | 1.0   | 0      |
|  798 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12]             | Done     | Done       | 1.0   | 0      |
|  799 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64]             | Done     | Done       | 1.0   | 0      |
|  800 | Tensor<[12, 14, 14]> self = ?,<br>List[int] size = [1, 12, 14, 14]             | Done     | Done       | 1.0   | 0      |
|  801 | Tensor<[12, 14, 64]> self = ?,<br>List[int] size = [1, 12, 14, 64]             | Done     | Done       | 1.0   | 0      |
|  802 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]             | Done     | Done       | 1.0   | 0      |
|  803 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64]             | Done     | Done       | 1.0   | 0      |
|  804 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197]         | Done     | Done       | 1.0   | 0      |
|  805 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]           | Done     | Done       | 1.0   | 0      |
|  806 | Tensor<[12, 201, 201]> self = ?,<br>List[int] size = [1, 12, 201, 201]         | Unknown  | Unknown    | N/A   | N/A    |
|  807 | Tensor<[12, 201, 64]> self = ?,<br>List[int] size = [1, 12, 201, 64]           | Unknown  | Unknown    | N/A   | N/A    |
|  808 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [1, 12, 24, 24]             | Unknown  | Done       | 1.0   | 0      |
|  809 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]                | Unknown  | Done       | 1.0   | 0      |
|  810 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64]             | Unknown  | Done       | 1.0   | 0      |
|  811 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]                | Unknown  | Done       | 1.0   | 0      |
|  812 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25]             | Removed  | Done       | 1.0   | 0      |
|  813 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64]             | Removed  | Done       | 1.0   | 0      |
|  814 | Tensor<[12, 257, 257]> self = ?,<br>List[int] size = [1, 12, 257, 257]         | Done     | Unknown    | N/A   | N/A    |
|  815 | Tensor<[12, 257, 64]> self = ?,<br>List[int] size = [1, 12, 257, 64]           | Done     | Unknown    | N/A   | N/A    |
|  816 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]                       | Done     | Done       | 1.0   | 0      |
|  817 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]                 | Done     | Done       | 1.0   | 0      |
|  818 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | 1.0   | 0      |
|  819 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | 1.0   | 0      |
|  820 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]             | Done     | Done       | 1.0   | 0      |
|  821 | Tensor<[12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]           | Done     | Done       | 1.0   | 0      |
|  822 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64]               | Done     | Done       | 1.0   | 0      |
|  823 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]                 | Done     | Done       | 1.0   | 0      |
|  824 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]                   | Done     | Done       | 1.0   | 0      |
|  825 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64]               | Done     | Done       | 1.0   | 0      |
|  826 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]                 | Done     | Done       | 1.0   | 0      |
|  827 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]             | Done     | Done       | 1.0   | 0      |
|  828 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]               | Done     | Done       | 1.0   | 0      |
|  829 | Tensor<[128, 384, 384]> self = ?,<br>List[int] size = [8, 16, 384, 384]        | Removed  | Unknown    | N/A   | N/A    |
|  830 | Tensor<[128, 384, 64]> self = ?,<br>List[int] size = [8, 16, 384, 64]          | Removed  | Unknown    | N/A   | N/A    |
|  831 | Tensor<[128, 49, 32]> self = ?,<br>List[int] size = [16, 8, 49, 32]            | Done     | Done       | 1.0   | 0      |
|  832 | Tensor<[128, 49, 49]> self = ?,<br>List[int] size = [16, 8, 49, 49]            | Done     | Done       | 1.0   | 0      |
|  833 | Tensor<[128, 64, 32]> self = ?,<br>List[int] size = [16, 8, 64, 32]            | Done     | Done       | 1.0   | 0      |
|  834 | Tensor<[128, 64, 64]> self = ?,<br>List[int] size = [16, 8, 64, 64]            | Done     | Done       | 1.0   | 0      |
|  835 | Tensor<[128]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Removed  | Done       | 1.0   | 0      |
|  836 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 1280]             | Done     | Done       | 1.0   | 0      |
|  837 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 16, 80]           | Done     | Done       | 1.0   | 0      |
|  838 | Tensor<[1370, 1, 16, 80]> self = ?,<br>List[int] size = [1370, 1280]           | Done     | Done       | 1.0   | 0      |
|  839 | Tensor<[1370, 1, 3840]> self = ?,<br>List[int] size = [1370, 1, 3, 1280]       | Done     | Done       | 1.0   | 0      |
|  840 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1, 1370, 1280]             | Done     | Done       | 1.0   | 0      |
|  841 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1370, 1, 1280]             | Done     | Done       | 1.0   | 0      |
|  842 | Tensor<[1370, 3840]> self = ?,<br>List[int] size = [1370, 1, 3840]             | Done     | Done       | 1.0   | 0      |
|  843 | Tensor<[1370, 5120]> self = ?,<br>List[int] size = [1, 1370, 5120]             | Removed  | Done       | 1.0   | 0      |
|  844 | Tensor<[14, 14]> self = ?,<br>List[int] size = [2, 7, 2, 7]                    | Done     | Done       | 1.0   | 0      |
|  845 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]                  | Done     | Done       | 1.0   | 0      |
|  846 | Tensor<[14, 2]> self = ?,<br>List[int] size = [1, 14, 2]                       | Done     | Done       | 1.0   | 0      |
|  847 | Tensor<[14, 3072]> self = ?,<br>List[int] size = [1, 14, 3072]                 | Done     | Done       | 1.0   | 0      |
|  848 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]                    | Done     | Done       | 1.0   | 0      |
|  849 | Tensor<[14, 768]> self = ?,<br>List[int] size = [1, 14, 768]                   | Done     | Done       | 1.0   | 0      |
|  850 | Tensor<[1444, 8]> self = ?,<br>List[int] size = [-1, 2]                        | Done     | Done       | 1.0   | 0      |
|  851 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]               | Done     | Done       | 1.0   | 0      |
|  852 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]               | Removed  | Done       | 1.0   | 0      |
|  853 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  854 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]                   | Unknown  | Done       | 1.0   | 0      |
|  855 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]                   | Unknown  | Done       | 1.0   | 0      |
|  856 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072]             | Unknown  | Done       | 1.0   | 0      |
|  857 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]               | Unknown  | Done       | 1.0   | 0      |
|  858 | Tensor<[16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]               | Unknown  | Done       | 1.0   | 0      |
|  859 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]                 | Unknown  | Done       | 1.0   | 0      |
|  860 | Tensor<[16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]                 | Unknown  | Done       | 1.0   | 0      |
|  861 | Tensor<[16, 1, 60]> self = ?,<br>List[int] size = [1, 16, 1, 60]               | Unknown  | Done       | 1.0   | 0      |
|  862 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]               | Unknown  | Done       | 1.0   | 0      |
|  863 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                 | Unknown  | Done       | 1.0   | 0      |
|  864 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  865 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  866 | Tensor<[16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]             | Unknown  | Done       | 1.0   | 0      |
|  867 | Tensor<[16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]             | Unknown  | Done       | 1.0   | 0      |
|  868 | Tensor<[16, 1370, 80]> self = ?,<br>List[int] size = [1, 16, 1370, 80]         | Done     | Done       | 1.0   | 0      |
|  869 | Tensor<[16, 16]> self = ?,<br>List[int] size = [2, 8, 2, 8]                    | Done     | Done       | 1.0   | 0      |
|  870 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]           | Done     | Done       | 1.0   | 0      |
|  871 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]                 | Removed  | Done       | 1.0   | 0      |
|  872 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]             | Done     | Done       | 1.0   | 0      |
|  873 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]             | Done     | Done       | 1.0   | 0      |
|  874 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 192]       | Done     | Done       | 1.0   | 0      |
|  875 | Tensor<[16, 49, 192]> self = ?,<br>List[int] size = [784, 192]                 | Done     | Done       | 1.0   | 0      |
|  876 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [1, 4, 4, 7, 7, 256]       | Done     | Done       | 1.0   | 0      |
|  877 | Tensor<[16, 49, 256]> self = ?,<br>List[int] size = [784, 256]                 | Done     | Done       | 1.0   | 0      |
|  878 | Tensor<[16, 49, 576]> self = ?,<br>List[int] size = [16, 49, 3, 6, 32]         | Done     | Done       | 1.0   | 0      |
|  879 | Tensor<[16, 49, 768]> self = ?,<br>List[int] size = [16, 49, 3, 8, 32]         | Done     | Done       | 1.0   | 0      |
|  880 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                 | Unknown  | Done       | 1.0   | 0      |
|  881 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]               | Unknown  | Done       | 1.0   | 0      |
|  882 | Tensor<[16, 50, 64]> self = ?,<br>List[int] size = [1, 16, 50, 64]             | Done     | Unknown    | N/A   | N/A    |
|  883 | Tensor<[16, 59, 59]> self = ?,<br>List[int] size = [1, 16, 59, 59]             | Unknown  | Done       | 1.0   | 0      |
|  884 | Tensor<[16, 59, 64]> self = ?,<br>List[int] size = [1, 16, 59, 64]             | Unknown  | Done       | 1.0   | 0      |
|  885 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [1, 16, 6, 49, 49]       | Done     | Done       | 1.0   | 0      |
|  886 | Tensor<[16, 6, 49, 49]> self = ?,<br>List[int] size = [96, 49, 49]             | Done     | Done       | 1.0   | 0      |
|  887 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64, 64]       | Done     | Done       | 1.0   | 0      |
|  888 | Tensor<[16, 6, 64, 64]> self = ?,<br>List[int] size = [96, 64, 64]             | Done     | Done       | 1.0   | 0      |
|  889 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 192]       | Done     | Done       | 1.0   | 0      |
|  890 | Tensor<[16, 64, 192]> self = ?,<br>List[int] size = [1024, 192]                | Done     | Done       | 1.0   | 0      |
|  891 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1, 4, 4, 8, 8, 256]       | Done     | Done       | 1.0   | 0      |
|  892 | Tensor<[16, 64, 256]> self = ?,<br>List[int] size = [1024, 256]                | Done     | Done       | 1.0   | 0      |
|  893 | Tensor<[16, 64, 576]> self = ?,<br>List[int] size = [16, 64, 3, 6, 32]         | Done     | Done       | 1.0   | 0      |
|  894 | Tensor<[16, 64, 768]> self = ?,<br>List[int] size = [16, 64, 3, 8, 32]         | Done     | Done       | 1.0   | 0      |
|  895 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]                | Done     | Done       | 1.0   | 0      |
|  896 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]                  | Done     | Done       | 1.0   | 0      |
|  897 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]                   | Done     | Done       | 1.0   | 0      |
|  898 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [1, 16, 8, 49, 49]       | Done     | Done       | 1.0   | 0      |
|  899 | Tensor<[16, 8, 49, 49]> self = ?,<br>List[int] size = [128, 49, 49]            | Done     | Done       | 1.0   | 0      |
|  900 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [1, 16, 8, 64, 64]       | Done     | Done       | 1.0   | 0      |
|  901 | Tensor<[16, 8, 64, 64]> self = ?,<br>List[int] size = [128, 64, 64]            | Done     | Done       | 1.0   | 0      |
|  902 | Tensor<[16, 9, 128]> self = ?,<br>List[int] size = [1, 16, 9, 128]             | Done     | Done       | 1.0   | 0      |
|  903 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]               | Done     | Done       | 1.0   | 0      |
|  904 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]                 | Done     | Done       | 1.0   | 0      |
|  905 | Tensor<[16384, 128]> self = ?,<br>List[int] size = [1, 16384, 128]             | Done     | Done       | 1.0   | 0      |
|  906 | Tensor<[16384, 256]> self = ?,<br>List[int] size = [1, 16384, 256]             | Done     | Done       | 1.0   | 0      |
|  907 | Tensor<[16384, 32]> self = ?,<br>List[int] size = [1, 16384, 32]               | Done     | Done       | 1.0   | 0      |
|  908 | Tensor<[192, 49, 32]> self = ?,<br>List[int] size = [64, 3, 49, 32]            | Done     | Done       | 1.0   | 0      |
|  909 | Tensor<[192, 49, 49]> self = ?,<br>List[int] size = [64, 3, 49, 49]            | Done     | Done       | 1.0   | 0      |
|  910 | Tensor<[192, 64, 32]> self = ?,<br>List[int] size = [64, 3, 64, 32]            | Done     | Done       | 1.0   | 0      |
|  911 | Tensor<[192, 64, 64]> self = ?,<br>List[int] size = [64, 3, 64, 64]            | Done     | Done       | 1.0   | 0      |
|  912 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]             | Done     | Done       | 1.0   | 0      |
|  913 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]               | Done     | Done       | 1.0   | 0      |
|  914 | Tensor<[196, 1152]> self = ?,<br>List[int] size = [4, 49, 1152]                | Done     | Done       | 1.0   | 0      |
|  915 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [1, 14, 14, 1536]            | Done     | Done       | 1.0   | 0      |
|  916 | Tensor<[196, 1536]> self = ?,<br>List[int] size = [4, 49, 1536]                | Done     | Done       | 1.0   | 0      |
|  917 | Tensor<[196, 2048]> self = ?,<br>List[int] size = [1, 14, 14, 2048]            | Done     | Done       | 1.0   | 0      |
|  918 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]               | Removed  | Done       | 1.0   | 0      |
|  919 | Tensor<[196, 384]> self = ?,<br>List[int] size = [1, 14, 14, 384]              | Done     | Done       | 1.0   | 0      |
|  920 | Tensor<[196, 384]> self = ?,<br>List[int] size = [4, 49, 384]                  | Done     | Done       | 1.0   | 0      |
|  921 | Tensor<[196, 512]> self = ?,<br>List[int] size = [1, 14, 14, 512]              | Done     | Done       | 1.0   | 0      |
|  922 | Tensor<[196, 512]> self = ?,<br>List[int] size = [4, 49, 512]                  | Done     | Done       | 1.0   | 0      |
|  923 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]                 | Done     | Done       | 1.0   | 0      |
|  924 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 1024]               | Done     | Done       | 1.0   | 0      |
|  925 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 16, 64]             | Done     | Done       | 1.0   | 0      |
|  926 | Tensor<[197, 1, 12, 64]> self = ?,<br>List[int] size = [197, 768]              | Done     | Done       | 1.0   | 0      |
|  927 | Tensor<[197, 1, 16, 64]> self = ?,<br>List[int] size = [197, 1024]             | Done     | Done       | 1.0   | 0      |
|  928 | Tensor<[197, 1, 2304]> self = ?,<br>List[int] size = [197, 1, 3, 768]          | Done     | Done       | 1.0   | 0      |
|  929 | Tensor<[197, 1, 3072]> self = ?,<br>List[int] size = [197, 1, 3, 1024]         | Done     | Done       | 1.0   | 0      |
|  930 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 12, 64]              | Done     | Done       | 1.0   | 0      |
|  931 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 768]                 | Done     | Done       | 1.0   | 0      |
|  932 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]               | Done     | Done       | 1.0   | 0      |
|  933 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [197, 1, 1024]               | Done     | Done       | 1.0   | 0      |
|  934 | Tensor<[197, 2304]> self = ?,<br>List[int] size = [197, 1, 2304]               | Done     | Done       | 1.0   | 0      |
|  935 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]               | Removed  | Done       | 1.0   | 0      |
|  936 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [197, 1, 3072]               | Done     | Done       | 1.0   | 0      |
|  937 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]               | Removed  | Done       | 1.0   | 0      |
|  938 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]                 | Done     | Done       | 1.0   | 0      |
|  939 | Tensor<[197, 768]> self = ?,<br>List[int] size = [197, 1, 768]                 | Done     | Done       | 1.0   | 0      |
|  940 | Tensor<[19]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       | 1.0   | 0      |
|  941 | Tensor<[19]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | 1.0   | 0      |
|  942 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                              | Done     | Done       | 1.0   | 0      |
|  943 | Tensor<[1]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       | 1.0   | 0      |
|  944 | Tensor<[2, 256, 32]> self = ?,<br>List[int] size = [1, 2, 256, 32]             | Done     | Done       | 1.0   | 0      |
|  945 | Tensor<[2, 32, 256]> self = ?,<br>List[int] size = [1, 2, 32, 256]             | Done     | Done       | 1.0   | 0      |
|  946 | Tensor<[2, 4096, 256]> self = ?,<br>List[int] size = [1, 2, 4096, 256]         | Done     | Done       | 1.0   | 0      |
|  947 | Tensor<[2, 4096, 32]> self = ?,<br>List[int] size = [1, 2, 4096, 32]           | Done     | Done       | 1.0   | 0      |
|  948 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]         | Done     | Done       | 1.0   | 0      |
|  949 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]           | Done     | Done       | 1.0   | 0      |
|  950 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]                  | Done     | Done       | 1.0   | 0      |
|  951 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]                    | Done     | Done       | 1.0   | 0      |
|  952 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]               | Done     | Done       | 1.0   | 0      |
|  953 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]                | Done     | Done       | 1.0   | 0      |
|  954 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]                | Done     | Done       | 1.0   | 0      |
|  955 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]                           | Done     | Done       | 1.0   | 0      |
|  956 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]               | Done     | Done       | 1.0   | 0      |
|  957 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]                  | Done     | Done       | 1.0   | 0      |
|  958 | Tensor<[201, 3072]> self = ?,<br>List[int] size = [1, 201, 3072]               | Unknown  | Unknown    | N/A   | N/A    |
|  959 | Tensor<[201, 768]> self = ?,<br>List[int] size = [1, 201, 768]                 | Unknown  | Unknown    | N/A   | N/A    |
|  960 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]             | Done     | Done       | 1.0   | 0      |
|  961 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]               | Done     | Done       | 1.0   | 0      |
|  962 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]               | Done     | Done       | 1.0   | 0      |
|  963 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, 2048, 768]               | Done     | Done       | 1.0   | 0      |
|  964 | Tensor<[2048]> self = ?,<br>List[int] size = [1, -1, 1, 1]                     | Removed  | Done       | 1.0   | 0      |
|  965 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       | 1.0   | 0      |
|  966 | Tensor<[20]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | 1.0   | 0      |
|  967 | Tensor<[225, 12]> self = ?,<br>List[int] size = [1, 15, 15, 12]                | Removed  | Done       | 1.0   | 0      |
|  968 | Tensor<[225, 16]> self = ?,<br>List[int] size = [1, 15, 15, 16]                | Removed  | Done       | 1.0   | 0      |
|  969 | Tensor<[225, 24]> self = ?,<br>List[int] size = [1, 15, 15, 24]                | Removed  | Done       | 1.0   | 0      |
|  970 | Tensor<[225, 32]> self = ?,<br>List[int] size = [1, 15, 15, 32]                | Removed  | Done       | 1.0   | 0      |
|  971 | Tensor<[225, 3]> self = ?,<br>List[int] size = [1, 15, 15, 3]                  | Removed  | Done       | 1.0   | 0      |
|  972 | Tensor<[225, 4]> self = ?,<br>List[int] size = [1, 15, 15, 4]                  | Removed  | Done       | 1.0   | 0      |
|  973 | Tensor<[225, 512]> self = ?,<br>List[int] size = [1, 15, 15, 512]              | Removed  | Done       | 1.0   | 0      |
|  974 | Tensor<[225, 6]> self = ?,<br>List[int] size = [1, 15, 15, 6]                  | Removed  | Done       | 1.0   | 0      |
|  975 | Tensor<[225, 8]> self = ?,<br>List[int] size = [1, 15, 15, 8]                  | Removed  | Done       | 1.0   | 0      |
|  976 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]                | Unknown  | Done       | 1.0   | 0      |
|  977 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]                | Unknown  | Done       | 1.0   | 0      |
|  978 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]                 | Unknown  | Done       | 1.0   | 0      |
|  979 | Tensor<[24, 49, 32]> self = ?,<br>List[int] size = [1, 24, 49, 32]             | Done     | Done       | 1.0   | 0      |
|  980 | Tensor<[24, 49, 49]> self = ?,<br>List[int] size = [1, 24, 49, 49]             | Done     | Done       | 1.0   | 0      |
|  981 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]                | Unknown  | Done       | 1.0   | 0      |
|  982 | Tensor<[24, 64, 32]> self = ?,<br>List[int] size = [1, 24, 64, 32]             | Done     | Unknown    | N/A   | N/A    |
|  983 | Tensor<[24, 64, 64]> self = ?,<br>List[int] size = [1, 24, 64, 64]             | Done     | Unknown    | N/A   | N/A    |
|  984 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]                   | Unknown  | Done       | 1.0   | 0      |
|  985 | Tensor<[2401, 12]> self = ?,<br>List[int] size = [49, 49, -1]                  | Removed  | Done       | 1.0   | 0      |
|  986 | Tensor<[2401, 16]> self = ?,<br>List[int] size = [49, 49, -1]                  | Removed  | Done       | 1.0   | 0      |
|  987 | Tensor<[2401, 24]> self = ?,<br>List[int] size = [49, 49, -1]                  | Removed  | Done       | 1.0   | 0      |
|  988 | Tensor<[2401, 32]> self = ?,<br>List[int] size = [49, 49, -1]                  | Removed  | Done       | 1.0   | 0      |
|  989 | Tensor<[2401, 3]> self = ?,<br>List[int] size = [49, 49, -1]                   | Removed  | Done       | 1.0   | 0      |
|  990 | Tensor<[2401, 4]> self = ?,<br>List[int] size = [49, 49, -1]                   | Removed  | Done       | 1.0   | 0      |
|  991 | Tensor<[2401, 6]> self = ?,<br>List[int] size = [49, 49, -1]                   | Removed  | Done       | 1.0   | 0      |
|  992 | Tensor<[2401, 8]> self = ?,<br>List[int] size = [49, 49, -1]                   | Removed  | Done       | 1.0   | 0      |
|  993 | Tensor<[24576, 1]> self = ?,<br>List[int] size = [-1]                          | Unknown  | Unknown    | N/A   | N/A    |
|  994 | Tensor<[25, 12]> self = ?,<br>List[int] size = [-1, 2]                         | Done     | Done       | 1.0   | 0      |
|  995 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]                       | Done     | Done       | 1.0   | 0      |
|  996 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]                 | Removed  | Done       | 1.0   | 0      |
|  997 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]                   | Done     | Done       | 1.0   | 0      |
|  998 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]               | Done     | Done       | 1.0   | 0      |
|  999 | Tensor<[256, 1152]> self = ?,<br>List[int] size = [4, 64, 1152]                | Done     | Done       | 1.0   | 0      |
| 1000 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]               | Done     | Done       | 1.0   | 0      |
| 1001 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [1, 16, 16, 1536]            | Done     | Done       | 1.0   | 0      |
| 1002 | Tensor<[256, 1536]> self = ?,<br>List[int] size = [4, 64, 1536]                | Done     | Done       | 1.0   | 0      |
| 1003 | Tensor<[256, 160]> self = ?,<br>List[int] size = [1, 256, 160]                 | Done     | Done       | 1.0   | 0      |
| 1004 | Tensor<[256, 2048]> self = ?,<br>List[int] size = [1, 16, 16, 2048]            | Done     | Done       | 1.0   | 0      |
| 1005 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                 | Removed  | Done       | 1.0   | 0      |
| 1006 | Tensor<[256, 32]> self = ?,<br>List[int] size = [1, 256, 32]                   | Done     | Done       | 1.0   | 0      |
| 1007 | Tensor<[256, 384]> self = ?,<br>List[int] size = [1, 16, 16, 384]              | Done     | Done       | 1.0   | 0      |
| 1008 | Tensor<[256, 384]> self = ?,<br>List[int] size = [4, 64, 384]                  | Done     | Done       | 1.0   | 0      |
| 1009 | Tensor<[256, 49, 32]> self = ?,<br>List[int] size = [64, 4, 49, 32]            | Done     | Done       | 1.0   | 0      |
| 1010 | Tensor<[256, 49, 49]> self = ?,<br>List[int] size = [64, 4, 49, 49]            | Done     | Done       | 1.0   | 0      |
| 1011 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 16, 16, 512]              | Done     | Done       | 1.0   | 0      |
| 1012 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                 | Done     | Done       | 1.0   | 0      |
| 1013 | Tensor<[256, 512]> self = ?,<br>List[int] size = [4, 64, 512]                  | Done     | Done       | 1.0   | 0      |
| 1014 | Tensor<[256, 64, 32]> self = ?,<br>List[int] size = [64, 4, 64, 32]            | Done     | Done       | 1.0   | 0      |
| 1015 | Tensor<[256, 64, 64]> self = ?,<br>List[int] size = [64, 4, 64, 64]            | Done     | Done       | 1.0   | 0      |
| 1016 | Tensor<[256, 64]> self = ?,<br>List[int] size = [1, 256, 64]                   | Done     | Done       | 1.0   | 0      |
| 1017 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]                 | Done     | Done       | 1.0   | 0      |
| 1018 | Tensor<[256]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Removed  | Done       | 1.0   | 0      |
| 1019 | Tensor<[257, 3072]> self = ?,<br>List[int] size = [1, 257, 3072]               | Removed  | Unknown    | N/A   | N/A    |
| 1020 | Tensor<[257, 768]> self = ?,<br>List[int] size = [1, 257, 768]                 | Done     | Unknown    | N/A   | N/A    |
| 1021 | Tensor<[28, 28]> self = ?,<br>List[int] size = [4, 7, 4, 7]                    | Done     | Done       | 1.0   | 0      |
| 1022 | Tensor<[2]> self = ?,<br>List[int] size = [-1, 1]                              | Done     | Done       | 1.0   | 0      |
| 1023 | Tensor<[2]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       | 1.0   | 0      |
| 1024 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445]       | Done     | Done       | 1.0   | 0      |
| 1025 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]           | Done     | Done       | 1.0   | 0      |
| 1026 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]                 | Done     | Done       | 1.0   | 0      |
| 1027 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]               | Done     | Done       | 1.0   | 0      |
| 1028 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]                 | Done     | Done       | 1.0   | 0      |
| 1029 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]                 | Done     | Done       | 1.0   | 0      |
| 1030 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]                   | Done     | Done       | 1.0   | 0      |
| 1031 | Tensor<[3072, 1024]> self = ?,<br>List[int] size = [8, 384, 1024]              | Done     | Unknown    | N/A   | N/A    |
| 1032 | Tensor<[3072, 2]> self = ?,<br>List[int] size = [8, 384, 2]                    | Done     | Unknown    | N/A   | N/A    |
| 1033 | Tensor<[3072, 4096]> self = ?,<br>List[int] size = [8, 384, 4096]              | Removed  | Unknown    | N/A   | N/A    |
| 1034 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [1, 56, 56, 128]             | Done     | Done       | 1.0   | 0      |
| 1035 | Tensor<[3136, 128]> self = ?,<br>List[int] size = [64, 49, 128]                | Done     | Done       | 1.0   | 0      |
| 1036 | Tensor<[3136, 288]> self = ?,<br>List[int] size = [64, 49, 288]                | Done     | Done       | 1.0   | 0      |
| 1037 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [1, 56, 56, 384]             | Done     | Done       | 1.0   | 0      |
| 1038 | Tensor<[3136, 384]> self = ?,<br>List[int] size = [64, 49, 384]                | Done     | Done       | 1.0   | 0      |
| 1039 | Tensor<[3136, 512]> self = ?,<br>List[int] size = [1, 56, 56, 512]             | Done     | Done       | 1.0   | 0      |
| 1040 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [1, 56, 56, 96]               | Done     | Done       | 1.0   | 0      |
| 1041 | Tensor<[3136, 96]> self = ?,<br>List[int] size = [64, 49, 96]                  | Done     | Done       | 1.0   | 0      |
| 1042 | Tensor<[32, 11008]> self = ?,<br>List[int] size = [1, 32, 11008]               | Unknown  | Unknown    | N/A   | N/A    |
| 1043 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]                 | Done     | Done       | 1.0   | 0      |
| 1044 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]             | Done     | Done       | 1.0   | 0      |
| 1045 | Tensor<[32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128]           | Unknown  | Unknown    | N/A   | N/A    |
| 1046 | Tensor<[32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]             | Unknown  | Unknown    | N/A   | N/A    |
| 1047 | Tensor<[32, 32000]> self = ?,<br>List[int] size = [1, 32, 32000]               | Unknown  | Unknown    | N/A   | N/A    |
| 1048 | Tensor<[32, 32]> self = ?,<br>List[int] size = [4, 8, 4, 8]                    | Done     | Done       | 1.0   | 0      |
| 1049 | Tensor<[32, 4096]> self = ?,<br>List[int] size = [1, 32, 4096]                 | Unknown  | Unknown    | N/A   | N/A    |
| 1050 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]                 | Done     | Done       | 1.0   | 0      |
| 1051 | Tensor<[32, 49, 32]> self = ?,<br>List[int] size = [1, 32, 49, 32]             | Done     | Done       | 1.0   | 0      |
| 1052 | Tensor<[32, 49, 49]> self = ?,<br>List[int] size = [1, 32, 49, 49]             | Done     | Done       | 1.0   | 0      |
| 1053 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]                 | Done     | Done       | 1.0   | 0      |
| 1054 | Tensor<[32, 64, 32]> self = ?,<br>List[int] size = [1, 32, 64, 32]             | Done     | Done       | 1.0   | 0      |
| 1055 | Tensor<[32, 64, 64]> self = ?,<br>List[int] size = [1, 32, 64, 64]             | Done     | Done       | 1.0   | 0      |
| 1056 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]                   | Done     | Unknown    | N/A   | N/A    |
| 1057 | Tensor<[3234, 2, 2]> self = ?,<br>List[int] size = [3234, 4]                   | Done     | Unknown    | N/A   | N/A    |
| 1058 | Tensor<[361, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Done     | Done       | 1.0   | 0      |
| 1059 | Tensor<[38]> self = ?,<br>List[int] size = [-1, 1]                             | Done     | Done       | 1.0   | 0      |
| 1060 | Tensor<[38]> self = ?,<br>List[int] size = [1, -1]                             | Done     | Done       | 1.0   | 0      |
| 1061 | Tensor<[3]> self = ?,<br>List[int] size = [-1, 1]                              | Done     | Done       | 1.0   | 0      |
| 1062 | Tensor<[3]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       | 1.0   | 0      |
| 1063 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [1, 4, 12, 49, 49]       | Done     | Done       | 1.0   | 0      |
| 1064 | Tensor<[4, 12, 49, 49]> self = ?,<br>List[int] size = [48, 49, 49]             | Done     | Done       | 1.0   | 0      |
| 1065 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [1, 4, 12, 64, 64]       | Done     | Done       | 1.0   | 0      |
| 1066 | Tensor<[4, 12, 64, 64]> self = ?,<br>List[int] size = [48, 64, 64]             | Done     | Done       | 1.0   | 0      |
| 1067 | Tensor<[4, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Done     | Done       | 1.0   | 0      |
| 1068 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [1, 4, 16, 49, 49]       | Done     | Done       | 1.0   | 0      |
| 1069 | Tensor<[4, 16, 49, 49]> self = ?,<br>List[int] size = [64, 49, 49]             | Done     | Done       | 1.0   | 0      |
| 1070 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [1, 4, 16, 64, 64]       | Done     | Done       | 1.0   | 0      |
| 1071 | Tensor<[4, 16, 64, 64]> self = ?,<br>List[int] size = [64, 64, 64]             | Done     | Done       | 1.0   | 0      |
| 1072 | Tensor<[4, 2048, 1, 1]> self = ?,<br>List[int] size = [4, 2048]                | Done     | Unknown    | N/A   | N/A    |
| 1073 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]                   | Unknown  | Done       | 1.0   | 0      |
| 1074 | Tensor<[4, 49, 1152]> self = ?,<br>List[int] size = [4, 49, 3, 12, 32]         | Done     | Done       | 1.0   | 0      |
| 1075 | Tensor<[4, 49, 1536]> self = ?,<br>List[int] size = [4, 49, 3, 16, 32]         | Done     | Done       | 1.0   | 0      |
| 1076 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 384]        | Done     | Done       | 1.0   | 0      |
| 1077 | Tensor<[4, 49, 384]> self = ?,<br>List[int] size = [196, 384]                  | Done     | Done       | 1.0   | 0      |
| 1078 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [1, 2, 2, 7, 7, 512]        | Done     | Done       | 1.0   | 0      |
| 1079 | Tensor<[4, 49, 512]> self = ?,<br>List[int] size = [196, 512]                  | Done     | Done       | 1.0   | 0      |
| 1080 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]                 | Unknown  | Done       | 1.0   | 0      |
| 1081 | Tensor<[4, 64, 1152]> self = ?,<br>List[int] size = [4, 64, 3, 12, 32]         | Done     | Done       | 1.0   | 0      |
| 1082 | Tensor<[4, 64, 1536]> self = ?,<br>List[int] size = [4, 64, 3, 16, 32]         | Done     | Done       | 1.0   | 0      |
| 1083 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 384]        | Done     | Done       | 1.0   | 0      |
| 1084 | Tensor<[4, 64, 384]> self = ?,<br>List[int] size = [256, 384]                  | Done     | Done       | 1.0   | 0      |
| 1085 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [1, 2, 2, 8, 8, 512]        | Done     | Done       | 1.0   | 0      |
| 1086 | Tensor<[4, 64, 512]> self = ?,<br>List[int] size = [256, 512]                  | Done     | Done       | 1.0   | 0      |
| 1087 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]                     | Unknown  | Done       | 1.0   | 0      |
| 1088 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                        | Done     | Done       | 1.0   | 0      |
| 1089 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [1, 64, 64, 128]             | Done     | Done       | 1.0   | 0      |
| 1090 | Tensor<[4096, 128]> self = ?,<br>List[int] size = [64, 64, 128]                | Done     | Done       | 1.0   | 0      |
| 1091 | Tensor<[4096, 12]> self = ?,<br>List[int] size = [64, 64, -1]                  | Removed  | Done       | 1.0   | 0      |
| 1092 | Tensor<[4096, 16]> self = ?,<br>List[int] size = [64, 64, -1]                  | Removed  | Done       | 1.0   | 0      |
| 1093 | Tensor<[4096, 24]> self = ?,<br>List[int] size = [64, 64, -1]                  | Removed  | Done       | 1.0   | 0      |
| 1094 | Tensor<[4096, 2560]> self = ?,<br>List[int] size = [1, 4096, 2560]             | Unknown  | Done       | 1.0   | 0      |
| 1095 | Tensor<[4096, 256]> self = ?,<br>List[int] size = [1, 4096, 256]               | Done     | Done       | 1.0   | 0      |
| 1096 | Tensor<[4096, 288]> self = ?,<br>List[int] size = [64, 64, 288]                | Done     | Done       | 1.0   | 0      |
| 1097 | Tensor<[4096, 320]> self = ?,<br>List[int] size = [1, 4096, 320]               | Unknown  | Done       | 1.0   | 0      |
| 1098 | Tensor<[4096, 32]> self = ?,<br>List[int] size = [64, 64, -1]                  | Removed  | Done       | 1.0   | 0      |
| 1099 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [1, 64, 64, 384]             | Removed  | Done       | 1.0   | 0      |
| 1100 | Tensor<[4096, 384]> self = ?,<br>List[int] size = [64, 64, 384]                | Done     | Done       | 1.0   | 0      |
| 1101 | Tensor<[4096, 3]> self = ?,<br>List[int] size = [64, 64, -1]                   | Removed  | Done       | 1.0   | 0      |
| 1102 | Tensor<[4096, 4]> self = ?,<br>List[int] size = [64, 64, -1]                   | Removed  | Done       | 1.0   | 0      |
| 1103 | Tensor<[4096, 512]> self = ?,<br>List[int] size = [1, 64, 64, 512]             | Removed  | Done       | 1.0   | 0      |
| 1104 | Tensor<[4096, 64]> self = ?,<br>List[int] size = [1, 4096, 64]                 | Done     | Done       | 1.0   | 0      |
| 1105 | Tensor<[4096, 6]> self = ?,<br>List[int] size = [64, 64, -1]                   | Removed  | Done       | 1.0   | 0      |
| 1106 | Tensor<[4096, 8]> self = ?,<br>List[int] size = [64, 64, -1]                   | Removed  | Done       | 1.0   | 0      |
| 1107 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [1, 64, 64, 96]               | Done     | Done       | 1.0   | 0      |
| 1108 | Tensor<[4096, 96]> self = ?,<br>List[int] size = [64, 64, 96]                  | Done     | Done       | 1.0   | 0      |
| 1109 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                 | Unknown  | Done       | 1.0   | 0      |
| 1110 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]               | Unknown  | Done       | 1.0   | 0      |
| 1111 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                   | Unknown  | Done       | 1.0   | 0      |
| 1112 | Tensor<[48, 49, 32]> self = ?,<br>List[int] size = [4, 12, 49, 32]             | Done     | Done       | 1.0   | 0      |
| 1113 | Tensor<[48, 49, 49]> self = ?,<br>List[int] size = [4, 12, 49, 49]             | Done     | Done       | 1.0   | 0      |
| 1114 | Tensor<[48, 64, 32]> self = ?,<br>List[int] size = [4, 12, 64, 32]             | Done     | Done       | 1.0   | 0      |
| 1115 | Tensor<[48, 64, 64]> self = ?,<br>List[int] size = [4, 12, 64, 64]             | Done     | Done       | 1.0   | 0      |
| 1116 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]               | Done     | Done       | 1.0   | 0      |
| 1117 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]               | Done     | Done       | 1.0   | 0      |
| 1118 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 49, 1024]                 | Done     | Done       | 1.0   | 0      |
| 1119 | Tensor<[49, 1024]> self = ?,<br>List[int] size = [1, 7, 7, 1024]               | Done     | Done       | 1.0   | 0      |
| 1120 | Tensor<[49, 2304]> self = ?,<br>List[int] size = [1, 49, 2304]                 | Done     | Done       | 1.0   | 0      |
| 1121 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 49, 3072]                 | Done     | Done       | 1.0   | 0      |
| 1122 | Tensor<[49, 3072]> self = ?,<br>List[int] size = [1, 7, 7, 3072]               | Done     | Done       | 1.0   | 0      |
| 1123 | Tensor<[49, 4096]> self = ?,<br>List[int] size = [1, 7, 7, 4096]               | Done     | Done       | 1.0   | 0      |
| 1124 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 49, 768]                   | Done     | Done       | 1.0   | 0      |
| 1125 | Tensor<[49, 768]> self = ?,<br>List[int] size = [1, 7, 7, 768]                 | Done     | Done       | 1.0   | 0      |
| 1126 | Tensor<[5, 1024, 256]> self = ?,<br>List[int] size = [1, 5, 1024, 256]         | Done     | Done       | 1.0   | 0      |
| 1127 | Tensor<[5, 1024, 32]> self = ?,<br>List[int] size = [1, 5, 1024, 32]           | Done     | Done       | 1.0   | 0      |
| 1128 | Tensor<[5, 1024]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  | Done       | 1.0   | 0      |
| 1129 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]         | Done     | Done       | 1.0   | 0      |
| 1130 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]           | Done     | Done       | 1.0   | 0      |
| 1131 | Tensor<[5, 256, 32]> self = ?,<br>List[int] size = [1, 5, 256, 32]             | Done     | Done       | 1.0   | 0      |
| 1132 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                   | Unknown  | Done       | 1.0   | 0      |
| 1133 | Tensor<[5, 32, 256]> self = ?,<br>List[int] size = [1, 5, 32, 256]             | Done     | Done       | 1.0   | 0      |
| 1134 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                   | Unknown  | Done       | 1.0   | 0      |
| 1135 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                 | Unknown  | Done       | 1.0   | 0      |
| 1136 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 1024]                 | Done     | Unknown    | N/A   | N/A    |
| 1137 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 16, 64]               | Done     | Unknown    | N/A   | N/A    |
| 1138 | Tensor<[50, 1, 12, 64]> self = ?,<br>List[int] size = [50, 768]                | Done     | Done       | 1.0   | 0      |
| 1139 | Tensor<[50, 1, 16, 64]> self = ?,<br>List[int] size = [50, 1024]               | Done     | Unknown    | N/A   | N/A    |
| 1140 | Tensor<[50, 1, 2304]> self = ?,<br>List[int] size = [50, 1, 3, 768]            | Done     | Done       | 1.0   | 0      |
| 1141 | Tensor<[50, 1, 3072]> self = ?,<br>List[int] size = [50, 1, 3, 1024]           | Done     | Unknown    | N/A   | N/A    |
| 1142 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 12, 64]                | Done     | Done       | 1.0   | 0      |
| 1143 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 768]                   | Done     | Done       | 1.0   | 0      |
| 1144 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [1, 50, 1024]                 | Done     | Done       | 1.0   | 0      |
| 1145 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [50, 1, 1024]                 | Done     | Unknown    | N/A   | N/A    |
| 1146 | Tensor<[50, 2304]> self = ?,<br>List[int] size = [50, 1, 2304]                 | Done     | Done       | 1.0   | 0      |
| 1147 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]                 | Done     | Done       | 1.0   | 0      |
| 1148 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [50, 1, 3072]                 | Done     | Unknown    | N/A   | N/A    |
| 1149 | Tensor<[50, 4096]> self = ?,<br>List[int] size = [1, 50, 4096]                 | Removed  | Done       | 1.0   | 0      |
| 1150 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]                   | Done     | Done       | 1.0   | 0      |
| 1151 | Tensor<[50, 768]> self = ?,<br>List[int] size = [50, 1, 768]                   | Done     | Done       | 1.0   | 0      |
| 1152 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                      | Removed  | Done       | 1.0   | 0      |
| 1153 | Tensor<[56, 56]> self = ?,<br>List[int] size = [8, 7, 8, 7]                    | Done     | Done       | 1.0   | 0      |
| 1154 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]                 | Unknown  | Done       | 1.0   | 0      |
| 1155 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272]               | Unknown  | Done       | 1.0   | 0      |
| 1156 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]                   | Unknown  | Done       | 1.0   | 0      |
| 1157 | Tensor<[5]> self = ?,<br>List[int] size = [-1, 1]                              | Done     | Done       | 1.0   | 0      |
| 1158 | Tensor<[5]> self = ?,<br>List[int] size = [1, -1]                              | Done     | Done       | 1.0   | 0      |
| 1159 | Tensor<[6, 1, 100, 256]> self = ?,<br>List[int] size = [600, 256]              | Done     | Done       | 1.0   | 0      |
| 1160 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]                 | Unknown  | Done       | 1.0   | 0      |
| 1161 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]                 | Unknown  | Done       | 1.0   | 0      |
| 1162 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]                   | Unknown  | Done       | 1.0   | 0      |
| 1163 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]                   | Unknown  | Done       | 1.0   | 0      |
| 1164 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]                 | Unknown  | Done       | 1.0   | 0      |
| 1165 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 1166 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]               | Unknown  | Done       | 1.0   | 0      |
| 1167 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]               | Unknown  | Done       | 1.0   | 0      |
| 1168 | Tensor<[600, 256]> self = ?,<br>List[int] size = [6, 1, 100, 256]              | Done     | Done       | 1.0   | 0      |
| 1169 | Tensor<[600, 4]> self = ?,<br>List[int] size = [6, 1, 100, 4]                  | Done     | Done       | 1.0   | 0      |
| 1170 | Tensor<[600, 92]> self = ?,<br>List[int] size = [6, 1, 100, 92]                | Done     | Done       | 1.0   | 0      |
| 1171 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 64, 1024]                 | Done     | Done       | 1.0   | 0      |
| 1172 | Tensor<[64, 1024]> self = ?,<br>List[int] size = [1, 8, 8, 1024]               | Done     | Done       | 1.0   | 0      |
| 1173 | Tensor<[64, 2304]> self = ?,<br>List[int] size = [1, 64, 2304]                 | Done     | Unknown    | N/A   | N/A    |
| 1174 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [1, 64, 3, 49, 49]       | Done     | Done       | 1.0   | 0      |
| 1175 | Tensor<[64, 3, 49, 49]> self = ?,<br>List[int] size = [192, 49, 49]            | Done     | Done       | 1.0   | 0      |
| 1176 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [1, 64, 3, 64, 64]       | Done     | Done       | 1.0   | 0      |
| 1177 | Tensor<[64, 3, 64, 64]> self = ?,<br>List[int] size = [192, 64, 64]            | Done     | Done       | 1.0   | 0      |
| 1178 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 64, 3072]                 | Done     | Done       | 1.0   | 0      |
| 1179 | Tensor<[64, 3072]> self = ?,<br>List[int] size = [1, 8, 8, 3072]               | Done     | Unknown    | N/A   | N/A    |
| 1180 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [1, 64, 4, 49, 49]       | Done     | Done       | 1.0   | 0      |
| 1181 | Tensor<[64, 4, 49, 49]> self = ?,<br>List[int] size = [256, 49, 49]            | Done     | Done       | 1.0   | 0      |
| 1182 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [1, 64, 4, 64, 64]       | Done     | Done       | 1.0   | 0      |
| 1183 | Tensor<[64, 4, 64, 64]> self = ?,<br>List[int] size = [256, 64, 64]            | Done     | Done       | 1.0   | 0      |
| 1184 | Tensor<[64, 4096]> self = ?,<br>List[int] size = [1, 8, 8, 4096]               | Done     | Done       | 1.0   | 0      |
| 1185 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 128]       | Done     | Done       | 1.0   | 0      |
| 1186 | Tensor<[64, 49, 128]> self = ?,<br>List[int] size = [3136, 128]                | Done     | Done       | 1.0   | 0      |
| 1187 | Tensor<[64, 49, 288]> self = ?,<br>List[int] size = [64, 49, 3, 3, 32]         | Done     | Done       | 1.0   | 0      |
| 1188 | Tensor<[64, 49, 32]> self = ?,<br>List[int] size = [4, 16, 49, 32]             | Done     | Done       | 1.0   | 0      |
| 1189 | Tensor<[64, 49, 384]> self = ?,<br>List[int] size = [64, 49, 3, 4, 32]         | Done     | Done       | 1.0   | 0      |
| 1190 | Tensor<[64, 49, 49]> self = ?,<br>List[int] size = [4, 16, 49, 49]             | Done     | Done       | 1.0   | 0      |
| 1191 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [1, 8, 8, 7, 7, 96]         | Done     | Done       | 1.0   | 0      |
| 1192 | Tensor<[64, 49, 96]> self = ?,<br>List[int] size = [3136, 96]                  | Done     | Done       | 1.0   | 0      |
| 1193 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 128]       | Done     | Done       | 1.0   | 0      |
| 1194 | Tensor<[64, 64, 128]> self = ?,<br>List[int] size = [4096, 128]                | Done     | Done       | 1.0   | 0      |
| 1195 | Tensor<[64, 64, 288]> self = ?,<br>List[int] size = [64, 64, 3, 3, 32]         | Done     | Done       | 1.0   | 0      |
| 1196 | Tensor<[64, 64, 32]> self = ?,<br>List[int] size = [4, 16, 64, 32]             | Done     | Done       | 1.0   | 0      |
| 1197 | Tensor<[64, 64, 384]> self = ?,<br>List[int] size = [64, 64, 3, 4, 32]         | Done     | Done       | 1.0   | 0      |
| 1198 | Tensor<[64, 64, 64]> self = ?,<br>List[int] size = [4, 16, 64, 64]             | Done     | Done       | 1.0   | 0      |
| 1199 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [1, 8, 8, 8, 8, 96]         | Done     | Done       | 1.0   | 0      |
| 1200 | Tensor<[64, 64, 96]> self = ?,<br>List[int] size = [4096, 96]                  | Done     | Done       | 1.0   | 0      |
| 1201 | Tensor<[64, 64]> self = ?,<br>List[int] size = [8, 8, 8, 8]                    | Done     | Done       | 1.0   | 0      |
| 1202 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 64, 768]                   | Done     | Unknown    | N/A   | N/A    |
| 1203 | Tensor<[64, 768]> self = ?,<br>List[int] size = [1, 8, 8, 768]                 | Done     | Done       | 1.0   | 0      |
| 1204 | Tensor<[64, 9, 64]> self = ?,<br>List[int] size = [1, 64, 9, 64]               | Done     | Done       | 1.0   | 0      |
| 1205 | Tensor<[64, 9, 9]> self = ?,<br>List[int] size = [1, 64, 9, 9]                 | Done     | Done       | 1.0   | 0      |
| 1206 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                       | Removed  | Done       | 1.0   | 0      |
| 1207 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]                 | Unknown  | Unknown    | N/A   | N/A    |
| 1208 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]                   | Done     | Done       | 1.0   | 0      |
| 1209 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]                         | Done     | Done       | 1.0   | 0      |
| 1210 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]                   | Done     | Done       | 1.0   | 0      |
| 1211 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]                   | Unknown  | Unknown    | N/A   | N/A    |
| 1212 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]                   | Unknown  | Unknown    | N/A   | N/A    |
| 1213 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]                 | Unknown  | Unknown    | N/A   | N/A    |
| 1214 | Tensor<[7, 768]> self = ?,<br>List[int] size = [1, 7, 768]                     | Done     | Done       | 1.0   | 0      |
| 1215 | Tensor<[71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]               | Unknown  | Unknown    | N/A   | N/A    |
| 1216 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]                 | Unknown  | Unknown    | N/A   | N/A    |
| 1217 | Tensor<[768, 196]> self = ?,<br>List[int] size = [1, 768, 196]                 | Done     | Done       | 1.0   | 0      |
| 1218 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]                 | Done     | Done       | 1.0   | 0      |
| 1219 | Tensor<[784, 1024]> self = ?,<br>List[int] size = [1, 28, 28, 1024]            | Done     | Done       | 1.0   | 0      |
| 1220 | Tensor<[784, 192]> self = ?,<br>List[int] size = [1, 28, 28, 192]              | Done     | Done       | 1.0   | 0      |
| 1221 | Tensor<[784, 192]> self = ?,<br>List[int] size = [16, 49, 192]                 | Done     | Done       | 1.0   | 0      |
| 1222 | Tensor<[784, 256]> self = ?,<br>List[int] size = [1, 28, 28, 256]              | Done     | Done       | 1.0   | 0      |
| 1223 | Tensor<[784, 256]> self = ?,<br>List[int] size = [16, 49, 256]                 | Done     | Done       | 1.0   | 0      |
| 1224 | Tensor<[784, 576]> self = ?,<br>List[int] size = [16, 49, 576]                 | Done     | Done       | 1.0   | 0      |
| 1225 | Tensor<[784, 768]> self = ?,<br>List[int] size = [1, 28, 28, 768]              | Done     | Done       | 1.0   | 0      |
| 1226 | Tensor<[784, 768]> self = ?,<br>List[int] size = [16, 49, 768]                 | Done     | Done       | 1.0   | 0      |
| 1227 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                 | Unknown  | Done       | 1.0   | 0      |
| 1228 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                   | Unknown  | Done       | 1.0   | 0      |
| 1229 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                   | Unknown  | Done       | 1.0   | 0      |
| 1230 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                 | Unknown  | Done       | 1.0   | 0      |
| 1231 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]       | Unknown  | Unknown    | N/A   | N/A    |
| 1232 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]               | Unknown  | Done       | 1.0   | 0      |
| 1233 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]               | Unknown  | Done       | 1.0   | 0      |
| 1234 | Tensor<[8, 16, 384, 384]> self = ?,<br>List[int] size = [128, 384, 384]        | Removed  | Unknown    | N/A   | N/A    |
| 1235 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]         | Done     | Done       | 1.0   | 0      |
| 1236 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]           | Done     | Done       | 1.0   | 0      |
| 1237 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]           | Done     | Done       | 1.0   | 0      |
| 1238 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]         | Done     | Done       | 1.0   | 0      |
| 1239 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]           | Done     | Done       | 1.0   | 0      |
| 1240 | Tensor<[8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]             | Done     | Done       | 1.0   | 0      |
| 1241 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]           | Done     | Done       | 1.0   | 0      |
| 1242 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]             | Done     | Done       | 1.0   | 0      |
| 1243 | Tensor<[8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]             | Done     | Done       | 1.0   | 0      |
| 1244 | Tensor<[8, 384, 1024]> self = ?,<br>List[int] size = [3072, 1024]              | Done     | Unknown    | N/A   | N/A    |
| 1245 | Tensor<[8, 384, 1024]> self = ?,<br>List[int] size = [8, 384, 16, 64]          | Removed  | Unknown    | N/A   | N/A    |
| 1246 | Tensor<[8, 384, 16, 64]> self = ?,<br>List[int] size = [8, 384, 1024]          | Removed  | Unknown    | N/A   | N/A    |
| 1247 | Tensor<[8, 384, 4096]> self = ?,<br>List[int] size = [3072, 4096]              | Done     | Unknown    | N/A   | N/A    |
| 1248 | Tensor<[8732, 1, 4]> self = ?,<br>List[int] size = [8732, 4]                   | Done     | Unknown    | N/A   | N/A    |
| 1249 | Tensor<[8732, 2, 2]> self = ?,<br>List[int] size = [8732, 4]                   | Done     | Unknown    | N/A   | N/A    |
| 1250 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]                   | Done     | Done       | 1.0   | 0      |
| 1251 | Tensor<[9, 1280]> self = ?,<br>List[int] size = [1, 9, 1280]                   | Unknown  | Done       | 1.0   | 0      |
| 1252 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]                     | Done     | Done       | 1.0   | 0      |
| 1253 | Tensor<[9, 12]> self = ?,<br>List[int] size = [-1, 2]                          | Done     | Done       | 1.0   | 0      |
| 1254 | Tensor<[9, 16384]> self = ?,<br>List[int] size = [1, 9, 16384]                 | Done     | Done       | 1.0   | 0      |
| 1255 | Tensor<[9, 2048]> self = ?,<br>List[int] size = [1, 9, 2048]                   | Done     | Done       | 1.0   | 0      |
| 1256 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]                 | Done     | Done       | 1.0   | 0      |
| 1257 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]                   | Done     | Done       | 1.0   | 0      |
| 1258 | Tensor<[9, 320]> self = ?,<br>List[int] size = [1, 9, 320]                     | Unknown  | Done       | 1.0   | 0      |
| 1259 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]                   | Done     | Done       | 1.0   | 0      |
| 1260 | Tensor<[9, 640]> self = ?,<br>List[int] size = [1, 9, 640]                     | Unknown  | Done       | 1.0   | 0      |
| 1261 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]                     | Done     | Done       | 1.0   | 0      |
| 1262 | Tensor<[9, 8192]> self = ?,<br>List[int] size = [1, 9, 8192]                   | Done     | Done       | 1.0   | 0      |
| 1263 | Tensor<[9, 8]> self = ?,<br>List[int] size = [-1, 2]                           | Done     | Done       | 1.0   | 0      |
| 1264 | Tensor<[920, 1, 2048]> self = ?,<br>List[int] size = [920, 2048]               | Done     | Done       | 1.0   | 0      |
| 1265 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 256]                 | Done     | Done       | 1.0   | 0      |
| 1266 | Tensor<[920, 1, 256]> self = ?,<br>List[int] size = [920, 8, 32]               | Done     | Done       | 1.0   | 0      |
| 1267 | Tensor<[920, 2048]> self = ?,<br>List[int] size = [920, 1, 2048]               | Done     | Done       | 1.0   | 0      |
| 1268 | Tensor<[920, 256]> self = ?,<br>List[int] size = [920, 1, 256]                 | Done     | Done       | 1.0   | 0      |
| 1269 | Tensor<[920, 8, 32]> self = ?,<br>List[int] size = [920, 256]                  | Done     | Done       | 1.0   | 0      |
| 1270 | Tensor<[96, 49, 32]> self = ?,<br>List[int] size = [16, 6, 49, 32]             | Done     | Done       | 1.0   | 0      |
| 1271 | Tensor<[96, 49, 49]> self = ?,<br>List[int] size = [16, 6, 49, 49]             | Done     | Done       | 1.0   | 0      |
| 1272 | Tensor<[96, 64, 32]> self = ?,<br>List[int] size = [16, 6, 64, 32]             | Done     | Done       | 1.0   | 0      |
| 1273 | Tensor<[96, 64, 64]> self = ?,<br>List[int] size = [16, 6, 64, 64]             | Done     | Done       | 1.0   | 0      |
| 1274 | Tensor<[s0*s1, 10240]> self = ?,<br>List[int] size = [1, <s0*s1>, 10240]       | Unknown  | Unknown    | N/A   | N/A    |
| 1275 | Tensor<[s0*s1, 1280]> self = ?,<br>List[int] size = [1, <s0*s1>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
| 1276 | Tensor<[s0*s1, 5120]> self = ?,<br>List[int] size = [1, <s0*s1>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
| 1277 | Tensor<[s0*s1, 640]> self = ?,<br>List[int] size = [1, <s0*s1>, 640]           | Unknown  | Unknown    | N/A   | N/A    |
| 1278 | Tensor<[s0, 256]> self = ?,<br>List[int] size = [1, <s0>, 256]                 | Unknown  | Unknown    | N/A   | N/A    |
| 1279 | Tensor<[s0, 768]> self = ?,<br>List[int] size = [1, <s0>, 768]                 | Unknown  | Unknown    | N/A   | N/A    |
| 1280 | Tensor<[s1*s2, 10240]> self = ?,<br>List[int] size = [1, <s1*s2>, 10240]       | Unknown  | Unknown    | N/A   | N/A    |
| 1281 | Tensor<[s1*s2, 1280]> self = ?,<br>List[int] size = [1, <s1*s2>, 1280]         | Unknown  | Unknown    | N/A   | N/A    |
| 1282 | Tensor<[s1*s2, 2560]> self = ?,<br>List[int] size = [1, <s1*s2>, 2560]         | Unknown  | Unknown    | N/A   | N/A    |
| 1283 | Tensor<[s1*s2, 320]> self = ?,<br>List[int] size = [1, <s1*s2>, 320]           | Unknown  | Unknown    | N/A   | N/A    |
| 1284 | Tensor<[s1*s2, 5120]> self = ?,<br>List[int] size = [1, <s1*s2>, 5120]         | Unknown  | Unknown    | N/A   | N/A    |
| 1285 | Tensor<[s1*s2, 640]> self = ?,<br>List[int] size = [1, <s1*s2>, 640]           | Unknown  | Unknown    | N/A   | N/A    |

