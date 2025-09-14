### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True           | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True           | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True         | Unknown  | Done       | 0.9999999986681035 | 0      |
|  4 | Tensor<[1, 10, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 0.9999999965891425 | 0      |
|  5 | Tensor<[1, 10, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 0.9999976521739878 | 0      |
|  6 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.999995740552091  | 0      |
|  7 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999964094634869 | 0      |
|  8 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True     | Done     | Done       | 0.9999966318515575 | 0      |
|  9 | Tensor<[1, 1024, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999965724811971 | 0      |
| 10 | Tensor<[1, 104, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999970891344223 | 0      |
| 11 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999951369257465 | 0      |
| 12 | Tensor<[1, 120, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999970017980424 | 0      |
| 13 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999938935603306 | 0      |
| 14 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999962779734631 | 0      |
| 15 | Tensor<[1, 120, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999966501726976 | 0      |
| 16 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999961586707357 | 0      |
| 17 | Tensor<[1, 1280, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999960405762062 | 0      |
| 18 | Tensor<[1, 1280, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999953966978996 | 0      |
| 19 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.999995876381589  | 0      |
| 20 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999965341182211 | 0      |
| 21 | Tensor<[1, 1280, 9, 9]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999960740101869 | 0      |
| 22 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999964272805676 | 0      |
| 23 | Tensor<[1, 144, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999981130313603 | 0      |
| 24 | Tensor<[1, 144, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999948733100883 | 0      |
| 25 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True          | Unknown  | Done       | 1.0                | 0      |
| 26 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999959679265972 | 0      |
| 27 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999967095221414 | 0      |
| 28 | Tensor<[1, 16, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999990235720059 | 0      |
| 29 | Tensor<[1, 1664, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963612913764 | 0      |
| 30 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999965534528326 | 0      |
| 31 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1]                                  | Done     | Done       | 0.9999979191887685 | 0      |
| 32 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963768039937 | 0      |
| 33 | Tensor<[1, 2048, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999957331958911 | 0      |
| 34 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999962480299768 | 0      |
| 35 | Tensor<[1, 208, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999971537767374 | 0      |
| 36 | Tensor<[1, 216, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999979794564327 | 0      |
| 37 | Tensor<[1, 2208, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999962901764137 | 0      |
| 38 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996446509853  | 0      |
| 39 | Tensor<[1, 232, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999963751123314 | 0      |
| 40 | Tensor<[1, 240, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999959310715282 | 0      |
| 41 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999962606070785 | 0      |
| 42 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999961669476553 | 0      |
| 43 | Tensor<[1, 288, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999955941106801 | 0      |
| 44 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999953873904734 | 0      |
| 45 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999961652470917 | 0      |
| 46 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True         | Unknown  | Unknown    | N/A                | N/A    |
| 47 | Tensor<[1, 320, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999954499551893 | 0      |
| 48 | Tensor<[1, 336, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999967849772732 | 0      |
| 49 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999965511349096 | 0      |
| 50 | Tensor<[1, 400, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999964478372919 | 0      |
| 51 | Tensor<[1, 440, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999966690322756 | 0      |
| 52 | Tensor<[1, 448, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999968041990952 | 0      |
| 53 | Tensor<[1, 48, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999954573983166 | 0      |
| 54 | Tensor<[1, 480, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996591564525  | 0      |
| 55 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999962154861115 | 0      |
| 56 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999958055841611 | 0      |
| 57 | Tensor<[1, 480, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996093151317  | 0      |
| 58 | Tensor<[1, 512, 256]> self = ?,<br>Optional[List[int]] dim = [2]                                  | Done     | Done       | 0.9999998244133573 | 0      |
| 59 | Tensor<[1, 512, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999961366760917 | 0      |
| 60 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999967195808773 | 0      |
| 61 | Tensor<[1, 528, 96, 96]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999994850432615  | 0      |
| 62 | Tensor<[1, 576, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999957353478194 | 0      |
| 63 | Tensor<[1, 576, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999967717897483 | 0      |
| 64 | Tensor<[1, 64, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999954959172311 | 0      |
| 65 | Tensor<[1, 672, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999960983908334 | 0      |
| 66 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999952728629812 | 0      |
| 67 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999961569543822 | 0      |
| 68 | Tensor<[1, 672, 20, 20]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999959683930192 | 0      |
| 69 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999958158711627 | 0      |
| 70 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True      | Done     | Done       | 0.999995965123556  | 0      |
| 71 | Tensor<[1, 696, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999963295293129 | 0      |
| 72 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999949208883139 | 0      |
| 73 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True     | Done     | Done       | 0.9999964584286392 | 0      |
| 74 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999963233482763 | 0      |
| 75 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999958128148887 | 0      |
| 76 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.9999953226079858 | 0      |
| 77 | Tensor<[1, 768, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True    | Done     | Done       | 0.9999963394467657 | 0      |
| 78 | Tensor<[1, 768, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999963678078561 | 0      |
| 79 | Tensor<[1, 768, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999964127804325 | 0      |
| 80 | Tensor<[1, 784, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999964587193771 | 0      |
| 81 | Tensor<[1, 888, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.999997034533576  | 0      |
| 82 | Tensor<[1, 896, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.9999966986187677 | 0      |
| 83 | Tensor<[1, 912, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999963490174809 | 0      |
| 84 | Tensor<[1, 96, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.9999970493675657 | 0      |
| 85 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True    | Done     | Done       | 0.9999957986425135 | 0      |
| 86 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True      | Done     | Done       | 0.9999958048662974 | 0      |
| 87 | Tensor<[4, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Unknown    | N/A                | N/A    |

