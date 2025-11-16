### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 16, 16]>, <[1, 1, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 23, 40, 64]>, <[1, 23, 40, 64]>],<br>int dim = 4                                                                        | Done     | Done       | 1.0   | 0      |
|  2 | List[Tensor] tensors = [<[1, 5, 16, 16]>, <[1, 5, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>]                        | Done     | Done       | 1.0   | 0      |
|  4 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
|  5 | List[Tensor] tensors = [<[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>],<br>int dim = -1                             | Done     | Done       | 1.0   | 0      |
|  6 | List[Tensor] tensors = [<[16, 1]>, <[16, 1]>]                                                                                                        | Done     | Unknown    | N/A   | N/A    |
|  7 | List[Tensor] tensors = [<[16384]>, <[16384]>],<br>int dim = -1                                                                                       | Done     | Unknown    | N/A   | N/A    |
|  8 | List[Tensor] tensors = [<[16]>, <[16]>]                                                                                                              | Done     | Unknown    | N/A   | N/A    |
|  9 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Done     | Done       | 1.0   | 0      |
| 10 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                                                     | Done     | Done       | 1.0   | 0      |
| 11 | List[Tensor] tensors = [<[200]>, <[200]>, <[200]>, <[200]>],<br>int dim = 1                                                                          | Done     | Unknown    | N/A   | N/A    |
| 12 | List[Tensor] tensors = [<[22]>]                                                                                                                      | Unknown  | Unknown    | N/A   | N/A    |
| 13 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Done     | Done       | 1.0   | 0      |
| 14 | List[Tensor] tensors = [<[300]>, <[300]>, <[300]>, <[300]>],<br>int dim = 1                                                                          | Done     | Unknown    | N/A   | N/A    |
| 15 | List[Tensor] tensors = [<[32, 1]>, <[32, 1]>]                                                                                                        | Done     | Unknown    | N/A   | N/A    |
| 16 | List[Tensor] tensors = [<[3234, 1]>, <[3234, 1]>, <[3234, 1]>, <[3234, 1]>],<br>int dim = 2                                                          | Done     | Unknown    | N/A   | N/A    |
| 17 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = 2                                                                                    | Done     | Unknown    | N/A   | N/A    |
| 18 | List[Tensor] tensors = [<[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>],<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
| 19 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
| 20 | List[Tensor] tensors = [<[42]>, <[42]>]                                                                                                              | Done     | Unknown    | N/A   | N/A    |
| 21 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Done     | Done       | 1.0   | 0      |
| 22 | List[Tensor] tensors = [<[8732, 1]>, <[8732, 1]>, <[8732, 1]>, <[8732, 1]>],<br>int dim = 2                                                          | Done     | Unknown    | N/A   | N/A    |
| 23 | List[Tensor] tensors = [<[8732, 2]>, <[8732, 2]>],<br>int dim = 2                                                                                    | Done     | Unknown    | N/A   | N/A    |
| 24 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Done     | Done       | 1.0   | 0      |
| 25 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                                                     | Done     | Done       | 1.0   | 0      |
| 26 | List[Tensor] tensors = [_folded_expand, _folded_expand_1],<br>int dim = -1                                                                           | Unknown  | Unknown    | N/A   | N/A    |

