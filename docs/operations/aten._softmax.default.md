### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995952448482348 | 0      |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995956320325505 | 0      |
|  2 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9997216520485389 | 0      |
|  4 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994400259935419 | 0      |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996696569997894 | 0      |
|  7 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996474870380884 | 0      |
| 10 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9997021682238129 | 0      |
| 11 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996100978679725 | 0      |
| 12 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996077376638378 | 0      |
| 13 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995851243193461 | 0      |
| 14 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995794973265706 | 0      |
| 15 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996030792481101 | 0      |
| 16 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996932918858498 | 0      |
| 17 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995934668894775 | 0      |
| 18 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996201231576003 | 0      |
| 19 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995666996026835 | 0      |
| 21 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996929338746177 | 0      |
| 22 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9995847382958131 | 0      |
| 25 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995857752597607 | 0      |
| 26 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995917190175739 | 0      |
| 27 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996134330504346 | 0      |
| 28 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996384185663771 | 0      |
| 29 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996901596636235 | 0      |
| 30 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995936550589795 | 0      |
| 31 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995931771310298 | 0      |
| 32 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996221193568223 | 0      |
| 33 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999601558939867  | 0      |
| 34 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995605067860233 | 0      |
| 35 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996117445847683 | 0      |
| 36 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996123707242127 | 0      |
| 37 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995933408620598 | 0      |
| 38 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999597430624479  | 0      |
| 39 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995162498418185 | 0      |
| 40 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9997783130723725 | 0      |
| 41 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 42 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9998874345410841 | 0      |
| 43 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 44 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996220922991087 | 0      |
| 45 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.999621304785548  | 0      |
| 46 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9993670173706437 | 0      |
| 47 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 48 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9994938312599468 | 0      |
| 49 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 50 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996073074813497 | 0      |
| 51 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999592347204346  | 0      |
| 52 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995372944878871 | 0      |
| 53 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995920085307656 | 0      |
| 54 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995954862376729 | 0      |
| 55 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996214637942396 | 0      |
| 56 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996025557092971 | 0      |
| 57 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Done       | 0.9995562412798265 | 0      |
| 58 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 59 | Tensor<[16, 19, 19]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996272594862875 | 0      |
| 60 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9995886568444501 | 0      |
| 61 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999599877312954  | 0      |
| 62 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996064013155318 | 0      |
| 63 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Done     | Done       | 0.999669421918507  | 0      |
| 64 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996110315769314 | 0      |
| 65 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996011586731212 | 0      |
| 66 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996038281176434 | 0      |
| 67 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996114327735666 | 0      |
| 68 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996051968645498 | 0      |
| 69 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996012126816872 | 0      |
| 70 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996120849967772 | 0      |
| 71 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999607281368595  | 0      |
| 72 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996070280807976 | 0      |
| 73 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996074056207018 | 0      |
| 74 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995892437470538 | 0      |
| 75 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9995866498199377 | 0      |
| 76 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.999586875662944  | 0      |

