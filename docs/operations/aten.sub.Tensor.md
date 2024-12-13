### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Done       | 1.0                 | 0      |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | None     | Fallback   | 1.0                 | -1     |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | None     | Fallback   | 1.0                 | -1     |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                  | Removed  | Fallback   | 1.0                 | -1     |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | None     | Fallback   | 1.0                 | -1     |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | None     | Fallback   | 1.0                 | -1     |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Removed  | Done       | 0.999997464111591   | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | None     | Fallback   | 1.0                 | -1     |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | None     | Fallback   | 1.0                 | -1     |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                  | Removed  | Fallback   | 1.0                 | -1     |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | None     | Fallback   | 1.0                 | -1     |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | None     | Fallback   | 1.0                 | -1     |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Removed  | Done       | 0.9999963845492877  | 0      |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.999997735274383   | 0      |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | None     | Done       | 0.43378842038553816 | 0      |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.9999982201086277  | 0      |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | None     | Done       | 0.8329000309584386  | 0      |
| 18 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.6943416581461275  | 0      |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 20 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999978600723755  | 0      |
| 21 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999982799384467  | 0      |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.5325932457519458  | 0      |
| 23 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | None     | Fallback   | 1.0                 | -1     |
| 24 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Fallback   | 1.0                 | -1     |
| 25 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999980050029409  | 0      |
| 26 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | None     | Fallback   | 1.0                 | -1     |
| 27 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | None     | Fallback   | 1.0                 | -1     |
| 28 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Fallback   | 1.0                 | -1     |
| 29 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999968309586927  | 0      |
| 30 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 31 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 32 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 33 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                         | Unknown  | Fallback   | 1.0                 | -1     |
| 34 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Unknown  | Done       | 0.9999979679359017  | 0      |
| 35 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Removed  | Done       | 0.9999983797855991  | 0      |
| 36 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 37 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Removed  | Done       | 0.9999976053464985  | 0      |
| 38 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 39 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Removed  | Done       | 0.9999974796651857  | 0      |
| 40 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.4556649916221338  | 0      |
| 41 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.4704505261436494  | 0      |
| 42 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 43 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Removed  | Done       | 0.9999983982911415  | 0      |
| 44 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | None     | Fallback   | 1.0                 | -1     |
| 45 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | None     | Done       | 0.6764065019869248  | 0      |
| 46 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Removed  | Done       | 0.9999983329699622  | 0      |
| 47 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 48 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999980469357446  | 0      |
| 49 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999979605989306  | 0      |
| 50 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Removed  | Done       | 0.9999983257276288  | 0      |
| 51 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Unknown  | Done       | 0.9999977869230698  | 0      |
| 52 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Fallback   | 1.0                 | -1     |
| 53 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Unknown  | Done       | 0.9999982486921309  | 0      |
| 54 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                           | Removed  | Fallback   | 1.0                 | -1     |
| 55 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Unknown  | Done       | 0.9999974966875278  | 0      |
| 56 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 57 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Removed  | Done       | 0.99999806719898    | 0      |
| 58 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | 0.99999807980141    | 0      |
| 59 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999981102519983  | 0      |
| 60 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | Done       | 0.9999982204019522  | 0      |
| 61 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.485894011716464   | 0      |
| 62 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.5065027928361661  | 0      |
| 63 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                           | Removed  | Fallback   | 1.0                 | -1     |
| 64 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Removed  | Done       | 0.9999995860849394  | 0      |
| 65 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Removed  | Done       | 0.9999984465306885  | 0      |
| 66 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 67 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Removed  | Done       | 0.9999987292256731  | 0      |
| 68 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                           | Removed  | Fallback   | 1.0                 | -1     |
| 69 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.3464460889325202  | 0      |
| 70 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.3517080218210681  | 0      |
| 71 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                          | Removed  | Fallback   | 1.0                 | -1     |
| 72 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Removed  | Done       | 0.9999978412155812  | 0      |
| 73 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Unknown  | Done       | 0.9999973487489863  | 0      |
| 74 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Fallback   | 1.0                 | -1     |
| 75 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                           | Removed  | Fallback   | 1.0                 | -1     |
| 76 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Removed  | Done       | 0.9999989998333151  | 0      |
| 77 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Done       | 0.9999980645435738  | 0      |
| 78 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999980092590302  | 0      |
| 79 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Done       | 0.9999979298772069  | 0      |

