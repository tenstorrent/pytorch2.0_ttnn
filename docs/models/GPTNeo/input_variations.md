# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default          |                 14 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.bmm.default               |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.cat.default               |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.clone.default             |                  8 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.cumsum.default            |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.embedding.default         |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.eq.Scalar                 |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.expand.default            |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.full.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.gt.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.lt.Tensor                 |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.masked_fill.Scalar        |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.mm.default                |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.mul.Tensor                |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.native_layer_norm.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.permute.default           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.pow.Tensor_Scalar         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.rsub.Scalar               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.select.int                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.slice.Tensor              |                 21 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.sub.Tensor                |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.sum.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.sym_size.int              |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.t.default                 |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.tanh.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.topk.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.transpose.int             |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.unsqueeze.default         |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.view.default              |                 34 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.where.self                |                  3 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996417744618268 | 0      |
|  1 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996005053200391 | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bool           | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bool      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bool          | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 12, 1, 64]> self = ?,<br>Optional[int] dtype = torch.float32       | Unknown  | Fallback   | 1.0   | -1     |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 12, 45, 64]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 12, 46, 64]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[45, 45]> self = ?,<br>Optional[int] dtype = torch.bfloat16            | Unknown  | Fallback   | 1.0   | -1     |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999945508127167 | 0      |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999979475435741 | 0      |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | 0.9999978588201103 | 0      |
|  3 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999977273790203 | 0      |
|  4 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999980260961997 | 0      |
|  6 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999947856191373 | 0      |
|  7 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999979819775014 | 0      |
|  8 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999979840204434 | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  | Done       | 0.999967 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | 0.999967 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  | Done       | 0.999941 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.999965 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[45, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | 0.999943 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.999967 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | 0.9999882265899276 | 0      |
|  1 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | 0.9999845056929473 | 0      |
|  2 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | 0.9999879670453474 | 0      |
|  5 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | 0.9999865273411653 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 12, 45, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2  | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 12, s10, 64]>, <[1, 12, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 45]>, <[1, 1]>],<br>int dim = -1                  | Unknown  | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[1, s24]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 12, 1, 46]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                       | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 12, 45, 45]> self = ?                                                           | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 45, 768]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = -1 | Unknown  | Done       | 0.9999022131087392 | 0      |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = -1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                              | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9 | Unknown  | Done       | 0.999996 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?   | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ? | Unknown  | Done       |     1 |      0 |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 45]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>number other = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1]> self = ?,<br>number other = 50256 | Unknown  | Done       | 1.0   | 0      |
### aten.expand.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                 | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>]     | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]               | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                       | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]             | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]             | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]             | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [45, 45],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | Unknown  | Fallback   |     1 |     -1 |
### aten.lt.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ?                     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Fallback   | 1.0   | -1     |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 45]> self = ?,<br>Tensor<[1, 45]> mask = ?,<br>number value = 1                                             | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                                    | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, s0]> self = ?,<br>Tensor<[1, s0]> mask = ?,<br>number value = 1                                             | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[45, 45]> self = ?,<br>Tensor<[45, 45]> mask = ?,<br>number value = 0                                           | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?  | Unknown  | Done       | 0.999969 |      0 |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.99997  |      0 |
|  2 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ? | Unknown  | Done       | 0.999969 |      0 |
|  3 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.999969 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715            | Unknown  | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                 | Unknown  | Done       | 1        |      0 |
|  2 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654  | Unknown  | Done       | 0.999997 |      0 |
|  3 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?     | Unknown  | Done       | 0.999996 |      0 |
|  4 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715           | Unknown  | Done       | 0.999995 |      0 |
|  5 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                | Unknown  | Done       | 1        |      0 |
|  6 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654 | Unknown  | Done       | 0.999997 |      0 |
|  7 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | 0.999998 |      3 |
|  1 | Tensor<[1, 45, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.998805 |      3 |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 45]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, s24]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 45, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999996 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999925705885033 | 0      |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999949010475493 | 0      |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?             | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, 46]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 45                  | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 45,<br>Optional[int] end = 46                 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ?     | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                    | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 46]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = 9223372036854775807    | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1 | Unknown  | Done       | 0.9999970747144696 | 0      |
|  1 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?    | Unknown  | Done       |     1 |      0 |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3072, 768]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[50257, 768]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[768, 3072]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[768, 768]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  1 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.999993 |      0 |
### aten.topk.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50257]> self = ?,<br>int k = 50 | Unknown  | Fallback   |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 12, 46, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 46]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 45, 45]> self = ?,<br>int dim = 1     | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 46]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1]> self = ?,<br>int dim = 1             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[45, 45]> self = ?,<br>int dim = 0        | Unknown  | Done       | 1.0   | 0      |
### aten.view.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]               | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                   | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                       | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [-1, 1, 768]                 | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]               | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                     | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]               | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]               | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]             | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]             | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]             | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]             | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]             | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, <s10 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                           | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                   | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] size = [1, 45, 768]             | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                 | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [-1, 45, 768]               | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [1, 45, 12, 64]             | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                   | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                         | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                 | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                     | Unknown  | Done       | 1.0   | 0      |
| 26 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]               | Unknown  | Done       | 1.0   | 0      |
| 27 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]               | Unknown  | Done       | 1.0   | 0      |
| 28 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s10 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]             | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]             | Unknown  | Done       | 1.0   | 0      |
| 31 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                 | Unknown  | Done       | 1.0   | 0      |
| 32 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]               | Unknown  | Done       | 1.0   | 0      |
| 33 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                   | Unknown  | Done       | 1.0   | 0      |
### aten.where.self
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 46]> condition = ?,<br>Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, s10 + 1]> condition = ?,<br>Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor other = ?         | Unknown  | Unknown    | N/A   | N/A    |

