### aten.gelu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?      | Unknown  | Done       | 0.9999914482841277 | 0      |
|  1 | Tensor<[1, 10, 3072]> self = ?     | Done     | Done       | 0.9999910216967718 | 0      |
|  2 | Tensor<[1, 10, 768]> self = ?      | Done     | Done       | 0.9999911306900023 | 0      |
|  3 | Tensor<[1, 1024, 512]> self = ?    | Done     | Done       | 0.9999912611151386 | 0      |
|  4 | Tensor<[1, 1024, 640]> self = ?    | Done     | Done       | 0.999991350769631  | 0      |
|  5 | Tensor<[1, 1200, 1280]> self = ?   | Done     | Done       | 0.9999913511669004 | 0      |
|  6 | Tensor<[1, 1370, 5120]> self = ?   | Done     | Done       | 0.9999913423958336 | 0      |
|  7 | Tensor<[1, 14, 14, 1536]> self = ? | Done     | Done       | 0.999991395609667  | 0      |
|  8 | Tensor<[1, 14, 14, 2048]> self = ? | Done     | Done       | 0.999991369917799  | 0      |
|  9 | Tensor<[1, 1445, 768]> self = ?    | Done     | Done       | 0.9999912709961096 | 0      |
| 10 | Tensor<[1, 1500, 3072]> self = ?   | Unknown  | Done       | 0.9999913417996924 | 0      |
| 11 | Tensor<[1, 16, 16, 1536]> self = ? | Done     | Done       | 0.9999913816187068 | 0      |
| 12 | Tensor<[1, 16, 16, 2048]> self = ? | Done     | Done       | 0.9999912868372212 | 0      |
| 13 | Tensor<[1, 16, 3072]> self = ?     | Done     | Done       | 0.9999912718522701 | 0      |
| 14 | Tensor<[1, 16384, 128]> self = ?   | Done     | Done       | 0.9999913416779048 | 0      |
| 15 | Tensor<[1, 19, 4096]> self = ?     | Done     | Done       | 0.9999914121925826 | 0      |
| 16 | Tensor<[1, 19200, 256]> self = ?   | Done     | Done       | 0.9999913397889529 | 0      |
| 17 | Tensor<[1, 196, 3072]> self = ?    | Done     | Done       | 0.9999912830637172 | 0      |
| 18 | Tensor<[1, 197, 3072]> self = ?    | Done     | Done       | 0.9999912845738765 | 0      |
| 19 | Tensor<[1, 197, 4096]> self = ?    | Done     | Done       | 0.9999913258448188 | 0      |
| 20 | Tensor<[1, 2048, 768]> self = ?    | Done     | Done       | 0.9999913578423801 | 0      |
| 21 | Tensor<[1, 24, 3072]> self = ?     | Done     | Done       | 0.999991179571964  | 0      |
| 22 | Tensor<[1, 25, 3072]> self = ?     | Done     | Done       | 0.9999912878607791 | 0      |
| 23 | Tensor<[1, 256, 1024]> self = ?    | Done     | Done       | 0.9999913363199983 | 0      |
| 24 | Tensor<[1, 256, 1280]> self = ?    | Done     | Done       | 0.9999913685114185 | 0      |
| 25 | Tensor<[1, 256, 256]> self = ?     | Done     | Done       | 0.9999912537091494 | 0      |
| 26 | Tensor<[1, 256, 4096]> self = ?    | Done     | Done       | 0.9999913899842103 | 0      |
| 27 | Tensor<[1, 28, 28, 1024]> self = ? | Done     | Done       | 0.9999913684437318 | 0      |
| 28 | Tensor<[1, 28, 28, 768]> self = ?  | Done     | Done       | 0.9999913156109658 | 0      |
| 29 | Tensor<[1, 300, 2048]> self = ?    | Done     | Done       | 0.9999913663726006 | 0      |
| 30 | Tensor<[1, 32, 32, 1024]> self = ? | Done     | Done       | 0.9999912813564626 | 0      |
| 31 | Tensor<[1, 32, 32, 768]> self = ?  | Done     | Done       | 0.9999913127358504 | 0      |
| 32 | Tensor<[1, 4, 3072]> self = ?      | Unknown  | Done       | 0.9999915006038    | 0      |
| 33 | Tensor<[1, 4096, 1280]> self = ?   | Unknown  | Done       | 0.9999913267350212 | 0      |
| 34 | Tensor<[1, 4096, 256]> self = ?    | Done     | Done       | 0.9999912758170294 | 0      |
| 35 | Tensor<[1, 4800, 512]> self = ?    | Done     | Done       | 0.9999912879142887 | 0      |
| 36 | Tensor<[1, 50, 3072]> self = ?     | Done     | Done       | 0.9999912943824334 | 0      |
| 37 | Tensor<[1, 50, 4096]> self = ?     | Done     | Done       | 0.9999913792684018 | 0      |
| 38 | Tensor<[1, 56, 56, 384]> self = ?  | Done     | Done       | 0.9999913427046061 | 0      |
| 39 | Tensor<[1, 56, 56, 512]> self = ?  | Done     | Done       | 0.999991293574931  | 0      |
| 40 | Tensor<[1, 64, 64, 384]> self = ?  | Done     | Done       | 0.9999913162080589 | 0      |
| 41 | Tensor<[1, 64, 64, 512]> self = ?  | Done     | Done       | 0.9999913544198998 | 0      |
| 42 | Tensor<[1, 7, 7, 3072]> self = ?   | Done     | Done       | 0.9999911310873266 | 0      |
| 43 | Tensor<[1, 7, 7, 4096]> self = ?   | Done     | Done       | 0.9999913590079349 | 0      |
| 44 | Tensor<[1, 768, 1500]> self = ?    | Unknown  | Done       | 0.9999913259703697 | 0      |
| 45 | Tensor<[1, 768, 3000]> self = ?    | Unknown  | Done       | 0.9999912997873184 | 0      |
| 46 | Tensor<[1, 768, 384]> self = ?     | Done     | Done       | 0.9999913597042712 | 0      |
| 47 | Tensor<[1, 8, 8, 3072]> self = ?   | Done     | Done       | 0.99999130127056   | 0      |
| 48 | Tensor<[1, 8, 8, 4096]> self = ?   | Done     | Done       | 0.9999913760599903 | 0      |
| 49 | Tensor<[1, s0*s1, 2560]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 50 | Tensor<[1, s0*s1, 5120]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 51 | Tensor<[1, s1*s2, 1280]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 52 | Tensor<[1, s1*s2, 2560]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 53 | Tensor<[1, s1*s2, 5120]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |

