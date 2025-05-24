### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995911123587566 | 0      |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False              | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995218680697651 | 0      |
|  3 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996492778418861 | 0      |
|  5 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995551309832266 | 0      |
|  6 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996323999446273 | 0      |
|  9 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.999640428036015  | 0      |
| 10 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996494001210244 | 0      |
| 11 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995677393763579 | 0      |
| 12 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995894684730797 | 0      |
| 13 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Removed  | Done       | 0.9996539856426249 | 0      |
| 14 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996004325695377 | 0      |
| 15 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9996577875256151 | 0      |
| 16 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9997214920522342 | 0      |
| 17 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
| 18 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995840364187301 | 0      |
| 19 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996881043881692 | 0      |
| 20 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9995792167688434 | 0      |
| 23 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996055718052355 | 0      |
| 24 | Tensor<[1, 16, 384, 384]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Removed  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996378567884476 | 0      |
| 26 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9996038158416894 | 0      |
| 27 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995916262041076 | 0      |
| 28 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996055290082383 | 0      |
| 29 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996046066083741 | 0      |
| 30 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995656789444244 | 0      |
| 31 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996039990831419 | 0      |
| 32 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996125798073257 | 0      |
| 33 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995940737107885 | 0      |
| 34 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Removed  | Done       | 0.9996351492006055 | 0      |
| 35 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996538703944349 | 0      |
| 36 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | 0      |
| 37 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9993378138080798 | 0      |
| 38 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 39 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996835964701707 | 0      |
| 40 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999595487430376  | 0      |
| 41 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Removed  | Done       | 0.9995230073948993 | 0      |
| 42 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995961654749698 | 0      |
| 43 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996161192026594 | 0      |
| 44 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Done       | 0.9995913022702289 | 0      |
| 45 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 46 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9996044694045335 | 0      |
| 47 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996091153470459 | 0      |
| 48 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996105659337324 | 0      |
| 49 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Done     | Done       | 0.9996586322162517 | 0      |
| 50 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995970942303362 | 0      |
| 51 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999609149851231  | 0      |
| 52 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996039627614918 | 0      |
| 53 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996043101624367 | 0      |
| 54 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996132618135057 | 0      |
| 55 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996084891153856 | 0      |
| 56 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996013477414063 | 0      |
| 57 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996071906699326 | 0      |
| 58 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996055982178864 | 0      |
| 59 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996100582994268 | 0      |

