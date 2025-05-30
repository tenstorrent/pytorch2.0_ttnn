### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995949787611575 | 0      |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995933635296388 | 0      |
|  2 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False              | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995131682248738 | 0      |
|  4 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994147011393795 | 0      |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996060251024714 | 0      |
|  7 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9995875432131943 | 0      |
| 10 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996165643413479 | 0      |
| 11 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996005627651112 | 0      |
| 12 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996519236428157 | 0      |
| 13 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995868848589692 | 0      |
| 14 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996401639960335 | 0      |
| 15 | Tensor<[1, 12, 257, 257]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996214389808059 | 0      |
| 17 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996704045399453 | 0      |
| 18 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9996798109882272 | 0      |
| 19 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9997592231905075 | 0      |
| 20 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
| 21 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996589700886791 | 0      |
| 22 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996741731373249 | 0      |
| 23 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996413113845821 | 0      |
| 26 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995899179885239 | 0      |
| 27 | Tensor<[1, 16, 384, 384]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Removed  | Unknown    | N/A                | N/A    |
| 28 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996442783404509 | 0      |
| 29 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9995621002331236 | 0      |
| 30 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995929170604418 | 0      |
| 31 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995880851943479 | 0      |
| 32 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995969617643147 | 0      |
| 33 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995939596569429 | 0      |
| 34 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999568467242144  | 0      |
| 35 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996023162360198 | 0      |
| 36 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996115460528181 | 0      |
| 37 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995903369254809 | 0      |
| 38 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995952707556907 | 0      |
| 39 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9997450206753418 | 0      |
| 40 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994717181488434 | 0      |
| 41 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 42 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9994868075423916 | 0      |
| 43 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 44 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996286950383058 | 0      |
| 45 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9996019403723324 | 0      |
| 46 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996835183086119 | 0      |
| 47 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 48 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9999385557027892 | 0      |
| 49 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 50 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9994709127255754 | 0      |
| 51 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995943166448185 | 0      |
| 52 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Removed  | Done       | 0.9995329845798182 | 0      |
| 53 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995852775485528 | 0      |
| 54 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995949528700272 | 0      |
| 55 | Tensor<[12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Unknown  | Unknown    | N/A                | N/A    |
| 56 | Tensor<[12, 1, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Unknown    | N/A                | N/A    |
| 57 | Tensor<[12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Unknown  | Unknown    | N/A                | N/A    |
| 58 | Tensor<[12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 59 | Tensor<[12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 60 | Tensor<[12, 1, s2 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 61 | Tensor<[12, 1, s4 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 62 | Tensor<[12, 1, s6 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 63 | Tensor<[12, 1, s8 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 64 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9996176536754441 | 0      |
| 65 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996062746324522 | 0      |
| 66 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Done       | 0.9995498818981408 | 0      |
| 67 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 68 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9996014664529318 | 0      |
| 69 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996043213157265 | 0      |
| 70 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996030220567175 | 0      |
| 71 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Done     | Done       | 0.9996679427178515 | 0      |
| 72 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996051581155108 | 0      |
| 73 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996122231557352 | 0      |
| 74 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996034022252236 | 0      |
| 75 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996093507083634 | 0      |
| 76 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996115639408407 | 0      |
| 77 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999603193745605  | 0      |
| 78 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996089745803269 | 0      |
| 79 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996082588166042 | 0      |
| 80 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996092207777179 | 0      |
| 81 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996091846420795 | 0      |
| 82 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.99959300749889   | 0      |
| 83 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995860551809638 | 0      |
| 84 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995859079660131 | 0      |

