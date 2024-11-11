# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._to_copy.default          |                 14 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                 10 |           1 |         0 |          0 | 🚧          |    0.1  |
|  3 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.bmm.default               |                  6 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.cat.default               |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.clone.default             |                  8 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.cumsum.default            |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.embedding.default         |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.expand.default            |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.full.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.gt.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.lift_fresh_copy.default   |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.lt.Tensor                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.masked_fill.Scalar        |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 17 | aten.mm.default                |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.mul.Tensor                |                  8 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.native_layer_norm.default |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.permute.default           |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.pow.Tensor_Scalar         |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.rsub.Scalar               |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.select.int                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.slice.Tensor              |                 21 |           0 |         0 |          1 | ✘           |    0    |
| 26 | aten.sub.Tensor                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.sum.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.sym_size.int              |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.t.default                 |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.tanh.default              |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 31 | aten.topk.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 32 | aten.transpose.int             |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 33 | aten.unsqueeze.default         |                  9 |           1 |         0 |          2 | 🚧          |    0.11 |
| 34 | aten.view.default              |                 35 |           0 |         0 |          2 | ✘           |    0    |
| 35 | aten.where.self                |                  3 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | True  |
|  1 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bool           | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bool      | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bool          | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 12, 1, 64]> self = ?,<br>Optional[int] dtype = torch.float32       | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 12, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 12, 45, 64]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Fallback   | True  |
| 11 | Tensor<[1, 12, 46, 64]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[45, 45]> self = ?,<br>Optional[int] dtype = torch.bfloat16            | Unknown  | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | True  |
|  3 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | True  |
|  4 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | True  |
|  6 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | True  |
|  7 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | True  |
|  8 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | True  |
|  9 | Tensor<[45]> self = ?,<br>Tensor other = 1                                    | Done     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | True  |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  | Done       | True  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[45, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | True  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | True  |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | True  |
|  1 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | True  |
|  2 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | True  |
|  5 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 12, 45, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   |
|  2 | List[Tensor] tensors = [<[1, 45]>, <[1, 1]>],<br>int dim = -1                  | Unknown  | Fallback   | True  |
|  3 | List[Tensor] tensors = [<[1, s24]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | None     | Done       | True  |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  | Done       | True  |
|  2 | Tensor<[1, 12, 1, 46]> self = ?                                                            | Unknown  | Done       | True  |
|  3 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                       | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 12, 45, 45]> self = ?                                                           | Unknown  | Done       | True  |
|  5 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | True  |
|  6 | Tensor<[1, 45, 768]> self = ?                                                              | Unknown  | Done       | True  |
|  7 | Tensor<[1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = -1 | Unknown  | Done       | True  |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A   |
### aten.div.Tensor
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9 | Unknown  | Fallback   | True  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?   | Unknown  | Fallback   | True  |
|  1 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?  | Unknown  | Fallback   | True  |
|  2 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?  | Unknown  | Fallback   | True  |
|  3 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ? | Unknown  | Fallback   | True  |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1]> self = ?,<br>number other = 50256 | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                 | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>]     | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]               | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                       | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Fallback   | True  |
|  9 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]             | Unknown  | Fallback   | True  |
| 11 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]             | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]             | Unknown  | Fallback   | True  |
| 13 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [45, 45],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor self = ?         | Unknown  | Unknown    | N/A   |
### aten.lt.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Fallback   | True  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Done       | False |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | False |
|  3 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                                    | Unknown  | Done       | False |
|  4 | Tensor<[45, 45]> self = ?,<br>Tensor<[45, 45]> mask = ?,<br>number value = 0                                           | Done     | Unknown    | N/A   |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | True  |
|  2 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ? | Unknown  | Done       | True  |
|  3 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715            | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                 | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654  | Unknown  | Done       | True  |
|  3 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?     | Unknown  | Done       | True  |
|  4 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715           | Unknown  | Done       | True  |
|  5 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                | Unknown  | Done       | True  |
|  6 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654 | Unknown  | Done       | True  |
|  7 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?   | Unknown  | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | N/A   |
|  1 | Tensor<[1, 45, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 45]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, s24]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       | True  |
|  2 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       | True  |
|  3 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       | True  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 45, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Fallback   | True  |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1 | None     | Fallback   | True  |
|  1 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                     | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?             | Unknown  | Failed     | N/A   |
|  2 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 1, 1, 46]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 45                  | Fallback | Done       | True  |
|  8 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 45,<br>Optional[int] end = 46                 | Unknown  | Done       | True  |
|  9 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?     | Unknown  | Failed     | N/A   |
| 10 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                    | None     | Fallback   | True  |
| 11 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Fallback   | True  |
| 13 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Fallback   | True  |
| 14 | Tensor<[1, 46]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Fallback   | True  |
| 15 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | True  |
| 16 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   |
| 19 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   |
| 20 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1 | Unknown  | Done       | True  |
|  1 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A   |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1]> self = ?    | None     | Fallback   | True  |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072, 768]> self = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[50257, 768]> self = ? | Unknown  | Done       | True  |
|  2 | Tensor<[768, 3072]> self = ?  | Unknown  | Done       | True  |
|  3 | Tensor<[768, 768]> self = ?   | Unknown  | Done       | True  |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | True  |
### aten.topk.default
|    | ATen Input Variations                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50257]> self = ?,<br>int k = 50 | Unknown  | Fallback   | True  |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
|  1 | Tensor<[1, 12, 46, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
|  2 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2      | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 46]> self = ?,<br>int dim = 2      | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 45, 45]> self = ?,<br>int dim = 1     | Fallback | Done       | True  |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = 1         | Fallback | Done       | True  |
|  5 | Tensor<[1, 46]> self = ?,<br>int dim = 1         | Unknown  | Done       | True  |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1]> self = ?,<br>int dim = 1             | Unknown  | Done       | True  |
|  8 | Tensor<[45, 45]> self = ?,<br>int dim = 0        | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]               | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                   | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                       | Fallback | Done       | True  |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [-1, 1, 768]                 | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]               | Unknown  | Done       | True  |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                     | Unknown  | Done       | True  |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]               | Unknown  | Done       | True  |
|  7 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]               | Unknown  | Done       | True  |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]             | Unknown  | Done       | True  |
| 10 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]             | Unknown  | Done       | True  |
| 11 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]             | Unknown  | Done       | True  |
| 12 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]             | Unknown  | Done       | True  |
| 13 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]             | Unknown  | Done       | True  |
| 14 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   |
| 15 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                           | Unknown  | Fallback   | True  |
| 17 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                   | Unknown  | Done       | True  |
| 18 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] size = [1, 45, 768]             | Unknown  | Done       | True  |
| 19 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                 | Unknown  | Done       | True  |
| 20 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [-1, 45, 768]               | Unknown  | Done       | True  |
| 21 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [1, 45, 12, 64]             | Unknown  | Done       | True  |
| 22 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                   | Unknown  | Done       | True  |
| 23 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                         | Unknown  | Done       | True  |
| 24 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                 | Unknown  | Done       | True  |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                     | Unknown  | Done       | True  |
| 26 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | True  |
| 27 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | True  |
| 28 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   |
| 29 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | True  |
| 30 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | True  |
| 31 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                 | Unknown  | Done       | True  |
| 32 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]               | Unknown  | Done       | True  |
| 33 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                   | Unknown  | Done       | True  |
| 34 | Tensor<[45]> self = ?,<br>List[int] size = [45, 1]                             | Fallback | Unknown    | N/A   |
### aten.where.self
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 46]> condition = ?,<br>Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[]> other = ?           | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> condition = ?,<br>Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[]> other = ?         | Unknown  | Fallback   | True  |

