### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[0, 1]>, <[0, 1]>, <[0, 1]>, <[0, 1]>],<br>int dim = 2                                                                      | Unknown  | Fallback   |     1 |     -1 |
|  1 | List[Tensor] tensors = [<[0, 2]>, <[0, 2]>],<br>int dim = 2                                                                                          | Unknown  | Fallback   |     1 |     -1 |
|  2 | List[Tensor] tensors = [<[0]>, <[0]>, <[0]>, <[0]>],<br>int dim = 1                                                                                  | Unknown  | Fallback   |     1 |     -1 |
|  3 | List[Tensor] tensors = [<[1, 1, 16, 16]>, <[1, 1, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Fallback   |     1 |     -1 |
|  4 | List[Tensor] tensors = [<[1, 23, 40, 64]>, <[1, 23, 40, 64]>],<br>int dim = 4                                                                        | None     | Fallback   |     1 |     -1 |
|  5 | List[Tensor] tensors = [<[1, 5, 16, 16]>, <[1, 5, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Fallback   |     1 |     -1 |
|  6 | List[Tensor] tensors = [<[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>]                        | None     | Fallback   |     1 |     -1 |
|  7 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Unknown  | Fallback   |     1 |     -1 |
|  8 | List[Tensor] tensors = [<[12, 16]>, <[12, 16]>],<br>int dim = -1                                                                                     | Removed  | Fallback   |     1 |     -1 |
|  9 | List[Tensor] tensors = [<[12]>, <[12]>, <[12]>, <[12]>],<br>int dim = 1                                                                              | Unknown  | Fallback   |     1 |     -1 |
| 10 | List[Tensor] tensors = [<[13600]>, <[13600]>, <[13600]>, <[13600]>],<br>int dim = 1                                                                  | Unknown  | Fallback   |     1 |     -1 |
| 11 | List[Tensor] tensors = [<[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>],<br>int dim = -1                             | Unknown  | Fallback   |     1 |     -1 |
| 12 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Unknown  | Fallback   |     1 |     -1 |
| 13 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                                                     | Unknown  | Fallback   |     1 |     -1 |
| 14 | List[Tensor] tensors = [<[221]>, <[221]>, <[221]>, <[221]>],<br>int dim = 1                                                                          | Unknown  | Fallback   |     1 |     -1 |
| 15 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Unknown  | Fallback   |     1 |     -1 |
| 16 | List[Tensor] tensors = [<[300]>, <[300]>, <[300]>, <[300]>],<br>int dim = 1                                                                          | Unknown  | Fallback   |     1 |     -1 |
| 17 | List[Tensor] tensors = [<[3234, 1]>, <[3234, 1]>, <[3234, 1]>, <[3234, 1]>],<br>int dim = 2                                                          | Unknown  | Fallback   |     1 |     -1 |
| 18 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = 2                                                                                    | Unknown  | Fallback   |     1 |     -1 |
| 19 | List[Tensor] tensors = [<[3400]>, <[3400]>, <[3400]>, <[3400]>],<br>int dim = 1                                                                      | Unknown  | Fallback   |     1 |     -1 |
| 20 | List[Tensor] tensors = [<[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>],<br>int dim = -1 | Unknown  | Fallback   |     1 |     -1 |
| 21 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Unknown  | Fallback   |     1 |     -1 |
| 22 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Unknown  | Fallback   |     1 |     -1 |
| 23 | List[Tensor] tensors = [<[63]>, <[63]>, <[63]>, <[63]>],<br>int dim = 1                                                                              | Unknown  | Fallback   |     1 |     -1 |
| 24 | List[Tensor] tensors = [<[850]>, <[850]>, <[850]>, <[850]>],<br>int dim = 1                                                                          | Unknown  | Fallback   |     1 |     -1 |
| 25 | List[Tensor] tensors = [<[8732, 1]>, <[8732, 1]>, <[8732, 1]>, <[8732, 1]>],<br>int dim = 2                                                          | Unknown  | Fallback   |     1 |     -1 |
| 26 | List[Tensor] tensors = [<[8732, 2]>, <[8732, 2]>],<br>int dim = 2                                                                                    | Unknown  | Fallback   |     1 |     -1 |
| 27 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Unknown  | Fallback   |     1 |     -1 |
| 28 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                                                     | Unknown  | Fallback   |     1 |     -1 |

