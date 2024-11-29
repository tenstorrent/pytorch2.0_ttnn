### aten.stack.default
|    | ATen Input Variations                                                                                                                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[0, 1]>, <[0, 1]>, <[0, 1]>, <[0, 1]>],<br>int dim = 2                                                                      | Unknown  | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[0, 2]>, <[0, 2]>],<br>int dim = 2                                                                                          | Unknown  | Fallback   | True  |
|  2 | List[Tensor] tensors = [<[0]>, <[0]>, <[0]>, <[0]>],<br>int dim = 1                                                                                  | Unknown  | Fallback   | True  |
|  3 | List[Tensor] tensors = [<[1, 1, 16, 16]>, <[1, 1, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Fallback   | True  |
|  4 | List[Tensor] tensors = [<[1, 23, 40, 64]>, <[1, 23, 40, 64]>],<br>int dim = 4                                                                        | None     | Fallback   | True  |
|  5 | List[Tensor] tensors = [<[1, 5, 16, 16]>, <[1, 5, 16, 16]>],<br>int dim = -1                                                                         | Unknown  | Fallback   | True  |
|  6 | List[Tensor] tensors = [<[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>, <[100, 1, 256]>]                        | None     | Fallback   | True  |
|  7 | List[Tensor] tensors = [<[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>, <[100]>],<br>int dim = -1 | Unknown  | Fallback   | True  |
|  8 | List[Tensor] tensors = [<[12, 16]>, <[12, 16]>],<br>int dim = -1                                                                                     | None     | Fallback   | True  |
|  9 | List[Tensor] tensors = [<[12]>, <[12]>, <[12]>, <[12]>],<br>int dim = 1                                                                              | Unknown  | Fallback   | True  |
| 10 | List[Tensor] tensors = [<[13600]>, <[13600]>, <[13600]>, <[13600]>],<br>int dim = 1                                                                  | Unknown  | Fallback   | True  |
| 11 | List[Tensor] tensors = [<[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>, <[1444]>],<br>int dim = -1                             | Unknown  | Fallback   | True  |
| 12 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                         | Unknown  | Fallback   | True  |
| 13 | List[Tensor] tensors = [<[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>, <[1]>],<br>int dim = -1                                                     | Unknown  | Fallback   | True  |
| 14 | List[Tensor] tensors = [<[221]>, <[221]>, <[221]>, <[221]>],<br>int dim = 1                                                                          | Unknown  | Fallback   | True  |
| 15 | List[Tensor] tensors = [<[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>, <[25]>],<br>int dim = -1             | Unknown  | Fallback   | True  |
| 16 | List[Tensor] tensors = [<[300]>, <[300]>, <[300]>, <[300]>],<br>int dim = 1                                                                          | Unknown  | Fallback   | True  |
| 17 | List[Tensor] tensors = [<[3234, 1]>, <[3234, 1]>, <[3234, 1]>, <[3234, 1]>],<br>int dim = 2                                                          | Unknown  | Fallback   | True  |
| 18 | List[Tensor] tensors = [<[3234, 2]>, <[3234, 2]>],<br>int dim = 2                                                                                    | Unknown  | Fallback   | True  |
| 19 | List[Tensor] tensors = [<[3400]>, <[3400]>, <[3400]>, <[3400]>],<br>int dim = 1                                                                      | Unknown  | Fallback   | True  |
| 20 | List[Tensor] tensors = [<[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>, <[361]>],<br>int dim = -1 | Unknown  | Fallback   | True  |
| 21 | List[Tensor] tensors = [<[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>, <[400]>],<br>int dim = -1 | Unknown  | Fallback   | True  |
| 22 | List[Tensor] tensors = [<[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>, <[4]>],<br>int dim = -1                         | Unknown  | Fallback   | True  |
| 23 | List[Tensor] tensors = [<[63]>, <[63]>, <[63]>, <[63]>],<br>int dim = 1                                                                              | Unknown  | Fallback   | True  |
| 24 | List[Tensor] tensors = [<[850]>, <[850]>, <[850]>, <[850]>],<br>int dim = 1                                                                          | Unknown  | Fallback   | True  |
| 25 | List[Tensor] tensors = [<[8732, 1]>, <[8732, 1]>, <[8732, 1]>, <[8732, 1]>],<br>int dim = 2                                                          | Unknown  | Fallback   | True  |
| 26 | List[Tensor] tensors = [<[8732, 2]>, <[8732, 2]>],<br>int dim = 2                                                                                    | Unknown  | Fallback   | True  |
| 27 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                         | Unknown  | Fallback   | True  |
| 28 | List[Tensor] tensors = [<[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>, <[9]>],<br>int dim = -1                                                     | Unknown  | Fallback   | True  |

