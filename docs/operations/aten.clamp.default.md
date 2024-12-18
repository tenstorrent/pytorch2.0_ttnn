### aten.clamp.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[0, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356     | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1066                  | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 800                   | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 82             | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 49             | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1066]> self = ?,<br>Optional[number] min = 0.0                                                | Unknown  | Fallback   |     1 |     -1 |
|  6 | Tensor<[1066]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 639                   | Unknown  | Fallback   |     1 |     -1 |
|  7 | Tensor<[12, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[120]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
|  9 | Tensor<[120]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 59                     | Removed  | Fallback   |     1 |     -1 |
| 10 | Tensor<[128]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
| 11 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 127                    | Removed  | Fallback   |     1 |     -1 |
| 12 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 15                     | Removed  | Fallback   |     1 |     -1 |
| 13 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 31                     | Removed  | Fallback   |     1 |     -1 |
| 14 | Tensor<[128]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 63                     | Removed  | Fallback   |     1 |     -1 |
| 15 | Tensor<[16, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | Fallback   |     1 |     -1 |
| 16 | Tensor<[160]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
| 17 | Tensor<[160]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 79                     | Removed  | Fallback   |     1 |     -1 |
| 18 | Tensor<[24, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | Fallback   |     1 |     -1 |
| 19 | Tensor<[240]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
| 20 | Tensor<[240]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 119                    | Removed  | Fallback   |     1 |     -1 |
| 21 | Tensor<[3, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | Fallback   |     1 |     -1 |
| 22 | Tensor<[300]> self = ?,<br>Optional[number] min = 0.0                                                 | Unknown  | Fallback   |     1 |     -1 |
| 23 | Tensor<[300]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 479                    | Unknown  | Fallback   |     1 |     -1 |
| 24 | Tensor<[300]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 639                    | Unknown  | Fallback   |     1 |     -1 |
| 25 | Tensor<[30]> self = ?,<br>Optional[number] min = 0.0                                                  | Removed  | Fallback   |     1 |     -1 |
| 26 | Tensor<[30]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 14                      | Removed  | Fallback   |     1 |     -1 |
| 27 | Tensor<[32, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092 | None     | Fallback   |     1 |     -1 |
| 28 | Tensor<[320]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
| 29 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 159                    | Removed  | Fallback   |     1 |     -1 |
| 30 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 319                    | Unknown  | Fallback   |     1 |     -1 |
| 31 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 479                    | Unknown  | Fallback   |     1 |     -1 |
| 32 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 639                    | Unknown  | Fallback   |     1 |     -1 |
| 33 | Tensor<[3234, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356  | Unknown  | Fallback   |     1 |     -1 |
| 34 | Tensor<[3234, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 320                | Unknown  | Done       |     1 |      0 |
| 35 | Tensor<[4, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | Fallback   |     1 |     -1 |
| 36 | Tensor<[4, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                     | Done     | Done       |     1 |      0 |
| 37 | Tensor<[40]> self = ?,<br>Optional[number] min = 0.0                                                  | Removed  | Fallback   |     1 |     -1 |
| 38 | Tensor<[40]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 19                      | Removed  | Fallback   |     1 |     -1 |
| 39 | Tensor<[480]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
| 40 | Tensor<[480]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 239                    | Removed  | Fallback   |     1 |     -1 |
| 41 | Tensor<[6, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | Fallback   |     1 |     -1 |
| 42 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                     | Done     | Done       |     1 |      0 |
| 43 | Tensor<[60]> self = ?,<br>Optional[number] min = 0.0                                                  | Removed  | Fallback   |     1 |     -1 |
| 44 | Tensor<[60]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 29                      | Removed  | Fallback   |     1 |     -1 |
| 45 | Tensor<[640]> self = ?,<br>Optional[number] min = 0.0                                                 | Removed  | Fallback   |     1 |     -1 |
| 46 | Tensor<[640]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 319                    | Removed  | Fallback   |     1 |     -1 |
| 47 | Tensor<[8, 1, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.605170185988092  | None     | Fallback   |     1 |     -1 |
| 48 | Tensor<[800]> self = ?,<br>Optional[number] min = 0.0                                                 | Unknown  | Fallback   |     1 |     -1 |
| 49 | Tensor<[800]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 479                    | Unknown  | Fallback   |     1 |     -1 |
| 50 | Tensor<[80]> self = ?,<br>Optional[number] min = 0.0                                                  | Removed  | Fallback   |     1 |     -1 |
| 51 | Tensor<[80]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 39                      | Removed  | Fallback   |     1 |     -1 |
| 52 | Tensor<[8732, 1]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 4.135166556742356  | Unknown  | Fallback   |     1 |     -1 |
| 53 | Tensor<[8732, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 300                | Unknown  | Done       |     1 |      0 |

