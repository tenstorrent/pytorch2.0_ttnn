### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 16, 16]>, <[1, 1, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Done       | 1.0   | -1     |
|  1 | List[Tensor] tensors = [<[1, 23, 40, 64]>, <[1, 23, 40, 64]>],<br>int dim = 4                                                                        | Unknown  | Done       | 1.0   | -1     |
|  2 | List[Tensor] tensors = [<[1, 5, 16, 16]>, <[1, 5, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Done       | 1.0   | -1     |
|  3 | List[Tensor] tensors = [<[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>]                        | Unknown  | Done       | 1.0   | -1     |
|  4 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Done     | Done       | 1.0   | -1     |
|  5 | List[Tensor] tensors = [<[12, 16]>, _folded_expand_1],<br>int dim = -1                                                                               | Done     | Unknown    | N/A   | N/A    |
|  6 | List[Tensor] tensors = [<[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>],<br>int dim = -1                             | Unknown  | Done       | 1.0   | -1     |
|  7 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Done     | Done       | 1.0   | -1     |
|  8 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                                                     | Unknown  | Done       | 1.0   | -1     |
|  9 | List[Tensor] tensors = [<[200]>, <[200]>, <[200]>, <[200]>],<br>int dim = 1                                                                          | Unknown  | Unknown    | N/A   | N/A    |
| 10 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Done     | Done       | 1.0   | -1     |
| 11 | List[Tensor] tensors = [<[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>],<br>int dim = -1 | Unknown  | Done       | 1.0   | -1     |
| 12 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Done     | Done       | 1.0   | -1     |
| 13 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Done     | Done       | 1.0   | -1     |
| 14 | List[Tensor] tensors = [<[8732, 1]>, <[8732, 1]>, <[8732, 1]>, <[8732, 1]>],<br>int dim = 2                                                          | Unknown  | Unknown    | N/A   | N/A    |
| 15 | List[Tensor] tensors = [<[8732, 2]>, <[8732, 2]>],<br>int dim = 2                                                                                    | Unknown  | Unknown    | N/A   | N/A    |
| 16 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Done     | Done       | 1.0   | -1     |
| 17 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                                                     | Unknown  | Done       | 1.0   | -1     |

