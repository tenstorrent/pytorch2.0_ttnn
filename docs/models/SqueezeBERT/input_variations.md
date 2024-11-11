# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.clone.default             |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  3 | aten.embedding.default         |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.mul.Tensor                |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  5 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  6 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.slice.Tensor              |                  4 |           0 |         3 |          1 | 🚧          |    0.75 |
|  8 | aten.unsqueeze.default         |                  2 |           1 |         0 |          1 | 🚧          |    0.5  |
***
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | None     | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ? | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 768]> self = ? | Fallback | Done       | True  |
### aten.embedding.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | None     | Fallback   | True  |
|  1 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0 | None     | Fallback   | True  |
|  2 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                           | None     | Fallback   | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Fallback | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0 | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                       | Fallback | Done       | True  |
|  3 | Tensor<[1, 8]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Fallback   | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 8]> self = ?,<br>int dim = 2 | Fallback | Done       | True  |
|  1 | Tensor<[1, 8]> self = ?,<br>int dim = 1    | Done     | Done       | True  |

