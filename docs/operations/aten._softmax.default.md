### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 16384, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999590859850558  | 0      |
|  1 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.9995923365449315 | 0      |
|  2 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False             | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996194679557745 | 0      |
|  4 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996347088899625 | 0      |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996306915444565 | 0      |
|  7 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9996263417438201 | 0      |
|  9 | Tensor<[1, 12, 201, 201]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9995915392500773 | 0      |
| 11 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996676850143346 | 0      |
| 12 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | 0      |
| 13 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996702765588044 | 0      |
| 14 | Tensor<[1, 16, 1, 6]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996064211210685 | 0      |
| 15 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9996542735165347 | 0      |
| 17 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996201180130945 | 0      |
| 18 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996049366152029 | 0      |
| 19 | Tensor<[1, 2, 4096, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995958192412465 | 0      |
| 20 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995916560860532 | 0      |
| 21 | Tensor<[1, 24, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996001313494212 | 0      |
| 22 | Tensor<[1, 24, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996212213974863 | 0      |
| 23 | Tensor<[1, 32, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996051947957444 | 0      |
| 24 | Tensor<[1, 32, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996028439525925 | 0      |
| 25 | Tensor<[1, 5, 1024, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995905769707857 | 0      |
| 26 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999596816069555  | 0      |
| 27 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9997535970940763 | 0      |
| 28 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
| 29 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996436881039042 | 0      |
| 30 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 31 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996360083699752 | 0      |
| 32 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996052808156428 | 0      |
| 33 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 1.0                | 0      |
| 34 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.99960445980549   | 0      |
| 35 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Unknown  | Unknown    | N/A                | N/A    |
| 36 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.999664980188939  | 0      |
| 37 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999593797498904  | 0      |
| 38 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.9995243487856813 | 0      |
| 39 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995817845517851 | 0      |
| 40 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.9995970896039388 | 0      |
| 41 | Tensor<[12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Unknown    | N/A                | N/A    |
| 42 | Tensor<[12, 1, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False        | Unknown  | Unknown    | N/A                | N/A    |
| 43 | Tensor<[12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False         | Unknown  | Unknown    | N/A                | N/A    |
| 44 | Tensor<[12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 45 | Tensor<[12, 1, s12 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Unknown    | N/A                | N/A    |
| 46 | Tensor<[12, 1, s2 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 47 | Tensor<[12, 1, s4 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 48 | Tensor<[12, 1, s6 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 49 | Tensor<[12, 1, s8 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Unknown    | N/A                | N/A    |
| 50 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False       | Unknown  | Done       | 0.9996158565407528 | 0      |
| 51 | Tensor<[16, 6, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996152178576013 | 0      |
| 52 | Tensor<[16, 6, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996078152363934 | 0      |
| 53 | Tensor<[16, 8, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996044623499182 | 0      |
| 54 | Tensor<[16, 8, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996063073979926 | 0      |
| 55 | Tensor<[4, 12, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996038414886995 | 0      |
| 56 | Tensor<[4, 12, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996043622338983 | 0      |
| 57 | Tensor<[4, 16, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996035121480559 | 0      |
| 58 | Tensor<[4, 16, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996082609646957 | 0      |
| 59 | Tensor<[64, 3, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996068759190907 | 0      |
| 60 | Tensor<[64, 3, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996053930351789 | 0      |
| 61 | Tensor<[64, 4, 49, 49]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996010780246662 | 0      |
| 62 | Tensor<[64, 4, 64, 64]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.9996083842657006 | 0      |
| 63 | Tensor<[8, 100, 100]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Done     | Done       | 0.9995747380885364 | 0      |
| 64 | Tensor<[8, 100, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Done     | Done       | 0.9995894527356797 | 0      |
| 65 | Tensor<[8, 920, 920]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Done     | Done       | 0.9995859648792744 | 0      |

