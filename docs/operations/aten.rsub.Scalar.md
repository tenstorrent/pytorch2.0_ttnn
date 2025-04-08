### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999844958878847 | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999904433414514 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999921313130852 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999895380596509 | 0      |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999911610812028 | 0      |
|  8 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999935511066776 | 0      |
| 10 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999983002316801 | 0      |
| 11 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999936535356139 | 0      |
| 12 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999916972352806 | 0      |
| 13 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 14 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999905831906153 | 0      |
| 15 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999828058694208 | 0      |
| 16 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999936495866483 | 0      |
| 17 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999924638116696 | 0      |
| 18 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999930633591085 | 0      |
| 19 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999963945679675 | 0      |
| 20 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999973648990507 | 0      |
| 21 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | 1.0                | 0      |
| 22 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 1.0                | 0      |
| 23 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999946014818526 | 0      |
| 28 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999939927492483 | 0      |
| 29 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999926446312705 | 0      |
| 30 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999772634629364 | 0      |
| 31 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.999994112765755  | 0      |
| 32 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999931253127602 | 0      |
| 33 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999935830596275 | 0      |
| 34 | Tensor<[1, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Unknown    | N/A                | N/A    |
| 35 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999934080350336 | 0      |

