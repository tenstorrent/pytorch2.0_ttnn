### aten.sum.dim_IntList
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True      | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True           | None     | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1024, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True   | None     | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | None     | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 10]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True             | None     | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [1]                                 | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [2]                                 | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
|  8 | Tensor<[1, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True            | None     | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 12]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True             | None     | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 16384, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True  | None     | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 21843]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 256, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True    | None     | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 3]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True              | None     | Fallback   | 1.0   | -1     |
| 15 | Tensor<[1, 4096, 256]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True   | None     | Fallback   | 1.0   | -1     |
| 16 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
| 17 | Tensor<[1, 512, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
| 18 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True           | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True            | None     | Fallback   | 1.0   | -1     |
| 20 | Tensor<[1, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True             | None     | Fallback   | 1.0   | -1     |
| 21 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
| 22 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | None     | Fallback   | 1.0   | -1     |
| 23 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True  | None     | Fallback   | 1.0   | -1     |
| 24 | Tensor<[1, 768, 14, 14]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True | None     | Fallback   | 1.0   | -1     |
| 25 | Tensor<[1, 768, 384]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True    | None     | Fallback   | 1.0   | -1     |
| 26 | Tensor<[1, 784]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True            | None     | Fallback   | 1.0   | -1     |
| 27 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [2, 3],<br>bool keepdim = True   | None     | Fallback   | 1.0   | -1     |
| 28 | Tensor<[1024, 160]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 29 | Tensor<[1024, 640]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 30 | Tensor<[14, 2048]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 31 | Tensor<[14, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True           | None     | Fallback   | 1.0   | -1     |
| 32 | Tensor<[16384, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True        | None     | Fallback   | 1.0   | -1     |
| 33 | Tensor<[16384, 32]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 34 | Tensor<[16384, 3]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True          | None     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[16384, 4]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True          | None     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[196, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 37 | Tensor<[196, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 38 | Tensor<[197, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 39 | Tensor<[197, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 40 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True           | None     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True            | None     | Fallback   | 1.0   | -1     |
| 42 | Tensor<[2, 7, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 43 | Tensor<[256, 1024]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 44 | Tensor<[256, 160]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 45 | Tensor<[256, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 46 | Tensor<[256, 32]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True           | None     | Fallback   | 1.0   | -1     |
| 47 | Tensor<[256, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True           | None     | Fallback   | 1.0   | -1     |
| 48 | Tensor<[4096, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True         | None     | Fallback   | 1.0   | -1     |
| 49 | Tensor<[4096, 64]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 50 | Tensor<[50, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |
| 51 | Tensor<[50, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True           | None     | Fallback   | 1.0   | -1     |
| 52 | Tensor<[768, 196]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True          | None     | Fallback   | 1.0   | -1     |

