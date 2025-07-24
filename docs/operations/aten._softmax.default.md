### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995902112196617 | 0      |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995949593575191 | 0      |
|  2 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False              | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9994118555597432 | 0      |
|  4 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9998019315866202 | 0      |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996142856351229 | 0      |
|  7 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996588157557775 | 0      |
| 10 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9995634348875633 | 0      |
| 11 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996832599877149 | 0      |
| 12 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996530113205069 | 0      |
| 13 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999596399889858  | 0      |
| 14 | Tensor<[1, 12, 201, 201]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996392853908659 | 0      |
| 16 | Tensor<[1, 12, 257, 257]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996082578819553 | 0      |
| 18 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995846645085437 | 0      |
| 19 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9995679526627929 | 0      |
| 20 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995905469666806 | 0      |
| 21 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
| 22 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.999634882181249  | 0      |
| 23 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996352927368093 | 0      |
| 24 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996399322638817 | 0      |
| 27 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996064382936716 | 0      |
| 28 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996267418684756 | 0      |
| 29 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9995877380929518 | 0      |
| 30 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995964249630536 | 0      |
| 31 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995981364528184 | 0      |
| 32 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996002638023392 | 0      |
| 33 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996019687354868 | 0      |
| 34 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999568011361317  | 0      |
| 35 | Tensor<[1, 32, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 36 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996067405164147 | 0      |
| 37 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996092129086219 | 0      |
| 38 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995888913252896 | 0      |
| 39 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995944746863238 | 0      |
| 40 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994612378582478 | 0      |
| 41 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996182756841366 | 0      |
| 42 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 43 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9995368380576868 | 0      |
| 44 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 45 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996190662989785 | 0      |
| 46 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9996258894250888 | 0      |
| 47 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Unknown    | N/A                | N/A    |
| 48 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.999713250294665  | 0      |
| 49 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 50 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9998967939779262 | 0      |
| 51 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 52 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995165387505925 | 0      |
| 53 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995942748588265 | 0      |
| 54 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Removed  | Done       | 0.9995158156475569 | 0      |
| 55 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995940501913422 | 0      |
| 56 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995968512459322 | 0      |
| 57 | Tensor<[12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Unknown  | Unknown    | N/A                | N/A    |
| 58 | Tensor<[12, 1, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Unknown    | N/A                | N/A    |
| 59 | Tensor<[12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Unknown  | Unknown    | N/A                | N/A    |
| 60 | Tensor<[12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 61 | Tensor<[12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 62 | Tensor<[12, 1, s2 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 63 | Tensor<[12, 1, s4 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 64 | Tensor<[12, 1, s6 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 65 | Tensor<[12, 1, s8 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Unknown    | N/A                | N/A    |
| 66 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9995920502927521 | 0      |
| 67 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996278594630797 | 0      |
| 68 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Done       | 0.9996506816971684 | 0      |
| 69 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 70 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9996068220792248 | 0      |
| 71 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996109853515098 | 0      |
| 72 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996077785453986 | 0      |
| 73 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Done     | Done       | 0.9995623937960293 | 0      |
| 74 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996084326357151 | 0      |
| 75 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996081990265843 | 0      |
| 76 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999604510112581  | 0      |
| 77 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996048065105618 | 0      |
| 78 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996033684021512 | 0      |
| 79 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996041678637647 | 0      |
| 80 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996095309995997 | 0      |
| 81 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996099239970794 | 0      |
| 82 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999606315343055  | 0      |
| 83 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999604732222298  | 0      |
| 84 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.999598496928906  | 0      |
| 85 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995865730837851 | 0      |
| 86 | Tensor<[8, 16, 384, 384]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Removed  | Unknown    | N/A                | N/A    |
| 87 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995854525866468 | 0      |

