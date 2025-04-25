### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True           | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True           | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True         | Unknown  | Done       | 0.9999999943385127 | 0      |
|  4 | Tensor<[1, 10, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 10, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 0.9999973086913315 | 0      |
|  6 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999960012533357 | 0      |
|  7 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963069112586 | 0      |
|  8 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True     | Done     | Done       | 0.9999960483432822 | 0      |
|  9 | Tensor<[1, 1024, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999967402089904 | 0      |
| 10 | Tensor<[1, 104, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996314679218  | 0      |
| 11 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999952318469046 | 0      |
| 12 | Tensor<[1, 120, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996389610142  | 0      |
| 13 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999951359023356 | 0      |
| 14 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999947244889759 | 0      |
| 15 | Tensor<[1, 120, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999958835538195 | 0      |
| 16 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999962473507793 | 0      |
| 17 | Tensor<[1, 1280, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999958549201565 | 0      |
| 18 | Tensor<[1, 1280, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999995276208621  | 0      |
| 19 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999961612936012 | 0      |
| 20 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963294594538 | 0      |
| 21 | Tensor<[1, 1280, 9, 9]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999962060946548 | 0      |
| 22 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999961695404428 | 0      |
| 23 | Tensor<[1, 144, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999953777401727 | 0      |
| 24 | Tensor<[1, 144, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999963742361624 | 0      |
| 25 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 0.9999999998786848 | 0      |
| 26 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999956407777392 | 0      |
| 27 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999968142611411 | 0      |
| 28 | Tensor<[1, 16, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999938936386447 | 0      |
| 29 | Tensor<[1, 1664, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999962815105742 | 0      |
| 30 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999958505221627 | 0      |
| 31 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1]                                  | Done     | Done       | 0.9999979611588498 | 0      |
| 32 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963073555034 | 0      |
| 33 | Tensor<[1, 2048, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999960660721782 | 0      |
| 34 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999959268703352 | 0      |
| 35 | Tensor<[1, 208, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999954692774858 | 0      |
| 36 | Tensor<[1, 216, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999960772188518 | 0      |
| 37 | Tensor<[1, 2208, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999961258452442 | 0      |
| 38 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999963691037562 | 0      |
| 39 | Tensor<[1, 232, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999967396679875 | 0      |
| 40 | Tensor<[1, 240, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999964961148013 | 0      |
| 41 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963551627373 | 0      |
| 42 | Tensor<[1, 256, 512]> self = ?,<br>Optional[List[int]] dim = [1]                                  | Done     | Unknown    | N/A                | N/A    |
| 43 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999956077500541 | 0      |
| 44 | Tensor<[1, 288, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999965322266303 | 0      |
| 45 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999954298003617 | 0      |
| 46 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963965631605 | 0      |
| 47 | Tensor<[1, 320, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999970401401191 | 0      |
| 48 | Tensor<[1, 336, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999955428145747 | 0      |
| 49 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999961245859467 | 0      |
| 50 | Tensor<[1, 400, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999970971737029 | 0      |
| 51 | Tensor<[1, 440, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999962589446687 | 0      |
| 52 | Tensor<[1, 448, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999953507946956 | 0      |
| 53 | Tensor<[1, 48, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999957585267466 | 0      |
| 54 | Tensor<[1, 480, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999961457012945 | 0      |
| 55 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999959549220008 | 0      |
| 56 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999957610377787 | 0      |
| 57 | Tensor<[1, 480, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999957117003966 | 0      |
| 58 | Tensor<[1, 512, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999966711186237 | 0      |
| 59 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999953108377823 | 0      |
| 60 | Tensor<[1, 528, 96, 96]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999956620985789 | 0      |
| 61 | Tensor<[1, 576, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999958752806166 | 0      |
| 62 | Tensor<[1, 576, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999961645404782 | 0      |
| 63 | Tensor<[1, 64, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999980470494876 | 0      |
| 64 | Tensor<[1, 672, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999957067675115 | 0      |
| 65 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999966761272084 | 0      |
| 66 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999963300537875 | 0      |
| 67 | Tensor<[1, 672, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999965266909612 | 0      |
| 68 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999966504197786 | 0      |
| 69 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True      | Done     | Done       | 0.9999961221334543 | 0      |
| 70 | Tensor<[1, 696, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999964456818438 | 0      |
| 71 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999981147122997 | 0      |
| 72 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True     | Done     | Done       | 0.9999956100771678 | 0      |
| 73 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999953229026907 | 0      |
| 74 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.99999690133179   | 0      |
| 75 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999953529057958 | 0      |
| 76 | Tensor<[1, 768, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999962632129304 | 0      |
| 77 | Tensor<[1, 768, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.999996161392116  | 0      |
| 78 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999969862193137 | 0      |
| 79 | Tensor<[1, 784, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999963885645816 | 0      |
| 80 | Tensor<[1, 888, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999960102762955 | 0      |
| 81 | Tensor<[1, 896, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999963648688851 | 0      |
| 82 | Tensor<[1, 912, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999957912324914 | 0      |
| 83 | Tensor<[1, 96, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999966201629751 | 0      |
| 84 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999971579723446 | 0      |
| 85 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True      | Done     | Done       | 0.9999965930428072 | 0      |

