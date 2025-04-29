### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995940823191904 | -1     |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Done       | 0.9995923073932014 | -1     |
|  2 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False              | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9997481365989298 | -1     |
|  4 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | -1     |
|  5 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995944294747235 | -1     |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.999535917755612  | -1     |
|  7 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996301334997931 | -1     |
| 10 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996810624575575 | -1     |
| 11 | Tensor<[1, 12, 14, 14]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996547377914653 | -1     |
| 12 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999622472469699  | -1     |
| 13 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995897411137767 | -1     |
| 14 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996153417952168 | -1     |
| 15 | Tensor<[1, 12, 257, 257]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996165798647788 | -1     |
| 17 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996381271834078 | -1     |
| 18 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996295020784567 | -1     |
| 19 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9997066190272254 | -1     |
| 20 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | -1     |
| 21 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994709116897559 | -1     |
| 22 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994476573191226 | -1     |
| 23 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9995819287635224 | -1     |
| 26 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995932975549049 | -1     |
| 27 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996066070335494 | -1     |
| 28 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.999580199610545  | -1     |
| 29 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996238988045469 | -1     |
| 30 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995946357338549 | -1     |
| 31 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Done       | 0.9995930127026001 | -1     |
| 32 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996089704211526 | -1     |
| 33 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995985188888952 | -1     |
| 34 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995631337247128 | -1     |
| 35 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995949758374507 | -1     |
| 36 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996161782782876 | -1     |
| 37 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995969712785591 | -1     |
| 38 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Done       | 0.9995869271186968 | -1     |
| 39 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996550812531834 | -1     |
| 40 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9994661420468245 | -1     |
| 41 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | -1     |
| 42 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9995285967647283 | -1     |
| 43 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 44 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995922818212657 | -1     |
| 45 | Tensor<[1, 64, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Done     | Done       | 0.9996153308981565 | -1     |
| 46 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996093731601781 | -1     |
| 47 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 1.0                | -1     |
| 48 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9991710762280672 | -1     |
| 49 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 50 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996560072670619 | -1     |
| 51 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999595150666714  | -1     |
| 52 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995353068852767 | -1     |
| 53 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9995995861451578 | -1     |
| 54 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9995991046300072 | -1     |
| 55 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9995615407992215 | -1     |
| 56 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996044175726144 | -1     |
| 57 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Done       | 0.9996471421063059 | -1     |
| 58 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 59 | Tensor<[16, 19, 19]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Done     | Done       | 0.9996231203197028 | -1     |
| 60 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Done       | 0.9996124363870721 | -1     |
| 61 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996106294210623 | -1     |
| 62 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996048987622741 | -1     |
| 63 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False          | Done     | Done       | 0.9996216617309029 | -1     |
| 64 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996058283092584 | -1     |
| 65 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996067481174934 | -1     |
| 66 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995999514270494 | -1     |
| 67 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9995992542750112 | -1     |
| 68 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996007535755072 | -1     |
| 69 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996131064908081 | -1     |
| 70 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996069409588692 | -1     |
| 71 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996086850821894 | -1     |
| 72 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.999609988139555  | -1     |
| 73 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | Done       | 0.9996095673848399 | -1     |
| 74 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995736040120117 | -1     |
| 75 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995799608087916 | -1     |
| 76 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9995796474912159 | -1     |

